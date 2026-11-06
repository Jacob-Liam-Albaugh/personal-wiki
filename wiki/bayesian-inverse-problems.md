---
type: concept
area: bayesian
source-ref: "Tsilifis et al. 2014, eqs. 1-6; Karumuri et al. 2024, §2.1"
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
- [[variational-inference]] per dataset (Tsilifis) or [[amortized-variational-inference]] across datasets (Karumuri).
- Field-valued unknowns: [[information-field-theory]] and [[physics-informed-functional-prior]].

## Related pages
- [[tsilifis-2014-variational-inverse-problems]] · [[karumuri-2024-amortized-vi-inverse-problems]] · [[alberts-2023-pift]] · [[karhunen-loeve-expansion]]
