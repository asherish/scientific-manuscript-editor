# Pre-experiment manuscript as an implementable specification

Use this reference when writing or substantially revising a paper-form manuscript whose experiments are not yet implemented and whose details will guide implementation. Also use it when the user explicitly requests research-design, reproducibility, implementation-specification, or completeness review. **Pre-experiment status alone does not trigger a separate exhaustive audit for a readability-only request.**

The goal is an understandable scientific paper that specifies enough to implement and appraise the work, not a standalone engineering manual. Page count is subordinate to necessary scientific detail. Mark planned work as planned; never write prospective outcomes as observed results.

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
