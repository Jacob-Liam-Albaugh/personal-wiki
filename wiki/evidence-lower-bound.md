---
type: definition
area: bayesian
areas: [bayesian, ml]
source-ref: "Tsilifis et al. 2014, eqs. 9-13; Kingma & Welling 2014, eqs. 1-3; Karumuri et al. 2024, eq. 1"
---

# Evidence lower bound (ELBO)

> [!definition] ELBO
> For any $q$,
> $$\log p(y)=\mathcal F[q]+\mathrm{KL}\big(q\,\|\,p(\omega\mid y)\big),$$
> $$\mathcal F[q]=\mathbb E_q\Big[\log\tfrac{p(y,\omega)}{q(\omega)}\Big]=H[q]+\mathbb E_q[\log p(y,\omega)]\le\log p(y).$$
>
> (source: `Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, eqs. 9-13)

**Intuition**: $\log p(y)$ does not depend on $q$, so raising the bound is the same as shrinking the KL gap to the posterior. It needs only the joint, never the evidence.

## Basic consequences
- Latent-variable form (Kingma & Welling eq. 3):
  $$\mathcal L=-\mathrm{KL}\big(q_\phi(z\mid x)\,\|\,p_\theta(z)\big)+\mathbb E_q[\log p_\theta(x\mid z)].$$
- Weight-space form (Kingma et al. 2015, eqs. 1-2):
  $$\mathcal L(\phi)=-\mathrm{KL}(q_\phi(w)\|p(w))+\textstyle\sum_{(x,y)}\mathbb E_q[\log p(y\mid x,w)].$$
- Gaussian $q$ against $N(0,I)$ has a closed-form KL term (AEVB App. B), see [[kl-divergence]].

## Estimating it
- Analytic approximation: entropy lower bound plus Taylor expansion of $\log p$ (Tsilifis, eqs. 16-24).
- Reparameterized Monte Carlo: [[reparameterization-trick]] (Kingma & Welling; Karumuri et al.).
- Margossian & Blei report it with 100 Monte Carlo draws (eq. 14).

## Where it appears
- [[tsilifis-2014-variational-inverse-problems]] · [[karumuri-2024-amortized-vi-inverse-problems]] (and its amortized expectation, the AELBO) · [[margossian-2024-amortized-vi-when-why]].
- [[kingma-2014-aevb]] · [[kingma-2015-variational-dropout]] · [[kingma-2019-intro-vae]] (App. A eqs. A.8-A.10).
- [[xu-2022-sde-bnn]] (path-space ELBO, eq. 1) · [[fortuin-2022-priors-in-bdl]] (VAE-prior ELBO, eqs. 12, 37).

**Sources**: `Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, `Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[variational-inference]] · [[kl-divergence]] · [[amortized-variational-inference]]
