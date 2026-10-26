# Verify scientific content across manuscript changes

Use this reference when making substantive revisions to an existing manuscript, running protected-element checks, or comparing original and revised versions. Verification protects scientific meaning; matching surface tokens is neither necessary nor sufficient proof of semantic equivalence. The workflow and `Local`/`Semantic`/`Structural` change types are defined in `SKILL.md`.

## Preserve the original and record intent

Produce a revised copy; do not overwrite the only original. Record changes by finding ID or clear location, before/after excerpts, anticipated reader benefit, change type(s), and any distinct scientific risk. Prioritize `Semantic` and `Structural` changes in the change log, then summarize `Local` expression edits. A change can have multiple types.

**When running the bundled verifier, write `approved_changes.txt`**, empty if no protected additions or removals are intended. For other revisions without suitable source files or a verifier run, document intentional substantive changes in the change log instead; a separate whitelist file is not required. List identifiers for intentionally changed protected elements, one per line, e.g. `cite:smith2020`, `label:fig:overview`, `math:<symbol or expression>`. Prefer `math:` for mathematics: it permits whitespace and expands to the verifier's `math-symbol` and `math-expr` keys. Explicit `math-symbol:` and `math-expr:` are also accepted; the verifier normalizes whitespace in `math-expr:`. Document both original and revised forms for an intentional equation change. The filename is historical: its entries represent **editor intent, not author approval**, and do not prove correctness. Do not add entries merely to silence errors.

## Run the deterministic protected-element check

When the script and suitable original/revised LaTeX or text sources are available, run:

```bash
python3 scripts/verify_protected.py ORIGINAL REVISED --approved approved_changes.txt --out verify_report.md --strict
```

Inspect changes in numbers and units, citation keys, references, labels, mathematics, and other protected elements. Compare surrounding contexts because an element-level whitelist does not approve each occurrence. `--strict` detects certain unapproved additions/removals, but **does not catch all contextual or semantic errors**, and extraction is imperfect with complex LaTeX, compound units, and unit macros. Treat the report as a diagnostic aid, not a success certificate.

## Check scientific meaning independently

Semantically inspect **every `Semantic` and `Structural` edit** for changed claims, evidence links, symbol identities, definitions, assumptions, scope qualifiers, causal direction, conditions, results, or information silently lost or misplaced. Spot-check `Local` edits. For a wholesale rewrite, compare the scientific argument and every substantive element to the original or author-supplied research material; matching paragraphs one-to-one is not expected, but preserving or explicitly accounting for meaning is.

When an equation symbol must change, identify its semantic role and all corresponding equations, definitions, figure labels, prose mentions, and cross-references **before** editing. Never make an unscoped global replacement. Read `references/notation.md` for the scope and consistency of a symbol-identity change; do not impose optional typography conventions unless notation itself is a reader-facing problem.

## Report limitations and unresolved issues

Report intended protected changes, unexpected discrepancies, unresolved author decisions, and materials not available for comparison. A clean script result **does not prove scientific equivalence**. Do not claim full verification if figures, source files, or other necessary information were unavailable.

