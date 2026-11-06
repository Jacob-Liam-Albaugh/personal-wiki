---
type: definition
area: math
areas: [math, bayesian]
source-ref: "Tsilifis et al. 2014, eqs. 7-8; Kingma & Welling 2014, App. B; Xu et al. 2022, eqs. 5-6"
tags: [bayesian, vi]
---

# Kullback-Leibler divergence

> [!definition] KL divergence
> $$\mathrm{KL}(q\,\|\,p)=\mathbb E_q\Big[\log\tfrac{q}{p}\Big]\ge0,$$
> with equality iff $q=p$. Not symmetric.
>
> (source: `Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, eqs. 7-8)

**Intuition**: the information lost when $q$ stands in for $p$. Minimising $\mathrm{KL}(q\|p)$ over $q$ (reverse KL, as in [[Variational inference]]) punishes mass where $p$ is small, so it is mode-seeking.

## Closed forms
- Diagonal Gaussian against $N(0,I)$ (AEVB App. B):
  $$-\mathrm{KL}=\tfrac12\textstyle\sum_j\big(1+\log\sigma_j^2-\mu_j^2-\sigma_j^2\big).$$
- Two SDEs with the same diffusion $g$ (Xu et al. eqs. 5-6, Girsanov):
  $$\mathrm{KL}(\mu_q\|\mu_p)=\mathbb E_q\!\int_0^1\tfrac12\|u\|^2dt,\quad u=g^{-1}(f_\theta-f_\phi).$$
  Infinite if the diffusions differ.
- $N(\theta,\alpha\theta^2)$ against the log-uniform prior: a cubic fit in $\alpha$ (Kingma et al. 2015, p. 6), see [[Variational dropout]].

## Failure modes
- Function-space priors with mismatched supports give infinite KL (Fortuin §4.2), one reason Wasserstein is proposed instead ([[Wasserstein distance]]).

## Where it appears
- [[Variational inverse problems (Tsilifis 2014)]] · [[Amortized VI for inverse problems (Karumuri 2024)]] (mode-seeking, p. 30) · [[Amortized VI when and why (Margossian 2024)]].
- [[VAE paper (Kingma 2014)]] · [[Variational dropout (Kingma 2015)]] · [[Intro to VAEs (Kingma 2019)]] (ML as KL to the data, p. 10).
- [[SDE-BNN (Xu 2022)]] · [[Bayesian DenseED surrogate (Zhu 2018)]] (SVGD derivative, p. 15) · [[Priors in Bayesian deep learning (Fortuin 2022)]].
- Non-negativity proved via Jensen's inequality in the book. (source: `inverse/vi/01_basics.md`)

## Examples

> [!example] Homework 6, problem 2 (source: homework/06_homework.ipynb)
> Show $D_{KL}(p\|q)\ge0$ using Jensen's inequality.

**Sources**: `Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, `Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`, `Bayesian/Chen, Xu, Li, Duvenaud - inf Deep Bayseian NN with Stochastic Diff. Eqns.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ELBO]] · [[Wasserstein distance]]
