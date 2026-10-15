---
name: scientific-manuscript-editor
description: Diagnose, edit and verify English scientific manuscripts (often LLM-drafted) for readability without changing their science. Use when asked to improve manuscript readability, remove AI-sounding prose, tighten a draft, complete a pre-experiment draft, or check a revision.
---

# Scientific Manuscript Editor

This skill makes a manuscript easier to read while keeping its scientific content intact. It is not a "humanizer". Removing AI-sounding words is never the goal; the surface tells of LLM writing are symptoms of deeper problems (missing overview, unsupported claims, unneeded content, drifting terms, unstated logical relations, undefined symbols), and those deeper problems are what this skill fixes.

## Default principle: continuity from accessible context to new information

Readers integrate new information most easily when it is attached to something already accessible: common knowledge in the field, or something stated earlier in the manuscript. So, by default, text moves from accessible context to the new point. This is a default heuristic for diagnosing breaks in continuity, not a rule every sentence must satisfy.

| Scale | Accessible context | New | Checked in |
|---|---|---|---|
| Sentence | topic position: a term from the previous sentence or a shared concept | stress position at the end: the new point | L4, L5 |
| Paragraph | purpose or claim the paragraph serves, identifiable early | support and detail | L2 |
| Section | context: an overview of what the parts are and how they relate | the parts in detail | L2 |
| Paper opening | context the intended reader can accept quickly, as close to the gap as practical | the gap and the contribution | L0 |

Where the principle does not apply: a sentence may open with new information when its discourse role is to introduce something — the first sentence of a paragraph or subsection, a definition, or a contrast. Flag a continuity break only when a sentence continues an existing thread yet opens with information the reader has not met. At the section scale the literature speaks of "context before content": the context may itself be new, as long as it frames what follows.

Sources by scale: sentence — Haviland & Clark's given-new contract (1974), Gopen & Swan, "The Science of Scientific Writing" (American Scientist, 1990), who present these positions as reader expectations rather than rules; paragraph — Daneš's thematic progression (1974), Mensh & Kording, "Ten simple rules for structuring papers" (PLoS Comput Biol, 2017), Rule 3; section and paper — Mensh & Kording Rule 3 (context–content–conclusion), Ausubel's advance organizers (meta-analyses show a small, consistent positive effect); opening — Swales' CARS model (1990). Empirical support that revision guided by a comprehension model (Kintsch) can improve recall and the conveyed structure of a text: Britton & Gülgöz, J. Educational Psychology, 1991. Use this principle to explain L0, L2 and L4 findings.

## Why LLM drafts read badly (use this to explain findings)

1. **No plan before writing.** Text is produced front to back, so the overall picture is missing, components are described one after another without how they connect, paragraphs restate their opening in their closing sentence, and sentences are joined with additive connectors ("Furthermore") instead of their real relation.
2. **Optimized to look good.** Significance is asserted, contributions are overstated, limitations are boilerplate, and evaluative adjectives (crucial, robust, comprehensive) stand in for evidence.
3. **Fluency fills missing content.** Abstract wording replaces numbers and conditions; symbols appear without definition; equations appear without their meaning; citations and figures can be wrong or invented.
4. **Trained on prose that rewards variation.** One concept is called region, area and zone; frequent phrasings and uniform rhythm appear.
5. **Correct but unneeded text is cheap.** Accurate general statements accumulate even when the research question does not need them.

## Inputs

- **manuscript**: LaTeX or Markdown, in the form of the paper to be submitted (same sections, same notation). Never edit the user's file in place; work on a copy.
- **RQs and contributions**: if the author does not give them, extract them, label them `[INFERRED]`, and report them at the top of the diagnosis so the author can correct them. Inferred RQs limit what L0 may delete (see L0).
- **target**: one of
  - `draft` — a pre-experiment manuscript, written in paper form, that also serves as the implementation specification for the experiments. Readers: the authors and whoever implements the experiments. No page limit; completeness wins over brevity.
  - `submission` — a manuscript with results, headed for a venue. Readers: reviewers. Page limit applies; density wins over completeness, except for anything a reviewer needs to judge the claims.
  Infer the target from the manuscript if not given (no results tables, placeholders, "we will" → `draft`) and state the inference.
- **venue** (for `submission`): the target venue and, if available, its author guidelines or a link to them. Conventions that vary by venue (first person, voice, tense, anonymization, spelling) are decided by the venue, not by this skill; see "Venue conventions" below.
- **constraints** (optional): page limit, sections not to touch, findings to skip.

## Modes and default flow

