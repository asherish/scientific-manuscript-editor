# Scientific figure and table design

Figures and tables should help the intended reader understand or evaluate a scientific idea, comparison, or body of evidence. Figures and tables **should** be designed from a **reader question and an evidence-supported message**. Use these principles when a visual would materially reduce understanding effort; concise prose or an equation may be more effective.

## Decide what the visual must communicate

State the question the reader should answer from the visual and what the available data or definitions actually establish. Identify whether its main role is to **orient** (a task example, conceptual relationship, or method overview), **define** (a data or notation table), **compare** (methods or conditions), or **substantiate** (a finding with measured evidence). A visual can serve more than one role, but its message and labels must not imply unsupported conclusions.

When figure planning would help expose missing evidence before prose is drafted, **consider** a figure-first outline of potential figures and tables. In pre-experiment writing, describe intended axes, variables, comparisons, and conditions without inventing measured values; use a grounded `[FIGURE: ...]` placeholder if necessary.

## Choose a representation that exposes the relationship

Use a diagram for meaningful entities, dependencies, mechanisms, or data flow; a table for precise repeated comparisons or definitions; and a plot for patterns in empirical values. A pipeline diagram should communicate actual inputs, transformations, intermediate quantities, and outputs, not merely section names connected by arrows.

Choose plot encodings according to data type, sample size, uncertainty, and the intended comparison. Check that scales, baselines, axis limits, units, denominators, grouping, aggregation, and any normalization do not distort interpretation. When a mean would conceal important spread or unusual observations, show suitable distributional information (for example, individual points for manageable samples, a box plot, or a distribution plot). 

Use legible text, meaningful labels, and distinguishable visual encodings. Do not rely on color alone to express a critical distinction. Avoid needless visual decoration and verify that the plot remains understandable at the target venue's display or print size.

## Choose tools to match the representation

Tool selection **should** follow the intended representation and the control it requires: numerical fidelity, connectivity, geometry, text, visual clarity, revision, and regeneration. Honor the user's specified tools and use capabilities actually available in the working environment. Check export options against the venue's accepted formats and intended display size. The same representation can be produced by several tool families; choose by the figure's needs rather than a fixed ranking.

| Representation or production need | Candidate tools | Selection question |
|---|---|---|
| Data-driven plots | matplotlib, ggplot2, PGFPlots | Can the plot be regenerated from source data with the required scales, aggregation, and uncertainty? |
| Connectivity-focused diagrams | Mermaid, Graphviz | Does automatic layout communicate the intended dependencies, branches, or transitions clearly? |
| Precisely positioned schematics | TikZ/PGF, direct SVG authoring | Can geometry, equations, labels, and placement be controlled at the needed precision? |
| Visual editing and panel layout | Inkscape, draw.io/diagrams.net | Would direct manipulation make construction, revision, or collaboration easier? |
| Existing-image processing and annotation | Pillow or an appropriate image editor | Can crops, annotations, and transformations be checked against the source images? |
| Geographic figures | QGIS or an appropriate geospatial plotting tool | Can coordinates, projection, scale, and spatial relationships be represented correctly? |
| Three-dimensional shapes or arrangements | Blender or an appropriate 3D tool | Does the explanation require controlled geometry, viewpoint, or occlusion? |
| Illustrations, model architectures, and method or pipeline overviews | Available image-generation tools, including image_gen | Would integrated shapes, icons, and visual styling make the scientific structure easier to understand? |
| Numerical or definition tables | Data processing plus LaTeX or the manuscript's table facilities | Can values remain consistent with their source while the typeset table stays readable? |

When a model or pipeline diagram needs to combine model-specific shapes with training or frozen states and data flow, **consider** image generation alongside code-based drawing and visual editors. Define the scientific content first: components, model types, inputs and outputs, connections, and training states actually present in the work. Shapes, colors, and icons **should** have explicit meanings where they encode scientific distinctions; explain those meanings through labels or a legend. A snowflake or lock, for example, should not leave readers guessing whether it means frozen weights, restricted access, or something else. Use additional guidance in `ml.md` when learned components are involved.

Scientific accuracy is a verification requirement for every production method, including image generation. Generate measured plots and numerical tables from their source data; an illustrative rendering is not measured evidence. For diagrams, compare the completed image with the defined structure regardless of how it was made.

Tools can be combined: for example, generate a plot from data and assemble panels in a vector editor, or combine generated illustrations with separately typeset labels. Retain the source data, code, editable documents, and, where applicable, generation prompts and reference assets needed for later revisions. For generated imagery, these records support revision and provenance rather than guaranteeing identical regeneration. Distinguish production methods from output formats: SVG, PDF, and PNG alone do not identify how an image was made or how editable it remains.

## Put consequential evidence where readers can find it

