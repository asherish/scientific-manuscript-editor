---
name: scientific-manuscript-editor
description: Diagnose, edit and verify English scientific manuscripts (often LLM-drafted) for readability without changing their science. Use when asked to improve readability of a paper, remove AI-sounding prose, tighten a draft, or check a revision, even if the user only says "読みやすくして" or "AIっぽさを消して".
---

# Scientific Manuscript Editor

This skill makes a manuscript easier to read while keeping its scientific content intact. It is not a "humanizer". Removing AI-sounding words is never the goal; the surface tells of LLM writing are symptoms of deeper problems (missing overview, unsupported claims, unneeded content, drifting terms, unstated logical relations), and those deeper problems are what this skill fixes.

## Why LLM drafts read badly (use this to explain findings)

1. **No plan before writing.** Text is produced front to back, so the overall picture is missing, components are described one after another without how they connect, paragraphs restate their opening in their closing sentence, and sentences are joined with additive connectors ("Furthermore") instead of their real relation.
2. **Optimized to look good.** Significance is asserted, contributions are overstated, limitations are boilerplate, and evaluative adjectives (crucial, robust, comprehensive) stand in for evidence.
3. **Fluency fills missing content.** Abstract wording replaces numbers and conditions; citations and figures can be wrong or invented.
4. **Trained on prose that rewards variation.** One concept is called region, area and zone; frequent phrasings and uniform rhythm appear.
5. **Correct but unneeded text is cheap.** Accurate general statements accumulate even when the research question does not need them.

## Inputs

- **manuscript**: LaTeX or Markdown. Never edit the user's file in place; work on a copy.
- **RQs and contributions**: if the author does not give them, extract them, label them `[INFERRED]`, and ask the author to confirm before any L0 finding is treated as actionable.
- **target**: `submission` (reviewers must understand the argument efficiently) or `specification` (another researcher must be able to implement the experiment). Default: ask; if the author is absent, assume `submission` and say so.
- **constraints** (optional): page limit, venue style, sections not to touch.

## Three modes — never combine them in one pass

| Mode | Changes the manuscript? | Output |
|---|---|---|
| `diagnose` | No | Findings table |
| `edit` | Only selected findings | Revised copy + change log |
| `verify` | No | Verification report |

Do not review, rewrite and self-review in a single pass. If the user asks to "just fix it", run `diagnose`, present the table, and ask which findings to apply. Apply Auto-edit=Yes findings without asking only if the user explicitly says so.

## Layers

Diagnose all layers; the order matters because higher-layer changes delete or rewrite text that lower layers would polish.

| Layer | Question | Allowed operation in `edit` |
|---|---|---|
| **L0 Necessity** | Is this content needed for the RQs and contributions? | Delete/move — **approval required** |
| **L1 Claims ↔ evidence** | What supports each claim? Do numbers, tables, figures and citations agree? | **Never supply evidence.** May only narrow a claim (with approval) or insert `[AUTHOR: …]` |
| **L2 Global structure** | Can the reader follow the argument? Is there an overview where one is needed? | Reorder / merge / split / add overview — **approval required** |
| **L3 Terminology & definitions** | Is each concept named by one term, defined before use? | Normalize terms — auto within scope |
| **L4 Logical relations** | What is the real relation between sentences and paragraphs? | Make relation explicit / reorder sentences within a paragraph — auto within scope |
| **L5 Sentence-level prose** | Is each sentence easy to read? | Rewrite / shorten — auto within scope |
| **L6 Information density** | Does each passage change the reader's understanding? | Delete repetition — **approval required** |

### Layer guidance

**L0 Necessity.** Flag statements that are true but do not build the research gap, method, evidence or interpretation (e.g., Introduction openers such as "traffic safety is important", "recent advances have enabled…"). Judge only against the confirmed RQs and contributions.

**L1 Claims ↔ evidence.** For every claim, name what supports it (number, table, figure, citation). Flag overclaims, generalizations beyond the experiments, boilerplate limitations, ambiguous "significant" (statistical vs. important), and inconsistencies between text, tables and figures. Do not check citations against memory; mark them `[VERIFY]` for the author unless the source is available.

**L2 Global structure.**
- Build a reverse outline (one line per paragraph: its purpose) and check order, gaps and duplication.
- Overview before detail **only when the reader needs a mental model before the details** — typically a method with several interacting components (state input, output, how components connect, why they are separated). Do not add overviews to short subsections, Results subsections, or every section of the Introduction.
- An overview must carry content. Roadmap-only text ("This section introduces… First, we… Next, we…") is not an overview and is itself an LLM pattern.
- Put each paragraph's purpose where the reader can identify it early. This does not mean the first sentence must be the claim; building a problem over two or three sentences before the claim is fine. Do not impose one rhythm on every paragraph.
- Flag paragraphs whose last sentence restates their first.
- Explain the problem a component solves before its mechanism; define a term or symbol before naming it.

**L3 Terminology.** List every concept with more than one name and propose one term each (prefer the term used in definitions or equations). Flag terms used before definition and symbols reused with different meanings.

**L4 Logical relations.** Replace additive connectors with the actual relation (cause: because, so; contrast: however, whereas; condition: if, when; restatement: that is; example: for example), or reorder sentences so the relation is evident. Deleting the connector alone can erase the logic.