| Mode | Changes the manuscript? | Output |
|---|---|---|
| `diagnose` | No | Findings table |
| `edit` | Yes, on a copy | Revised copy + change log |
| `verify` | No | Verification report |

Default flow when asked to improve a manuscript: `diagnose` → `edit` (all findings except those marked No) → `verify`, with the three outputs delivered together. Run `diagnose` alone when the user asks only for a review or for findings. Keep the three modes as separate passes even when running them back to back: the pass that rewrites does not also decide what to rewrite, and the pass that verifies does not rewrite.

## Layers

Diagnose all layers; the order matters because higher-layer changes delete or rewrite text that lower layers would polish.

| Layer | Question | Operation in `edit` |
|---|---|---|
| **L0 Necessity and opening** | Is this content needed for the RQs and contributions? Does the opening establish context close to the gap? | Delete / move / replace opener from existing content |
| **L1 Claims ↔ evidence** | What supports each claim? Do text, tables, figures and citations agree? Are symbols and equations defined? | Narrow claims; insert `[AUTHOR: …]` / `[VERIFY]`. **Never supply evidence, numbers, citations or definitions the manuscript does not contain** |
| **L2 Global structure** | Can the reader follow the argument? Is there an overview (text or figure) where the detail has several parts? | Reorder / merge / split / add overview from existing content / insert `[FIGURE: …]` |
| **L3 Terminology & definitions** | Is each concept named by one term, defined before use? | Normalize terms |
| **L4 Logical relations** | What is the real relation between sentences and paragraphs? Does a sentence that continues a thread start from accessible information? | Make relation explicit / reorder sentences within a paragraph |
| **L5 Sentence-level prose** | Is each sentence easy to read? | Rewrite / shorten |
| **L6 Density or completeness** | `submission`: does each passage change the reader's understanding? `draft`: can the reader implement from this? | `submission`: delete repetition, move detail to appendix. `draft`: add structure and placeholders for missing content |

All layers may be edited automatically. The one hard limit is content: the editor never invents numbers, results, citations, mechanisms or definitions. Missing content becomes a marker for the author. Edits differ in how much damage a mistake can do, so every finding and every change carries a Risk label (see "Mode: diagnose"); Semantic and Structural changes always go through the semantic check in `verify`.

### Layer guidance

**L0 Necessity.** Flag statements that are true but do not build the research gap, method, evidence or interpretation. Judge only against the RQs and contributions. For `draft`, be lenient: context that helps an implementer understand why a design choice was made stays.
When the RQs or contributions are `[INFERRED]`, L0 edits may remove obvious redundancy, but must not delete scientifically substantive content solely because it seems unrelated to an inferred RQ: the editor would be dropping information on the strength of its own interpretation. Prefer relocation (e.g., to an appendix or a later section) or a `[VERIFY: needed for RQ?]` flag. When the author has stated the RQs and contributions, delete as usual.

**L0 Opening of the Abstract and Introduction.** Opening by establishing the territory is a standard, legitimate move (Swales, CARS Move 1: claiming centrality, making topic generalizations, or reviewing previous research). The problem is the generic execution LLMs produce, not the move. The opening should establish context that the intended reader can accept quickly and that is **as close as practical to the research gap**, so the next sentences can build on it. It may be common ground, a well-established cited fact, or a concise synthesis of prior work. "Road traffic accidents are a major cause of death worldwide" is accepted by everyone in the field and used by nothing that follows; "Segment-level crash records are sparse, so risk models for road networks are trained on few positives" is equally quick to accept and already carries the gap.
- "Intended reader" means the venue's readers, not the general public.
- Test 1: does the second sentence use the first to move toward the gap? If not, the opening is too far from the gap.
- Test 2: could the sentence open another paper in the same field unchanged? If yes, it is too generic. Generic is the failure; needing a citation is not.
- Also flag the opposite failure: an opening that is a contestable claim presented without support; the reader then starts in doubt.
- In the Abstract, keep context to one sentence where possible; the gap should arrive by the second. In the Introduction, context may take a few sentences, but each should be closer to the gap than the last.
- Replace the opener only from content already in the manuscript (usually the gap statement itself, moved earlier); otherwise mark `[AUTHOR: …]`.

**L1 Claims ↔ evidence.** For every claim, name what supports it (number, table, figure, citation; for `draft`, the planned experiment). Flag overclaims, generalizations beyond the experiments, boilerplate limitations, ambiguous "significant" (statistical vs. important), and inconsistencies between text, tables and figures. Do not check citations against memory; mark them `[VERIFY]` unless the source is available.
Also under L1, since they are claims the reader must be able to check:
- every symbol defined at first use (what it denotes, its domain, its indices);
- every equation accompanied by prose that says what it computes and why it has this form, not a word-for-word reading of the symbols;
- every term in a formal problem statement (inputs, outputs, assumptions, objective) defined before the statement.

