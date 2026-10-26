# Scientific Manuscript Editor

A reader-centered skill for **writing, diagnosing, revising, and verifying scientific manuscripts** without inventing scientific content. Its goal is to communicate defensible research so that intended readers can understand the scientific argument and evidence with reasonable effort.

The skill uses four common principles—**Purpose, Coherence, Comprehensibility, and Scientific Accuracy**—at paper, section, paragraph, and sentence scales. Paragraph writing is a method for organizing an explanation, not a rigid topic-sentence template. Equations, figures, and tables complement surrounding prose and must be explained and interpreted as part of the scientific argument.

For substantial writing whose purpose or structure is unclear, an **optional Question → Answer → Paragraph** scaffold makes a reader question explicit, plans an evidence-grounded answer, and then composes the prose. It is informed by question-driven manuscript outlining such as 60QA but does not require a literal Q&A or one question for every paragraph. Topic/support relationships, Pyramid, context–content–conclusion, Problem–Solution, and CARS are available as conditional techniques rather than mandatory templates.

An important information-ordering heuristic is to **connect information already established or reasonably known by the reader to new information**. It applies across sentences and sections without forcing a fixed sentence shape.

## Manuscript purposes

- **Pre-experiment specification:** Write a paper-form, implementation-ready account of planned methods and evaluations; necessary detail takes priority over page length.
- **Post-experiment submission preparation:** Present completed research and its evidence efficiently while following the current official requirements of the target venue.

These purposes are independent of whether the task is new writing, diagnosis, local revision, structural reorganization, a full rewrite, or verification. An existing manuscript may need no changes at all.

## Repository contents

```text
.
├── SKILL.md
├── references/
│   ├── argument-and-exposition.md
│   ├── introduction.md
│   ├── abstract.md
│   ├── diagnosis.md
│   ├── pre-experiment-specification.md
│   ├── submission-preparation.md
│   ├── notation.md
│   └── verification.md
└── scripts/
    └── verify_protected.py
```

`SKILL.md` contains the always-applicable purpose, principles, workflow, scientific safeguards, and **conditions for consulting references**. Each file under `references/` expands a specific task; none is a universal checklist. The verification script compares protected surface elements between two manuscript versions, but semantic verification remains necessary.

## Working approach

1. Establish the user task, intended reader, scientific material, and manuscript purpose.
2. Design an argument for new writing, or diagnose the actual reader difficulties in existing material.
3. Write or intervene at an appropriate scale: local editing, paragraph/section restructuring, or a justified full rewrite.
4. Check reader comprehension and scientific accuracy. For an existing revision, preserve the original, document changes, and verify protected content and meaning.

For revisions with suitable text files, use `references/verification.md` and the bundled script:

```bash
python3 scripts/verify_protected.py original.tex revised.tex \
  --approved approved_changes.txt --out verify_report.md --strict
```

`approved_changes.txt` records intended protected-element additions/removals, **not author approval**; `--strict` cannot prove semantic equivalence. For a brand-new manuscript, check scientific grounding against supplied sources instead of inventing a baseline for comparison.

**Current version:** v0.5.0
