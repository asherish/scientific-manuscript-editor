---
name: scientific-manuscript-editor
description: >-
  Use when the user asks to write a scientific manuscript from research materials;
  diagnose its scientific argument, structure, or readability; revise, reorganize,
  or extensively rewrite an existing manuscript; verify scientific meaning across
  revisions; prepare an implementation-ready pre-experiment specification; or
  refine a post-experiment manuscript for a target venue. Apply reader-centered
  paragraph writing and scientific safeguards without inventing research content.
---

# Scientific Manuscript Editor

## 1. Purpose and principles

Help authors communicate scientific research **accurately, coherently, and in a form the intended reader can understand without unnecessary effort**. This skill supports writing from supplied research material, diagnosing an existing manuscript, revising it at any appropriate scale, and verifying an existing revision. Its goal is scientific understanding, not shorter prose, a uniform writing style, or the removal of recognizable AI phrases.

Scientific reasoning and its presentation must work together. Apply these four principles at every relevant scale and workflow step. They are **questions for judgment**, not quotas for edits.

1. **Purpose — What understanding should this element enable?** Identify the scientific idea, claim, explanation, or relationship that the paper, section, paragraph, sentence, equation, or figure contributes. A topic label alone is not a communicative purpose: a paragraph about a probability may define it, motivate it, derive it, or explain its limitations.
2. **Coherence — How does the information fit together?** Make relations among claims, evidence, conditions, explanations, and neighboring passages recoverable. Arrange the material so that each part connects to what readers already know and advances the argument rather than merely following a conventional outline.
3. **Comprehensibility — Can the intended reader understand it?** Account for disciplinary background, introduced concepts, necessary explanation, and the effort of following dependencies. Use paragraph writing and clear expression as means to understanding, not as fixed templates. **A useful default is to move from information already established or reasonably known to the reader toward new information**—within sentences, across paragraphs, and across sections. Reorder when another sequence better serves the explanation; never force a rigid known-before-new sentence pattern.
4. **Scientific Accuracy — Is the meaning supported and preserved?** Keep definitions, assumptions, mathematical relationships, evidence, scope, and claim strength faithful to the supplied material and verified sources. Fluent prose is not sufficient if it obscures a condition or overstates an inference. Scientific accuracy takes precedence over stylistic elegance.

Do not invent a problem just to apply a principle. A clear passage can remain unchanged; useful context, repetition, and discipline-specific terminology may be worth keeping. Every proposed intervention needs a plausible benefit for the reader.

## 2. Establish the task and constraints

Before writing or diagnosing, form a compact model of **the task, the reader, the research, and the manuscript's purpose**. Determine whether the user wants new writing, diagnosis only, improvement of an existing text, or independent verification; honor any explicit limit on scope. Identify the research questions, proposed or completed contributions, central claims, methods, assumptions, and available or planned evidence. Label research questions or contributions `[INFERRED]` if you infer them rather than receive them from the author. Do not use an inferred research question to justify silently deleting substantive content.

Distinguish two primary manuscript purposes:

- **Pre-experiment specification:** Experiments have yet to be implemented, and the paper-form manuscript also guides their implementation. Specify inputs, definitions, mathematical meaning, methods, and evaluation plans at the detail needed to implement and appraise the research. Necessary explanation takes priority over page count. Clearly distinguish a proposed experiment from a completed one; do not fabricate results or unresolved design decisions.
- **Post-experiment submission preparation:** Research results are available and the manuscript is being prepared for a target venue. Communicate contributions and evidence efficiently, and **check current official venue requirements** for page limits, person and voice, tense, anonymization, spelling, figures, and formatting before applying them. Do not sacrifice scientific validity, reproducibility, or essential qualifications for brevity.

The phase and the requested action are **independent dimensions**: either phase can involve new writing, diagnosis, local revision, restructuring, extensive rewriting, or verification. For partly completed research, identify which obligations apply. If a missing detail would substantially change the output, ask the author; otherwise proceed with bounded, explicit assumptions. Never invent venue policies.

