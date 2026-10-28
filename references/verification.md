# Verify that revisions preserve intended meaning

Verification answers two different questions: **Which protected elements changed?** and **Did any change alter the intended meaning?** The bundled script helps answer the first; comparison with the source manuscript and author-supplied material is still needed for the second. Use the workflow and `Local` / `Semantic` / `Structural` change types defined in `SKILL.md`.

## Preserve the original and explain substantive edits

Keep the original available alongside the revision. A reviewer cannot reliably evaluate a rewrite if the source of comparison has been lost.

Record substantive edits by finding ID or location. For each, explain what changed, show before/after excerpts where helpful, and state the expected reader benefit, change type(s), and any separate risk to the meaning. Document `Semantic` and `Structural` changes individually; routine `Local` expression edits can be summarized. One edit may have several change types.

## Declare intentional protected-element changes for the script

When running the bundled verifier, create `approved_changes.txt` even if no changes are intended (an empty file is valid). Add **one identifier per line** for each intentionally added or removed protected element. For example:

```text
cite:smith2020
label:fig:overview
math:<symbol or expression>
```

The `math:` form accepts whitespace and expands to the verifier's `math-symbol` and `math-expr` keys. The explicit `math-symbol:` and `math-expr:` forms are also valid; whitespace within `math-expr:` is normalized by the verifier. For an intentional equation change, document both original and revised forms in the change record so the meaning can be reviewed.

Despite its historical filename, this file records **editor intent, not author approval**. An entry does not prove that a change is correct. Do not add one merely to make a failed check disappear. If you are not running the script or lack suitable original/revised source files, record intended substantive changes in the ordinary change log; no separate allowlist is required.

## Run the deterministic protected-element check

When the script and suitable original/revised LaTeX or text sources are available, run:

```bash
python3 scripts/verify_protected.py ORIGINAL REVISED --approved approved_changes.txt --out verify_report.md --strict
```

Use the report to locate additions or removals involving numbers, units, citations, cross-references, labels, or mathematics. Compare the surrounding text as well: an allowed token change does not validate every occurrence of that token. `--strict` detects some unexpected additions and removals, but extraction is imperfect with complex LaTeX, compound units, and unit macros. A clean report is therefore not a certificate of correctness.

## Check scientific meaning independently

Inspect **every `Semantic` and `Structural` edit** against the source. Follow the relationships among claims, evidence, definitions, assumptions, conditions, results, and qualifications; look for changed causal direction or omitted information, not just different wording. Spot-check `Local` edits. For a wholesale rewrite, trace substantive meaning across the entire new organization rather than expecting paragraphs to match one-to-one.

If a mathematical symbol changes, first identify the object it represents and all its uses in equations, definitions, figures, prose, and cross-references. Rename that semantic role rather than globally replacing matching characters. Consult `notation.md` when the change involves symbol identity; optional typography conventions are not a reason to rewrite otherwise understandable mathematics.

## Report limitations and unresolved issues

Report intended protected changes, unexpected discrepancies, unresolved author decisions, and any material that could not be compared. State what was checked and what remains uncertain; an automated check cannot establish semantic equivalence by itself.

