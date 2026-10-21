---
name: scientific-manuscript-editor
description: Support reader-centered writing, diagnosis, revision, and verification of scientific papers and paper-form research drafts. Improve readers' understanding without imposing mechanical prose rules or inventing scientific content. Use for readability reviews, revisions of LLM-drafted manuscripts, and readability-focused drafting from supplied scientific material.
---

# Scientific Manuscript Editor

## Purpose

Help the intended reader understand a paper's scientific contribution **accurately, efficiently, and without unnecessary effort**. The aim is not to enforce a writing template, eliminate recognizable AI phrases, or maximize brevity.

**Every proposed change must have a plausible benefit for the reader.** Identify what the reader is trying to understand, what the text currently enables them to understand, and what prevents progress. Edit only when an intervention is likely to help. Keeping effective text unchanged is a valid outcome.

Treat rhetorical principles and examples as **diagnostic tools, not requirements**. A conventional sentence, repeated explanation, passive construction, or unusual notation is not automatically a problem. Fluent prose can still obscure definitions or logic. **Flag unsupported or overstated consequential claims even when the wording is easy to read**: accuracy is part of clarity.

## Establish the reading context

Before diagnosing or writing, establish a compact working model:

- **Reader:** What relevant knowledge can the intended audience reasonably bring? What should they learn from this paper? Avoid assuming either a novice or an expert without justification.
- **Scientific argument:** What are the research questions, contributions, central claims, and evidence or planned evaluations? If extracted rather than supplied by the author, label RQs and contributions `[INFERRED]`.
- **Manuscript stage:** `draft` or `submission`.
  - `draft` is already written in paper form but may precede experiments and also guide their implementation. Preserve the detail needed to understand and implement the work; page length is not the priority.
  - `submission` must communicate the contribution and evidence efficiently to reviewers, subject to the venue's requirements. Do not sacrifice validity, reproducibility, or essential qualification for brevity.
- **Venue and constraints:** When available, consult author guidelines for person, voice, tense, anonymization, spelling, and formatting. Otherwise retain consistent manuscript practice; do not invent venue rules.

If details are missing, proceed with stated assumptions where reasonable. Do not treat an inferred RQ as sufficient justification for deleting substantive scientific content.

## Diagnose the reader's path through the argument

Read the complete available manuscript, including figures, tables, captions, and relevant linked sections. Build a **brief manuscript map** (argument, section roles, definitions, evidence). When structure seems confusing, use a **reverse outline** (one purpose per paragraph) of the affected section or whole paper to find gaps, repetition, and dependencies.

At the paper, section, and passage levels, ask:

1. **What should the reader understand here?** What question is this passage meant to resolve?
2. **What is already accessible?** Which terms, assumptions, claims, and relationships have been introduced or can reasonably be assumed?
3. **What blocks understanding?** Look for likely confusion, unsupported interpretations, missing context, unnecessary memory load, excessive searching backward, or detail that obscures the point.
4. **What would help?** Could a definition, explanation, different order, tighter claim, example, useful repetition, or visual overview remove the obstacle? Would leaving the text alone be better?

Explain findings in terms of their **anticipated effect on a reader**, grounded in the manuscript. Do not claim to know how actual readers reacted.

Use the following lenses only where they clarify a diagnosed problem; **do not apply all lenses to every section or produce findings just to fill categories**:

| Lens | Possible source of difficulty |
|---|---|
| L0 — Relevance | Material does not help establish the problem, contribution, method, evidence, or interpretation. |
| L1 — Scientific support | A consequential claim lacks adequate support, exceeds the evaluated scope, or conflicts with a figure, table, equation, or assumption. |
| L2 — Structure | The reader cannot see how parts fit together, why they appear in this order, or how they lead to the contribution. |
| L3 — Concepts and notation | Ambiguous terminology, undefined concepts, or inconsistent symbols prevent correct interpretation. |
| L4 — Logical continuity | The intended cause, contrast, condition, inference, or transition is hard to recover. |
| L5 — Expression | Sentence construction imposes avoidable effort or obscures the actual agent, action, or meaning. |
| L6 — Information allocation | Necessary explanation is missing, or detail/repetition consumes attention without helping the reader. |

Useful heuristics include accessible-context-to-new-information, context–content–conclusion, and the progression from established context toward a research gap (Haviland & Clark; Mensh & Kording; Swales). They are guides to reader expectations, **not mandatory sentence shapes or fixed section templates**.

For a generic-seeming opening, ask: **Does the next sentence build toward the research gap? Could this opener introduce many other papers unchanged?** These are probes, not rules about sentence count or citation. Consult `references/patterns.md` for recurring prose symptoms, never as a banned-phrases list.

## Consider visual overviews when relationships are hard to convey

A figure can give the reader a mental model before the detailed explanation. Evaluate whether a visual representation would **materially reduce the effort of understanding relationships, processes, or the contribution**. Examples at different scales include:

- **Whole paper:** An early overview of the problem setting, central scientific idea, contribution relative to existing methods, study design, or an illustrative comparison. This may be Figure 1, but neither an early figure nor a pipeline diagram is mandatory.
- **Section:** A conceptual diagram of the entities, assumptions, components, or data relationships explained across several subsections, so readers can locate each detail within a larger structure.
- **Method or processing pipeline:** A diagram showing inputs, transformations, intermediate representations, component dependencies, and outputs, particularly when the stages are difficult to hold together from prose alone.

A good overview communicates substantive relationships; **boxes labeled with section headings and connected by arrows are not sufficient**. Check that labels agree with the manuscript and that the figure and caption communicate their intended point without requiring a line-by-line reading of the method. The prose should complement, not merely repeat, the figure.

