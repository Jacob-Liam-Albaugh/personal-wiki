---
type: method
area: bayesian
areas: [bayesian, ml]
source-ref: "Margossian & Blei 2024, eq. 1; Tsilifis et al. 2014, eq. 14; Kingma et al. 2015, eqs. 1-2"
---

# Variational inference

> [!algorithm] Variational inference
> Pick a tractable family $\mathcal Q$ and solve
> $$q^*=\arg\min_{q\in\mathcal Q}\mathrm{KL}\big(q(\theta,z)\,\|\,p(\theta,z\mid x)\big),$$
> equivalently maximise the [[evidence-lower-bound]] $\mathcal F[q]$.
>
> (source: `Bayesian/Margossian, Blei - Amortized Variational Inference When & Why.pdf`, eq. 1)

**Intuition**: replace sampling from the posterior with optimisation over a family of simple distributions. The answer is only as good as the family, and the reverse-KL objective is mode-seeking, so a unimodal family locks onto one mode of a multimodal posterior.

## Variants
- **Factorized (F-VI)**: one set of parameters $\nu_n$ per latent (Margossian & Blei).
- **Amortized**: a learned map from data to variational parameters, see [[amortized-variational-inference]].
- **Global weights**: $q_\phi(w)$ over network weights, gradients via the [[reparameterization-trick]] (Kingma et al. 2015, eqs. 1-3), the basis of [[variational-dropout]].
- **Particle**: [[stein-variational-gradient-descent]] transports a particle set by the KL steepest-descent direction.
- **Path space**: ELBO over SDE path measures (Xu et al. 2022, eq. 1).

## Failure modes
- Mode-seeking reverse KL: Karumuri et al.'s Gaussian guide misses the second mode of the inverse-kinematics posterior; a [[normalizing-flows]] guide recovers it (p. 30).

## Where it appears
- [[tsilifis-2014-variational-inverse-problems]]: Gaussian-mixture family, analytic ELBO, one run per dataset.
- [[karumuri-2024-amortized-vi-inverse-problems]]: amortized Gaussian and flow guides.
- [[margossian-2024-amortized-vi-when-why]]: when amortized matches factorized.
- [[kingma-2014-aevb]] · [[kingma-2015-variational-dropout]] · [[kingma-2019-intro-vae]] (variational EM, App. A).
- [[xu-2022-sde-bnn]] (path-space VI) · [[zhu-2018-bayesian-denseed-surrogate]] (SVGD as VI).

**Sources**: `Bayesian/Margossian, Blei - Amortized Variational Inference When & Why.pdf`, `Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, `Bayesian/Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[evidence-lower-bound]] · [[kl-divergence]] · [[stochastic-gradient-mcmc]] · [[bayesian-inverse-problems]]
