# Scientific figure and table design

Figures and tables should help the intended reader understand or evaluate a scientific idea, comparison, or body of evidence. Design them from a **reader question and an evidence-supported message**, not from a required figure count or a preference for decoration. Use these principles when a visual would materially reduce understanding effort; concise prose or an equation may be more effective.

## Decide what the visual must communicate

State the question the reader should answer from the visual and what the available data or definitions actually establish. Identify whether its main role is to **orient** (a task example, conceptual relationship, or method overview), **define** (a data or notation table), **compare** (methods or conditions), or **substantiate** (a finding with measured evidence). A visual can serve more than one role, but its message and labels must not imply unsupported conclusions.

When planning a manuscript, an outline of potential figures and tables can expose missing evidence before prose is drafted. This is an **optional figure-first workflow**, not a rule to draw figures before every section. In pre-experiment writing, describe intended axes, variables, comparisons, and conditions without inventing measured values; use a grounded `[FIGURE: ...]` placeholder if necessary.

## Choose a representation that exposes the relationship

Use a diagram for meaningful entities, dependencies, mechanisms, or data flow; a table for precise repeated comparisons or definitions; and a plot for patterns in empirical values. A pipeline diagram should communicate actual inputs, transformations, intermediate quantities, and outputs, not merely section names connected by arrows.

Choose plot encodings according to data type, sample size, uncertainty, and the intended comparison. Check that scales, baselines, axis limits, units, denominators, grouping, aggregation, and any normalization do not distort interpretation. When a mean would conceal important spread or unusual observations, show suitable distributional information (for example, individual points for manageable samples, a box plot, or a distribution plot). Do not impose one plot type on every experiment.

Use legible text, meaningful labels, and distinguishable visual encodings. Do not rely on color alone to express a critical distinction. Avoid needless visual decoration and verify that the plot remains understandable at the target venue's display or print size.

## Put consequential evidence where readers can find it

When a paper has an important, easy-to-understand result or real-world example that directly conveys its central contribution, consider showing it early as a **crown-jewel figure**. Select it for explanatory and evidential value, not simply because it is the most favorable result. One or more visuals may be appropriate; some papers are better served by a problem example or conceptual overview, and others need no early figure.

In the Introduction, orient the reader to what the figure demonstrates and how it connects to the research question. Never present a planned result as observed or let a selective showcase conceal conflicting results or important limitations.

## Write captions that stand on their own

Make the figure or table identifiable without forcing the reader to search the main text for its subject: describe the compared quantities or entities, meaningful conditions, units, encodings, and interpretation aids at the detail needed for correct reading. The text should develop the implication rather than mechanically repeat every plotted mark.

**Optional two- or three-word bold takeaway tag:** When a concise, evidence-supported result is immediately useful to a reader scanning figures, consider starting the caption with a bold 2–3-word label, such as **Linear scaling.**, **Improved recall.**, or **Consistent performance gains.** Follow it with an informative description, for example: “**Linear scaling.** Runtime versus input size under the stated hardware and workload.” These examples are illustrative labels, not claims about a particular experiment. A tag is a communication aid, **not** a required element of every caption, and it must not turn uncertainty or correlation into a stronger claim. Omit it when a descriptive title is clearer, the message is not a supported result, the tag adds clutter, or the venue's caption conventions disallow it.

## Integrate figures with the argument and verify them

Introduce each visual near the relevant question or claim, refer to it accurately, and explain the consequential observation or conceptual relationship it contributes. Align the prose, caption, legend, symbols, data values, and units. Distinguish a demonstration or cherry-picked example from an estimate of population-wide performance. Explain relevant uncertainty, experimental conditions, and caveats.

Review the graphic at its likely display size and as a standalone entry point: What will the reader think it shows? Does that takeaway match the evidence and the text? Can its axes, comparisons, and uncertainty be interpreted? If a reader's likely inference is stronger than warranted, repair the encoding, caption, or prose. Respect applicable venue instructions.

## Sources and applicability

- Faloutsos, *MetaPaper v14* — early crown-jewel figure and optional short caption takeaway tags: https://www.cs.cmu.edu/~christos/MetaPaper/faloutsos_MetaPaper_v14.pdf
- Faloutsos, *Lessons from 1K Rejected Research Papers* — reader attention and showing what a method achieves: https://www.cs.cmu.edu/~christos/MetaPaper/faloutsos_MetaPaper_1KR.pdf
- Rougier, Droettboom, and Bourne (2014), *Ten Simple Rules for Better Figures* — audience, message, graphic construction, and medium: https://doi.org/10.1371/journal.pcbi.1003833
- Weissgerber et al. (2015), *Beyond Bar and Line Graphs* — how aggregate plots can conceal very different data distributions: https://doi.org/10.1371/journal.pbio.1002128
- Whitesides (2004), *Whitesides' Group: Writing a Paper* — organizing and revising the argument around data, tables, and figures: https://doi.org/10.1002/adma.200400767

Faloutsos offers field-oriented writing heuristics, not mandatory publication rules or evidence that a particular figure placement will always succeed. Prefer truthful, reviewable graphics over persuasive showmanship.
