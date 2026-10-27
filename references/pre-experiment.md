# Pre-experiment manuscripts: implementation readiness

Use this reference when writing or substantially revising a paper-form manuscript before the proposed experiments have been implemented, or when an author explicitly requests a design-completeness or implementation-readiness audit. A readability-only diagnosis of an early manuscript does not authorize a comprehensive research-design review.

The objective is a **scientifically understandable manuscript that can guide implementation and critical appraisal**. Necessary definitions, procedures, assumptions, and evaluation choices take priority over a submission page limit. This remains a paper, not merely a software specification or a sequence of planning answers.

## Distinguish commitments from open decisions

Identify which research questions, hypotheses, problem definitions, design choices, data sources, and evaluation procedures are already decided by the author. Mark material unknowns explicitly instead of inventing plausible implementation details. Distinguish a proposed outcome from an empirical finding, and do not fill a conventional Results slot with expected numbers or untested conclusions.

If definitions or evaluation objectives are unsettled, resolve or flag these upstream dependencies before polishing descriptions that rely on them. Writing the problem and evaluation protocol before a polished Introduction can reduce rework, but do not impose a fixed drafting order independent of the project.

## Audit whether the plan can be implemented and tested

Read the relevant section references selected in `SKILL.md` for the scientific particulars: `problem.md` for the task and assumptions, `method.md` for the algorithm, and `experiments.md` for data and evaluation design. Use `ml.md` only when the study actually employs machine learning. Ask whether a competent implementer could reconstruct consequential data transformations, quantities, model operations, parameters, protocols, comparison conditions, and selection rules without asking the author to guess.

Check that each material claim or research question has a plausible planned source of evidence and that the experiment could distinguish relevant interpretations. An analysis may serve several questions, and a question may require several analyses. Identify missing controls or decisions that threaten validity, not omissions from an arbitrary question quota.

## Describe intended results without inventing them

When result presentation affects implementation planning, describe the *purpose* of a proposed table or figure, its relevant units, axes, categories, comparison conditions, and what interpretation it is intended to enable. Label it as planned. Do not fabricate measurements, distributions, qualitative examples, statistical significance, or diagram contents. For a missing but important display, use the evidence-grounded placeholder convention in `SKILL.md`.

## Report the gaps that matter

For a requested completeness audit, prioritize omissions that obstruct implementation, scientific appraisal, or interpretation. State what information is missing, why it matters, and whether an author decision, source verification, or design revision is needed. Some study types will not use classifiers, train/test splits, ablations, or numerical significance tests; their absence is not intrinsically a defect.
