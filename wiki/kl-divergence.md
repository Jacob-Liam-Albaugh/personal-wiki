---
type: definition
area: math
areas: [math, bayesian]
source-ref: "Tsilifis et al. 2014, eqs. 7-8; Kingma & Welling 2014, App. B; Xu et al. 2022, eqs. 5-6"
---

# Kullback-Leibler divergence

> [!definition] KL divergence
> $$\mathrm{KL}(q\,\|\,p)=\mathbb E_q\Big[\log\tfrac{q}{p}\Big]\ge0,$$
> with equality iff $q=p$. Not symmetric.
>
> (source: `Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, eqs. 7-8)

**Intuition**: the information lost when $q$ stands in for $p$. Minimising $\mathrm{KL}(q\|p)$ over $q$ (reverse KL, as in [[variational-inference]]) punishes mass where $p$ is small, so it is mode-seeking.

## Closed forms
- Diagonal Gaussian against $N(0,I)$ (AEVB App. B):
  $$-\mathrm{KL}=\tfrac12\textstyle\sum_j\big(1+\log\sigma_j^2-\mu_j^2-\sigma_j^2\big).$$
- Two SDEs with the same diffusion $g$ (Xu et al. eqs. 5-6, Girsanov):
  $$\mathrm{KL}(\mu_q\|\mu_p)=\mathbb E_q\!\int_0^1\tfrac12\|u\|^2dt,\quad u=g^{-1}(f_\theta-f_\phi).$$
  Infinite if the diffusions differ.
- $N(\theta,\alpha\theta^2)$ against the log-uniform prior: a cubic fit in $\alpha$ (Kingma et al. 2015, p. 6), see [[variational-dropout]].

## Failure modes
- Function-space priors with mismatched supports give infinite KL (Fortuin §4.2), one reason Wasserstein is proposed instead ([[wasserstein-distance]]).

## Where it appears
- [[tsilifis-2014-variational-inverse-problems]] · [[karumuri-2024-amortized-vi-inverse-problems]] (mode-seeking, p. 30) · [[margossian-2024-amortized-vi-when-why]].
- [[kingma-2014-aevb]] · [[kingma-2015-variational-dropout]] · [[kingma-2019-intro-vae]] (ML as KL to the data, p. 10).
- [[xu-2022-sde-bnn]] · [[zhu-2018-bayesian-denseed-surrogate]] (SVGD derivative, p. 15) · [[fortuin-2022-priors-in-bdl]].

**Sources**: `Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, `Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`, `Bayesian/Chen, Xu, Li, Duvenaud - inf Deep Bayseian NN with Stochastic Diff. Eqns.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[evidence-lower-bound]] · [[wasserstein-distance]]
