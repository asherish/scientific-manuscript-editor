# Experiments: connect research questions to reproducible evidence

An Experimental Setup explains **what evidence a study can produce, why its comparisons are informative, and how its procedures can be reproduced or critically assessed**. Select the parts relevant to the actual research design; computational, observational, simulation, and human-participant studies do not share one fixed protocol.

**Map the main claims to answerable experimental questions.** For each consequential contribution, identify the experimental question, the evidence needed to answer it, the conditions under which the answer would hold, and where the result will be reported. Concise, stable contribution labels can connect the Introduction, experiment headings, Results, and Conclusion without imposing a one-question–one-experiment rule. A pre-experiment manuscript describes planned evidence rather than findings.

## Explain why the data can answer the question

Data are useful only insofar as they represent the phenomenon the study aims to examine. Identify each source and explain its fit with the target population, task, measurement, or setting. If new data were needed, explain which requirements existing resources could not meet. If established data were selected, state the consequential versions and selection criteria rather than relying on the dataset name alone.

Describe how the data were collected or constructed. Where applicable, include sampling, annotation instructions, quality checks, disagreement handling, and provenance. Then explain preprocessing, filtering, aggregation, transformations, and augmentation in an order that reveals how raw observations become analysis-ready cases.

Report the statistics needed to judge the resulting dataset's scope and limitations. These might be counts, distributions, observation periods, units, annotator characteristics, or study conditions; select them according to the actual design. A long table of irrelevant dataset attributes does not improve reproducibility.

Where relevant, document intended use, licensing or access restrictions, privacy safeguards, population or class coverage, and consequential data biases. Data documentation should explain how the dataset can support the study's purpose, not merely catalog metadata. See Gebru et al.'s *Datasheets for Datasets* and applicable research-ethics guidance.

## Make data allocation and leakage controls visible

When observations are divided for fitting, selection, calibration, or final evaluation, explain **how the partitions were made and what each was used for**. Give meaningful sizes or allocation rules and describe steps that prevent leakage or dependent reuse. For example, a time-dependent evaluation may need a chronological split so later observations do not influence an earlier forecast. This is a conditional illustration, not a required split for every study. ML-specific data-use decisions are covered in `ml.md`.

Audit **independence at the unit required by the scientific claim**: records can be disjoint yet share a person, location, encounter, recording session, time period, or near-duplicate content. Consider whether feature engineering, preprocessing, normalization, hyperparameter selection, or pretraining exposed test information. If such dependence cannot be ruled out, qualify what the test can establish rather than calling it independent.

## Choose comparisons that test specific claims

Each baseline or reference condition should serve a scientific purpose. Explain what claim a comparison tests, why the alternatives are relevant, and whether they have comparable inputs, assumptions, tuning, or computational budgets. If important conditions differ, make that limitation clear before interpreting the results.

For trained or tuned models, consider whether search effort, validation access, data availability, and compute budgets are comparable. A single best test-set score may conflate model quality with hyperparameter-search effort; report meaningful development or validation information where available and relevant. Do not manufacture a controlled comparison when the study lacks one.

An ablation or controlled variation asks whether changing a specified factor alters an outcome under comparable conditions. State the factor, what remains fixed, and the inference the contrast is designed to support. Include such analyses when they can answer a meaningful question, rather than adding them by convention.

## Explain what the metrics measure and what they miss

Readers cannot judge a result without knowing what the evaluation measure means. Identify primary and secondary metrics, define how they are computed, and explain their units, direction, aggregation, and relevant denominators. Connect the choice of measure to the original research question. Also state consequential behavior that a metric might conceal or fail to assess.

**Check construct validity explicitly:** Does the observable outcome represent the phenomenon or capability named in the claim? Are task definitions, labels, thresholds, sample selection, and metrics aligned with that claim? State important proxy assumptions and avoid claiming success on a broader target merely because a related benchmark score improved. Connect this audit to the task definition in `problem.md`.

Describe how repeated trials, variability, uncertainty, formal statistical inference, and sensitivity analyses will be handled when relevant. For an implementation-ready plan, settle or flag material choices such as thresholds, exclusions, sample sizes, and spatial or temporal resolution. There is no universal p-value threshold or standard set of tests suitable for every design. Define what error bars or intervals represent (for example, independent samples, random seeds, train/test splits, or bootstrap resamples), how they were computed, and what assumptions they require. Distinguish effect size, uncertainty, and practical meaning; never treat a fixed significance threshold as a substitute for interpreting evidence.

## Report the settings needed to reproduce the work

Reproducibility depends on knowing which procedures and settings could change the outcome. Describe consequential algorithms, parameter-selection procedures, software, instruments, randomization, and computing resources. If the paper makes efficiency claims, report processing or training time, inference cost, or other meaningful measures with a defined workload and measurement environment; ML-specific complexity measures are covered in `ml.md`.

Keep the protocol's status clear: before experiments, describe intended conditions and unresolved decisions; after experiments, document the conditions actually used and material deviations. The Results section reports what occurred under the protocol and identifies any analyses that were added later. Distinguish analyses planned to test an existing question from exploratory follow-ups suggested by observed data; do not narrate post-hoc discoveries as if they were predetermined confirmation.

## Sources and applicability

- Gebru et al. (2021), *Datasheets for Datasets* — data motivation, composition, collection, and documentation: https://doi.org/10.1145/3458723
- Pineau et al. (2021), *Improving Reproducibility in Machine Learning Research* — reproducible ML experiments and reporting: https://www.jmlr.org/papers/v22/20-303.html
- Ulmer et al. (2022), *Experimental Standards for Deep Learning in Natural Language Processing Research* — comparison and experimental-analysis practices in deep-learning NLP: https://aclanthology.org/2022.findings-emnlp.196/
- NeurIPS, *Paper Checklist Guidelines* — examples of transparent reporting for datasets, splits, hyperparameters, uncertainty, and computing resources: https://neurips.cc/public/guides/PaperChecklist
- Walsh et al. (2021), *DOME: Recommendations for Supervised Machine Learning Validation in Biology* — data independence, optimization, model and evaluation reporting: https://doi.org/10.1038/s41592-021-01205-4
- Dodge et al. (2019), *Show Your Work* — comparable results relative to hyperparameter-search and compute budgets: https://aclanthology.org/D19-1224/
- Bean et al. (2025), *Measuring What Matters* — construct validity of tasks and metrics: https://proceedings.nips.cc/paper_files/paper/2025/hash/1967e0fc3aa6cbbace562f5cb8e3954e-Abstract-Datasets_and_Benchmarks_Track.html
- ACL, *Responsible Research Checklist* — limits, data licensing, privacy, and experiment documentation where relevant: https://ethics.aclweb.org/roles/researchers/
- Wagenmakers et al. (2012), *An Agenda for Purely Confirmatory Research* — differentiating planned tests from exploratory analyses: https://doi.org/10.1177/1745691612463078

These sources span ML, NLP, biological ML, LLM benchmarks, and psychology. Adapt their transferable design and reporting principles to the actual study; do not impose a venue's checklist, a biology-specific protocol, or psychology preregistration practices as universal requirements.