**L5 Prose.**
- Rule: **do not replace a vague evaluation with a weaker one. Replace it with evidence, mechanism, scope, or nothing.** "crucial" → "important" is not a fix. If the evidence or mechanism is not in the manuscript, this becomes an L1 finding with `[AUTHOR: …]`, not an invented specific.
- Turn nominalizations back into verbs; use active voice when the agent is the authors or the method.
- Let sentence length follow content. Never vary length for its own sake; that is detector evasion, not editing.
- Remove empty framing ("It is important to note that", "In this paper, we aim to", "plays a crucial role in").
- `references/patterns.md` lists frequent LLM phrasings with their usual underlying problem. Use it to locate candidates, never as a replacement table.

**L6 Information density.** Criteria depend on `target`:
- `submission`: does this information need to be here for the scientific argument? Candidates for moving to the appendix or supplement: implementation detail not needed to judge the claims.
- `specification`: can another researcher implement the experiment from this text? Keep definitions, conditions and hyperparameters even if repetitive.

Repetition is acceptable when a location must stand alone for its reader (the Abstract; figure and table captions). Delete only when (a) the passage does not change the reader's understanding, and (b) the information survives somewhere else in the manuscript. Typical candidates: equations restated word for word in prose, "In other words" restatements, contribution lists repeated verbatim in Abstract, Introduction and Conclusion, captions duplicated in body text.

## Protected elements

Protected by default; change only with explicit authorization naming the element:

numerical values and units; citations and bibliography keys; equation contents; equation, figure, table and section labels and references; variable and symbol definitions; dataset, model and method names; experimental conditions; thresholds and hyperparameters; reported results; RQs; stated contributions; scope statements and assumptions; hedges and qualifications that limit a claim.

A rewrite of a sentence containing a protected element must keep that element and its meaning (what it measures, against what, under which condition).

## Mode: diagnose

1. Confirm or extract RQs, contributions and target.
2. Read the whole manuscript before writing any finding.
3. Produce the findings table, ordered by layer then location:

| ID | Layer | Location | Severity | Problem | Suggested action | Auto-edit |
|---|---|---|---|---|---|---|
| D01 | L0 | Intro ¶3 | Medium | General statement not used by the research gap | Delete | Approval |
| D02 | L1 | Intro ¶6 | High | "substantially" is not supported by Table 2 (+1.1 pt) | Narrow claim or add evidence | No |
| D03 | L3 | §3.2 | Medium | area / region / zone denote one concept | Use "region" | Yes |
| D04 | L4 | §4.1 ¶2 | Medium | "Furthermore" joins a cause and its effect | State the causal relation | Yes |

- Location: section and paragraph number (¶), plus a short quote (under 15 words) when ambiguous.
- Severity: **High** = could mislead a reviewer or misstate a result; **Medium** = costs the reader noticeable effort; **Low** = local polish.
- Auto-edit: `Yes` (L3–L5), `Approval` (L0, L2, L6, and L1 claim narrowing), `No` (L1 evidence gaps — only the author can fix).
- Group recurring L5 patterns into one finding with a count and a few locations instead of dozens of rows.
4. End with a short summary: the 3–5 findings that most affect readability, and the questions only the author can answer.

Write findings in the user's language; quote manuscript text as is.

## Mode: edit

1. Take the list of finding IDs to apply (e.g., "D01, D03–D05"). Apply nothing else. Do not fix problems you notice along the way; add them as new findings at the end of the change log instead.
2. Work on a copy named `<name>.revised.<ext>`.
3. Preserve protected elements unless an approved finding names them.
4. Produce a change log next to the revision (`<name>.changes.md`):

| ID | Location | Before (short) | After (short) | Reason |

5. Write `approved_changes.txt` listing every protected element the approved findings intentionally add or remove (`num:50epochs`, `cite:smith2020`, `label:fig:overview`, `math:x_t`), so `verify` can separate intended from unintended changes.

## Mode: verify

Do not edit anything in this mode.

1. **Deterministic check** — run:
   ```bash
   python3 scripts/verify_protected.py ORIGINAL REVISED --approved approved_changes.txt --out verify_report.md
   ```
   It extracts numbers and units, citation keys (`\cite*`, `\citep`, `\citet`, pandoc `@key`), `\label`, `\ref`/`\eqref`/`\autoref`/`\cref`, math expressions and symbols, and acronyms, and reports each as unchanged / added / removed / changed-context. LaTeX comments are ignored in `.tex` files. Every unapproved added or removed element must be explained or reverted. Review every `changed-context` row: the number survived but its sentence changed.
2. **Semantic check** — compare original and revised paragraph by paragraph for:
   - new claims or citations not in the original
   - lost assumptions, conditions or experimental details
   - scope expansion (e.g., "on dataset X" → "in general")
   - weakened or removed qualifications (may, in our setting, on average)
   - changed causal meaning (correlation stated as cause, direction reversed)
3. Report: deterministic summary, semantic issues with locations, and a verdict per issue (revert / keep with author confirmation).

Run the semantic check with fresh context when possible (a subagent that sees only the two versions and this section), so the editor does not grade its own edit.

## Rules across modes

- Never invent numbers, results, citations or mechanisms. Missing content becomes `[AUTHOR: …]`.
- After the author edits by hand, do not run a full-manuscript L5 pass again unless asked; it reintroduces patterns the author removed.
- Keep the author's voice where it is clear and correct; this skill fixes problems, not style preferences.
- If the manuscript is in Japanese, diagnose with the same layers and defer prose rules to the japanese-writing-style skill if available.
