# Scientific Manuscript Editor

A reader-centered skill for writing and improving English scientific papers and paper-form research drafts without inventing scientific content.

The skill asks what the intended reader needs to understand and identifies genuine obstacles to comprehension, rather than applying a mechanical list of prose rules. It can support drafts that also serve as specifications for experiments, while preserving scientific meaning and sources.

## Repository contents

```text
.
├── SKILL.md
├── references/
│   ├── patterns.md
│   ├── notation.md
│   └── draft-checklist.md
└── scripts/
    └── verify_protected.py
```

- [`SKILL.md`](SKILL.md) contains the core principles, modes, editing safeguards, and reference triggers.
- `references/` contains **optional** tools for diagnosing recurring prose problems, resolving notation choices, and reviewing experimental completeness. These are not checklists to run on every draft.
- `scripts/verify_protected.py` compares protected surface elements before and after a revision. The editor must still perform semantic verification.

## Workflow

1. `diagnose`: find material reader difficulties; do not change the manuscript.
2. `edit`: make feasible changes on a copy; write a change log and `approved_changes.txt` for editor-intended protected-element additions/removals.
3. `verify`: run deterministic and semantic checks. For example:

   ```bash
   python3 scripts/verify_protected.py original.tex revised.tex \
      --approved approved_changes.txt --out verify_report.md --strict
   ```

For intentional mathematical changes, prefer `math:<symbol or expression>` in `approved_changes.txt`; spaces in expressions are accepted. An approval-list entry records an **intended** change; it is not author sign-off or proof of semantic correctness. The script has known extraction limits (including some compound units and LaTeX unit macros), and `--strict` does not fail on every context warning. Examine these separately.

For new prose without an original file, verify scientific grounding against the supplied research material rather than pretending a before-and-after comparison exists.

**Current version:** v0.3.2