When a paper has an important, easy-to-understand result or real-world example that directly conveys its central contribution, consider showing it early as a **crown-jewel figure**. Select it for explanatory and evidential value, not simply because it is the most favorable result. One or more visuals may be appropriate; some papers are better served by a problem example or conceptual overview, and others need no early figure.

In the Introduction, orient the reader to what the figure demonstrates and how it connects to the research question. Never present a planned result as observed or let a selective showcase conceal conflicting results or important limitations.

## Write captions that stand on their own

Make the figure or table identifiable without forcing the reader to search the main text for its subject: describe the compared quantities or entities, meaningful conditions, units, encodings, and interpretation aids at the detail needed for correct reading. The text should develop the implication rather than mechanically repeat every plotted mark.

**Two- or three-word bold takeaway tag:** When a concise, evidence-supported result would help a reader scanning the figures, consider starting the caption with a bold 2–3-word label. Examples include **Linear scaling.**, **Improved recall.**, and **Consistent performance gains.** These are illustrative labels, not claims about any particular experiment.

Follow the label with an informative description. For example: “**Linear scaling.** Runtime versus input size under the stated hardware and workload.” The label must not turn uncertainty or correlation into a stronger claim.

Omit a takeaway tag when a descriptive title is clearer, the message is not a supported result, the label adds clutter, or venue conventions disallow it.

## Integrate figures with the argument and verify them

Each visual **should** be introduced near the relevant question or claim, referenced accurately, and accompanied by an explanation of its consequential observation or conceptual relationship. Align the prose, caption, legend, symbols, data values, and units. Distinguish a demonstration or cherry-picked example from an estimate of population-wide performance. Explain relevant uncertainty, experimental conditions, and caveats.

Review the graphic at its likely display size and as a standalone entry point: What will the reader think it shows? Does that takeaway match the evidence and the text? Can its axes, comparisons, and uncertainty be interpreted? If a reader's likely inference is stronger than warranted, repair the encoding, caption, or prose. Respect applicable venue instructions.

Check the exported artifact as well as the working version: compare plotted values and table entries with source data, and compare diagram components and connections with the definitions. For model diagrams, verify model types, trained/frozen states, arrow directions, branches, and labels against the Method. Check for missing or invented elements, ambiguous shape or icon meanings, and export damage to text, equations, lines, or layout. Confirm that the sources needed to revise the figure remain available.

## Sources and applicability

- Faloutsos, *MetaPaper v14* — early crown-jewel figure and optional short caption takeaway tags: https://www.cs.cmu.edu/~christos/MetaPaper/faloutsos_MetaPaper_v14.pdf
- Faloutsos, *Lessons from 1K Rejected Research Papers* — reader attention and showing what a method achieves: https://www.cs.cmu.edu/~christos/MetaPaper/faloutsos_MetaPaper_1KR.pdf
- Rougier, Droettboom, and Bourne (2014), *Ten Simple Rules for Better Figures* — audience, message, graphic construction, and medium: https://doi.org/10.1371/journal.pcbi.1003833
- Weissgerber et al. (2015), *Beyond Bar and Line Graphs* — how aggregate plots can conceal very different data distributions: https://doi.org/10.1371/journal.pbio.1002128
- Whitesides (2004), *Whitesides' Group: Writing a Paper* — organizing and revising the argument around data, tables, and figures: https://doi.org/10.1002/adma.200400767

Faloutsos offers field-oriented writing heuristics, not mandatory publication rules or evidence that a particular figure placement will always succeed. Prefer truthful, reviewable graphics over persuasive showmanship.

### Tool documentation and selection scope

The tool table is an editorial mapping from documented capabilities to figure needs, not evidence that one tool is academically superior. Consult current official documentation for the tools actually selected:

- Plotting: [matplotlib](https://matplotlib.org/stable/plot_types/), [ggplot2](https://ggplot2.tidyverse.org/), and [PGFPlots](https://tikz.dev/pgfplots/).
- Structural and geometric diagrams: [Mermaid](https://mermaid.js.org/intro/), [Graphviz](https://graphviz.org/), [PGF/TikZ](https://tikz.dev/), and the [SVG specification](https://www.w3.org/TR/SVG2/).
- Visual editing: [Inkscape project](https://github.com/inkscape/inkscape) and [draw.io](https://www.drawio.com/).
- Specialized production: [Pillow](https://pillow.readthedocs.io/en/stable/), [QGIS print layouts](https://documentation.qgis.org/3.44/en/docs/user_manual/print_composer/index.html), and [Blender](https://www.blender.org/features/).

For image generation, use the documentation of the available tool or provider. The model-diagram selection example and its verification guidance are editorial applications of the scientific-fidelity principles above, not claims that image generation always outperforms other methods.
