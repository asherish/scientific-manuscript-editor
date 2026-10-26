# Pre-experiment manuscript as an implementable specification

Use this reference when writing or substantially revising a paper-form manuscript whose experiments are not yet implemented and whose details will guide implementation. Also use it when the user explicitly requests research-design, reproducibility, implementation-specification, or completeness review. **Pre-experiment status alone does not trigger a separate exhaustive audit for a readability-only request.**

The goal is an understandable scientific paper that specifies enough to implement and appraise the work, not a standalone engineering manual. Page count is subordinate to necessary scientific detail. Mark planned work as planned; never write prospective outcomes as observed results.

## Use adaptable implementation questions

When creating a substantial specification or conducting an explicitly requested completeness review, it may help to treat each part of the manuscript as an answer to a question an implementer or reviewer would ask. This borrows the question-driven organization of Sugiura's *60 Questions & Answers (60QA)* without treating the number 60, one-question-per-paragraph, or any discipline-specific question as mandatory. Customize the questions to the research, then write integrated prose rather than a questionnaire unless the user explicitly requests a Q&A document.

| Part of the research | Illustrative implementer/reviewer questions |
|---|---|
| Problem and scope | What exactly is being studied? What counts as a valid output or solution? Which cases and assumptions are in or out of scope? |
| Data and inputs | What observations or data are available? At what unit or resolution? Why are these data suitable? |
| Method | What components are necessary, and what does each one consume, produce, and accomplish? Which definitions or parameters remain unsettled? |
| Evaluation | Which questions will each analysis inform? What comparisons, metrics, splits, and uncertainty assessments are needed? |
| Reproducibility | Which preprocessing, algorithmic decisions, data versions, selection procedures, and resources must be specified to repeat the essential work? |

There is no prescribed writing order. If definitions and evaluation targets are unstable, settle or flag them before polishing downstream sections. Some authors find it easier to draft the problem formulation and experimental plan before the Introduction; others have a clearer contribution after writing the evidence. Select an order that avoids propagating unresolved assumptions, rather than adopting one workflow mechanically.

## State the argument and formulation

Specify the research problem, question, proposed contribution, assumptions, and what planned evidence could bear on consequential claims. State inputs, outputs, objectives, constraints, units of analysis, and scope to the extent required for the proposed study. Explain author-created concepts and the role of non-obvious equations so another researcher can understand and implement them. Do not infer that a missing item is mandatory simply because a template contains it.

## Explain the proposed method

For substantive components, make their purpose, inputs, outputs, dependencies, and interactions recoverable. Motivate design choices that affect validity or implementation, without inventing a history of alternatives. Consider a conceptual overview or a diagram of inputs, transformations, and outputs when it materially reduces reader effort. Keep prose, equations, and diagrams complementary: necessary implementation meaning belongs in the explanation, not solely in a caption or variable list.

## Specify the planned evaluation at useful resolution

Make clear which experiment, study, or analysis will inform each material research question or claim. A rigid one-to-one mapping of contributions to plots or experiments is unnecessary. As applicable, specify:

- Data sources and versions, collection, cleaning, preprocessing, and spatial/temporal units.
- Sampling, splits, baselines, comparison fairness, and leakage controls.
- Metrics and operational definitions, thresholds and their selection, ablations, and uncertainty treatment.
- Hyperparameters and their selection procedures, random seeds or repeated trials, and computational settings when consequential.
- The intended analyses or comparisons, and what they can and cannot establish.

Explain planned interpretations according to whether the study is hypothesis-driven, exploratory, descriptive, or qualitative. Do not force a binary accept/reject outcome when the evaluation does not support one.

## Prepare results presentation without inventing results

Describe planned tables and figures when their purpose affects the implementation: axes, columns, comparison groups, relationships, and the intended reader question. Do not create fabricated numbers, outcomes, or diagrams. Explain known limitations and threats to validity concretely, and distinguish open decisions from fixed conditions.

## Apply completeness prompts proportionately

For an explicit completeness or implementation review, report only material gaps that block implementation, scientific appraisal, or interpretation. Identify where information is missing, why it matters, and whether the author must supply it. Mark genuinely irrelevant prompts `N/A` with a short reason when reporting in checklist form is useful; do not manufacture compliance scores or scatter placeholders throughout a readable draft merely to fill a list.
