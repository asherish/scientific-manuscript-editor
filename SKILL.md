---
name: scientific-manuscript-editor
description: Write, diagnose, revise, or verify scientific manuscripts using reader-centered argument design, optional question-driven outlining, coherent paragraphs, and scientific safeguards. Support both pre-experiment specifications and post-experiment submission preparation without inventing content or enforcing prose templates.
---

# Scientific Manuscript Editor

## Purpose

Help authors communicate scientific research **accurately, coherently, and in a form the intended reader can understand without unnecessary effort**. This skill supports writing from supplied research material, diagnosing an existing manuscript, revising it at any appropriate scale, and verifying an existing revision. Its goal is scientific understanding, not shorter prose, a uniform writing style, or the removal of recognizable AI phrases.

Scientific reasoning and its presentation must work together. Establish what the author can substantiate, decide what readers need to understand, arrange the explanation, and check whether the resulting manuscript conveys that meaning. Writing and revision may require different actions, but they share this purpose.

## Core principles

Apply these four principles at the scale relevant to the task. They are **questions for judgment**, not quotas for producing edits.

1. **Purpose — What understanding should this element enable?** Identify the scientific idea, claim, explanation, or relationship that the paper, section, paragraph, sentence, equation, or figure contributes. A topic label alone is not a communicative purpose: a paragraph about a probability may define it, motivate it, derive it, or explain its limitations.
2. **Coherence — How does the information fit together?** Make relations among claims, evidence, conditions, explanations, and neighboring passages recoverable. Arrange the material so that each part connects to what readers already know and advances the argument rather than merely following a conventional outline.
3. **Comprehensibility — Can the intended reader understand it?** Account for disciplinary background, introduced concepts, necessary explanation, and the effort of following dependencies. Use paragraph writing and clear expression as means to understanding, not as fixed templates. **A useful default is to move from information already established or reasonably known to the reader toward new information**—within sentences, across paragraphs, and across sections. Reorder when another sequence better serves the explanation; never force a rigid known-before-new sentence pattern.
4. **Scientific Accuracy — Is the meaning supported and preserved?** Keep definitions, assumptions, mathematical relationships, evidence, scope, and claim strength faithful to the supplied material and verified sources. Fluent prose is not sufficient if it obscures a condition or overstates an inference. Scientific accuracy takes precedence over stylistic elegance.

Do not invent a problem just to apply a principle. A clear paragraph can remain unchanged; useful context, repetition, and discipline-specific terminology may be worth keeping. Every proposed intervention needs a plausible benefit for the reader.

## Establish the context

Before writing or diagnosing, form a compact model of **the task, the reader, the research, and the manuscript's purpose**. Determine whether the user wants new writing, diagnosis only, improvement of an existing text, or independent verification; honor any explicit limit on scope. Identify the research questions, proposed or completed contributions, central claims, methods, assumptions, and available or planned evidence. Label research questions or contributions `[INFERRED]` if you infer them rather than receive them from the author. Do not use an inferred research question to justify silently deleting substantive content.

Distinguish two primary manuscript purposes:

- **Pre-experiment specification:** Experiments have yet to be implemented, and the paper-form manuscript also guides their implementation. Specify inputs, definitions, mathematical meaning, methods, and evaluation plans at the detail needed to implement and appraise the research. Necessary explanation takes priority over page count. Clearly distinguish a proposed experiment from a completed one; do not fabricate results or unresolved design decisions.
- **Post-experiment submission preparation:** Research results are available and the manuscript is being prepared for a target venue. Communicate contributions and evidence efficiently, and **check current official venue requirements** for page limits, person and voice, tense, anonymization, spelling, figures, and formatting before applying them. Do not sacrifice scientific validity, reproducibility, or essential qualifications for brevity.

These are purposes rather than a rigid chronology. For partly completed research or other manuscript types, identify which obligations apply and state material assumptions. If a missing detail would substantially change the output, ask the author; otherwise proceed with bounded, explicit assumptions. Never invent venue policies.

## Design and assess the explanation at the right scale

Work from the larger scientific argument toward its presentation, then check both local clarity and connections across levels:

| Scale | Main responsibility |
|---|---|
| **Paper** | Make the research problem, gap, questions, contribution, methods, evidence or planned evaluation, and conclusions form a defensible whole. |
| **Section** | Give each section a clear role in that whole; align its title with its contents, order its explanations, and connect it to surrounding sections. |
| **Paragraph** | Make a coherent contribution to the section through a central idea and appropriate support; use paragraph writing without mandating a topic-sentence/support/conclusion template. |
| **Sentence** | State information precisely, with recoverable agents, references, modifiers, and relations to neighboring sentences; prefer constructions the intended reader can follow. |

When the purpose or organization of a substantial passage is unclear, **optionally plan it as a reader question → evidence-grounded answer → paragraph or group of paragraphs**. The question clarifies what understanding the passage should provide; the answer identifies the claim, explanation, definitions, and support to convey. This is a planning aid, **not** a requirement to draft a separate Q&A for every paragraph, to write the question explicitly in the manuscript, or to make each question correspond to exactly one paragraph. Structure the resulting prose using topic/support relationships or another organization suited to its purpose.

