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
> (source: `papers/Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, eqs. 7-8)

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
- [[Path Integral Sampler (Zhang 2022)]]: reverse KL between path measures via Girsanov is the training loss (eqs. 11-14).
- [[Variational inverse problems (Tsilifis 2014)]] · [[Amortized VI for inverse problems (Karumuri 2024)]] (mode-seeking, p. 30) · [[Amortized VI when and why (Margossian 2024)]].
- [[VAE paper (Kingma 2014)]] · [[Variational dropout (Kingma 2015)]] · [[Intro to VAEs (Kingma 2019)]] (ML as KL to the data, p. 10).
- [[SDE-BNN (Xu 2022)]] · [[Bayesian DenseED surrogate (Zhu 2018)]] (SVGD derivative, p. 15) · [[Priors in Bayesian deep learning (Fortuin 2022)]].
- Non-negativity proved via Jensen's inequality in the book. (source: `inverse/vi/01_basics.md`)
- [[Amortized VI systematic review (Ganguly 2023)]]: reverse vs forward KL (zero-forcing) and alternatives (§6).

## Examples

> [!example] Homework 6, problem 2 (source: homework/06_homework.ipynb)
> Show $D_{KL}(p\|q)\ge0$ using Jensen's inequality.

## KL in IFT variational schemes (Enßlin)
The Gibbs free energy $G$ with a Gaussian ansatz satisfies $G\,\widehat=\,D_{\rm KL}(Q\|P)$ up to $-\ln P(d)$ ([[Gibbs free energy]]); [[Metric Gaussian variational inference]] minimises the sample estimate of the same KL with the covariance fixed by the Fisher metric.

(source: Ensslin - Information Theory & Information Field Theory.pdf, §11.3, §17.1, pp. 133-137, 171-173; p. = PDF page)

**Covered in**: Enßlin IT & IFT ch. 2 §2.6 (pp. 42-47), ch. 3 (pp. 53-69); Enßlin IT & IFT §11.3, §17.1 (pp. 133-137, 171-173)
**Sources**: `papers/Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, `papers/Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`, `papers/Bayesian/Chen, Xu, Li, Duvenaud - inf Deep Bayseian NN with Stochastic Diff. Eqns.pdf`, `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

## Information-theoretic reading (Enßlin)
Enßlin derives the KL divergence as the *ideal achieved information gain*: the expected log ratio of what Bob's updated knowledge says to what his prior said, averaged over what Alice knows, from five criteria (additivity, locality, analyticality, properness, calibration) (source: Ensslin - Information Theory & Information Field Theory.pdf, §2.6, pp. 42-47; PDF page). Notation: the book writes $D_S(I_A,I_B)$ with the *first* argument the distribution averaged over; this is $D_{\mathrm{KL}}(P(\cdot\mid I_A)\,\|\,P(\cdot\mid I_B))$. Its second-order expansion is the [[Fisher information]]. Choosing the update that minimizes the KL to the prior under a moment constraint is the [[Maximum entropy principle]]; see [[Achieved information gain]].

---

## Related pages
- [[ELBO]] · [[Wasserstein distance]]
- [[GAN paper (Goodfellow 2014)]]: GAN value equals $-\log 4+2\,\mathrm{JSD}$
- [[Free energy]]
- [[Achieved information gain]] · [[Maximum entropy principle]] · [[Fisher information]]
- [[Gibbs free energy]] · [[Metric Gaussian variational inference]]
