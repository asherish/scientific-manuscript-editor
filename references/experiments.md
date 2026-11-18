# Experiments: connect research questions to reproducible evidence

An Experimental Setup explains **what evidence a study can produce, why its comparisons are informative, and how its procedures can be reproduced or critically assessed**. The Experimental Setup **should** cover the procedures and evidence relevant to its actual computational, observational, simulation, or human-participant design.

**Map the main claims to answerable experimental questions.** For each consequential contribution, identify the experimental question, the evidence needed to answer it, the conditions under which the answer would hold, and where the result will be reported. When several contributions need to be tracked across the manuscript, **consider** concise, stable labels linking the Introduction, experiments, Results, and Conclusion. A pre-experiment manuscript describes planned evidence rather than findings.

## Organize the setup around questions and design choices

The opening **should** orient readers to the main evaluation objectives and the role of each experiment. When experiments share data, partitions, metrics, or conditions, explain the shared setup together and identify experiment-specific differences where they are used. Group subsections around related questions or experiments, making the corresponding Results easy to locate.

Each paragraph or paragraph group **should** establish the purpose of a design choice or procedure before details become difficult to interpret. State consequential choices and their rationale early, then develop the procedure and conditions needed to assess or reproduce them. Use context already established rather than repeating a motivation readers can readily recover.

When a setup passage reads as an unexplained inventory or its relation to the research question is unclear, **consider** one of these explanatory progressions:

| Explanatory role | Possible progression |
|---|---|
| Data selection | Required evaluation properties → selected data and reasons for their fit → scope represented |
| Data construction or preprocessing | Purpose → operations and conditions → resulting analysis cases |
| Comparative experiment | Question → comparators and controlled conditions → evaluation procedure → scope of the inference the design permits |
| Evaluation measure | Property to assess → metric and calculation → interpretation and consequential omissions |

The final element of an experiment's explanation identifies what the design can distinguish; it does not announce an unobserved result. Describe data construction and execution steps in the order needed to trace how observations are processed or transformed. Distinguish that operational sequence from the author's history of trial and error. Keep one continuous explanation together; use a table or schematic when prose would only enumerate settings. Apply the general paragraph guidance in `composition.md`.

## Explain why the data can answer the question

Data are useful only insofar as they represent the phenomenon the study aims to examine. Identify each source and explain its fit with the target population, task, measurement, or setting. If new data were needed, explain which requirements existing resources could not meet. If established data were selected, state the consequential versions and selection criteria rather than relying on the dataset name alone.

Describe how the data were collected or constructed. Where applicable, include sampling, annotation instructions, quality checks, disagreement handling, and provenance. Then explain preprocessing, filtering, aggregation, transformations, and augmentation in an order that reveals how raw observations become analysis-ready cases.

Report the statistics needed to judge the resulting dataset's scope and limitations. These might be counts, distributions, observation periods, units, annotator characteristics, or study conditions; select them according to the actual design. A long table of irrelevant dataset attributes does not improve reproducibility.

Where relevant, document intended use, licensing or access restrictions, privacy safeguards, population or class coverage, and consequential data biases. Data documentation should explain how the dataset can support the study's purpose, not merely catalog metadata. See Gebru et al.'s *Datasheets for Datasets* and applicable research-ethics guidance.

## Make data allocation and leakage controls visible

When observations are divided for fitting, selection, calibration, or final evaluation, explain **how the partitions were made and what each was used for**. Give meaningful sizes or allocation rules and describe steps that prevent leakage or dependent reuse. For example, a time-dependent evaluation may need a chronological split so later observations do not influence an earlier forecast. State each partition's construction unit and consequential grouping, temporal, spatial, or class constraints.

Audit **independence at the unit required by the scientific claim**: records can be disjoint yet share a person, location, encounter, recording session, time period, or near-duplicate content. Consider whether feature engineering, preprocessing, normalization, hyperparameter selection, or pretraining exposed test information. If such dependence cannot be ruled out, qualify what the test can establish rather than calling it independent.