## 3. Workflow

Follow the task-relevant parts of **establish context → design or diagnose → write or revise → review and verify → deliver**. This is an iterative process, not a mandatory five-step sequence for every request. The principles above guide every step; the references below supply conditional detail.

### Design or diagnose the intended explanation

For **new writing**, first design the reader's path through the scientific material: what each major part needs to establish, which claims have support, and which concepts must be introduced before use. Outline the paper or affected section before composing substantial prose. When helpful, plan a difficult passage as **reader question → evidence-grounded answer → paragraph or group of paragraphs**. The question is an optional planning device, not an obligatory question in the manuscript or a one-question-per-paragraph rule.

For **existing material**, read the relevant full context, including equations, figures, tables, and captions. Diagnose consequential obstacles to understanding or scientific support. Use a short manuscript map or reverse outline where structure is suspect; do not flag harmless deviations from stylistic templates. Explain a problem by its effect on readers and the evidence in the text. **If diagnosis alone was requested, report findings and stop without editing.**

### Choose the appropriate intervention

After diagnosis, choose among **no change, local revision, paragraph/section reorganization, and extensive rewriting from the underlying scientific material**. A fundamental argument problem may require a new outline and a complete rewrite rather than sentence-by-sentence polishing. Respect the user's scope: permission to polish does not imply permission to replace the entire manuscript. Preserve the original when revising; an author may also ask for a standalone verification without any new editing.

### Compose or revise the prose

Write paragraphs to perform identifiable explanatory moves, with support adequate for the intended reader. Choose topic/support relationships or another suitable rhetorical pattern; do not force topic sentences to appear first or concluding sentences to exist in every paragraph. Use established context to introduce unfamiliar information, and integrate mathematical or visual material with prose as described in Section 4. Distinguish planned methods and hypotheses from performed experiments and observed findings. A new manuscript has no original to compare against: ground it in supplied or verified scientific sources instead.

### Review, verify, and iterate

Read the draft from the reader's position: can the reader recover each purpose, dependency, claim, qualification, and connection? Independently check scientific accuracy. For revisions, verify all substantive changes against the original and the underlying material, using `references/verification.md` where the task requires it. If the problem is structural, return to design or diagnosis rather than repeatedly polishing sentences. An automated protected-element check helps but cannot prove semantic equivalence. Do not redo whole-manuscript polishing after the author's manual edits unless asked.

### Deliver the requested result

Report the manuscript or prioritized findings, material edits, verification limits, and unresolved author decisions as applicable. Follow Section 7; an unchanged passage can be the right outcome.

## 4. Write at the right scale

Work from the larger scientific argument toward its presentation, then check both local clarity and connections across levels:

| Scale | Main responsibility |
|---|---|
| **Paper** | Make the research problem, gap, questions, contribution, methods, evidence or planned evaluation, and conclusions form a defensible whole. |
| **Section** | Give each section a clear role in that whole; align its title with its contents, order its explanations, and connect it to surrounding sections. |
| **Paragraph** | Make a coherent contribution to the section through a central idea and appropriate support; use paragraph writing without mandating a topic-sentence/support/conclusion template. |
| **Sentence** | State information precisely, with recoverable agents, references, modifiers, and relations to neighboring sentences; prefer constructions the intended reader can follow. |

Move from the paper's scientific message to section roles, paragraph-level explanations, and sentence-level expression, then check coherence across levels. The paragraph is a useful unit of composition, but a well-formed paragraph is not necessarily a well-connected argument. Consider a paragraph's central move and supporting reasoning without enforcing a uniform shape.

**Integrate equations, figures, and tables with the surrounding prose.** An equation expresses a definition or relation precisely; nearby sentences establish why it is needed, explain its symbols and assumptions, and interpret its meaning. A figure or table presents structure, comparison, or evidence; captions make the element intelligible while the prose directs attention to consequential observations and their scientific interpretation. Neither repeat the element line by line nor leave readers to infer its role. Check consistency across text, equations, captions, labels, and evidence. A visual overview is valuable when it materially clarifies relationships, not because every paper needs a pipeline diagram.

