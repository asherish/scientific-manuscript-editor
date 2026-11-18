# Pre-experiment manuscripts: implementation readiness

An implementation-ready pre-experiment manuscript serves two readers: someone assessing the scientific idea and someone implementing its proposed procedures. The **main-paper draft should target the intended venue's verified page budget** while remaining understandable and scientifically assessable. Preserve additional technical detail in an appendix or supplement permitted by the venue and, when that cannot accommodate everything, in separate **non-submitted technical notes**. Together, these materials should make definitions, assumptions, methods, and evaluation choices sufficiently explicit for implementation without turning the main paper into a software manual.

A comprehensive implementation audit is appropriate when the author asks for one, but not automatically when the request is only to improve the readability of an early manuscript.

## Allocate scientific explanation and implementation detail

At drafting time, **identify the intended venue's main-paper page limit, what counts toward it, and whether an appendix or supplement is allowed and subject to its own limit**; consult `submission.md`. The main paper **should** retain the problem, essential definitions and assumptions, central method, evaluation rationale, and information needed to judge the claims. Supporting material **should** hold extended derivations, step-by-step procedures, parameter-selection details, additional evaluation conditions, and other implementation information that would make the main paper exceed its budget.

When the venue restricts or prohibits appended material, the editor **should preserve further useful details in a clearly marked non-submitted technical appendix or implementation notes** for the author. These notes are not part of the submission and **must not** be cited as if reviewers can inspect them. If information essential to scientific appraisal will not fit in the actual submission, flag the trade-off rather than silently moving it to private notes. Where no venue is specified, use an explicitly provisional or author-specified main-paper budget, not an invented venue rule.

## Distinguish commitments from open decisions

The specification **must** distinguish **decided methods from decisions that have yet to be made**. Identify which research questions, hypotheses, task definitions, design choices, data sources, and evaluation procedures are settled. Flag material unknowns as author decisions rather than silently supplying plausible details. Describe expected behavior as a hypothesis, not as an observed result.

If definitions or evaluation objectives are unsettled, resolve or flag these upstream dependencies before polishing descriptions that rely on them. When unresolved upstream definitions would cause rework, **consider** drafting the problem and evaluation protocol before polishing the Introduction.

## Audit whether the plan can be implemented and tested

Implementation readiness requires more than a plausible conceptual overview. Use the relevant section references selected in `SKILL.md`: `problem.md` for the task and assumptions, `method.md` for the algorithm, and `experiments.md` for data and evaluation design. For learned components, use the conditional guidance in `method.md` and `experiments.md`; use `results.md` for planned output-specific error analyses. Ask whether an implementer could reproduce the consequential transformations, quantities, parameters, comparison conditions, and selection rules.

For example, a method may define a threshold mathematically but never explain how its value is chosen. That omission can prevent implementation and can also change the meaning of the evaluation. Flag the missing selection rule instead of choosing a convenient value.

Check that each material claim or research question has a plausible planned source of evidence and that the experiment could distinguish relevant interpretations. Identify missing controls or decisions that threaten validity.

## Describe intended results without inventing them

When planning result displays would clarify necessary measurements or comparisons, **consider** outlining those displays. Describe the *purpose* of a proposed table or figure, along with the axes, categories, units, and comparison conditions necessary to produce it. Keep the display prospective; use the placeholder convention in `SKILL.md` for important figures that cannot yet be grounded in observed evidence.

## Report the gaps that matter

For a requested completeness audit, prioritize omissions that obstruct implementation, scientific appraisal, or interpretation. State what information is missing, why it matters, and whether an author decision, source verification, or design revision is needed. 