For learned or tuned systems, identify which observations influenced development and which were reserved for final evaluation. Explain where preprocessing parameters, hyperparameters, checkpoints, and decision thresholds were fitted or selected. Check whether overlapping pretraining sources or model-selection data contaminate the intended evaluation. Grouped or temporal evaluation is warranted by the scientific generalization or deployment claim, not automatically by the use of ML. If a test set was reused to select a threshold or model, disclose that reuse and its effect on what the evaluation can establish.

## Choose comparisons that test specific claims

Each baseline or reference condition should serve a scientific purpose. Explain what claim a comparison tests, why the alternatives are relevant, and whether they have comparable inputs, assumptions, tuning, or computational budgets. If important conditions differ, make that limitation clear before interpreting the results.

For trained or tuned models, assess whether search effort, validation access, data availability, and compute budgets are comparable. Disclose how much validation search and training compute each approach received where known; identify unavailable information and its effect on the comparison. A single best test-set score may conflate model quality with hyperparameter-search effort and does not establish superiority at comparable search budgets. Do not manufacture a controlled comparison when the study lacks one.

An ablation or controlled variation asks whether changing a specified factor alters an outcome under comparable conditions. Identify the evaluated variant, changed component or training condition, other conditions held fixed, and outcome used for comparison, then state the inference the contrast is designed to support. When a controlled variation can answer a meaningful question, **consider** including it.

## Explain what the metrics measure and what they miss

Readers cannot judge a result without knowing what the evaluation measure means. The Experimental Setup **should** identify primary and secondary metrics, define how they are computed, and explain their units, direction, aggregation, and relevant denominators. Connect the choice of measure to the original research question. Also state consequential behavior that a metric might conceal or fail to assess.

**Check construct validity explicitly:** Does the observable outcome represent the phenomenon or capability named in the claim? Are task definitions, labels, thresholds, sample selection, and metrics aligned with that claim? State important proxy assumptions and avoid claiming success on a broader target merely because a related benchmark score improved. Connect this audit to the task definition in `problem.md`.

Describe how repeated trials, variability, uncertainty, formal statistical inference, and sensitivity analyses will be handled when relevant. For an implementation-ready plan, settle or flag material choices such as thresholds, exclusions, sample sizes, and spatial or temporal resolution.

Define what error bars or intervals represent (for example, independent samples, random seeds, train/test splits, or bootstrap resamples), how they were computed, and what assumptions they require. Distinguish effect size, uncertainty, and practical meaning. There is no universal p-value threshold or standard set of tests suitable for every design; never treat a fixed significance threshold as a substitute for interpreting evidence.

## Document reproducible procedures and analysis status

Reproducibility depends on knowing which procedures and settings could change the outcome. Describe consequential algorithms, parameter-selection procedures, software, instruments, randomization, and computing resources. If the paper makes efficiency claims, report processing or training time, inference cost, or other meaningful measures with a defined workload and measurement environment.

For model-efficiency comparisons, report relevant parameter counts, operations such as FLOPs, memory, training cost, or inference time together with input size, batch size, hardware, precision, and measurement procedure. Parameter count, theoretical operations, measured speed, and energy use measure different properties; do not treat them as interchangeable or require a measure irrelevant to the claim.

When the study trains or fine-tunes a model, report settings that materially affect reproducibility. Depending on the system, these include optimizer settings, learning-rate schedule, batch size, stopping criterion, augmentation, initialization, regularization, seeds, and repetitions. Explain their selection rather than silently supplying defaults. When configurations are numerous or need direct comparison, **consider** a compact table instead of a prose inventory. A study using a fixed pretrained model without training should document the weights and inference conditions actually used, not describe unperformed training.

