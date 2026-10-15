# Scientific Manuscript Editor

A reusable skill for diagnosing, editing, and verifying English scientific manuscripts for readability while preserving their scientific content.

This repository is the canonical source for the skill. It is designed for manuscripts that may be LLM-drafted, but the goal is not to "humanize" prose or evade AI detection. The skill addresses deeper readability problems such as unsupported claims, unnecessary content, weak global structure, terminology drift, unclear logical relations, undefined notation, and poor information density or draft completeness.

## Structure

```text
.
├── SKILL.md
├── references/
│   └── patterns.md
└── scripts/
    └── verify_protected.py
```

## Modes

- `diagnose`: review the manuscript without changing it.
- `edit`: apply the diagnosed edits to a copy while preserving protected scientific elements.
- `verify`: compare the original and revised manuscripts and report potentially unsafe changes.

See [`SKILL.md`](./SKILL.md) for the complete workflow and editing rules.

## Targets

- `draft`: a pre-experiment manuscript in submission-paper form that also serves as the implementation specification. Completeness and implementability take priority over brevity.
- `submission`: a manuscript with results headed for a venue. Reviewer-facing information density and venue conventions take priority.

## Verification script

```bash
python3 scripts/verify_protected.py ORIGINAL REVISED --strict
```

The script checks protected surface elements such as numbers, units, citation keys, labels, cross-references, and mathematical expressions. Semantic changes such as new claims, lost assumptions, scope expansion, and weakened qualifications still require semantic verification.

## Version

Current canonical skill: **v0.2.1**.
