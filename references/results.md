# Results: connect observations to warranted answers

Readers should be able to trace each important result from **the question motivating an analysis to the observation and the answer it supports**. Completed studies report actual findings; pre-experiment manuscripts can only describe planned displays and analyses.

## Lead each substantial result with its purpose

An analysis becomes meaningful when readers know why it was performed. Introduce the evaluated setting when necessary, then organize findings by the questions or propositions they address rather than merely recounting the order of experiments. A useful pattern is **question or motivation → observation → warranted answer**. Later results can build on the answers established earlier; headings should match what the evidence actually shows. Where the Introduction uses short contribution labels, let readers recognize the corresponding evidence and question in Results. Preserve the distinction between a demonstrated finding and a planned goal or hypothesis.

## Explain what each numerical comparison shows

Before interpreting a table or plot, orient readers to the comparison it represents. Make axes, rows, columns, units, sample sizes, repetitions, and aggregation clear through the caption and nearby prose. Then identify the few observations that matter for the research question. Report actual values and absolute differences where informative; a relative improvement alone may conceal the practical size of a change.

When a visual would benefit from a short bold takeaway tag or a more informative encoding, consult `figures.md`; avoid unsupported headlines and preserve the venue's caption rules.

For an illustrative writing contrast, “Method A performs better (Table 2)” leaves the comparison and its meaning unclear. A more informative account would identify **the metric, evaluation condition, observed difference, and scope of the inference**. This is a writing example, not an assertion about any measured study.

Report uncertainty, variability, repeatability, or statistical comparisons at the level the design supports. Distinguish an effect's estimated magnitude from statistical and practical significance. Use the measures and comparators defined in `experiments.md`, or explain a consequential change in the analysis. A claimed improvement should be evaluated in light of effect magnitude, the variation represented by its interval or error bar, the study design, and any meaningful difference in tuning or compute budget. Do not infer general superiority from a narrowly selected best run.

## Use examples and failures to explain behavior

Qualitative examples are valuable when they reveal something an aggregate measure hides. Introduce why a success, counterexample, or failure was selected, then point to the feature that supports the interpretation. Avoid captions or paragraphs that merely announce an image and expect readers to infer the result for themselves. Selected examples do not establish population-wide prevalence without a defensible sampling procedure. When patterns of failure suggest a mechanism, state a **testable explanation** and what additional stratification, control, or measurement could distinguish it from alternatives. A vivid example alone does not demonstrate its cause.

When error frequency or severity matters, specify the denominator and distinguish total observed failures from illustrative cases. Group failures into meaningful, reproducibly defined categories when the data permit. Select a breakdown appropriate to the task; classification-specific examples such as a confusion matrix appear in `ml.md`.

## Bound what controlled and exploratory findings establish

A controlled comparison is interpretable only relative to the factor that changed and the conditions that stayed fixed. For ablations or sensitivity analyses, name that contrast, report the observed outcome, and distinguish supported conclusions from possible confounding explanations. Discuss dominant bottlenecks using observed evidence; label a proposed remedy as a hypothesis until it has been evaluated.

Separate analyses specified before examining outcomes from exploratory checks added after observing the data. Both can be informative, but exploratory observations should not be described as independent confirmation.

Results should explain **what the evidence establishes**. Broader implications, relationships to previous literature, and limits on generalization can be developed in Discussion. Figures and tables carry detail; prose selects and explains the observations that answer the question, without repeating every cell or bar.

## Sources and applicability

- MIT EECS Communication Lab, *Paper: Results* — connecting the motivating question, analysis, figures or tables, and observed finding: https://mitcommlab.mit.edu/eecs/commkit/journal-article-results/
- Faloutsos, *MetaPaper v14* — aligning experiment questions and contribution labels; optional short figure-caption messages: https://www.cs.cmu.edu/~christos/MetaPaper/faloutsos_MetaPaper_v14.pdf
- Weissgerber et al. (2015), *Beyond Bar and Line Graphs* — the limitations of plots that conceal empirical distributions: https://doi.org/10.1371/journal.pbio.1002128
- Mensh and Kording (2017), *Ten Simple Rules for Structuring Papers*, Rule 7 — a logical progression of results supported by evidence and figures: https://doi.org/10.1371/journal.pcbi.1005619
- Ulmer et al. (2022), *Experimental Standards for Deep Learning in Natural Language Processing Research* — experimental analysis and fair comparison in NLP: https://aclanthology.org/2022.findings-emnlp.196/
- van Miltenburg et al. (2021), *Underreporting of Errors in NLG Output, and What to Do About It* — identifying, categorizing, and reporting error behavior beyond aggregate metrics: https://aclanthology.org/2021.inlg-1.14/

Error-category examples in the last source are specific to natural-language generation. Generalize the need for systematic failure analysis, not those particular categories or a required number of examples.