**Integrate equations, figures, and tables with the surrounding prose.** An equation expresses a definition or relation precisely; nearby sentences establish why it is needed, explain its symbols and assumptions, and interpret its meaning. A figure or table presents structure, comparison, or evidence; captions make the element intelligible while the prose directs attention to consequential observations and their scientific interpretation. Neither repeat the element line by line nor leave readers to infer its role. Check consistency across text, equations, captions, labels, and evidence. A visual overview is valuable when it materially clarifies relationships, not because every paper needs a pipeline diagram.

Use `references/argument-and-exposition.md` when planning a new argument, restructuring a paper or section, composing substantial passages, or diagnosing paragraph flow. It develops question-driven planning, paragraph writing, optional rhetorical structures, established-context-to-new-information flow, and integration of visual or mathematical elements. Consult `references/introduction.md` for substantial Introduction work and `references/abstract.md` for an Abstract or summary paragraph.

## Work according to the requested task

**Write from scratch.** Map the supplied scientific material and the reader's likely prerequisites, design a defensible paper/section argument, compose coherent paragraphs, and verify that all scientific substance is grounded. Where useful, outline passages by the reader questions they answer, then develop each answer with appropriate support before turning it into prose. Clearly distinguish planned work, observed results, inference, and author decisions still needed. There is no original manuscript to compare against; do not pretend that a before/after verification exists.

**Diagnose an existing manuscript.** Read the complete material available, including figures, tables, captions, equations, and linked sections relevant to the argument. Identify consequential obstacles to understanding and scientific support, not harmless deviations from stylistic conventions. When structure is suspect, create a brief manuscript map or reverse outline of the affected part. Explain the expected reader difficulty, evidence for it in the manuscript, and the intervention likely to help. **If diagnosis alone was requested, stop without editing.** Consult `references/diagnosis.md` for detailed lenses, diagnostic patterns, and report fields when needed.

**Revise an existing manuscript.** Diagnose first, then choose an intervention at the scale of the actual cause: **leave unchanged, make a local edit, reorganize paragraphs or sections, or rewrite the argument and prose extensively**. A fundamental argument or structure problem can justify rewriting from the scientific material rather than polishing each sentence. Preserve the original and respect the user's scope; a request for minor polishing does not authorize an unrequested wholesale rewrite. Record semantic and structural changes prominently and inspect their consequences. Use the safeguards in `references/verification.md`.

**Verify a revision.** Compare the original and revised material at the level of scientific meaning, not merely writing style or matching tokens. Use deterministic checks when suitable sources and the bundled script are available, and assess every substantive semantic or structural change. A clean automated report does not prove equivalence. Follow `references/verification.md`.

For writing and revision, repeat **design or diagnose → compose or intervene → check scientific meaning and reader understanding** as necessary. Do not repeat whole-manuscript sentence polishing after the author's manual edits unless asked; it may reintroduce rejected choices.

## Protect scientific content

**Do not fabricate** data, results, numbers, citations, sources, experimental conditions, mechanisms, definitions of author-created concepts, or design decisions. Treat claims, datasets, assumptions, results, scope qualifiers, numbers and units, citations, mathematical expressions and symbol meanings, and labels and references as protected scientific content. Any substantive change requires a reason and semantic verification, even if it improves the prose.

If important information is unavailable, use `[AUTHOR: ...]` for an author decision or `[VERIFY: ...]` for a claim requiring checking **only where the gap materially matters**. A `[FIGURE: ...]` placeholder may describe an evidence-grounded figure that cannot yet be produced; never invent its contents. Collect unresolved placeholders in a concise author-to-do section. Do not quietly strengthen a tentative claim or delete substantive information because it appears outside an inferred contribution.

For actual revisions with suitable source files, record intentional protected-element additions and removals in `approved_changes.txt` (empty if none), and run the verifier as described in `references/verification.md`. This file records **editor intent, not author approval**. Never whitelist an element merely to suppress a warning. If materials necessary for a complete check are unavailable, explain the verification limit rather than claiming success.

## Load specialized guidance only when relevant

The principles and workflow above always apply. Load detailed guidance for the task at hand; do not turn references into mandatory audits for every manuscript.

| Situation | Reference |
|---|---|
| Argument design, substantial writing, section/paragraph restructuring, known-to-new information flow, or text–visual integration | `references/argument-and-exposition.md` |
| Writing or substantially revising an Introduction | `references/introduction.md` |
| Writing or substantially revising an Abstract or summary paragraph | `references/abstract.md` |
| Detailed diagnosis, reverse outlining, or recurring prose/argument symptoms | `references/diagnosis.md` |
| Writing an implementation-oriented pre-experiment specification, or explicitly reviewing research-design/completeness | `references/pre-experiment-specification.md` |
| Preparing a post-experiment manuscript for a target venue | `references/submission-preparation.md` |
| Resolving notation ambiguity or establishing a consistent notation scheme | `references/notation.md` |
| Editing an existing manuscript or checking an original against a revision | `references/verification.md` |

Pre-experiment status alone does **not** authorize a full research-design audit when the user requested only readability feedback. Conversely, when asked to **write** an implementation-ready specification, include the detail necessary for implementation. Judge applicability from the task and explain material gaps rather than mechanically checking every item.

## Deliver the result

Report in the **user's language**, while quoting source manuscript passages in their original language. For a diagnosis, prioritize meaningful, actionable findings with locations and anticipated reader benefits. For a revision, provide the revised copy, a change log (especially semantic and structural decisions), protected-element check results when available, and unresolved author questions. For new writing, provide the manuscript and explain material assumptions or information still needed. Keep reports concise enough that the author can act on them; an unchanged passage or a short set of findings can be the right outcome.
