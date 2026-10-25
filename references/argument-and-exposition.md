# Scientific argument and exposition

Use this reference when designing a new manuscript or substantial passage, diagnosing a difficult explanation, reorganizing sections or paragraphs, or deciding how prose should work with mathematical and visual elements. These are **tools for reader understanding**, not mandatory rhetorical templates.

## Design what the reader needs to understand

Begin with the scientific content the author can substantiate. At paper scale, identify the research question, contribution, central claim, assumptions, and available evidence or planned evaluation. At section scale, ask what question the section resolves and why readers need it before the next section. At paragraph scale, identify the specific explanatory move: motivate, define, distinguish, derive, justify, compare, interpret, or qualify. A topic such as “collision probability” is not yet a purpose; “define the event whose probability is estimated” is.

Build an explanation that exposes dependencies. If a method depends on an assumption, introduce or point to that assumption before relying on it. If a result supports a claim only in a particular setting, keep the qualification near the inference. Use a brief outline or a map of claims and evidence when the connections are hard to hold in memory. Do not force one contribution per section, one experiment per research question, or a fixed IMRaD outline if the research calls for another organization.

## Make section roles and headings agree

Each section should contribute something identifiable to the paper's argument. Check that its heading names what the section actually covers; its opening establishes the question or purpose when that is not already clear; its subsections arrive in a comprehensible order; and its closing or transition gives readers enough context to proceed. Move material when it depends on an explanation presented later, but keep useful repetition where an abstract, caption, or other passage must stand alone.

Do not replace substantive headings with generic process labels merely to make an outline look uniform. In an Introduction, the logic from prior understanding toward the unresolved research problem is often more important than matching a conventional sequence of headings; see `introduction.md` when that section is the focus.

## Use paragraph writing to convey an explanatory move

A paragraph should have a recognizable central idea or role and enough support for the intended reader to understand it. The support may be a definition, mechanism, example, comparison, derivation, caveat, or evidence. Arrange sentences so that the relation among them is recoverable. Split a paragraph if it is performing unrelated moves that readers cannot comfortably integrate; combine fragments if their separation hides one continuous explanation.

A topic sentence can help, but it need not be the first sentence in every paragraph. A concluding sentence can help when the paragraph needs an inference or transition, but a formulaic summary often adds no value. Paragraph unity does not mean every sentence repeats the same claim; a well-placed qualification or contrast may be essential. Prefer purpose and reader comprehension to a rigid topic–support–conclusion template.

## Lead from established context toward new information

**Readers generally follow new information more easily when it is anchored to information they already know or that the manuscript has established.** This is the known-to-new (given-to-new) heuristic, closely related to accessible-context-to-new-information and Haviland and Clark's given–new account. It applies across scales:

- **Within a sentence:** A familiar entity or condition can orient readers before introducing an unfamiliar result or distinction.
- **Between sentences:** A previous result, entity, or question can provide the starting point for the next sentence's new contribution.
- **Between paragraphs and sections:** An established finding or limitation can motivate the next question, method, or analysis.

For illustration, compare a jarring transition—“The estimator uses a calibration factor. The observation rate varies across locations.”—with a connected one—“The observation rate varies across locations. To account for this variation, the estimator uses a calibration factor.” The second sequence is easier **if observation-rate variation is already relevant to the reader**. This is a hypothetical writing example, not a claim about any particular estimator.

Do not mechanically put old information at the beginning of every sentence. Surprise, contrast, definitions, and mathematical exposition can justify another order. Also do not mistake an unsupported or unknown premise for shared knowledge. Ask what context the intended reader can actually retrieve, and place genuinely new information where its role is clear.

Other useful, nonbinding patterns include context–content–conclusion and the progression from established research context toward an identifiable gap (Mensh & Kording; Swales). These are ways to reason about reader expectations, not templates to impose on every paragraph or Introduction.

## Integrate mathematical and visual elements with prose

**Equations are part of an explanation, not detached objects.** Use surrounding sentences to establish the quantity or relationship being defined, explain non-obvious symbols and assumptions, and interpret what the expression means or why this form is useful. Avoid stopping after a mechanical “where x is…” list if readers still cannot understand the equation's role. Conversely, do not restate a self-evident expression at length.

**Figures and tables complement the narrative.** A figure can reveal geometry, dependencies, trends, comparisons, or examples that would be cumbersome in prose. A table can make definitions, experimental conditions, or results comparable. Captions should identify what is shown, including necessary units, conditions, and encodings; prose should introduce the relevant element and explain its consequential features or implications. Do not narrate every bar, cell, arrow, or axis value, and do not leave the reader to guess why the element matters. Check that text, caption, legend, label, and quantitative values agree.

At paper scale, an overview figure may establish the problem setting, central scientific idea, approach relative to existing work, or study design. At section scale, it may orient readers to the entities or dependencies developed in later paragraphs. In a processing pipeline, it may show inputs, transformations, intermediate representations, and outputs. **A chain of boxes labeled only with section headings does not itself explain a scientific relationship.** Neither Figure 1 nor a pipeline diagram is mandatory. Use a table, equation, or concise prose instead when it communicates better. If a needed figure cannot be grounded in the available material, specify what it should convey or use `[FIGURE: ...]`; never fabricate results.

## Check the result from the reader's position

After composing or rearranging, follow the reader's path: What do they know at this point? What question does the next passage answer? Can they understand important terms, equations, evidence, and relations without excessive searching backward? Does a transition express cause, contrast, condition, inference, or mere addition accurately? Does each section deliver what its heading promises?

Repair the source of confusion at the smallest effective scale. That may mean defining a term, changing a sentence, moving a paragraph, adding a conceptual overview, or redesigning a whole argument. An unchanged passage is acceptable when it already serves its readers.
