# Adaptable 60QA question bank

This is an **adapted, paraphrased set of 60 optional planning questions**, organized using the seven sections and IDs of Komei Sugiura's *60 Questions & Answers (60QA)* approach. It preserves the coverage of the original question set while reframing some prompts to be useful beyond machine-learning conference papers. The source is acknowledged below; this file is not a verbatim reproduction or a venue requirement.

Use this reference **only** when a user requests a detailed question-driven manuscript outline, substantial section planning, or an explicit completeness/implementation audit. Select, combine, rewrite, or omit questions to fit the scientific problem, article type, and manuscript stage. A list of 60 prompts does **not** mean that the paper should contain 60 paragraphs, that each question must have its own paragraph, or that every question must be answered. The questions in a writer's outline need not appear in the manuscript.

For **pre-experiment specifications**, use questions about experiments and results to identify what must be planned or remains undecided; do not fabricate data or fill result slots with imagined findings. For **post-experiment submission preparation**, answer from completed work and verified sources, not the intended protocol. Use the official venue policy for formatting and reporting requirements. Question wording may assume a proposed method, learning model, or benchmark: mark such a question inapplicable when the research has no corresponding concept.

## 1. Introduction — 10 questions

| ID | Optional reader/reviewer question | Applicability note |
|---|---|---|
| 1-1 | What broader scientific, technical, or societal context makes the work worth considering? | Choose the context relevant to the paper; societal impact is not mandatory. |
| 1-2 | What precise task, phenomenon, or research problem does the study address? | General. |
| 1-3 | What concrete example or use case helps readers understand the problem? | If an example clarifies the task. |
| 1-4 | Why is the problem challenging, and where do existing approaches fail or become inadequate? | Ground limitations in evidence rather than generic difficulty claims. |
| 1-5 | What relevant limitations or unanswered questions remain across prior work? | Characterize the literature fairly; no fixed number of citations. |
| 1-6 | What does this study propose or investigate, and which part of the problem does it address? | Distinguish planned and demonstrated outcomes. |
| 1-7 | What is the most consequential distinction from the closest prior approaches? | Multiple genuine distinctions may exist; prioritize the central one. |
| 1-8 | Why should that distinction or design choice help address the identified limitation? | Separate plausible mechanism from established evidence. |
| 1-9 | What scientific contributions can this work substantiate? | Avoid unsupported novelty or exaggerated scope. |
| 1-10 | Would an overview figure materially clarify the setting, idea, or comparison? | Create only if useful and evidence-grounded; not conference-mandatory. |

## 2. Related Work — 4 questions

| ID | Optional reader/reviewer question | Applicability note |
|---|---|---|
| 2-1 | What does the first relevant line of research establish, and what important papers represent it? | Organize by substantive relationship, not arbitrary citation counts. |
| 2-2 | What other relevant research lines are needed to position the study? | Repeat by meaningful subfield if necessary. |
| 2-3 | Which established datasets, benchmarks, protocols, or reference tasks shape comparison in this field? | Only when such benchmarks exist and matter. |
| 2-4 | How does this work relate to the most similar methods or findings, including important similarities and differences? | Avoid caricaturing alternatives. |

## 3. Problem Statement — 8 questions

| ID | Optional reader/reviewer question | Applicability note |
|---|---|---|
| 3-1 | How is the target problem or research task formally defined? | General for a formal problem statement. |
| 3-2 | What would count as a valid, useful, or desirable solution or outcome? | Match the scientific objective, not just the proposed method. |
| 3-3 | Would a representative example, scenario, or schematic clarify the task? | Use only if it makes the formulation easier to understand. |
| 3-4 | What inputs or observations are available in the task, independent of this particular method? | Distinguish task inputs from method-internal features. |
| 3-5 | What output, estimate, decision, or explanation does the task require? | Specify units, domains, or granularity when important. |
| 3-6 | Which terms, quantities, and symbols must be defined for unambiguous interpretation? | Define author-created concepts explicitly. |
| 3-7 | What assumptions, exclusions, constraints, or scope boundaries does the formulation impose? | Do not silently generalize beyond them. |
| 3-8 | By what criterion or measure could a proposed solution be assessed? | Evaluation can be theoretical, empirical, or qualitative. |

## 4. Methodology — 10 questions

| ID | Optional reader/reviewer question | Applicability note |
|---|---|---|
| 4-1 | What method or approach is proposed, and how does it relate to existing methods or ideas? | It need not extend a named baseline. |
| 4-2 | Which parts of the approach could generalize beyond this specific implementation, and which cannot? | Discuss generality only to the extent supported. |
| 4-3 | What are the consequential methodological differences from the relevant alternatives? | A prose comparison or table may work better than a list. |
| 4-4 | Would a diagram of the method's structure, dependencies, or data flow improve understanding? | Only if grounded and useful. |
| 4-5 | What principal components or stages make up the approach, and how do they interact? | Do not invent modules solely for symmetry. |
| 4-6 | What are the method's inputs, mathematical representations, shapes or units, and definitions? | Dimensionality matters when it affects interpretation or implementation. |
| 4-7 | How are required features, intermediate quantities, or representations derived? | A learned backbone is only one possible case. |
| 4-8 | For each substantive component, what motivates it, what enters and leaves it, and how does it work? | Repeat for actual components, not a predetermined count. |
| 4-9 | How is the final estimate, prediction, or output constructed from the preceding definitions? | Use equations where they convey needed precision. |
| 4-10 | What objective, loss, optimization criterion, or decision rule governs the method? | Not all methods have a trainable loss function. |

## 5. Experimental Setup — 11 questions

