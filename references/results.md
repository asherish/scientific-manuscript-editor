# Results: show evidence and what it supports

Use this reference when writing, diagnosing, or substantially revising a Results, Findings, or Evaluation Results section. A reader should recover **the question behind an analysis, the observation that answers it, and the strength and limits of the inference**. Report observed data rather than the author's expectations; for a pre-experiment manuscript, only design proposed displays and analyses without supplying fabricated values.

## Organize findings as connected answers

Begin with an overview of the evaluated setting or approach when readers need it to interpret the findings. Then organize substantial passages by the questions, comparisons, or propositions they establish, rather than a chronology of every experiment conducted. A useful, optional progression is motivation or question → relevant observation → warranted answer. Check that each later claim uses prior findings consistently and that the section's headings reflect what is actually demonstrated.

## Make quantitative comparisons interpretable

Introduce each consequential table or plot with the comparison it answers. State how to read axes, row and column meanings, units, sample sizes, repetitions, aggregation, uncertainty summaries, and relevant conditions when they are not already clear from the caption. Present observed absolute values and differences where those matter; a relative improvement alone can obscure practical magnitude or poor baseline performance.

Report variability, repeatability, confidence or uncertainty intervals, and formal statistical evidence when appropriate to the design. Distinguish statistical significance, effect size, practical relevance, and descriptive variation. Do not attach a significance claim to an unspecified test or use a universal p-value cutoff. Use the measures and comparators justified in `experiments.md`; if an analysis differs, explain why.

## Explain examples and failure behavior

Select informative qualitative successes, counterexamples, or failures to illuminate behavior that aggregate metrics conceal. Explain **what the example shows and which observation supports that interpretation** rather than asking the reader to interpret a figure without guidance. Examples should not be presented as representative of a population without a defensible sampling rationale.

When failures matter, define their denominator and frequency, distinguish observed cases from selected illustrations, and group them into meaningful failure modes using explicit, repeatable definitions where the data permit. An error breakdown such as a confusion matrix is useful for some classification tasks, not a requirement for other studies; see `ml.md` for classification-specific practice.

## Interpret controlled comparisons without overstating them

For ablations, sensitivity studies, or other controlled comparisons, identify the factor varied and report the observed change under the conditions set out in the evaluation protocol. Explain what the comparison supports and what remains confounded or uncertain. Discuss dominant bottlenecks or plausible failure mechanisms with evidence, and label proposed remedies as hypotheses unless they have actually been tested.

The main Results narrative should remain distinct from broader implications and literature-level interpretation, which may belong in Discussion. Figures and tables contain evidence; prose identifies salient observations, makes defensible inferences, and connects them to the research questions without reciting every cell or bar.
