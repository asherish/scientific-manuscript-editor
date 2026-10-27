# Experiments: make the evaluation credible and reproducible

Use this reference when planning, writing, diagnosing, or substantially revising an Experimental Setup, Evaluation Protocol, Study Design, or related methods-of-evaluation passage. Its purpose is to establish **what evidence the study can produce, why it is informative, and how the procedures can be reproduced or critically assessed**. Apply only the parts relevant to empirical, simulation, human-subject, observational, or computational work.

## Explain data selection and construction

Identify each data source or dataset and explain its suitability for the scientific question. When collecting or creating new data, justify why available resources are insufficient and describe the required coverage, sampling, measurement, or quality properties. Explain collection, annotation protocols, instructions, validation, disagreement handling, and provenance to the degree that they affect interpretation and reproducibility. When using established data, give the relevant versions and selection criteria rather than treating name recognition as a rationale.

Specify material preprocessing, filtering, transformations, aggregation, and augmentation, including their order and effects. Report the statistics readers need to judge size, representativeness, completeness, and granularity: the relevant counts, distributions, observation periods, measurement units, annotators, or study conditions depend on the field. Do not reproduce an irrelevant fixed inventory of dataset statistics.

## Define partitions, controls, and comparisons

Explain how training, development, validation, testing, calibration, or other data partitions are formed **when the study uses them**, along with their sizes or allocation rules and permitted uses. Describe measures that prevent leakage, dependent reuse, selection bias, or incomparable sampling. Not all studies use train/validation/test splits; specialized ML guidance is in `ml.md`.

Choose reference conditions, baselines, and comparator methods to test the study's material claims. Explain what each comparison is meant to establish and why it is fair under differences in data, assumptions, tuning, or computational budget. An ablation or controlled variation should name the design factor being changed, the claim it probes, the held-constant conditions, and the inference the contrast permits. Do not prescribe ablations when they cannot isolate a meaningful question.

## Define measures and interpretation limits

Identify primary and secondary evaluation measures, their operational or mathematical definitions, direction, units, aggregation, and relevant denominators. Explain why they address the central objective and which important properties they cannot capture. In a pre-experiment specification, fix or flag consequential choices such as thresholds, confidence procedures, exclusions, sample sizes, spatial or temporal resolution, and statistical analysis methods. Do not add arbitrary metrics just to appear thorough.

Specify how repeated trials, uncertainty, variability, statistical comparisons, and sensitivity analyses will be handled where meaningful. A universal `p < 0.05` rule is not appropriate across research designs; the uncertainty method must match the data and inferential claims.

## Report resources and execution conditions

Describe parameter selection, algorithms, software, seeds, instruments, hardware, and resource requirements that materially affect replication or a claim about efficiency. Report computational complexity, processing time, training time, or per-sample inference cost when meaningful, with a defined workload, measurement environment, and denominator. Model parameter counts and FLOPs are machine-learning-specific examples, not required outputs for every paper; detailed cases belong in `ml.md`.

For planned experiments, state protocols and intended comparisons without manufacturing results. For completed experiments, use the actual conditions and disclose material deviations from the proposed plan. The Results section should report what happened under these conditions rather than redefining the evaluation after observing outcomes.
