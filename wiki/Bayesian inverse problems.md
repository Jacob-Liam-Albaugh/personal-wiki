---
type: concept
area: bayesian
source-ref: "Tsilifis et al. 2014, eqs. 1-6; Karumuri et al. 2024, §2.1"
tags: [bayesian, inverse-problems]
---

# Bayesian inverse problems

**Summary**: infer the unknown inputs $\xi$ of a forward model $f$ from noisy data $y$ by computing a posterior, rather than a single best fit.

**Sources**: `Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, `Bayesian/Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf`.
**Last updated**: 2026-11-06

---

## Setup
Likelihood through the forward model (Tsilifis eqs. 1-2), with noise scale $\theta$:
$$p(y\mid\xi,\theta)=N\big(y\mid f(\xi),e^{2\theta}I\big)$$
Posterior over $\omega=(\xi,\theta)$ (eq. 6):
$$p(\omega\mid y)=\frac{p(y\mid\omega)\,p(\omega)}{p(y)}$$
Karumuri fixes the noise: $p(y\mid\xi)=N(y\mid f(\xi),\gamma^2I)$.

## Ways to solve it
- MAP and Laplace: cheap but crude summaries (both lab papers).
- MCMC: the costly gold standard; Karumuri compares against NUTS via KS statistics.
- [[Variational inference]] per dataset (Tsilifis) or [[Amortized VI]] across datasets (Karumuri).
- Field-valued unknowns: [[Information field theory]] and [[Physics-informed prior]].

## Related pages
- [[Variational inverse problems (Tsilifis 2014)]] · [[Amortized VI for inverse problems (Karumuri 2024)]] · [[PIFT (Alberts 2023)]] · [[Karhunen-Loève expansion]]
