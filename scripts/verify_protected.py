#!/usr/bin/env python3
"""Deterministic check of protected elements between two manuscript versions.

Extracts protected elements from the original and the revised manuscript
(LaTeX or Markdown/plain text), compares them as multisets, and reports
each element as unchanged / added / removed / changed-context.

It never edits either file. It reports; the author decides.

Usage:
    python3 verify_protected.py ORIGINAL REVISED [--approved FILE] [--out FILE] [--strict]

--approved FILE  One element per line (e.g. "cite:smith2020", "num:12.4%",
                 "label:fig:overview", "math:x_t"). Listed elements are
                 marked as approved when they are added or removed.
--strict         Exit with status 1 if any unapproved added/removed element exists.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------- extraction

CITE_RE = re.compile(r"\\(?:cite|citep|citet|citealp|citeauthor|citeyear|autocite|parencite|textcite)\*?"
                     r"(?:\[[^\]]*\]){0,2}\{([^}]*)\}")
LABEL_RE = re.compile(r"\\label\{([^}]*)\}")
REF_RE = re.compile(r"\\(ref|eqref|autoref|cref|Cref|pageref)\{([^}]*)\}")
# Markdown/pandoc-style citations: [@key], @key
MD_CITE_RE = re.compile(r"(?<![\w.])@([A-Za-z][\w:.-]*\w)")

MATH_ENVS = ("equation", "equation*", "align", "align*", "gather", "gather*",
             "multline", "multline*", "eqnarray", "eqnarray*", "math", "displaymath")
MATH_BLOCK_RE = re.compile(
    r"\$\$(.+?)\$\$"
    r"|\\\[(.+?)\\\]"
    r"|\\\((.+?)\\\)"
    r"|\\begin\{(" + "|".join(re.escape(e) for e in MATH_ENVS) + r")\}(.+?)\\end\{\4\}"
    r"|(?<!\\)\$(.+?)(?<!\\)\$",
    re.S,
)
MATH_SYMBOL_RE = re.compile(r"\\[A-Za-z]+|[A-Za-z](?:_\{[^}]*\}|_[A-Za-z0-9])?(?:\^\{[^}]*\}|\^[A-Za-z0-9])?")
MATH_IGNORE = {"\\label", "\\nonumber", "\\notag", "\\left", "\\right", "\\quad", "\\qquad",
               "\\begin", "\\end", "\\text", "\\mathrm", "\\mathbf", "\\mathcal", "\\operatorname"}

UNITS = (r"\\%|%|‰|pp|pt|pts|ms|s|sec|min|h|hr|hrs|Hz|kHz|MHz|GHz|nm|mm|cm|m|km|km/h|m/s|kg|g|"
         r"KB|MB|GB|TB|K|M|B|x|×|epochs?|steps?|layers?|heads?|samples?|images?|tokens?|"
         r"GPUs?|hours?|days?|°|deg|px|dB|W|kW|V|USD|JPY")
NUM_RE = re.compile(
    r"(?<![\w.\\])"
    r"([<>≤≥~±]?\s?[-−]?\d+(?:[.,]\d+)*(?:[eE][-+]?\d+)?)"
    r"(?:\s?(" + UNITS + r"))?"
    r"(?![\w])"
)
ACRONYM_RE = re.compile(r"\b[A-Z][A-Z0-9]{1,}(?:-[A-Z0-9]+)*s?\b")
ACRONYM_IGNORE = {"I", "A", "AND", "OR", "THE", "TODO", "AUTHOR", "NOTE"}

COMMENT_RE = re.compile(r"(?<!\\)%.*")


def strip_comments(text: str) -> str:
    return "\n".join(COMMENT_RE.sub("", line) for line in text.splitlines())


def context(text: str, start: int, end: int, width: int = 6) -> str:
    """Return a few words on each side of a match, whitespace-normalized."""
    left = re.sub(r"\s+", " ", text[:start]).split(" ")[-width:]
    right = re.sub(r"\s+", " ", text[end:]).split(" ")[:width]
    return " ".join(w for w in left + ["⟨·⟩"] + right if w)


def extract(text: str, latex: bool = True) -> dict[str, list[tuple[str, str]]]:
    """Return {category: [(element, context), ...]}."""
    if latex:
        text = strip_comments(text)
    found: dict[str, list[tuple[str, str]]] = defaultdict(list)

    # Commands whose arguments must not be read as numbers or acronyms.
    masked = list(text)

    def mask(s: int, e: int) -> None:
        for i in range(s, e):
            if masked[i] != "\n":
                masked[i] = " "

    for m in CITE_RE.finditer(text):
        for key in m.group(1).split(","):
            key = key.strip()
            if key:
                found["cite"].append((key, context(text, m.start(), m.end())))
        mask(m.start(), m.end())
    for m in MD_CITE_RE.finditer(text):
        found["cite"].append((m.group(1), context(text, m.start(), m.end())))
        mask(m.start(), m.end())
    for m in LABEL_RE.finditer(text):
        found["label"].append((m.group(1).strip(), context(text, m.start(), m.end())))
        mask(m.start(), m.end())
    for m in REF_RE.finditer(text):
        for key in m.group(2).split(","):
            found["ref"].append((f"{m.group(1)}:{key.strip()}", context(text, m.start(), m.end())))
        mask(m.start(), m.end())

    masked_text = "".join(masked)

    # Math: whole expressions and their symbols.
    for m in MATH_BLOCK_RE.finditer(masked_text):
        body = next(g for g in (m.group(1), m.group(2), m.group(3), m.group(5), m.group(6)) if g is not None)
        norm = re.sub(r"\s+", "", body)
        if not norm:
            continue
        ctx = context(masked_text, m.start(), m.end())
        found["math-expr"].append((norm, ctx))
        for s in MATH_SYMBOL_RE.findall(body):
            if s not in MATH_IGNORE:
                found["math-symbol"].append((s, ctx))
        mask(m.start(), m.end())

    prose = "".join(masked)

    for m in NUM_RE.finditer(prose):
        num = re.sub(r"\s+", "", m.group(1)).replace("−", "-")
        unit = (m.group(2) or "").replace("\\%", "%")
        found["num"].append((f"{num}{unit}", context(prose, m.start(), m.end())))

    for m in ACRONYM_RE.finditer(prose):
        tok = m.group(0)
        if tok not in ACRONYM_IGNORE:
            found["acronym"].append((tok, context(prose, m.start(), m.end())))

    return found


# ---------------------------------------------------------------- comparison

def ctx_words(c: str) -> set[str]:
    return {w.lower().strip(".,;:()[]") for w in c.split() if w != "⟨·⟩"}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b)


def compare(orig, rev, approved: set[str]):
    rows = []  # (category, element, status, approved?, detail)
    for cat in sorted(set(orig) | set(rev)):
        o = Counter(e for e, _ in orig.get(cat, []))
        r = Counter(e for e, _ in rev.get(cat, []))
        octx = defaultdict(list)
        rctx = defaultdict(list)
        for e, c in orig.get(cat, []):
            octx[e].append(c)
        for e, c in rev.get(cat, []):
            rctx[e].append(c)
        for e in sorted(set(o) | set(r)):
            key = f"{cat}:{e}"
            ok = key in approved
            if o[e] == r[e]:
                # Same count: flag if the surrounding words changed a lot.
                worst = min(
                    max(jaccard(ctx_words(a), ctx_words(b)) for b in rctx[e])
                    for a in octx[e]
                )
                if cat in ("num", "cite", "math-expr") and worst < 0.35:
                    rows.append((cat, e, "changed-context", ok,
                                 f"before: …{octx[e][0]}… / after: …{rctx[e][0]}…"))
                else:
                    rows.append((cat, e, "unchanged", ok, f"×{o[e]}"))
            elif r[e] > o[e]:
                rows.append((cat, e, "added", ok, f"×{o[e]} → ×{r[e]}; after: …{rctx[e][0]}…"))
            else:
                ctx = octx[e][0] if octx[e] else ""
                rows.append((cat, e, "removed", ok, f"×{o[e]} → ×{r[e]}; before: …{ctx}…"))
    return rows


# ---------------------------------------------------------------- report

CAT_TITLES = {
    "num": "Numbers and units",
    "cite": "Citation keys",
    "label": "Labels",
    "ref": "Cross-references",
    "math-expr": "Math expressions",
    "math-symbol": "Math symbols",
    "acronym": "Acronyms and named entities (advisory)",
}


def render(rows, orig_path, rev_path) -> tuple[str, int]:
    out = [f"# Protected-element check\n",
           f"- Original: `{orig_path}`\n- Revised: `{rev_path}`\n"]
    flagged = [r for r in rows if r[2] != "unchanged"]
    unapproved = [r for r in flagged if not r[3] and r[2] in ("added", "removed") and r[0] != "acronym"]
    counts = Counter(r[2] for r in rows)
    out.append(f"\n**Summary:** {counts.get('unchanged', 0)} unchanged, "
               f"{counts.get('added', 0)} added, {counts.get('removed', 0)} removed, "
               f"{counts.get('changed-context', 0)} changed-context. "
               f"**Unapproved additions/removals (excluding acronyms): {len(unapproved)}**\n")
    for cat in CAT_TITLES:
        items = [r for r in flagged if r[0] == cat]
        if not items:
            continue
        out.append(f"\n## {CAT_TITLES[cat]}\n\n| Element | Status | Approved | Detail |\n|---|---|---|---|\n")
        for _, e, status, ok, detail in items:
            d = detail.replace("|", "\\|")
            el = e.replace("|", "\\|")
            out.append(f"| `{el}` | {status} | {'yes' if ok else 'no'} | {d} |\n")
    if not flagged:
        out.append("\nAll protected elements are unchanged.\n")
    out.append("\nThis check covers surface forms only. Meaning-level changes "
               "(new claims, lost assumptions, scope, qualifications, causal meaning) "
               "need the semantic check.\n")
    return "".join(out), len(unapproved)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("original")
    ap.add_argument("revised")
    ap.add_argument("--approved", help="file listing approved changes, one 'category:element' per line")
    ap.add_argument("--out", help="write the Markdown report here instead of stdout")
    ap.add_argument("--strict", action="store_true", help="exit 1 on unapproved additions/removals")
    a = ap.parse_args()

    orig_text = Path(a.original).read_text(encoding="utf-8")
    rev_text = Path(a.revised).read_text(encoding="utf-8")
    approved = set()
    if a.approved:
        approved = {ln.strip() for ln in Path(a.approved).read_text(encoding="utf-8").splitlines()
                    if ln.strip() and not ln.startswith("#")}

    is_tex = lambda p: Path(p).suffix.lower() in (".tex", ".ltx", ".sty")
    rows = compare(extract(orig_text, is_tex(a.original)), extract(rev_text, is_tex(a.revised)), approved)
    report, n_bad = render(rows, a.original, a.revised)
    if a.out:
        Path(a.out).write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)
    return 1 if (a.strict and n_bad) else 0


if __name__ == "__main__":
    sys.exit(main())
