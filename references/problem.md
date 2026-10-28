# Problem statement: specify what the research asks

The Problem Statement defines **what must be solved or investigated**, independently of the particular approach proposed by the paper. Readers should leave it knowing the target outcome, available information, and boundaries of the task.

## Define the objective and a valid solution

State the target task, phenomenon, or research question precisely. Explain what would count as a valid, desirable, or useful outcome and why; distinguish the objective of the task from properties that the proposed method happens to produce. If the study makes predictions, estimates, classifications, decisions, or explanations, specify the intended meaning and relevant granularity of each output.

Separate information provided by the task from quantities produced inside a particular method. For example, an observed image can be an input to the task, whereas features extracted from it belong to the proposed method. Specify units, domains, time horizons, spatial scales, populations, and other dimensions when they affect interpretation. Define unfamiliar terms and author-created quantities where readers first need them; use `notation.md` for symbol conventions when applicable.

## Make scope and assumptions testable

Explicitly state material assumptions, restrictions, exclusions, and operating conditions. Distinguish the general research problem from the subset actually investigated. Avoid silently extending an estimate, method, or empirical finding to settings excluded by the formulation. Where success requires an evaluation criterion, describe what it measures and how it relates to the target problem; detailed metric selection and implementation belong to `experiments.md`.

## Show a representative case when it clarifies the formulation

A concrete example or schematic may make unfamiliar entities, available inputs, desired outputs, or a boundary case more intelligible. Choose a representative case that is consistent with the formal definition; an illustrative example is not evidence of empirical performance. Introduce the figure in prose and interpret its role. General principles for figures, equations, and their complementarity with text belong to `composition.md`.

## Check the formulation against the rest of the paper

Verify that the Method actually operates on the declared inputs, that the Experiments assess the stated output or objective, and that the Results and Conclusions do not silently change the target task. If these disagree, resolve the scientific definition before polishing prose. Do not fill unresolved definitions with invented author decisions.
