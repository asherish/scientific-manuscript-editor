# Scientific Manuscript Editor

A skill for **writing and improving scientific manuscripts so readers can follow the research without losing scientific accuracy**.

Scientific Manuscript Editor helps researchers turn scientific material into a clear explanation of the problem, approach, evidence, and conclusions. It can also diagnose an existing manuscript, identify where understanding breaks down, and improve the writing at the scale the problem requires.

## When to use it

Use the skill to:

- **Write before experiments:** Produce a paper-form specification detailed enough to implement the proposed methods and evaluations. Necessary explanations may take more pages than a submission allows.
- **Write after experiments:** Turn completed research and actual evidence into a manuscript suitable for a target venue.
- **Diagnose without editing:** Identify unclear reasoning, missing explanations, unsupported claims, or problems in the manuscript's structure.
- **Revise at the right scale:** Improve a passage, reorganize sections, or rewrite an argument when smaller edits cannot solve the problem.
- **Verify changes:** Check whether revisions preserve definitions, claims, equations, results, and other protected scientific content.

## Try it

With the skill available in your assistant, provide your research materials or manuscript and state what you want done. For example:

> Write a pre-experiment manuscript from this research plan. Include enough methodological and evaluation detail for another researcher to implement it. Flag unresolved decisions.

> Diagnose the logical structure of this manuscript and explain the most important problems. Do not revise the text yet.

> Revise this completed manuscript for submission to [venue]. Verify the current official author instructions before applying page limits or style requirements.

> Compare the original and revised LaTeX manuscripts. Report substantive changes and any scientific information that may have been lost.

You can ask for a diagnosis only, request a specific section, or set strict limits on what may be changed. The skill does not assume that every passage needs editing.

## How it works

The workflow is **Context → Design / Diagnose → Write / Revise → Review / Verify → Deliver**. It is iterative: a problem found during review may require returning to the argument's design.

The central idea is to decide **what the reader needs to understand** and then make the paper, sections, paragraphs, sentences, equations, figures, and tables work together to communicate it. A useful planning question is: *What should readers understand here, and which evidence or explanation lets them understand it?* The answer may need a paragraph, an equation, a figure, or a combination.

Four principles guide the work: **Purpose, Coherence, Comprehensibility, and Scientific Accuracy**. Paragraph writing, claim–support reasoning, Context–Content–Conclusion (CCC), and moving from familiar context to new information are available as techniques, not rigid templates. Figures and tables complement the surrounding prose rather than replacing its explanation.

## Scientific safeguards

The skill does **not invent** results, data, citations, mechanisms, or research decisions. It distinguishes proposed experiments from completed work and flags consequential missing information for the author. For submissions, it checks current official venue requirements rather than assuming a universal page limit or writing style.

For revisions, the original should remain available for comparison. A bundled [verification script](scripts/verify_protected.py) can help detect changed citations, numbers, labels, and mathematical elements when suitable text or LaTeX sources are available. Its output is not proof of semantic equivalence; scientific review remains necessary.

## Repository guide

- [SKILL.md](SKILL.md) — Always-applicable purpose, principles, workflow, scientific safeguards, and rules for loading specialized guidance.
- [composition.md](references/composition.md) — Scientific argument, paragraph writing, reader questions, information order, and integration of equations, figures, and tables.
- [questions.md](references/questions.md) — Optional adapted 60QA planning questions; select those relevant to the work rather than treating all 60 as mandatory.
- [pre-experiment.md](references/pre-experiment.md) and [submission.md](references/submission.md) — Stage-specific guidance.
- [introduction.md](references/introduction.md) and [abstract.md](references/abstract.md) — Section-specific guidance.
- [diagnosis.md](references/diagnosis.md), [verification.md](references/verification.md), and [notation.md](references/notation.md) — Focused checks and conventions.

The assistant reads `SKILL.md` when the skill activates and loads relevant reference files only when needed. That separation keeps core instructions available without imposing every detailed checklist on every task.

The optional question bank adapts the *60 Questions & Answers (60QA)* approach attributed to [Komei Sugiura](https://komeisugiura.jp/software/software_jp.html). Paragraph-structure guidance is also informed by [Mensh and Kording (2017)](https://doi.org/10.1371/journal.pcbi.1005619) and [Seitaro Iwama's academic-writing lecture](https://speakerdeck.com/neuroiwm/paragurafu-kara-hajimeru-akademikku).

**Current version:** v0.6.0
