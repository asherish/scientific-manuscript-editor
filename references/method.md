# Method: explain the approach from purpose to output

The Method should let readers understand **what the approach does, why its design is plausible, and how its parts produce the required output**. For an implementation-ready manuscript, that explanation must also be detailed enough to reconstruct consequential operations.

## Establish the central idea before implementation details

Readers need a mental model of the approach before they can interpret its individual components. The Method **should** begin with the objective established in the Problem Statement, the central design idea, and the consequential difference from relevant alternatives. A short overview of the stages and their relationships can prepare readers for the details that follow. Use a diagram if it makes dependencies or data flow easier to grasp; explain its significance in prose.

Describe the method's relationship to prior work accurately. A contribution need not extend a named baseline. Where general applicability is part of the claim, distinguish transferable ideas from choices tied to a specific implementation, dataset, or assumption.

## Explain why each component is needed before how it works

Readers can follow a component's implementation more easily once they understand its role. Each substantive component **should** be introduced through its motivating problem or dependency, then its inputs, outputs, and transformation. Connect its output to the next step or final objective. For example, if a calibration stage corrects an estimate using an observed condition, explain the condition and purpose of calibration before presenting its formula. 

Use the same sequence for feature extraction, transformations, aggregation, inference, or any other substantive operations actually present. Define intermediate representations where readers need them. Arrange components according to conceptual dependencies rather than the order in which the author developed them; do not invent modules to make the section symmetrical.

## Connect inputs, equations, and the final output

A reader should be able to trace the defined inputs through intermediate quantities to the final estimate, decision, or output. State important dimensions and units, and keep variable meanings consistent with the Problem Statement. Each consequential equation **should** be introduced by its purpose, with non-obvious terms and assumptions explained and the result interpreted. Include the actual objective function, optimization criterion, or decision rule when it governs the method; not every approach has a trainable loss.

Choose the detail level according to the manuscript's purpose. Before experiments, identify unresolved decisions that would prevent implementation. After experiments, describe the procedure actually used. Equations, diagrams, pseudocode, and examples can carry precise detail, but surrounding prose must still explain how they advance the method.

## Explain learned components and their training objective

When an ML model is part of the approach, the Method **should** distinguish learned components from fixed transformations. Within the purpose-and-dependency explanation above, identify the architecture and relevant pretrained weights, then specify each learned component's inputs and outputs, consequential feature representations and tensor dimensions, and how the final output is assembled.

The description **should** identify which parameters are trained, frozen, or fine-tuned. For example, explain that an image encoder is frozen and only a classifier is trained before presenting the training objective. Define actual loss terms and their weights, constraints, and the optimization procedure where they govern the approach. Distinguish this method definition from the experimental training settings and model-selection protocol described in `experiments.md`. A fixed pretrained model used only for inference still needs its architecture, weights, and role explained; it does not imply that this study performed training.

## Consider a memorable method name when useful

When naming an author-proposed method would aid explanation, reference, or recall, **consider** the naming heuristics in Faloutsos's *MetaPaper*:

1. Prefer a distinctive, English-like coined name rather than an ordinary dictionary word.
2. Try saying it **three times in succession**: a good name should be easy to pronounce and remember.
3. Convey the method's **principal insight, purpose, or benefit**. **Avoid names that merely describe implementation steps.** For instance, `FraudSpot` is a more meaningful name than `DeepLearnFraud`, which primarily lists a technique and task.
4. Prefer positive connotations and avoid misleading implications.

These criteria apply only when considering a new name; retain an author's existing terminology unless a substantive change is authorized. Check for collisions or ambiguity when relevant, and obtain the author's choice before making a substantive naming change. Once chosen, define the name and use it consistently across the Abstract, Introduction, Method, figures, and Conclusion. A memorable name must not imply performance or novelty the evidence cannot support.

## Sources and applicability

- MIT EECS Communication Lab, *Paper: Methods (CS)* — explaining algorithm or system components, justifying design choices, developing intuition, and providing consequential replication detail: https://mitcommlab.mit.edu/eecs/commkit/journal-article-methods-cs/
- Faloutsos, *MetaPaper v14* — optional English-like, pronounceable, benefit-oriented, positive method naming: https://www.cs.cmu.edu/~christos/MetaPaper/faloutsos_MetaPaper_v14.pdf
- Pineau et al. (2021), *Improving Reproducibility in Machine Learning Research* — reproducibility of learned methods and computational experiments where relevant: https://www.jmlr.org/papers/v22/20-303.html

Apply the learned-component guidance only where those components are present. Use Pineau et al. when machine learning or experimental replication is applicable; not every method has a learned model, loss, or experimental training procedure. Faloutsos's method-naming advice is optional and should not override author terminology.