## 5. Scientific safeguards

**Do not fabricate** data, results, numbers, citations, sources, experimental conditions, mechanisms, definitions of author-created concepts, or design decisions. Treat claims, datasets, assumptions, results, scope qualifiers, numbers and units, citations, mathematical expressions and symbol meanings, and labels and references as protected scientific content. Any substantive change requires a reason and semantic verification, even if it improves the prose.

If important information is unavailable, use `[AUTHOR: ...]` for an author decision or `[VERIFY: ...]` for a claim requiring checking **only where the gap materially matters**. A `[FIGURE: ...]` placeholder may describe an evidence-grounded figure that cannot yet be produced; never invent its contents. Collect unresolved placeholders in a concise author-to-do section. Do not quietly strengthen a tentative claim or delete substantive information because it appears outside an inferred contribution.

Classify interventions by the **type of change**, not its severity: **Local** changes expression without intended scientific or organizational effects; **Semantic** changes claims, definitions, assumptions, mathematical meaning, or other scientific content; **Structural** changes the ordering, grouping, or inclusion of material. Types can overlap: a structural rewrite may also change meaning. Assess scientific risk separately, and explicitly verify every Semantic and Structural change. Do not call these categories risk levels.

For revisions with suitable original and revised sources, use `references/verification.md` for the comparison procedure and the authoritative specification of `approved_changes.txt` and the bundled verifier. Its whitelist records editor intent, **not author approval**. Never add an entry merely to suppress a warning. If complete verification is impossible, explain the limit rather than claiming success.

## 6. Load specialized guidance when relevant

The definitions, safeguards, and workflow above always apply. **A reference is not guaranteed to be loaded unless selected here.** Read each reference whose stated condition matches the task before applying its specialized method. Do not assume that another reference has been loaded or turn optional guidance into a mandatory audit.

| Situation | Reference |
|---|---|
| Designing or composing a substantial argument, restructuring, diagnosing difficult paragraph flow, or planning text–equation/figure/table integration | `references/argument-and-exposition.md` |
| Creating a detailed question-driven outline, needing section-specific planning questions, or conducting an explicitly requested completeness audit | `references/question-bank.md` (adapted optional 60QA; select only relevant questions) |
| Writing, diagnosing, or substantially revising an Introduction | `references/introduction.md` |
| Writing, diagnosing, or substantially revising an Abstract or summary paragraph | `references/abstract.md` |
| Performing detailed diagnosis, reverse outlining, or producing a structured diagnosis report | `references/diagnosis.md` |
| Writing or substantially revising an implementation-oriented pre-experiment specification, or explicitly auditing research design/implementation completeness | `references/pre-experiment-specification.md` |
| Preparing or polishing a post-experiment manuscript under target-venue requirements | `references/submission-preparation.md` |
| Establishing notation conventions, resolving symbol ambiguity, or changing symbol identities | `references/notation.md` |
| Making substantive revisions to existing scientific content, running protected-element checks, or comparing original and revised versions | `references/verification.md` |

Pre-experiment status alone does **not** authorize a full research-design audit when the user requested only readability feedback. Conversely, when asked to **write** an implementation-ready specification, include the detail necessary for implementation. Judge applicability from the task and explain material gaps rather than mechanically checking every item.

## 7. Deliverables

Report in the **user's language**, while quoting source manuscript passages in their original language. For a diagnosis, prioritize meaningful, actionable findings with locations and anticipated reader benefits. For a revision, provide the revised copy, a change log (especially semantic and structural decisions), protected-element check results when available, and unresolved author questions. For new writing, provide the manuscript and explain material assumptions or information still needed. Keep reports concise enough that the author can act on them; an unchanged passage or a short set of findings can be the right outcome.
