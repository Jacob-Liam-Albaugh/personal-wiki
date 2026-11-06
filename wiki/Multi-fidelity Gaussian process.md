---
type: method
area: gp
areas: [gp, uq]
source-ref: "Lee, Bilionis, Buganza Tepole 2020, eqs. 20-23"
tags: [gp, uq, ml]
---

# Multi-fidelity Gaussian process

**Summary**: A GP model that fuses data from several simulators or experiments of increasing accuracy and cost, learning the expensive function from many cheap runs and few costly ones. This page covers the GP constructions; the general idea is [[Multi-fidelity modeling]].

**Sources**: `Guassian Processes/Bilionis, Lee, Buganza - Propagation of Uncertainty in Tissues Reponse via multi-fidelity GP Regression.pdf`.
**Last updated**: 2026-11-06

---

## Setup
Levels $t=1,\dots,S$ with unknown functions $f_t$, data $D_t=(X_t,y_t)$. Level 1 is cheapest, level $S$ is the target. The bet is that all describe the same physics, so their trends are similar (Lee 2020, p. 7).

## Three constructions (as described by Lee 2020, p. 8)

> [!definition] Autoregressive (Kennedy-O'Hagan)
> $$f_t(x)=\rho_{t-1}f_{t-1}(x)+\delta_t(x)$$
> $\rho$ scales the lower level, $\delta_t$ is a GP correction. Joint covariance over all levels: too costly for many levels or points.

> [!definition] Recursive (Le Gratiet)
> Use the posterior $f^*_{t-1}$ in place of the prior. Levels decouple, cost $\sum_t O(n_t^3)$. Requires nested inputs $X_t\subseteq X_{t-1}$. Constant $\rho$ gives linear correlation between levels; $\rho(x)$ allows more.

> [!definition] Nonlinear / deep (Perdikaris)
> $$f_t(x)=g_t\big(x,f^*_{t-1}(x)\big),\quad g_t\sim\mathcal{GP}$$
> with kernel
> $$k_{g_t}=k_{\rho_t}\,k_{f_t}\big(f^*_{t-1}(x),f^*_{t-1}(x')\big)+k_{\delta_t}.$$
> Inputs have dimension $d+1$ above level 1. Posteriors above level 2 are non-Gaussian, so predictions use Monte Carlo.

The kernel in the last construction is a product-and-sum built from simpler kernels: see [[Kernel composition]].

## Practical notes
- Nested [[Latin hypercube sampling]] designs keep space-filling and nesting at once (Lee 2020, p. 9).
- More high-fidelity data is not always better for the fused model: with enough of it a single-fidelity GP catches up (Lee 2020, p. 12-13).
- Cost reasoning: Cholesky is $O(n^3)$, so splitting one big GP into per-level GPs is the main saving.

## Where it appears
- [[Multi-fidelity GP for tissue expansion (Lee 2020)]]: three FE mesh levels, 10 high-fidelity, 60 medium and 160 low-fidelity runs (nested).

## Related pages
- [[Gaussian process]] · [[Multi-fidelity modeling]] · [[Surrogate model]] · [[Kernel methods]] · [[Kernel composition]] · [[Active learning]]
