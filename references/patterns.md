# Common LLM prose patterns — diagnose the cause, do not word-swap

This file is a locator aid for L5 diagnosis. A match is not automatically a problem. The editor must identify the underlying defect and fix that defect. Never use this as a replacement table.

## Empty importance framing

Typical forms:

- `It is important to note that ...`
- `It should be noted that ...`
- `It is worth noting that ...`
- `plays a crucial/important/key role in ...`
- `is crucial/essential/vital for ...`
- `This is particularly important because ...`

Usual underlying problem: the sentence asserts importance instead of stating evidence, mechanism, or scope.

Fix: replace the evaluation with the evidence, mechanism, or scope already present in the manuscript, or delete the framing. If the necessary support is absent, create an L1 finding; do not invent it.

Bad repair: `crucial` → `important`.

## Empty paper-intent framing

Typical forms:

- `In this paper, we aim to ...`
- `This paper seeks to ...`
- `The purpose of this study is to ...`
- `In this section, we describe/present/discuss ...`

Usual underlying problem: meta-language delays the actual action or claim.

Fix: state the research action or content directly when possible. Keep explicit objective statements when they genuinely orient the reader, especially around RQs.

## Additive connectors hiding the real relation

Typical forms:

- `Furthermore, ...`
- `Moreover, ...`
- `Additionally, ...`
- `In addition, ...`

Usual underlying problem: the sentences are not merely additive. The second may be a consequence, contrast, condition, example, or restatement.

Fix: identify and state the real relation, or reorder the sentences so the relation is evident. Do not simply delete the connector if that would remove needed logic.

## Restatement and recap

Typical forms:

- `In other words, ...`
- `Put differently, ...`
- `Taken together, ...`
- `Overall, these results suggest that ...`
- a paragraph's final sentence repeats its first sentence

Usual underlying problem: local generation tries to make each paragraph self-contained, producing duplicate information.

Fix: keep the version that best advances the argument. Retain a restatement only when it materially changes abstraction level or resolves genuine difficulty.

## Vague evaluative adjectives

Typical words:

- `robust`
- `comprehensive`
- `significant`
- `substantial`
- `effective`
- `promising`
- `novel`
- `sophisticated`
- `seamless`
- `meaningful`

Usual underlying problem: evaluation substitutes for a measurable result or bounded claim.

Fix: replace with a reported quantity, comparison, mechanism, or explicit scope if already supported. Otherwise narrow or delete the evaluation. `significant` must be disambiguated between statistical significance and practical importance.

## Abstract nouns and nominalization

Typical forms:

- `the evaluation of X was conducted`
- `the characterization of X was performed`
- `an investigation into X was carried out`
- `the utilization of X enables ...`

Usual underlying problem: the agent and action are hidden, increasing sentence length and processing cost.

Fix: restore the verb and, when appropriate, the agent: `We evaluated X`; `X enables Y`.

## Generic transition or conclusion sentences

Typical forms:

- `These findings highlight the importance of ...`
- `These results underscore the need for ...`
- `This demonstrates the effectiveness of ...`
- `This provides valuable insights into ...`

Usual underlying problem: the manuscript says that a result matters without specifying what scientific inference follows.

Fix: state the inference directly, including its scope and condition. If no distinct inference exists, delete the sentence.

## Premature or repeated roadmaps

Typical forms:

- `First, we ... Next, we ... Finally, we ...`
- `The remainder of this section is organized as follows ...`
- repeated mini-roadmaps at the beginning of short subsections

Usual underlying problem: a roadmap is standing in for a conceptual overview.

Fix: when the reader needs a mental model, explain the input, output, component relationships, and decomposition rationale. Otherwise remove the roadmap.

## Synonym drift

Typical examples:

- `region / area / zone`
- `method / approach / framework / scheme`
- `interaction / encounter / event` when they denote the same defined object

Usual underlying problem: stylistic variation conflicts with technical precision.

Fix: choose one term per concept, preferably the term used in its formal definition, equation, figure, or data schema. Do not vary terminology merely to avoid repetition.

## Uniform sentence rhythm

Symptoms:

- many sentences of similar length and syntax
- repeated `This X ... This Y ... This Z ...`
- every paragraph starts with a claim and ends with a summary

Usual underlying problem: repeated local generation template rather than content-driven syntax.

Fix: do **not** vary sentence length artificially. Rebuild sentences according to logical structure. If the content naturally produces similar lengths, leave them alone.

## Boilerplate limitations

Typical forms:

- `Despite these promising results, several limitations remain.`
- `Future work will explore ...`
- limitations that could apply to almost any paper

Usual underlying problem: a generic genre template replaces the actual validity boundary.

Fix: name the concrete limitation, what inference it threatens, and whether it affects internal validity, external validity, measurement, or generalization. Never invent a limitation just to fill the section.

## Overclaim patterns

Typical forms:

- `demonstrates that X is generally applicable`
- `establishes a new paradigm`
- `outperforms existing methods` when only a subset was compared
- `solves` a problem evaluated only on one dataset or condition

Usual underlying problem: claim scope exceeds experiment scope.

Fix: bound the claim to the evaluated datasets, conditions, baselines, metrics, and uncertainty. This is an L1 issue, not merely an L5 wording issue.
