# Frequent LLM phrasings and what they usually hide

Use this list to **find candidates**, not to substitute words. Each pattern points to a layer; fix the underlying problem there. If the manuscript does not contain the information needed for the fix, raise an L1 finding with `[AUTHOR: …]`.

## Evaluation without content → L5 (or L1 if evidence is missing)

| Pattern | Usual underlying problem | Fix |
|---|---|---|
| crucial, pivotal, vital, essential, key role | Importance asserted, reason not given | State what depends on it (mechanism) or the measured effect (evidence); else delete |
| robust, comprehensive, extensive, thorough | Scope or test conditions not stated | State the conditions tested (noise levels, datasets, ablations) |
| significant(ly) | Statistical vs. practical meaning unclear | Report the test and effect size, or use a non-statistical word with a number |
| substantially, remarkably, notably, dramatically | Size of the effect hidden | Give the number and the baseline |
| novel, first, unique | Novelty claim without delimitation | State what is new relative to which prior work; L1 if unsupported |
| state-of-the-art | Comparison set unstated | Name benchmark, metric, and compared methods |

## Empty framing → L5

| Pattern | Fix |
|---|---|
| It is important/worth noting that | Delete; state the fact |
| In this paper/section, we aim to | State what is done or shown |
| plays a crucial/important role in | State the relation (X determines / limits / enables Y) |
| delve into, shed light on, pave the way for | Use the precise verb (measure, show, allow) |
| In the realm/landscape/context of | Delete or name the field once |
| serves as a testament to, underscores | Say what the result shows |

## Connectors standing in for logic → L4

| Pattern | Check |
|---|---|
| Furthermore, Moreover, Additionally, In addition | Is it really an addition? Often cause, contrast, condition or example |
| Notably, Importantly | Why is it notable? State the reason or delete |
| Thus, Therefore, Hence | Does the previous sentence actually imply this? |
| In other words, That is | Is the restatement needed (L6)? |

## Structure → L2 / L6

| Pattern | Underlying problem |
|---|---|
| Paragraph ends with "Overall, …" / "In summary, …" repeating its first sentence | Redundant closing (L6) |
| "This section introduces… First… Next… Finally…" | Roadmap without content; replace with a real overview only if needed (L2) |
| Method subsection starts directly with component details | Missing overview (L2) |
| Abstract/Introduction opens with a universal truth ("X is a major cause of…", "With the rapid development of…") | A legitimate centrality claim executed generically; replace with the shared premise closest to the gap (L0) |
| Equation followed by "where x is…, y is…" and nothing else | Symbols listed, meaning absent; add what the equation computes and why this form (L1) |
| Overview figure with section names in boxes joined by arrows | Roadmap in figure form; show inputs, outputs and data flow (L2) |
| Three-item lists everywhere ("X, Y, and Z") | Padding to a rhythm; check each item is needed (L0/L6) |
| "not only X but also Y" | Often inflation; check Y is a real result |
| Generic Limitations ("future work could explore more datasets") | Real weaknesses not stated (L1) |

## Terminology drift → L3

Same concept, several names: region / area / zone; framework / approach / method / pipeline / system; risk / hazard / danger; metric / measure / score. Fix one term per concept, matching the definition or equation.

## Formatting habits (low priority)

Bold for emphasis inside paragraphs, colon-led mini-headings, em-dash chains, bullet lists inside prose sections. Convert to prose where the venue style expects it.
