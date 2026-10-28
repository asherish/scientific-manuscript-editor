# Scientific composition

Scientific writing becomes easier to follow when the author plans **what readers should understand, in what order, and with which explanation or evidence**. The techniques below help build and review that path at multiple scales. They are tools for judgment, not mandatory rhetorical templates.

## Design what the reader needs to understand

Begin with the scientific content the author can substantiate. At paper scale, identify the research question, contribution, central claim, assumptions, and available evidence or planned evaluation. At section scale, ask what question the section resolves and why readers need it before the next section. At paragraph scale, identify the specific explanatory move: motivate, define, distinguish, derive, justify, compare, interpret, or qualify. A topic such as “collision probability” is not yet a purpose; “define the event whose probability is estimated” is.

Build an explanation that exposes dependencies. If a method depends on an assumption, introduce or point to that assumption before relying on it. If a result supports a claim only in a particular setting, keep the qualification near the inference. Use a brief outline or a map of claims and evidence when the connections are hard to hold in memory. Do not force one contribution per section, one experiment per research question, or a fixed IMRaD outline if the research calls for another organization.

**Trace major claims across the whole manuscript.** For each substantive contribution or benefit asserted in the Abstract or Introduction, identify the supporting reasoning, experiment, figure, theorem, or other evidence, together with its assumptions and limits. Check that Results answer the relevant question and that the Conclusion claims no more than those findings warrant. Short, stable labels for main contributions can help readers follow the same thread across sections; neither impose a number of labels nor repeat words mechanically. For a pre-experiment manuscript, distinguish planned tests from evidence already obtained.

## Optionally outline by reader questions

**Question → Answer → Paragraph** is a useful scaffold when a passage's purpose or content is not yet clear. Formulate the question an intended reader should be able to answer after reading it; identify an answer grounded in the author's material; gather the supporting definitions, reasoning, evidence, or qualifications; and then write a coherent paragraph or group of paragraphs. The question may remain only in the author's outline. It is not necessary to write an explicit Q&A for every paragraph, and some questions need several paragraphs or a figure and accompanying prose.

Question-first planning can divide a difficult writing task into manageable explanatory modules. For example, a problem-formulation section may need to establish the target task, available inputs, desired output, assumptions, and success criteria. A method section may instead need to explain why each component is needed and how its output advances the overall approach. These are purposes to adapt, not slots in a universal questionnaire.

Use the relevant section reference selected through `SKILL.md` for more detailed guidance. Reader-question planning is consistent with MIT EECS Communication Lab's *Planning Your Paper*, which suggests organizing an outline around questions and answers, and Mensh and Kording (2017, Rules 7 and 9), which describe question-driven results and planning each paragraph's role. These are adaptable writing practices, not requirements for a fixed questionnaire, section order, or paragraph count.

Outlining the answer before prose can reveal missing information and invalid inferences early. Do not fill a gap by inventing a design decision, result, or citation. In an existing well-structured passage, simply use the four core principles and leave it alone when no substantive obstacle exists.

## Make section roles and headings agree

Each section should contribute something identifiable to the paper's argument. Check that its heading names what the section actually covers; its opening establishes the question or purpose when that is not already clear; its subsections arrive in a comprehensible order; and its closing or transition gives readers enough context to proceed. Move material when it depends on an explanation presented later, but keep useful repetition where an abstract, caption, or other passage must stand alone.

Do not replace substantive headings with generic process labels merely to make an outline look uniform. In an Introduction, the logic from prior understanding toward the unresolved research problem is often more important than matching a conventional sequence of headings; see `introduction.md` when that section is the focus.

## Use paragraph writing to convey an explanatory move

A paragraph should have a recognizable central idea or role and enough support for the intended reader to understand it. The support may be a definition, mechanism, example, comparison, derivation, caveat, or evidence. Arrange sentences so that the relation among them is recoverable. Split a paragraph if it is performing unrelated moves that readers cannot comfortably integrate; combine fragments if their separation hides one continuous explanation. Purdue OWL's *On Paragraphs* discusses paragraph unity, topic sentences, supporting evidence, and coherence without prescribing a single position for every topic sentence.