**L2 Global structure.**
- Build a reverse outline (one line per paragraph: its purpose) and check order, gaps and duplication.
- **Overview before detail when what follows has several parts the reader must hold at once** — a method with interacting components, a Results section answering several RQs with several experiments, an Introduction whose contribution list is itself the paper's overview. The test is the need, not the section type. Where the detail that follows is a single thing, no overview is needed.
- An overview must carry content: what the parts are, what goes in and comes out, how they connect, why they are separated. Roadmap-only text ("This section introduces… First, we… Next, we…") is not an overview and is itself an LLM pattern.
- **An overview can be a figure.** Check figures as part of the structure:
  - Paper level, in two steps. First decide whether an early figure would materially reduce the reader's effort in grasping the contribution. It often would; it may not for pure theory, for a method whose contribution is best stated as equations, for a short paper, or where a central results table is clearer. Only if it would, check whether Figure 1 (or another early figure) performs that role, and whether the reader can grasp the intended contribution from that figure and its caption without reading the detailed method. Its form depends on the contribution: a method pipeline, the problem setting, a qualitative side-by-side comparison with prior methods (common in vision and generation papers), a teaser plot of the main trade-off, or a dataset construction pipeline.
  - Section level: flag a missing overview figure where the overview criterion above applies and the relations are hard to state linearly in prose (data flow among several components). Do not ask for one where prose does the job.
  - Content: a figure whose boxes are section names joined by arrows is the figure form of a roadmap paragraph. An overview figure must show inputs, outputs, data flow and the split into components.
  - Reference order: the text must point to the figure before entering the details it summarizes.
  - Division of labor: if the figure shows how components connect, the text overview adds what the figure cannot (why the components are separated), not a restatement of the figure.
  - Terms and symbols in figure labels must match the text (L3). If figure content is only in an image file, read the image when possible; otherwise list the labels as `[VERIFY]`.
  - Creating a figure is the author's job. `edit` inserts a `[FIGURE: …]` placeholder stating what the figure should show and which claim it supports.
- Put each paragraph's purpose where the reader can identify it early. This does not mean the first sentence must be the claim; building a problem over two or three sentences before the claim is fine. Do not impose one rhythm on every paragraph.
- Flag paragraphs whose last sentence restates their first.
- Explain the problem a component solves before its mechanism; define a term or symbol before naming it.

**L3 Terminology.** List every concept with more than one name and propose one term each (prefer the term used in definitions or equations). Flag terms used before definition and symbols reused with different meanings. For `draft`, also produce a notation table if the manuscript lacks one and has more than a handful of symbols.

**L4 Logical relations.** Replace additive connectors with the actual relation (cause: because, so; contrast: however, whereas; condition: if, when; restatement: that is; example: for example), or reorder sentences so the relation is evident. Deleting the connector alone can erase the logic. Check continuity at sentence level: when a sentence continues an existing thread, place accessible information before the new point where practical. A sentence whose role is to open a new paragraph, subsection, definition or contrast may introduce a new topic at its start; do not "fix" it.

**L5 Prose.**
- Rule: **do not replace a vague evaluation with a weaker one. Replace it with evidence, mechanism, scope, or nothing.** "crucial" → "important" is not a fix. If the evidence or mechanism is not in the manuscript, this becomes an L1 finding with `[AUTHOR: …]`, not an invented specific.
- Turn nominalizations back into verbs. Default to active voice when the agent is the authors or the method, **but only within the venue's conventions**: if the venue restricts first person or prefers impersonal constructions, keep the passive or impersonal form and fix readability by other means (shorter sentences, continuity of topic, explicit agents where allowed). Do not convert voice or person before the venue conventions are settled.
- Let sentence length follow content. Never vary length for its own sake; that is detector evasion, not editing.
- Remove empty framing ("It is important to note that", "In this paper, we aim to", "plays a crucial role in").
- `references/patterns.md` lists frequent LLM phrasings with their usual underlying problem. Use it to locate candidates, never as a replacement table.

**L6 Density (`submission`) or completeness (`draft`).** The direction of editing flips with the target.
- `submission`: does this information need to be here for the scientific argument? Move implementation detail not needed to judge the claims to the appendix or supplement. Repetition is acceptable where a location must stand alone (the Abstract; captions). Delete only when (a) the passage does not change the reader's understanding and (b) the information survives elsewhere. Typical candidates: equations restated word for word in prose, "In other words" restatements, contribution lists repeated verbatim in Abstract, Introduction and Conclusion, captions duplicated in body text.
- `draft`: can another researcher implement the experiments from this text? Page length is not a concern. Never delete definitions, assumptions, conditions, hyperparameters or equation explanations, even if repeated. Run the draft completeness checklist below and add structure and markers for whatever is missing.

