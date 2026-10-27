# Machine-learning-specific manuscript guidance

Use this reference **only** when a manuscript's research question, approach, or evaluation actually involves machine learning. Read the relevant general section reference as well under the `SKILL.md` routing rules; the guidance here supplies ML-specific detail rather than redefining section structure or scientific safeguards. For classification without an ML model, use only the relevant error-analysis guidance rather than assuming a training pipeline.

## Explain the model and training criterion

When the method uses a learned representation or backbone, identify the architecture and any pretrained weights or provenance needed to understand and reproduce it. Explain the feature representation, relevant tensor dimensions, stage interfaces, fine-tuning or freezing decisions, and how the final prediction is assembled. State the loss terms, objectives, weights, constraints, and optimization process if training is part of the method. These are conditional descriptions: a deterministic, probabilistic, or optimization-based method may have no backbone or trainable loss.

## Make data usage and tuning auditable

For supervised or self-supervised evaluation, report the roles of training, validation, test, and any other partitions actually used. Explain splitting units, class or group stratification, temporal or spatial separation, preprocessing fit, hyperparameter search, checkpoint or threshold selection, and any risk of information leakage as relevant. Distinguish a validation set used to choose models from an untouched test set used for final assessment. Do not impose one splitting convention across all research designs.

Provide consequential optimization choices such as optimizer, learning rate and schedule, batch size, epochs or stopping criterion, augmentation, initialization, regularization, seeds, repetitions, and selected hyperparameters when they affect reproducibility. A compact table is often helpful; avoid filling it with irrelevant defaults.

## Report computational burden and task-specific behavior

When efficiency or complexity matters to the paper, report trainable and total parameter counts, FLOPs or another computational measure, training compute/time, memory, and inference latency or throughput under specified input sizes, batch sizes, hardware, precision, and measurement conditions. Distinguish theoretical operations from measured runtime. Parameter count and FLOPs are not mandatory for every ML study, and are not interchangeable with speed or energy use.

For classification tasks, a confusion matrix or per-class error breakdown can expose failures hidden by aggregate metrics. Explain the class definitions, denominators, normalization, class imbalance, and whether outputs are single-label or multilabel. For regression, retrieval, segmentation, generation, or other tasks, choose the error breakdown that actually addresses the scientific question instead; no fixed diagnostic plot is universal.

In ablation studies, make variants and changed factors unmistakable while keeping other important conditions controlled. Explain which component or training decision each variation tests and which inferences the evidence supports. Do not require a particular variant-labeling scheme or interpret a correlated performance difference as isolated causation without an adequate design.
