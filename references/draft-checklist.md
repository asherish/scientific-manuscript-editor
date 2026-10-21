# Research-draft completeness — optional review prompts

Consult only when the user explicitly requests **research-design, experiment-implementation, reproducibility, or completeness review**. The paper-form `draft` stage—even when intended to guide later experiments—does not automatically trigger this separate audit.

These prompts support an author/implementer reading the draft. They do **not** define one required research design. Ask whether a missing item would prevent implementation, appraisal, or interpretation. Mark genuinely inapplicable items `N/A` with a brief reason. Do not invent hypotheses, experiments, numerical choices, citations, results, or design decisions to fill a slot. Add `[AUTHOR: ...]` only for gaps that matter.

## Contribution and argument

- Is the contribution distinct from existing work and articulated with appropriate scope? Is it clear what evidence—planned or already available—would support each important claim?
- Can readers follow how the problem, RQs, proposal, experiment or analysis, and interpretation connect?
- Is the paper-form draft organized well enough to guide its implementation without becoming a separate engineering manual?

## Problem formulation and meaning

- Are inputs, outputs, objectives, constraints, assumptions, and the unit of analysis specified sufficiently for the proposed work?
- Are symbols and important technical or author-coined concepts explained at the level required by the intended implementer? Is each equation's role or non-obvious mechanism understandable from nearby prose?
- Would a notation table, worked example, or conceptual diagram remove an actual source of confusion? Consult `notation.md` only for an ambiguity or when defining a scheme, not as an audit quota.

## Proposed approach

- For each substantive component, can an implementer determine why it exists, what it consumes and produces, and how it interacts with the other parts?
- Where competing design choices matter to validity or implementation, is the choice sufficiently motivated? Do not invent a list of rejected alternatives.
- Would an overview of the entire method, a subsection, or the input–transformation–output pipeline help establish relationships before details?

## Planned evaluation or analysis

- For each material RQ or claim, is it clear what study, analysis, or evidence will bear on it? A one-to-one mapping of contributions to experiments or figures is **not** required.
- Where relevant: datasets/versions, collection and preprocessing, spatial and temporal units, splits, baselines, metrics and operational definitions, ablations, thresholds, hyperparameters and selection procedures, stochasticity, seeds, repeats, resources and computational settings.
- Are comparisons fair for the claims being made, and can the implementer reproduce the critical conditions? Are the planned interpretations stated at an appropriate level (hypothesis-driven, exploratory, descriptive, or qualitative), without forcing a binary confirm/refute criterion?

## Results presentation and boundaries

- Are the purposes of planned tables and figures clear enough to implement, including key axes, columns, relationships, comparisons, and the reader takeaway? Do not fabricate results or demand a fixed set of plots.
- Are known uncertainties, threats to validity, and scope boundaries conveyed without boilerplate?

## Output discipline

Only report **material gaps** in a short author-to-do list: where the information is needed, what understanding or implementation task it enables, and whether the missing detail must come from the author. Do not convert these prompts into a table of compliance scores or place placeholders throughout a readable draft solely to satisfy the list.
