# Method: explain the approach from purpose to output

The Method should let readers understand **what the approach does, why its design is plausible, and how its parts produce the required output**. For an implementation-ready manuscript, that explanation must also be detailed enough to reconstruct consequential operations.

## Establish the central idea before implementation details

Readers need a mental model of the approach before they can interpret its individual components. Begin with the objective established in the Problem Statement, the central design idea, and the consequential difference from relevant alternatives. A short overview of the stages and their relationships can prepare readers for the details that follow. Use a diagram if it makes dependencies or data flow easier to grasp; explain its significance in prose.

Describe the method's relationship to prior work accurately. A contribution need not extend a named baseline. Where general applicability is part of the claim, distinguish transferable ideas from choices tied to a specific implementation, dataset, or assumption.

## Explain why each component is needed before how it works

Readers can follow a component's implementation more easily once they understand its role. Introduce the problem or dependency motivating the component, then explain its inputs, outputs, and transformation. Connect its output to the next step or final objective. For example, if a calibration stage corrects an estimate using an observed condition, explain the condition and purpose of calibration before presenting its formula. The example illustrates explanation order, not a requirement to add calibration to a method.

Use the same sequence for feature extraction, transformations, aggregation, inference, or any other substantive operations actually present. Define intermediate representations where readers need them. Arrange components according to conceptual dependencies rather than the order in which the author developed them; do not invent modules to make the section symmetrical. For learned components, consult the additional guidance in `ml.md` when that reference is applicable.

## Connect inputs, equations, and the final output

A reader should be able to trace the defined inputs through intermediate quantities to the final estimate, decision, or output. State important dimensions and units, and keep variable meanings consistent with the Problem Statement. Introduce each consequential equation by its purpose, explain non-obvious terms and assumptions, and interpret what the result means. Include the actual objective function, optimization criterion, or decision rule when it governs the method; not every approach has a trainable loss.

Choose the detail level according to the manuscript's purpose. Before experiments, identify unresolved decisions that would prevent implementation. After experiments, describe the procedure actually used. Equations, diagrams, pseudocode, and examples can carry precise detail, but surrounding prose must still explain how they advance the method.

## Sources and applicability

- MIT EECS Communication Lab, *Paper: Methods (CS)* — explaining algorithm or system components, justifying design choices, developing intuition, and providing consequential replication detail: https://mitcommlab.mit.edu/eecs/commkit/journal-article-methods-cs/
- Pineau et al. (2021), *Improving Reproducibility in Machine Learning Research* — reproducibility of learned methods and computational experiments where relevant: https://www.jmlr.org/papers/v22/20-303.html

Use the second source when machine learning or experimental replication is applicable; not every method has a learned model, loss, or experimental training procedure.