A topic sentence can help, but it need not be the first sentence in every paragraph. A concluding sentence can help when the paragraph needs an inference or transition, but a formulaic summary often adds no value. Paragraph unity does not mean every sentence repeats the same claim; a well-placed qualification or contrast may be essential. Prefer purpose and reader comprehension to a rigid topic–support–conclusion template.

## Choose a rhetorical pattern for the purpose

Several established patterns can make a paragraph or larger explanation easier to compose or assess. They answer **different questions** and can be combined; none is a mandatory template.

| Pattern | Useful question | Appropriate use |
|---|---|---|
| **Topic–Supporting–(optional) Concluding** | What is this paragraph's central move, and how do its sentences support it? | Paragraph unity, supporting details, evidence, and necessary qualifications. |
| **Pyramid / claim–support** | Why or how does the evidence justify this claim? | Presenting a claim alongside reasons or mechanisms; checking whether the conclusion exceeds its premises. |
| **Context–Content–Conclusion (CCC)** | What context is needed, what advances the explanation, and what follows? | Organizing paragraphs, sections, Abstracts, or an argument as a whole when context-first exposition helps. |
| **Problem–Solution** | What difficulty motivates the approach, and how is it addressed? | Explaining a research problem, intervention, or methodological choice. |

In a claim–support paragraph, ask whether the cited results actually entail or substantiate the stated conclusion. A convenient or flexible method is not automatically effective, reliable, or generalizable. An optional concluding sentence should communicate a warranted inference, not inflate the opening claim. A CCC sequence should orient readers without burying the central contribution in background. A Problem–Solution passage should distinguish the proposed solution from demonstrated success; scientific discourse research distinguishes the problem, the response, and its evaluation. These patterns help diagnose meaning, not merely rearrange labels.

Use the same ideas across scales cautiously. A whole paper can establish context in the Introduction, develop evidence in Methods and Results, and interpret it in Discussion, but disciplinary structures vary. Section-level CCC can be useful; requiring every section and paragraph to follow identical three-part shapes creates repetition. Paragraphs can be designed as modules without forcing a fixed count or length.

## Lead from established context toward new information

**Readers generally follow new information more easily when it is anchored to information they already know or that the manuscript has established.** This is the known-to-new (given-to-new) heuristic, closely related to accessible-context-to-new-information and Haviland and Clark's given–new account. It applies across scales:

- **Within a sentence:** A familiar entity or condition can orient readers before introducing an unfamiliar result or distinction.
- **Between sentences:** A previous result, entity, or question can provide the starting point for the next sentence's new contribution.
- **Between paragraphs and sections:** An established finding or limitation can motivate the next question, method, or analysis.

For illustration, compare a jarring transition—“The estimator uses a calibration factor. The observation rate varies across locations.”—with a connected one—“The observation rate varies across locations. To account for this variation, the estimator uses a calibration factor.” The second sequence is easier **if observation-rate variation is already relevant to the reader**. This is a hypothetical writing example, not a claim about any particular estimator.

Do not mechanically put old information at the beginning of every sentence. Surprise, contrast, definitions, and mathematical exposition can justify another order. Also do not mistake an unsupported or unknown premise for shared knowledge. Ask what context the intended reader can actually retrieve, and place genuinely new information where its role is clear.

The progression from established research context toward an identifiable gap (Mensh & Kording; Swales) is another way to reason about reader expectations, especially in an Introduction. None of these patterns is a template to impose on every paragraph.

**Use topic and stress positions as additional reader-expectation lenses.** Where helpful, put the subject that a sentence is about and the context linking backward near its opening, and place the important new contribution where the reader will notice the emphasis, often toward the end. Keep subjects and actions easy to identify. Gopen and Swan describe these as interpretive principles, not fixed rules: technical precision, contrast, or another rhetorical purpose may justify a different order.

## Integrate mathematical and visual elements with prose

