---
type: method
area: me697
areas: [me697, uq]
tags: [uq, sampling]
---

# Sobol indices

**Summary**: Variance-based global sensitivity measures. The first-order index of an input is the share of output variance explained by that input alone; the total index adds all interactions involving it.

---

## Definitions
Wiki note: the standard definitions (the lecture states them in words only). For output $Y=f(X_1,\dots,X_d)$ with independent inputs:
$$S_i=\frac{\mathbb V\big[\mathbb E[Y\mid X_i]\big]}{\mathbb V[Y]}$$
$$S_{T_i}=1-\frac{\mathbb V\big[\mathbb E[Y\mid X_{\sim i}]\big]}{\mathbb V[Y]}$$
$X_{\sim i}$ is all inputs except $X_i$.

## What the book does (08)
- SALib: `sobol.sample` draws a Saltelli design from a Sobol sequence; `analyze` returns `S1`, `ST` (and second-order terms if requested).
- Duffing oscillator, parameter ranges $\pm1\%$, $N=512$, indices per time step for $x(t)$ and $v(t)$.
- First-order indices often do not sum to 1: interactions carry variance. Total indices sum to at least 1 and rarely less.
- Cost: the design size is a multiple of $N$ that grows with $d$, so doing this on the true model is expensive. On a surrogate it is cheap (autoinjector example: injection time depends mostly on viscosity and needle diameter) (source: `up/surrogates/02_nn_surrogates.ipynb`).

## From polynomial chaos
With an orthonormal expansion $f=\sum_\alpha c_\alpha\phi_\alpha$, variance is $\sum_{\alpha\ne0}c_\alpha^2$, and each index is the sum of $c_\alpha^2$ over multi-indices involving the input(s), divided by that total. Wiki note: standard PCE result, the lecture only says the indices can be read off the expansion (source: `05_pc_ode_1d.ipynb`, `07_pce_dynamical_system.ipynb`).

## Wiki notes
- "Indices sum to 1" holds only for additive models. In general first-order indices sum to at most 1.
- The inputs must be independent for these definitions to apply **[unverified]** for the book's usage, which does not say.

> [!example] Homework 2, Duffing Sobol indices (source: homework/02_homework.ipynb)
> Map each $\theta_i$ to a uniform $\xi_i$ through its CDF, then compute Sobol indices of the Duffing oscillator on $t\in[0,30]$ with step 0.1.

**Covered in**: ASML book up/sensitivity_analysis (ME 697 2.1); homework 2
**Sources**: `courses/ME 697/advanced-scientific-machine-learning/book/up/sensitivity_analysis/07_sobol.ipynb`, `08_global_sensitivity_analysis.ipynb`; `up/surrogates/02_nn_surrogates.ipynb`, `courses/ME 697/advanced-scientific-machine-learning/book/up/intro.md`, `up/sensitivity_analysis/00_intro.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sensitivity analysis]] · [[Latin hypercube sampling]] · [[Polynomial chaos]] · [[Surrogate model]]
