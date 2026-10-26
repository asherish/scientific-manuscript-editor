# Diagnose obstacles to scientific understanding

Use this reference for substantive readability or structure diagnosis. Diagnose problems because they affect the reader, **not** because text violates a preferred phrasing rule. Follow the task boundary and intervention choices in `SKILL.md`.

## Trace the reader's path

Read all available relevant text, equations, figures, tables, and captions before reporting a structural finding. Make a compact manuscript map of the claims, section roles, definitions, and evidence. When the organization is hard to follow, use a **reverse outline**: write one short description of what each paragraph accomplishes, then inspect redundancy, missing links, misplaced explanations, and dependencies. Do this only where it clarifies an actual structural doubt.

For each suspected obstacle, ask what the passage should enable the intended reader to understand, what knowledge is already available, where understanding breaks down, and which change would help. A likely difficulty is a prediction about readers, not observed user-study evidence; explain it as such.

When a paragraph seems directionless, **optionally reconstruct its implicit reader question and the answer it offers**. Check that the supporting explanations or evidence actually establish that answer, and that the conclusion does not go beyond them. A missing literal question, a topic sentence that is not first, or an absent concluding sentence is not a defect by itself. For complex sections, a question-to-paragraph map can reveal redundant answers, missing links, or unanswered reader needs. This is a diagnostic scaffold, not another mandatory output artifact.

## Optional diagnostic lenses

Use the lens or lenses that explain a material problem. **Do not produce findings merely to fill every category.**

| Lens | Possible difficulty |
|---|---|
| L0 — Relevance | Material does not help establish the problem, contribution, method, evidence, or interpretation. |
| L1 — Scientific support | A consequential claim lacks adequate support, exceeds evaluated scope, or conflicts with a figure, table, equation, or assumption. |
| L2 — Structure | Readers cannot see how parts fit together, why they appear in this order, or how they establish the contribution. |
| L3 — Concepts and notation | Ambiguous terminology, undefined concepts, or inconsistent symbols prevent correct interpretation. |
| L4 — Logical continuity | An intended cause, contrast, condition, inference, or transition is hard to recover. |
| L5 — Expression | Sentence construction imposes avoidable effort or obscures an agent, action, reference, or meaning. |
| L6 — Information allocation | Necessary explanation is missing or detail/repetition consumes attention without helping readers. |

## Recurring symptoms and their likely causes

The following are **diagnostic prompts, not banned expressions or automatic substitutions**. Fix the underlying issue if one exists. Some are common in LLM-generated prose, but none is a reliable marker of authorship.

| Symptom | Question to ask or possible repair |
|---|---|
| “crucial,” “pivotal,” “important,” “key role” | What mechanism or evidence establishes importance? State it, qualify the claim, or remove unsupported emphasis. |
| “robust,” “comprehensive,” “extensive,” “thorough” | Which scope, noise levels, datasets, or testing conditions support the description? |
| “significant(ly)” | Is significance statistical or practical? Give the test/effect size if available, or use accurate descriptive language. |
| “substantially,” “dramatically,” “remarkably” | What effect size and baseline justify the modifier? |
| “novel,” “first,” “unique” | New in relation to which particular prior work? Flag unsupported novelty. |
| “state-of-the-art” | Which benchmark, metric, and comparison set establish this? |
| “It is important to note that,” “In this paper we aim to” | Is framing obscuring the substantive statement? Prefer the actual action or finding where appropriate. |
| “delve into,” “shed light on,” “pave the way for” | Would a precise verb such as measure, compare, or explain convey the claim better? |
| “Furthermore,” “Moreover,” “Additionally” | Is the connection addition, or actually cause, contrast, condition, or evidence? |
| “Thus,” “Therefore,” “Hence” | Does the previous sentence really support the inference? |
| “Notably,” “Importantly” | Why is the result notable? State the reason if needed. |
| “In other words,” “Overall,” “In summary” | Does repetition help independent comprehension, or merely restate the same idea? |
| Paragraph has several unrelated topic moves | Would splitting or reordering the explanations make the central purpose recoverable? |
| Topic sentence or closing claim exceeds the supporting details | What narrower conclusion actually follows from the presented evidence? |
| A section lists analyses but not their motivating questions | Can readers see why the analyses were performed and which claims they inform? |
| Method starts with component details | Would an overview of purpose, dependencies, and inputs/outputs orient readers? |
| Abstract/Introduction starts with a universal truth | Does the premise lead specifically toward this paper's problem and gap? |
| Equation followed only by “where x is…” | Does the reader know what the equation computes or defines and why it is needed? |
| Figure with section names in boxes and arrows | Does it communicate actual entities, dependencies, or transformations? |
| Three-item lists, “not only X but also Y” | Does each item or contrast contribute substance, or just rhythm? |
| Generic limitations and future work | Have actual scope boundaries, uncertainty, and weaknesses been explained? |
| Terminology drift (region/area/zone; method/framework/pipeline; risk/hazard/score) | Are different terms describing one concept without reason? Use a defined term consistently. |
| Bold mini-headings, em-dash chains, lists inside prose | Do these conflict with reader needs or venue style? Treat as low-priority if harmless. |

Known-to-new information flow can diagnose abrupt transitions: if a sentence introduces several unfamiliar entities before giving readers a usable anchor, move established context forward or add a bridge. But **do not impose a fixed given-before-new word order**; see `references/composition.md` for examples and exceptions when that file is also selected by `SKILL.md`.

## Report actionable findings

Prioritize by expected impact on understanding. For each material finding, provide an **ID and location**, the likely reader difficulty and its textual basis, a proposed intervention and expected benefit, and **feasibility** (`Yes`, `Partial`, or `No`). When the likely intervention is clear, indicate its anticipated **change type(s)** from `SKILL.md` (`Local`, `Semantic`, and/or `Structural`); do not present them as risk levels or pretend an edit has already occurred. Report consequential scientific risks separately and group repeated manifestations of one cause.

Keep diagnosis separate from editing. An author may choose a local fix, section reorganization, or complete rewrite after understanding the diagnosis. Do not promise to fix a missing scientific definition, result, or citation without author input or verifiable evidence.