| ID | Optional reader/reviewer question | Applicability note |
|---|---|---|
| 5-1 | If new data were created, why were existing resources insufficient, and what design and quality requirements guided collection? | Conditional on creating a dataset. |
| 5-2 | If established data were used, what are they, and why are they appropriate to this study? | Conditional on reusing data. |
| 5-3 | How were data collected, annotated, constructed, and quality-checked? | Describe relevant provenance and validation. |
| 5-4 | What preprocessing, filtering, transformations, or augmentation were applied, and why? | Distinguish planned from performed operations. |
| 5-5 | Which dataset or sample statistics are needed to assess scope, representativeness, and reproducibility? | Report domain-appropriate statistics, not an exhaustive fixed list. |
| 5-6 | How were development, training, validation, test, or other analysis partitions defined, and what are their sizes? | Use only partitions relevant to the design. |
| 5-7 | What role did each partition or data subset play, and how was leakage or dependent reuse avoided? | If partitions or repeated analyses are relevant. |
| 5-8 | Which parameter choices, computational procedures, and experimental settings are needed to reproduce the comparison? | A table can help; specific ML hyperparameters are conditional. |
| 5-9 | What model complexity or computational-cost quantities matter to the claim? | Trainable parameters/FLOPs only where meaningful. |
| 5-10 | Which hardware, instruments, software, or computational resources materially affect reproducibility? | Disclose consequential resources, not arbitrary specifications. |
| 5-11 | What training, processing, or inference time and efficiency measurements are relevant? | Measure using a defined unit and conditions; not always applicable. |

## 6. Experimental Results — 14 questions

| ID | Optional reader/reviewer question | Applicability note |
|---|---|---|
| 6-1 | What are the main quantitative comparisons, and how should the table or plot be read? | Explain units, variation, sample sizes, and comparison conditions when relevant. |
| 6-2 | Which baselines or reference conditions were actually compared? | A baseline algorithm is not required for every study. |
| 6-3 | Why are those comparators appropriate for the scientific claims? | Address fairness and representativeness. |
| 6-4 | How are the evaluation measures defined, and which directly address the primary objective? | Give mathematical definitions when helpful. |
| 6-5 | Why are these measures informative, and what important behavior might they miss? | Do not require unrelated metrics. |
| 6-6 | What are the actual values and relevant absolute differences, beyond relative improvements or rankings? | State evidence with calibrated precision and uncertainty. |
| 6-7 | What uncertainty, repeatability, or statistical evidence supports the observed differences? | Use appropriate tests/intervals if applicable; no universal p-value threshold. |
| 6-8 | Which representative successful examples illuminate the method's behavior, and what evidence supports their interpretation? | If qualitative examples are informative. |
| 6-9 | Which failures or counterexamples reveal important limitations, and what might explain them? | Number and balance of examples depend on the analysis. |
| 6-10 | What component, condition, or mechanism did each ablation or controlled comparison test, and what followed? | Only where an ablation is meaningful; do not claim causation without design support. |
| 6-11 | Would a confusion matrix or comparable error breakdown reveal behavior obscured by aggregate metrics? | Primarily relevant to classification; otherwise omit. |
| 6-12 | How frequent are consequential error or failure cases under a clearly defined denominator? | If counting failure cases is meaningful. |
| 6-13 | Can observed failures be grouped into interpretable categories with reproducible definitions? | If enough cases and information exist; no fixed sample count. |
| 6-14 | What appears to be the main bottleneck, what evidence supports that diagnosis, and what remedies remain hypotheses? | Separate observed limitation from speculation. |

## 7. Conclusion — 3 questions

| ID | Optional reader/reviewer question | Applicability note |
|---|---|---|
| 7-1 | What problem or scientific question did the paper address? | Keep consistent with the formulation and Introduction. |
| 7-2 | What contributions or findings are actually supported by the work? | Match wording and tense to completed versus planned work and venue style. |
| 7-3 | What important limitation, open question, or future direction follows from the evidence? | Do not invent generic future work merely to fill a closing sentence. |

## Turn selected questions into writing

1. Establish the intended reader, writing/revision task, manuscript stage, and scientific sources.
2. Pick **only** questions that illuminate actual parts of this paper; merge overlapping questions and add missing domain-specific ones.
3. Draft an evidence-grounded answer for each selected question, marking material missing facts or author decisions instead of guessing.
4. Group compatible answers into section and paragraph roles. Use **Question → Answer → Paragraph** when it helps; one question may span several paragraphs, and one paragraph may resolve related subquestions.
5. Choose an explanatory pattern (claim–support, context–content–conclusion, problem–solution, derivation, comparison, etc.) that serves the reader. Integrate equations, figures, and tables with prose rather than turning them into detached answers.
6. Check Purpose, Coherence, Comprehensibility, and Scientific Accuracy, including whether the supporting evidence warrants the conclusion. Do not generate a 60-item compliance report unless explicitly requested.

The question order here follows the **presentation sections** of the original 60QA, not a prescribed **writing order**. Drafting a sound formulation and evaluation plan before the Introduction can reduce rework; actual writing order should follow dependencies in the research and the author's needs. The source set has no standalone Discussion category; use `submission-preparation.md` for interpreting results, relating evidence to prior work, and discussing limitations.

**Attribution:** Adapted from the publicly described *60 Questions & Answers (60QA)* method of Komei Sugiura and his laboratory: https://komeisugiura.jp/software/software_jp.html. Additional paragraph-writing context: Mensh & Kording (2017), https://doi.org/10.1371/journal.pcbi.1005619, and Seitaro Iwama's lecture, https://speakerdeck.com/neuroiwm/paragurafu-kara-hajimeru-akademikku.