### Draft completeness checklist (`target: draft`)

A draft is judged by whether the authors and an implementer can work from it. Check each item; for a missing item, `edit` adds the section or sentence skeleton with `[AUTHOR: …]` markers for the content only the author has.

Apply each item when it is scientifically applicable to the study design. Mark an item or sub-item `N/A` when the design genuinely does not need it (e.g., no hyperparameters in a parameter-free or deterministic geometric method; no confirm/refute rule for an exploratory or descriptive study), and say why in one line. Never invent an experimental component merely to satisfy the checklist.

1. **Contributions** — stated explicitly, each one checkable (what is new, relative to what, and what evidence will show it). Each contribution maps to at least one planned experiment or analysis and one figure or table.
2. **Problem setting and formalization** — inputs, outputs, assumptions, constraints and objective stated in prose first, then formally. Every symbol defined at first use; a notation table when there are many. Every equation followed by its meaning: what it computes, why this form, what each term contributes.
3. **Proposed method** — each component: the problem it solves, its mechanism, its inputs and outputs, and, where real alternatives existed, the alternatives rejected and why. Overview before components.
4. **Experiment design as a specification** — for each experiment or analysis: the RQ or contribution it addresses; datasets with versions, splits and preprocessing; baselines and their configurations; metrics with definitions; ablations; hyperparameters and search ranges; compute, seeds and number of runs; the expected interpretation or decision rule (what result would support, weaken or refute the claim, or, for exploratory work, how the result will be read).
5. **Figure and table plan** — for each planned figure or table: what it shows, axes or columns, which claim it supports, and how it will be read. Decide explicitly whether an early overview figure is needed and, if so, which form conveys the contribution most directly.
6. **Limitations and threats** — the real weaknesses the authors already anticipate, not boilerplate.

## Venue conventions (`submission`)

Several style choices are set by the venue, and a readability edit that ignores them produces work the author must undo. Before L5 edits on a `submission` manuscript, settle these from the venue's author guidelines (ask for them, or fetch them if a URL is given). If they cannot be obtained, infer the conventions from the manuscript's own consistent practice, state the inference, and do not change person or voice.

| Convention | What to check | If unknown |
|---|---|---|
| First person | Is "we" / "I" allowed, discouraged, or required? | Keep the manuscript's current practice |
| Voice | Active preferred, passive preferred, or no stance? | Keep the manuscript's current practice |
| Tense | Past for Methods and Results, present for established facts and for referring to figures? | Keep the manuscript's current practice |
| Anonymization | Double-blind: self-citations written in third person, no institution or project names that identify the authors | Flag every "our previous work" style reference as `[VERIFY: anonymity]` |
| Spelling and format | British vs. American spelling; number, unit and equation formatting; reference style | Normalize to the manuscript's majority form (L3-style consistency), never to a guessed venue rule |

Record the settled conventions at the top of the change log so a reviewer of the edit can see which rules were applied. For `draft`, use the authors' own practice and note that these will need settling at submission time.

## Protected elements

Protected by default; the editor changes them only when a finding explicitly concerns them and the change log records it:

numerical values and units; citations and bibliography keys; equation contents; equation, figure, table and section labels and references; variable and symbol definitions; dataset, model and method names; experimental conditions; thresholds and hyperparameters; reported results; RQs; stated contributions; scope statements and assumptions; hedges and qualifications that limit a claim.

A rewrite of a sentence containing a protected element must keep that element and its meaning (what it measures, against what, under which condition).

## Mode: diagnose

1. Confirm or extract RQs, contributions and target. For `submission`, settle the venue conventions (see above) before anything else.
2. Read the whole manuscript, including figures and captions, before writing any finding.
3. Produce the findings table, ordered by layer then location:

