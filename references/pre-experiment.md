# Pre-experiment manuscripts: implementation readiness

An implementation-ready pre-experiment manuscript has two readers in mind: someone assessing the scientific idea and someone who may implement its proposed procedures. Both should understand the definitions, assumptions, methods, and evaluation choices without guessing at consequential details. Necessary explanations take priority over a submission page limit; the result remains a coherent paper, not a software manual or a questionnaire.

A comprehensive implementation audit is appropriate when the author asks for one, but not automatically when the request is only to improve the readability of an early manuscript.

## Distinguish commitments from open decisions

Readers need to distinguish **decided methods from decisions that have yet to be made**. Identify which research questions, hypotheses, task definitions, design choices, data sources, and evaluation procedures are settled. Flag material unknowns as author decisions rather than silently supplying plausible details. Describe expected behavior as a hypothesis, not as an observed result.

If definitions or evaluation objectives are unsettled, resolve or flag these upstream dependencies before polishing descriptions that rely on them. Writing the problem and evaluation protocol before a polished Introduction can reduce rework, but do not impose a fixed drafting order independent of the project.

## Audit whether the plan can be implemented and tested

Implementation readiness requires more than a plausible conceptual overview. Use the relevant section references selected in `SKILL.md`: `problem.md` for the task and assumptions, `method.md` for the algorithm, and `experiments.md` for data and evaluation design. Apply `ml.md` only for its relevant method-specific or classification guidance. Ask whether an implementer could reproduce the consequential transformations, quantities, parameters, comparison conditions, and selection rules.

For example, a method may define a threshold mathematically but never explain how its value is chosen. That omission can prevent implementation and can also change the meaning of the evaluation. Flag the missing selection rule instead of choosing a convenient value.

Check that each material claim or research question has a plausible planned source of evidence and that the experiment could distinguish relevant interpretations. An analysis may serve several questions, and a question may require several analyses. Identify missing controls or decisions that threaten validity, not omissions from an arbitrary question quota.

## Describe intended results without inventing them

Planned result displays can clarify what must be measured or compared. Describe the *purpose* of a proposed table or figure, along with the axes, categories, units, and comparison conditions necessary to produce it. Keep the display prospective; use the placeholder convention in `SKILL.md` for important figures that cannot yet be grounded in observed evidence.

## Report the gaps that matter

For a requested completeness audit, prioritize omissions that obstruct implementation, scientific appraisal, or interpretation. State what information is missing, why it matters, and whether an author decision, source verification, or design revision is needed. Some study types will not use classifiers, train/test splits, ablations, or numerical significance tests; their absence is not intrinsically a defect.
