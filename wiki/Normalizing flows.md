---
type: method
area: ml
areas: [ml, bayesian]
source-ref: "Karumuri et al. 2024, eq. 6, pp. 10-15"
tags: [generative, ml, vi]
---

# Normalizing flows

> [!algorithm] Normalizing flow
> Base $z_0\sim N(0,I)$, invertible $T=T_K\circ\dots\circ T_1$, $\xi=T(z_0)$:
> $$q_\lambda(\xi)=q(z_0)\,\Big|\det\tfrac{\partial\xi}{\partial z_0}\Big|^{-1}.$$
>
> (source: `papers/Bayesian/Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf`, eq. 6)

**Intuition**: build a flexible density by warping a Gaussian through maps whose Jacobian determinant is cheap. Unlike a Gaussian guide, it can be multimodal.

## Conditional coupling block (Karumuri p. 12)
Split $u=(u_1,u_2)$ and condition on data $y$:
$$v_1=u_1\odot e^{s(u_2,y)}+t(u_2,y)$$
$$v_2=u_2\odot e^{a(v_1,y)}+b(v_1,y)$$
Log-determinant $\sum s+\sum a$. A fixed random permutation follows each block; $K=15$ blocks for inverse kinematics.

Entropy of the guide (p. 15):
$$H=\tfrac d2\log(2\pi e)+\mathbb E\log|\det\partial G/\partial Z_0|.$$

## Where it appears
- [[Amortized VI for inverse problems (Karumuri 2024)]]: the flow guide recovers the two-mode kinematics posterior.
- [[SDE-BNN (Xu 2022)]]: flow-based BNN posteriors as prior work.
- [[Priors in Bayesian deep learning (Fortuin 2022)]]: flow priors for VAEs (eq. 39).
- [[Score SDE (Song 2021)]]: the probability-flow ODE is a continuous flow with exact likelihood (eq. 39); Table 2 compares it with RealNVP, Glow, FFJORD and Flow++.
- [[Intro to VAEs (Kingma 2019)]]: ch. 3 (IAF) is listed in the contents but missing from the PDF.
- [[Neural ODEs (Chen 2018)]] — continuous normalizing flows: log-density changes by an integral of a trace instead of a determinant (see [[Neural ODE]]).

**Sources**: `papers/Bayesian/Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Amortized VI]] · [[Flow matching]] · [[Diffusion models]]
- The book's guide families (diagonal, full-rank, transformed Gaussians) are the non-flow baseline that flows extend: [[Variational inference]]. (source: `inverse/vi/01_basics.md`) Wiki note: the book does not mention flows in Part 4 sources read.
