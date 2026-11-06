---
type: concept
area: me697
areas: [me697, uq]
tags: [uq, sampling, optimization]
---

# Sensitivity analysis

**Summary**: Asking how much a model output changes when its inputs change. The course splits it into local analysis (derivatives at a nominal point) and global analysis (variance-based, over the whole input range). Both are used to find which uncertain inputs matter before spending effort on them.

---

## Local sensitivity
- Linearize the output in the parameters about a nominal value. For an ODE $\dot x=f(x,t,\theta)$ with Gaussian $\theta\approx\mathcal N(\mu,\Sigma)$ the first-order solution is a Gaussian process.
- The needed derivative $\nabla_\theta x$ comes from autodiff through the solver or from a sensitivity ODE. See [[Local sensitivity analysis of ODEs]].
- Valid only for small input uncertainty, differentiable $f$, and non-chaotic dynamics. On the Lorenz system it fails quickly (source: `up/sensitivity_analysis/01_theory.md`, `04_example_lorenz.ipynb`).

## Global sensitivity
- Decompose the output variance into contributions of each input and of their interactions: [[Sobol indices]].
- Needs many model runs on a space-filling design ([[Latin hypercube sampling]], Sobol sequence), or a cheap [[Surrogate model]] or [[Polynomial chaos]] expansion, from which the indices come almost free.
- Duffing example, $\ddot x+\delta\dot x+\alpha x+\beta x^3=\gamma\cos(\omega t)$ with nominal $(\alpha,\beta,\gamma,\delta,\omega)=(1,5,0.37,0.1,1)$, zero initial state, $t\in[0,50]$ (limit cycle): early output variance is dominated by one parameter ($\gamma$), later by another ($\omega$), and interactions matter because first-order indices do not sum to 1 (source: `08_global_sensitivity_analysis.ipynb`).

## Choosing a method
| Question | Tool |
|---|---|
| Small perturbation about a point | local, one Jacobian |
| Which inputs drive the variance | Sobol indices |
| Full output density, few inputs | [[Polynomial chaos]], [[Fokker-Planck equation]] |
| Expensive model, many queries | [[Surrogate model]] first |

Wiki note: this table is a summary of the lecture's structure, not a table from the book.

## Where it appears
- Local and global methods (SALib); [[Polynomial chaos]] (indices from coefficients), [[Surrogate model]] (indices from a surrogate).
- Related idea in optimization: the gradient is a local sensitivity; see [[Automatic differentiation]].

**Covered in**: ASML book up/sensitivity_analysis (ME 697 2.1)
**Sources**: `text_books/advanced-scientific-machine-learning/book/up/sensitivity_analysis/00_intro.md`, `01_theory.md`, `04_example_lorenz.ipynb`, `08_global_sensitivity_analysis.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Local sensitivity analysis of ODEs]] · [[Sobol indices]] · [[Latin hypercube sampling]] · [[Polynomial chaos]]
- [[Surrogate model]] · [[Gaussian process]] · [[Fokker-Planck equation]]
