# Method: make the approach understandable and implementable

Use this reference when writing, diagnosing, or substantially revising a Method, Methodology, Model, or Approach section. Readers should understand **what the method does, why its design is plausible, and how its substantive parts produce the required output**.

## Orient the reader before component details

Identify the method's objective and relationship to the problem definition and relevant prior approaches. Explain its central design idea and consequential differences from alternatives without assuming that every contribution extends a named baseline. A method overview can establish its stages, dependencies, and data flow before the details. Include a diagram only when it materially reduces the effort of understanding these relationships; surrounding prose must still explain its purpose.

Where general applicability matters to the claim, distinguish components that could transfer to other settings from those tied to a particular implementation, dataset, or assumption. Generality is a claim to support, not a mandatory virtue of every method.

## Explain each substantive component

For each meaningful component or processing stage, explain its motivation and role, what enters it, what comes out, what transformation it performs, and how it depends on or supports other components. Sequence explanations according to conceptual dependencies, not merely the chronology of development. Do not invent modules or repeat nearly identical headings to achieve a symmetrical outline.

Describe the representations or intermediate quantities required to understand the algorithm. Explain feature extraction, transformation, aggregation, inference, or other substantive operations at the level needed for the manuscript's purpose. Learned backbones are one possible mechanism, not a presumed component; use `ml.md` for machine-learning-specific details when applicable.

## Close the mathematical and procedural chain

Define important inputs, outputs, variables, dimensionality, and units consistently with the Problem Statement. Where equations are useful, explain what relationship each expresses and how its variables connect to earlier definitions. Derive or describe how the final estimate, decision, or output is assembled from intermediate quantities. Define an objective function, optimization procedure, decision rule, or other governing criterion when the method actually has one; do not invent a training loss for an untrained procedure.

For an implementation-ready pre-experiment manuscript, provide sufficient detail to implement consequential choices and identify unsettled parameters explicitly. For a completed study, ensure the description corresponds to the method that was actually run. Algorithmic examples, pseudocode, diagrams, and mathematical expressions should complement the prose rather than substituting for missing explanations.
