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

## 2. Context

First establish **the task, reader, research, and manuscript's purpose** from the user's request and supplied research material. Determine whether the user wants new writing, diagnosis only, revision, or independent verification; honor the requested scope. Identify research questions, proposed or completed contributions, claims, methods, assumptions, and available or planned evidence. Label questions or contributions `[INFERRED]` when inferred rather than author-supplied; an inference does not authorize removing scientific content. Do not load bundled reference files merely to complete this initial context-gathering step.

Distinguish two primary manuscript purposes:

- **Pre-experiment specification:** Experiments have yet to be implemented, and the paper-form manuscript also guides their implementation. Specify inputs, definitions, mathematical meaning, methods, and evaluation plans at the detail needed to implement and appraise the research. Necessary explanation takes priority over page count. Clearly distinguish a proposed experiment from a completed one; do not fabricate results or unresolved design decisions.
- **Post-experiment submission preparation:** Research results are available and the manuscript is being prepared for a target venue. Communicate contributions and evidence efficiently under verified venue requirements; do not sacrifice scientific validity, reproducibility, or essential qualifications for brevity. Check official requirements during Design / Diagnose when relevant.

The phase and the requested action are **independent dimensions**: either phase can involve new writing, diagnosis, local revision, restructuring, extensive rewriting, or verification. For partly completed research, identify which obligations apply. If a missing detail would substantially change the output, ask the author; otherwise proceed with bounded, explicit assumptions. Never invent venue policies.

## 3. Workflow

Follow the task-relevant parts of **Context → Design / Diagnose → Write / Revise → Review / Verify → Deliver**. This is an iterative process, not five mandatory steps for every request. Apply the common construction principles in Section 4 throughout; select conditional guidance only through the routing rules in Section 6.

### Design / Diagnose

For **new writing**, work initially from paper to section to paragraph, designing the scientific message or explanatory purpose of each and the relations among them. Plan which equations, figures, or tables should supply definitions, relationships, or evidence, and how surrounding prose will introduce and interpret them. A visual may serve several paragraphs; iterate between prose and visuals instead of requiring one-to-one correspondence. Check the target venue's **current official** author instructions and template, if known, for required structure; distinguish binding requirements from common disciplinary conventions. Do not invent venue rules.

For **existing material**, read the relevant full context, including equations, figures, tables, and captions. Diagnose consequential obstacles to understanding or scientific support. Use a brief manuscript map or reverse outline where structure is suspect; do not flag harmless deviations from stylistic templates. Explain the likely reader difficulty and its basis in the text. **If diagnosis alone was requested, report findings and stop without editing.**

### Choose the intervention

After diagnosis, choose among **no change, local revision, paragraph/section reorganization, and extensive rewriting from the underlying scientific material**. A fundamental argument problem may require a new outline and a complete rewrite rather than sentence-by-sentence polishing. Respect the user's scope: permission to polish does not imply permission to replace the entire manuscript. Preserve the original when revising; an author may also ask for a standalone verification without any new editing.

### Write / Revise

Express the designed content using coherent paragraphs and appropriate evidence. Choose paragraph writing, claim–support, CCC, Problem–Solution, or another pattern **because it suits the explanatory purpose**, not to satisfy a template. Anchor new information in context already established or reasonably known to the reader. Introduce and interpret equations, figures, and tables in the prose without duplicating them mechanically. Distinguish planned methods and hypotheses from observed findings. For entirely new writing, check grounding against supplied or verified scientific sources; there is no original-versus-revision comparison.

### Review / Verify

Perform two distinct checks. **Reader-oriented review:** reconstruct the reader questions and the answers conveyed by the paper, sections, paragraphs, and supporting visuals; check purpose, continuity, prerequisites, and whether evidence warrants each inference. **Scientific verification:** check definitions, assumptions, results, mathematical meaning, references, and all substantive edits against their sources. For revisions, compare the original and revised material with the procedure in the applicable verification reference. If a problem is structural, return to design rather than repeatedly polishing sentences. Automated checks cannot prove scientific equivalence; do not repeat whole-manuscript polishing after the author's manual edits unless asked.

### Deliver

Provide the requested manuscript, diagnosis, revision, or verification report. Explain consequential edits, uncertainties, limits of verification, and unresolved author decisions as applicable. An unchanged passage can be the right outcome.

## 4. Logical construction across scales

At every scale, identify **what the reader should understand, how the material answers that need, and how it connects to its neighbors**. The question may be about research, a definition, a method, an argument, or an interpretation; it need not be written as a literal question in the manuscript.

