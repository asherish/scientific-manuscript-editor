# Problem statement: specify what the research asks

The Problem Statement defines **what must be solved or investigated**, independently of the particular approach proposed by the paper. Readers should leave it knowing the target outcome, available information, and boundaries of the task.

## Organize the formulation around reader dependencies

The opening **should** orient readers to the situation being studied and what must be determined. Arrange the explanation so that readers encounter the entities and relationships needed to understand a definition before that definition relies on them. Apply the paragraph principles in `composition.md`: each paragraph **should** perform one recognizable explanatory move, such as describing the task, defining an output, or explaining a restriction, with the supporting definitions, reasons, and conditions kept together.

When a formal definition would be hard to interpret without an intuitive account, **consider** introducing the situation and input–output relationship in ordinary language before formalizing them. One possible progression is situation → available inputs and desired output → formal definition → conditions and success criteria. Adapt the order to dependencies: an assumption may need to precede the quantity it makes meaningful, or the objective may need to come first to explain why particular inputs matter. Map the prose to the formal objects rather than presenting two disconnected descriptions.

When the section is long or its definitions are dispersed, **consider** closing with a concise synthesis of what is given, what is sought, and under which conditions. Supply the context needed to proceed to the Method without repeating an already clear formulation.

## Define the objective and a valid solution

The Problem Statement **should** state the target task, phenomenon, or research question precisely. Explain what would count as a valid, desirable, or useful outcome and why; distinguish the objective of the task from properties that the proposed method happens to produce. If the study makes predictions, estimates, classifications, decisions, or explanations, specify the intended meaning and relevant granularity of each output.

Separate information provided by the task from quantities produced inside a particular method. For example, an observed image can be an input to the task, whereas features extracted from it belong to the proposed method. Specify units, domains, time horizons, spatial scales, populations, and other dimensions when they affect interpretation. Define unfamiliar terms and author-created quantities where readers first need them; use `notation.md` for symbol conventions when applicable.

When using both an ordinary-language account and a mathematical definition, connect them: identify which formal objects represent the described inputs, outputs, and relationships. Explain why the chosen formulation addresses the research question, especially when alternative formulations would represent a different objective.

## Make scope and assumptions testable

Explicitly state material assumptions, restrictions, exclusions, and operating conditions. Distinguish the general research problem from the subset actually investigated. Avoid silently extending an estimate, method, or empirical finding to settings excluded by the formulation. Where success requires an evaluation criterion, describe what it measures and how it relates to the target problem; detailed metric selection and implementation belong to `experiments.md`.

Place each assumption or restriction where readers can identify the definition or claim it limits; introduce it before relying on it, or provide an explicit reference when it is established elsewhere.

When objectives rely on proxies, the construct-validity link **must** be audited. Trace the intended phenomenon or capability to the observable target, task or labels, chosen metric, and claim the paper hopes to support. For example, accuracy on a surrogate annotation task may not alone establish the validity of a broad real-world risk claim. State the assumptions linking the proxy to the construct and what the evaluation cannot establish; do not treat a score as proof of a wider phenomenon.

## Show a representative case when it clarifies the formulation

When unfamiliar entities, inputs, outputs, or boundary cases obstruct understanding, **consider** a concrete example or schematic. Choose a representative case that is consistent with the formal definition; an illustrative example is not evidence of empirical performance. Introduce the figure in prose and interpret its role, identifying which entities or relationships in the definition the example or schematic makes concrete. General principles for integrating figures, equations, and prose belong to `composition.md`; use `figures.md` for detailed figure or table design and verification when the visual itself is the focus.

## Check the reader's route and the formulation's consistency

Use these checks when drafting or reviewing the formulation. If the passage already meets a reader need, retain it; report consequential findings at the level appropriate to the user's task rather than reproducing this table as a mandatory deliverable.

| Check | Fix when the check fails |
|---|---|
| Can the intended reader identify what must be determined from the opening, using context already established? | Add or move a concise task overview before details whose purpose is unclear. |
| Does each definition rely only on concepts already explained or reasonably known to the intended reader? | Introduce the prerequisite or reorder the definitions. |
| Can readers map the verbal account to the formal inputs, outputs, and relationships? | Explain the correspondence or resolve a substantive mismatch with the author. |
| Can each paragraph's explanatory role be stated briefly? | Split unrelated moves or combine fragments that obscure one continuous explanation. |
| Is it clear which definition or claim each assumption restricts? | Move the condition near its use or add an explicit reference. |
| Before the Method, are the available information, target outcome, and material conditions recoverable? | Supply missing definitions; add a closing synthesis only when their dispersion makes it useful. |

### Check against the rest of the paper

Verify that the Method actually operates on the declared inputs, that the Experiments assess the stated output or objective, and that the Results and Conclusions do not silently change the target task. If these disagree, resolve the scientific definition before polishing prose. Do not fill unresolved definitions with invented author decisions.

## Sources and applicability

- Abhiram Ranade, IIT Bombay, *Report Writing* — problem statements (PDF p. 6), dependency-based ordering (p. 12), section overviews and summaries (p. 13), and paragraph unity (p. 19): https://www.cse.iitb.ac.in/~ranade/facad/archive/w3.pdf
- University of Illinois, CS 510 lecture material, *Typical Structure of a Research Paper (cont.)*, “Problem definition/formulation” — informal and formal descriptions, reasons for the formulation, assumptions, and challenges: https://timan.cs.illinois.edu/pdfjs_csintro/static/slides/CS%20510/optimizing-research/CS%20510---optimizing-research---slide34.pdf
- MIT EECS Communication Lab, *Paper: Introduction* — stating the research problem, motivation, and intended contribution: https://mitcommlab.mit.edu/eecs/commkit/journal-article-introduction/
- MIT EECS Communication Lab, *Paper: Methods (CS)* — explaining a technical approach at the level needed for appraisal and replication: https://mitcommlab.mit.edu/eecs/commkit/journal-article-methods-cs/
- NeurIPS, *Paper Checklist Guidelines* — communicating claims, assumptions, limitations, and evaluation conditions: https://neurips.cc/public/guides/PaperChecklist
- Bean et al. (2025), *Measuring What Matters: Construct Validity in Large Language Model Benchmarks* — connecting evaluated phenomena, tasks, metrics, and claims: https://proceedings.nips.cc/paper_files/paper/2025/hash/1967e0fc3aa6cbbace562f5cb8e3954e-Abstract-Datasets_and_Benchmarks_Track.html

These sources collectively support clear task and scope definitions; none mandates an independent Problem Statement section or one universal list of inputs, outputs, and metrics. NeurIPS checklist items are venue-specific reporting guidance. Bean et al. studies LLM benchmarks; apply its construct-validity principle to other fields only where the measurement problem is analogous.

Ranade and the Illinois slides provide educational writing guidance, not experimental evidence that a particular paragraph order is optimal. The example progression, placement guidance, and Check / Fix table above adapt their principles to problem formulation; neither source prescribes that exact sequence or checklist, and the checks are not a validated scoring instrument. Ranade discusses technical reports more broadly, whereas the Illinois slide directly addresses research-paper problem formulation.