When the description of data use, optimization, model, and evaluation is difficult to audit, **consider** a compact **Data–Optimization–Model–Evaluation (DOME)** summary: dataset provenance and partitions; search/selection protocol; trained and frozen components; evaluation populations, metrics, and uncertainty. Describe only components and procedures actually present. Explain restrictions on sharing data or model artifacts; discuss consequential model or dataset-use limitations in `discussion.md`.

Keep the protocol's status clear: before experiments, describe intended conditions and unresolved decisions; after experiments, document the conditions actually used and material deviations. The Results section reports what occurred under the protocol and identifies any analyses that were added later. Distinguish analyses planned to test an existing question from exploratory follow-ups suggested by observed data; do not narrate post-hoc discoveries as if they were predetermined confirmation.

## Sources and applicability

- Nature Scitable, *Scientific Papers*, “Materials and methods” — early paragraph orientation, explanations of procedural choices, and alternatives to prose inventories: https://www.nature.com/scitable/topicpage/scientific-papers-13815490/
- MIT EECS Communication Lab, *Paper: Methods (CS)* — methodological rationale, replication detail, grouping related content, and correspondence with Results: https://mitcommlab.mit.edu/eecs/commkit/journal-article-methods-cs/

- Gebru et al. (2021), *Datasheets for Datasets* — data motivation, composition, collection, and documentation: https://doi.org/10.1145/3458723
- Pineau et al. (2021), *Improving Reproducibility in Machine Learning Research* — reproducible ML experiments and reporting: https://www.jmlr.org/papers/v22/20-303.html
- Ulmer et al. (2022), *Experimental Standards for Deep Learning in Natural Language Processing Research* — comparison and experimental-analysis practices in deep-learning NLP: https://aclanthology.org/2022.findings-emnlp.196/
- NeurIPS, *Paper Checklist Guidelines* — examples of transparent reporting for datasets, splits, hyperparameters, uncertainty, and computing resources: https://neurips.cc/public/guides/PaperChecklist
- Walsh et al. (2021), *DOME: Recommendations for Supervised Machine Learning Validation in Biology* — data independence, optimization, model and evaluation reporting: https://doi.org/10.1038/s41592-021-01205-4
- Dodge et al. (2019), *Show Your Work* — comparable results relative to hyperparameter-search and compute budgets: https://aclanthology.org/D19-1224/
- Bean et al. (2025), *Measuring What Matters* — construct validity of tasks and metrics: https://proceedings.nips.cc/paper_files/paper/2025/hash/1967e0fc3aa6cbbace562f5cb8e3954e-Abstract-Datasets_and_Benchmarks_Track.html
- ACL, *Responsible Research Checklist* — limits, data licensing, privacy, and experiment documentation where relevant: https://ethics.aclweb.org/roles/researchers/
- Nityasya et al. (2023), *On "Scientific Debt" in NLP: A Case for More Rigour in Language Model Pre-Training Research* — ablations and comparisons under matched conditions (language-model-specific): https://aclanthology.org/2023.acl-long.477/
- Wagenmakers et al. (2012), *An Agenda for Purely Confirmatory Research* — differentiating planned tests from exploratory analyses: https://doi.org/10.1177/1745691612463078

Apply training-specific guidance only when the study performs training or fine-tuning, and model-efficiency guidance when relevant to the claim. DOME originates in supervised biological ML, and Nityasya et al. addresses language-model pretraining; transfer their applicable reporting and comparison principles without imposing domain-specific protocols.

These sources span ML, NLP, biological ML, LLM benchmarks, and psychology. Adapt their transferable design and reporting principles to the actual study; do not impose a venue's checklist, a biology-specific protocol, or psychology preregistration practices as universal requirements.

The Nature and MIT resources provide writing guidance for Methods. Apply their organizational principles here to experimental setup, keeping the proposed approach itself in the Method where appropriate. The role-specific progressions above are editorial applications of that guidance, not exact sequences prescribed or experimentally validated by those sources.
