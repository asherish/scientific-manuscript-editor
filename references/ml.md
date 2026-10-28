# Machine learning: explain training and evaluation choices

Machine-learning manuscripts need additional detail to make learned components, data usage, and comparisons interpretable. Use the relevant sections below **when an ML model or training process is part of the work**. The classification-error guidance can also help with non-ML classifiers; in that case, skip the training-specific sections. The corresponding general section reference, selected through `SKILL.md`, remains responsible for the broader writing purpose.

## Explain what is learned and how it produces an output

Readers need to distinguish the learned parts of a system from the fixed transformations around them. Identify the architecture and relevant pretrained weights, then explain what each learned component receives and produces. State consequential feature representations, tensor dimensions, and how the final output is assembled.

Explain which parameters are trained, frozen, or fine-tuned. For example, if an image encoder is frozen and only a classifier is trained, say so before presenting the training objective. Define actual loss terms, weights, constraints, and optimization procedures where relevant; a non-learning method need not have any of them.

## Explain how data are separated and used

Readers must know which observations influenced model development and which were reserved for final evaluation. State the role of each partition actually used, its construction unit, and any grouping, temporal, spatial, or class constraints. Explain where preprocessing parameters, hyperparameters, checkpoints, and decision thresholds were fitted or selected so leakage can be assessed. For example, selecting a threshold on the test set changes what that test result can establish; disclose such reuse rather than describing the test set as untouched.

Report training settings that materially affect reproducibility. Depending on the system, these may include optimizer, learning-rate schedule, batch size, stopping criterion, augmentation, initialization, regularization, seeds, and repetitions. A compact table makes comparable configurations easier to inspect than a long prose inventory. Do not require a particular split or training recipe when the study uses another design.

## Compare computational costs under stated conditions

Computational comparisons are interpretable only when the workload and measurement conditions are known. Where efficiency matters, report relevant parameter counts, operations (such as FLOPs), memory, training cost, or inference time together with the input size, batch size, hardware, precision, and measurement procedure. Parameter count, theoretical operations, measured speed, and energy use represent different properties; do not treat them as interchangeable or report them when irrelevant to the claim.

## Choose error analyses that expose important behavior

An aggregate score may conceal which types of cases a system gets wrong. In classification, a confusion matrix or per-class breakdown can reveal these differences if class definitions, denominators, normalization, and single-label or multilabel behavior are clear. For regression, retrieval, segmentation, or generation, select a breakdown suited to that output rather than automatically adding a confusion matrix. This guidance also applies to a non-ML classifier.

## Make ablation comparisons interpretable

An ablation should help readers understand which design choice is under examination. Identify the variant, the changed component or training condition, the other conditions held fixed, and the outcome used for comparison. Explain what inference follows from the design and observed results. A particular variant-labeling convention is optional; a performance difference alone does not isolate causation when other conditions changed too.