Do not request figures reflexively: if a concise explanation, equation, or table works better, use it. When a figure would help but cannot be produced from available material, propose what it should communicate or add a `[FIGURE: ...]` placeholder; never fabricate a result or diagram content.

## Choose the smallest effective intervention

Prefer repairing the cause of confusion over changing surface wording. For example, a vague importance claim may need a concrete mechanism or bounded inference—not a different adjective. A difficult equation may need an explanation of its purpose—not a recitation of every symbol. An introductory context sentence may be useful even when general or cited; judge whether it helps readers approach the actual research gap.

Keep useful repetition where passages must stand alone, especially abstracts and figure captions. Preserve deliberate terminology and the author's voice. Fix notation only for reader-facing ambiguity or inconsistency. Consult `references/notation.md` for **optional defaults** when setting or repairing a convention, not a list of deviations to report. If a symbol must be renamed, identify its **semantic role and all corresponding occurrences** first; never perform an unscoped global replacement.

For `draft`, clarify what is already specified without dropping definitions, equation explanations, or experimental conditions needed for implementation. Consult `references/draft-checklist.md` as **optional, applicability-sensitive prompts** only when the user explicitly asks for research-design, implementation-specification, reproducibility, or completeness review. The `draft` stage alone does not trigger this audit, even though such drafts may guide experiment implementation. Otherwise keep the task focused on readability.

## Workflow: diagnose → edit → verify

Keep the passes separate, even when completing them in one request. If the user asks only for a diagnosis, stop after `diagnose`. Otherwise perform all three without requiring an intermediate approval step.

### 1. Diagnose — no manuscript changes

Report **meaningful, actionable obstacles**, prioritized by their expected effect on understanding; a short report is better than exhaustive low-value comments. For each finding include:

- **ID and location**, with a short quote if useful.
- **Reader difficulty:** what a reader may misunderstand or have to work unusually hard to infer, and why.
- **Intervention and benefit:** what to change and how that helps.
- **Risk:** `Local` (expression only), `Semantic` (meaning, claim strength, definition, or symbol identity), or `Structural` (ordering, inclusion, or organization).
- **Feasibility:** `Yes` (grounded edit possible), `Partial` (only a placeholder or limited repair possible), or `No` (author input required).

Do not automatically raise findings for harmless conventions or patterns. Group repeated instances when they share one cause. Use L0–L6 as optional labels, not required quotas.

### 2. Edit — produce a revised copy

Apply the diagnosed, feasible improvements unless the user limits scope. Preserve the original. Record changes with finding ID, location, **reader benefit**, before/after excerpt, and risk. List substantive `Semantic` and `Structural` changes first so the author can review them efficiently. **Write `approved_changes.txt`** (empty if none) listing intentional protected-element additions/removals using identifiers such as `cite:smith2020`, `label:fig:overview`, or `math:<symbol or expression>`. For mathematics, **prefer `math:`**: it accepts whitespace and expands to the script's `math-symbol` and `math-expr` keys. Explicit `math-symbol:` and `math-expr:` identifiers are also accepted, and the verifier normalizes whitespace in `math-expr:`. Document both the original and revised expressions when an equation is intentionally changed. Despite its name, this file records **editor intent, not author approval**. Explain changes in the log and review them semantically; never whitelist merely to silence an error.

The editor may reorganize, shorten, expand, or narrow text **using information justified by the supplied manuscript and verified sources**, but may not make up experimental facts. If a scientifically necessary value, citation, novel definition, mechanism, or decision is absent, insert `[AUTHOR: ...]` or `[VERIFY: ...]` only when it is genuinely needed. Collect all placeholders in an author-to-do section. Do not silently convert a tentative claim into a stronger one.

### 3. Verify — no new edits

Check the original against the revision, focusing on meaning rather than conformity to prose rules:

- Run `python3 scripts/verify_protected.py ORIGINAL REVISED --approved approved_changes.txt --out verify_report.md --strict` when the script and suitable text sources are available. Inspect every flagged change in numbers and units, citation keys, references, math, and labels; distinguish deliberate changes documented in the log from accidental ones. **Strict mode does not catch semantic errors or all context changes.** Entries are element-level rather than occurrence-level: check their contexts independently.
- Semantically examine **every Semantic and Structural edit** for changes to claims, evidence links, definitions, assumptions, scope, qualifications, causal direction, experiment conditions, and information lost or misplaced. Spot-check Local edits.
- Report unresolved issues explicitly. A clean script result **does not prove scientific equivalence**: extraction is imperfect (especially with complex LaTeX), and only a meaning-level comparison can catch many important errors.

Do not claim that verification passed if relevant source files, figures, or referenced material were unavailable.

## Non-negotiable constraints

- **Do not fabricate** data, results, numerical values, citations, sources, experimental conditions, mechanisms, or definitions of author-created concepts.
- Treat numbers and units, citations, equations, symbol meanings, labels and references, datasets, results, claims, assumptions, and scope qualifiers as **protected scientific content**. Any necessary change must have an explicit reason and be examined in `verify`.
- Do not remove substantive material merely because it appears unrelated to an `[INFERRED]` RQ. Prefer retaining, relocating, or flagging it for the author.
- Do not invent a readability problem to satisfy a checklist. **An unchanged passage can be the correct result.**

Report in the **user's language**; quote the original manuscript language. After manual author edits, **do not repeat whole-manuscript sentence polishing unless asked**: this can reintroduce rejected patterns.

For newly drafted passages, plan with the same reader model and verify grounding against supplied research material, not a nonexistent original. **Do not invent scientific substance.**