**Equations are part of an explanation, not detached objects.** Use surrounding sentences to establish the quantity or relationship being defined, explain non-obvious symbols and assumptions, and interpret what the expression means or why this form is useful. Avoid stopping after a mechanical “where x is…” list if readers still cannot understand the equation's role. Conversely, do not restate a self-evident expression at length.

**Figures and tables complement the narrative.** A figure can reveal geometry, dependencies, trends, or examples that would be cumbersome in prose; a table can make definitions, experimental conditions, or results comparable. Choose the representation for the relationship it helps readers see.

Captions identify what is shown, including necessary units, conditions, and encodings. Surrounding paragraphs explain why the figure or table matters and what consequential observation or inference readers should take from it. Neither narrate every bar or cell nor leave the interpretation entirely to readers. Check that prose, caption, legend, labels, and values agree.

An overview figure can orient readers before they encounter detailed explanations. At paper scale, it may establish the problem setting, central idea, or study design. At section scale, it may reveal entities or dependencies that later paragraphs develop.

A processing diagram should show actual inputs, transformations, intermediate quantities, and outputs. **Boxes labeled only with section headings do not explain a scientific relationship.** Neither Figure 1 nor a pipeline diagram is automatically required; use an equation, table, or concise prose if it communicates better. If a needed figure cannot yet be grounded in available material, describe its purpose with `[FIGURE: ...]` rather than inventing contents.

When the visual itself needs to be designed or evaluated, use `figures.md` for the detailed figure/table decision, caption, plot-encoding, and evidence checks. An optional figure-and-table outline can clarify the evidential structure before drafting long prose; it does not dictate a writing order.

## Support multiple routes through the paper

Readers may encounter the Abstract, headings, figures and captions, or Conclusion before reading every intervening paragraph. Check whether those entry points convey a consistent, bounded scientific takeaway and whether a reader seeking its evidence can locate the relevant analyses or definitions. A caption may need enough self-contained context even when the surrounding text already defines it. Do not turn useful signposting into repetitive marketing language.

## Check the result from the reader's position


After composing or rearranging, follow the reader's path: What do they know at this point? What question does the next passage answer? Can they understand important terms, equations, evidence, and relations without excessive searching backward? Does a transition express cause, contrast, condition, inference, or mere addition accurately? Does each section deliver what its heading promises?

Repair the source of confusion at the smallest effective scale. That may mean defining a term, changing a sentence, moving a paragraph, adding a conceptual overview, or redesigning a whole argument. An unchanged passage is acceptable when it already serves its readers.

## Further reading

- Mensh and Kording (2017), *Ten simple rules for structuring papers*: https://doi.org/10.1371/journal.pcbi.1005619
- Gopen and Swan (1990), *The Science of Scientific Writing* — reader expectations, topic/stress positions: https://www.cs.tufts.edu/comp/150FP/archive/george-gopen/sci.html
- Peyton Jones, *How to Write a Great Research Paper* — explicit claims and evidence in the body: https://john.cs.olemiss.edu/~hcc/researchMethods/2016spr/notes/PeytonJones/Writing_paper_handout.pdf
- Purdue Online Writing Lab, *On Paragraphs* (topic sentences, paragraph unity, support, and coherence): https://owl.purdue.edu/owl/general_writing/academic_writing/paragraphs_and_paragraphing/
- Purdue Online Writing Lab, *Organizing Your Argument* (claims, evidence, and warrants in the Toulmin model): https://owl.purdue.edu/owl/general_writing/academic_writing/establishing_arguments/organizing_your_argument.html
- Minto (1996), *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving* (hierarchical claim–support organization): https://barbaraminto.com/
- Heffernan and Teufel (2018), *Identifying problems and solutions in scientific text* (problem–response–evaluation discourse patterns): https://doi.org/10.1007/s11192-018-2718-6
- MIT EECS Communication Lab, *Journal or Conference Paper: Planning Your Paper* (reader questions, answer-first planning, flexible section tasks): https://mitcommlab.mit.edu/eecs/commkit/journal-or-conference-paper/