| Scale | Main responsibility |
|---|---|
| **Paper** | Connect the scientific problem, contribution, method, evidence or planned evaluation, and defensible conclusions. |
| **Section** | Establish what the section contributes, why readers need it, and how it connects to other sections; align its title with that role. |
| **Paragraph** | Convey one recognizable explanatory move with the definitions, reasons, evidence, or qualifications needed to support it. |
| **Sentence** | Convey precise meaning and intelligible relations to surrounding sentences; make terms, agents, and references recoverable. |

Use **Question → Answer** across paper, section, and paragraph scales to expose missing reader needs or weak support. When useful, develop an answer into a paragraph or group of paragraphs (**Question → Answer → Paragraph**). This is an optional scaffold, not a rule that every paragraph must start with a question or that one question maps to one paragraph. An answer may instead require a figure, table, equation, and accompanying prose. In a pre-experiment manuscript, distinguish a question the study *will investigate* from an answer already established by evidence.

**Integrate equations, figures, and tables with the surrounding prose.** Equations express relationships precisely; nearby sentences establish their purpose, define unfamiliar symbols or assumptions, and interpret the meaning. Figures and tables present structure, comparisons, or evidence; captions identify what is shown, while paragraphs discuss consequential observations or implications. Neither duplicate them line by line nor leave readers to infer their role. Check text, mathematics, visuals, and captions for consistency. They complement prose rather than forming a separate writing hierarchy.

## 5. Scientific safeguards

**Do not fabricate** data, results, numbers, citations, sources, experimental conditions, mechanisms, definitions of author-created concepts, or design decisions. Treat claims, datasets, assumptions, results, scope qualifiers, numbers and units, citations, mathematical expressions and symbol meanings, and labels and references as protected scientific content. Any substantive change requires a reason and semantic verification, even if it improves the prose.

If important information is unavailable, use `[AUTHOR: ...]` for an author decision or `[VERIFY: ...]` for a claim requiring checking **only where the gap materially matters**. A `[FIGURE: ...]` placeholder may describe an evidence-grounded figure that cannot yet be produced; never invent its contents. Collect unresolved placeholders in a concise author-to-do section. Do not quietly strengthen a tentative claim or delete substantive information because it appears outside an inferred contribution.

Classify interventions by the **type of change**, not its severity: **Local** changes expression without intended scientific or organizational effects; **Semantic** changes claims, definitions, assumptions, mathematical meaning, or other scientific content; **Structural** changes the ordering, grouping, or inclusion of material. Types can overlap: a structural rewrite may also change meaning. Assess scientific risk separately, and explicitly verify every Semantic and Structural change. Do not call these categories risk levels.

For revisions with suitable original and revised sources, follow `references/verification.md` for the comparison procedure, the `approved_changes.txt` specification, and the bundled verifier. If complete verification is impossible, report the limit rather than claiming success.

## 6. Reference selection and deliverables

The definitions and workflow above always apply. **Reference files are not automatically in context.** Read a file when its condition below is met, and do not assume another reference has been read. All shared definitions needed across tasks are in this file; references expand task-specific techniques and should not duplicate common rules.

| Read when the task involves… | Reference |
|---|---|
| Substantial logical design, writing, restructuring, or reader-oriented review across paper, paragraph, equation, figure, or table | `references/composition.md` |
| Detailed question-driven planning or an explicitly requested completeness audit; select only relevant prompts | `references/questions.md` (optional adapted 60QA) |
| Writing, diagnosing, or substantially revising an Introduction | `references/introduction.md` |
| Writing, diagnosing, or substantially revising an Abstract or summary paragraph | `references/abstract.md` |
| Systematic diagnosis, reverse outlining, or a structured reader-difficulty report | `references/diagnosis.md` |
| Writing or substantially revising an implementation-ready pre-experiment manuscript, or explicitly auditing design completeness | `references/pre-experiment.md` |
| Checking a target venue's submission requirements or refining a post-experiment manuscript for that venue | `references/submission.md` |
| Establishing notation conventions, resolving symbol ambiguity, or changing symbol identities | `references/notation.md` |
| Substantive scientific revisions, protected-element checks, or comparing original and revised versions | `references/verification.md` |

Pre-experiment status alone does **not** authorize a full research-design audit when the user requested only readability feedback; writing an implementation-ready specification does require sufficient implementation detail. Do not use optional references as compulsory checklists.

Report in the **user's language**, while quoting manuscript excerpts in their source language. For a diagnosis, prioritize actionable findings with locations and expected reader benefits. For a revision, provide the revised copy, major decisions, relevant scientific checks, and unresolved questions. For new writing, provide the manuscript and material assumptions or gaps. Keep the report proportionate to the request.
