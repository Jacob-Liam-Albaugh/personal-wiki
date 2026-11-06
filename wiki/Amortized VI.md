---
type: method
area: bayesian
areas: [bayesian, ml]
source-ref: "Margossian & Blei 2024, eqs. 3-5, Prop. 2.1, Thm 3.4; Karumuri et al. 2024, eq. 2, Thms 1-2"
tags: [bayesian, vi, ml]
---

# Amortized variational inference

> [!algorithm] Amortized VI
> Replace per-datum variational parameters with a shared inference function $f_\phi$:
> $$\mathcal Q_A=\Big\{q_0(\theta)\textstyle\prod_n q\big(z_n;f_\phi(x_n)\big)\Big\}.$$
> Over whole datasets (Karumuri): $\lambda=\lambda(y)$ and
> $$\mathrm{AELBO}[\lambda]=\mathbb E_Y\big[\mathrm{ELBO}(\lambda(Y);Y)\big].$$
>
> (source: `Bayesian/Margossian, Blei - Amortized Variational Inference When & Why.pdf`, eq. 3; `Bayesian/Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf`, eq. 2)

**Intuition**: pay once to train a network that maps data to a posterior approximation, then get new posteriors with one forward pass. The price is the **amortization gap**: the shared function may not reach each datum's optimum.

## Results
> [!theorem] Inclusion (Margossian & Blei, Prop. 2.1)
> $\mathcal Q_A(\mathcal F)\subsetneq\mathcal Q_F$. Amortized matches factorized iff some $f_\phi$ interpolates the optima: $f_\phi(x_n)=\nu_n^*$ for all $n$ (eq. 5).

> [!theorem] When an ideal function exists (Margossian & Blei, Thm 3.4)
> An ideal inference function exists iff the model is simple hierarchical ($p(z_n\mid\theta)$ depends on $x$ only through $x_n$, Def. 3.3). Linear model: an ideal function with 3 parameters (Prop. 3.6). HMM: none exists (Prop. 3.8).

> [!theorem] Bounds and optima (Karumuri et al., Thms 1-2)
> $\mathrm{AELBO}\le-H[p(Y)]$ when the entropy is finite. Under $C^2$ smoothness and no amortization gap, a local max of the AELBO is a local max of the ELBO for every $y$.

## Where it appears
- [[Amortized VI for inverse problems (Karumuri 2024)]]: guides trained on simulated datasets for inverse problems.
- [[Amortized VI when and why (Margossian 2024)]]: theory of when amortization costs nothing.
- [[VAE paper (Kingma 2014)]] · [[Intro to VAEs (Kingma 2019)]] (p. 4 coins "amortized inference"): the VAE encoder.

**Sources**: `Bayesian/Margossian, Blei - Amortized Variational Inference When & Why.pdf`, `Bayesian/Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Variational inference]] · [[VAE]] · [[Bayesian inverse problems]]