| ID | Layer | Location | Severity | Risk | Problem | Action | Editable |
|---|---|---|---|---|---|---|---|
| D01 | L0 | Abstract s1 | Medium | Structural | Opening is accepted by all but unused by the gap | Open with the sparsity premise the gap relies on (from Intro ¶2) | Yes |
| D02 | L1 | Intro ¶6 | High | Semantic | "substantially" is not supported by Table 2 (+1.1 pt) | Narrow claim; author may add evidence | Yes (narrow) |
| D03 | L1 | §3.1 eq. 2 | High | Semantic | $\lambda$ undefined; equation has no prose meaning | Insert `[AUTHOR: define λ]`; add meaning sentence from §3.2 | Partial |
| D04 | L2 | §3 | High | Structural | Five-module method has no overview in text or figure | Add overview paragraph from component descriptions + `[FIGURE: …]` | Yes |
| D05 | L3 | §3.2 | Medium | Local | area / region / zone denote one concept | Use "region" | Yes |
| D06 | L4 | §4.1 ¶2 | Medium | Local | "Furthermore" joins a cause and its effect | State the causal relation | Yes |
| D07 | L6 | §5 | High (draft) | Structural | No expected interpretation for Experiment 2 | Add `[AUTHOR: how will the result for C2 be read?]` | Partial |

- Location: section and paragraph number (¶), plus a short quote (under 15 words) when ambiguous.
- Severity: **High** = could mislead a reviewer, misstate a result, or (draft) block implementation; **Medium** = costs the reader noticeable effort; **Low** = local polish.
- Risk: how much a wrong edit could damage the paper.
  - **Local** — wording within a sentence; meaning unchanged by design (term normalization, nominalization, connector choice, empty framing).
  - **Semantic** — the edit changes what a sentence claims or how strongly (narrowing a claim, rewording a hedge, adding a meaning sentence for an equation, replacing an evaluative word with a mechanism).
  - **Structural** — the edit removes, moves, merges or splits content, or changes the order of the argument (L0 deletion, L2 reorder, L6 move to appendix, replacing the opener, adding an overview).
- Editable: `Yes` (editor can complete it from the manuscript), `Partial` (editor adds structure and a marker; content needed from the author), `No` (nothing the editor can do; author only).
- Group recurring L5 patterns into one finding with a count and a few locations instead of dozens of rows.
4. End with a short summary: the 3–5 findings that most affect readability (or, for draft, implementability), and the questions only the author can answer.

Write findings in the user's language; quote manuscript text as is.

## Mode: edit

1. Apply every finding marked Yes or Partial, unless the user restricts the set by ID or by layer. Do not fix problems not in the table; add them as new findings at the end of the change log instead.
2. Work on a copy named `<name>.revised.<ext>`.
3. Preserve protected elements except where a finding names them.
4. Produce a change log next to the revision (`<name>.changes.md`), with Structural and Semantic changes listed before Local ones so the author sees them first:

| ID | Risk | Location | Before (short) | After (short) | Reason |

5. Write `approved_changes.txt` listing every protected element the applied findings intentionally add or remove (`num:50epochs`, `cite:smith2020`, `label:fig:overview`, `math:x_t`), so `verify` can separate intended from unintended changes.
6. List all `[AUTHOR: …]`, `[VERIFY]` and `[FIGURE: …]` markers at the end of the change log as the author's to-do list.

## Mode: verify

Do not edit anything in this mode.

1. **Deterministic check** — run:
   ```bash
   python3 scripts/verify_protected.py ORIGINAL REVISED --approved approved_changes.txt --out verify_report.md
   ```
   It extracts numbers and units, citation keys (`\cite*`, `\citep`, `\citet`, pandoc `@key`), `\label`, `\ref`/`\eqref`/`\autoref`/`\cref`, math expressions and symbols, and acronyms, and reports each as unchanged / added / removed / changed-context. LaTeX comments are ignored in `.tex` files. Every unapproved added or removed element must be explained or reverted. Review every `changed-context` row: the number survived but its sentence changed.
2. **Semantic check** — every Semantic and Structural change in the change log must be checked; Local changes may be sampled. Compare original and revised for:
   - new claims, citations or definitions not in the original
   - lost assumptions, conditions, definitions or experimental details (for `draft`, any loss is High)
   - scope expansion (e.g., "on dataset X" → "in general")
   - weakened or removed qualifications (may, in our setting, on average)
   - changed causal meaning (correlation stated as cause, direction reversed)
   - for Structural changes: content deleted on the basis of `[INFERRED]` RQs, and argument order that now uses a term or result before it is introduced
3. Report: deterministic summary, semantic issues with locations, and a verdict per issue (revert / keep with author confirmation).

Run the semantic check with fresh context when possible (a subagent that sees only the two versions, the change log and this section), so the editor does not grade its own edit.

## Rules across modes

- Never invent numbers, results, citations, mechanisms or definitions. Missing content becomes `[AUTHOR: …]`.
- After the author edits by hand, do not run a full-manuscript L5 pass again unless asked; it reintroduces patterns the author removed.
- Keep the author's voice where it is clear and correct; this skill fixes problems, not style preferences.
- If the manuscript is not in English, diagnose with the same layers and defer prose rules to a language-specific writing-style skill if one is available.
