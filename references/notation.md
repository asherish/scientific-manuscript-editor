# Notation: keep mathematical objects identifiable

Notation helps readers recognize **which mathematical object a symbol denotes and when two expressions refer to the same thing**. The goal is consistency and intelligibility. A coherent convention already used in the manuscript may be better than an extensive typographic rewrite.

## Prioritize semantic coherence

- Distinguish genuinely different objects when their notation would cause confusion. Avoid reusing one symbol for different meanings within an overlapping scope; some reuse across clearly separated contexts may be harmless.
- Keep a defined object's representation consistent enough to be identifiable (for example, do not alternate between $x$ and $\mathbf{x}$ for one vector without explanation).
- When many interdependent symbols are difficult to track, **consider** a notation table.
- If a symbol is overloaded, identify which equations, definitions, figure labels, prose descriptions, and cross-references belong to **each semantic role**. Rename only the relevant role. Do not run a global string replacement.
- Treat a consequential renaming as a **Semantic** change under `SKILL.md`. Document the reason and all affected scientific elements, and verify every occurrence semantically. Follow `references/verification.md` for the authoritative `approved_changes.txt` syntax and verification procedure.

## Choose a convention only when needed

Notation conventions **should** follow established usage in the target venue, field, and central prior work, then the manuscript's existing consistent practice; use the table below as a tie-breaker when a choice remains unresolved. Record any adopted or changed notation convention in the edit change log, not as a typographic-convention statement in the paper. Explain the **meaning** of notation in the manuscript when readers need that explanation; do not insert prose merely to justify font choices. 

| Notation | Typical use (not a requirement) | Examples |
|---|---|---|
| Lowercase Greek | Parameters, hyperparameters, coefficients, some standard functions | $\theta$, $\lambda$, $\alpha$, $\epsilon$, $\sigma(\cdot)$ |
| Calligraphic | Sets, spaces, collections, loss functions, distributions, complexity classes | $\mathcal{V}$, $\mathcal{D}$, $\mathcal{X}$, $\mathcal{L}$, $\mathcal{O}(\cdot)$ |
| Blackboard bold | Number sets, expectation, indicators | $\mathbb{R}$, $\mathbb{N}$, $\mathbb{E}$, $\mathbb{1}[\cdot]$ |
| Lowercase italic | Scalars and indices | $x$, $i$, $t$ |
| Uppercase italic | Counts, dimensions, random variables, graphs | $N$, $T$, $X$, $G$ |
| Bold lowercase / uppercase | Vectors / matrices when field practice uses bold | $\mathbf{x}$ / $\mathbf{W}$ |
| Bold sans-serif or another distinct consistent form | Higher-order tensors, if distinguishing tensors helps | $\boldsymbol{\mathsf{T}}$ |
| Italic subscripts | Variables and indices | $x_i$, $y_t$ |
| Upright subscripts | Descriptive labels, words, abbreviations | $v_{\mathrm{max}}$, $\mathcal{L}_{\mathrm{CE}}$, $\mathcal{D}_{\mathrm{train}}$ |
| Upright mathematical text | Named functions, operators, units | $\log$, $\exp$, $\operatorname{softmax}$, $10\,\mathrm{m}$ |
| Monospace | Code identifiers and filenames | `edge_id`, `osmnx` |
| Conditioning separator (`\mid`) | Conditional probabilities or densities | $p(y\mid \mathbf{x})$ |
| Semicolon (`;`) | Separating inputs from fixed or model parameters, when customary | $f(\mathbf{x};\theta)$, $p(y\mid\mathbf{x};\theta)$ |
| Set-builder separator | A chosen consistent style (`\mid` or colon) | $\{v\in\mathcal{V}\mid d(v)>\tau\}$ |

## Sources and applicability

Goodfellow, Bengio & Courville, *Deep Learning* (2016), for common machine-learning notation; ISO 80000-2 for mathematical signs and symbols in science and technology. These are reference points rather than a mandate overriding a journal's or discipline's convention.
