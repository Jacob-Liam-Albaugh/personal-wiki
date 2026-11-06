---
type: definition
area: bayesian
areas: [bayesian, ml]
source-ref: "Tsilifis et al. 2014, eqs. 9-13; Kingma & Welling 2014, eqs. 1-3; Karumuri et al. 2024, eq. 1"
tags: [bayesian, vi, generative]
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
- Gaussian $q$ against $N(0,I)$ has a closed-form KL term (AEVB App. B), see [[KL divergence]].
- Diffusion form (Ho et al. 2020, eqs. 3, 5): with a fixed forward chain $q(x_{1:T}\mid x_0)$ as the encoder,
```
L = L_T + Σ_{t>1} L_{t-1} + L_0
L_T     = KL(q(x_T|x_0) ‖ p(x_T))
L_{t-1} = KL(q(x_{t-1}|x_t,x_0)
             ‖ p_θ(x_{t-1}|x_t))
L_0     = -log p_θ(x_0|x_1)
```
  Every $L_{t-1}$ compares Gaussians in closed form. See [[DDPM]].

## Estimating it
- Analytic approximation: entropy lower bound plus Taylor expansion of $\log p$ (Tsilifis, eqs. 16-24).
- Reparameterized Monte Carlo: [[Reparameterization trick]] (Kingma & Welling; Karumuri et al.).
- Margossian & Blei report it with 100 Monte Carlo draws (eq. 14).

## Where it appears
- [[Variational inverse problems (Tsilifis 2014)]] · [[Amortized VI for inverse problems (Karumuri 2024)]] (and its amortized expectation, the AELBO) · [[Amortized VI when and why (Margossian 2024)]].
- [[VAE paper (Kingma 2014)]] · [[Variational dropout (Kingma 2015)]] · [[Intro to VAEs (Kingma 2019)]] (App. A eqs. A.8-A.10).
- [[DDPM (Ho 2020)]] (eqs. 3, 5).
- [[SDE-BNN (Xu 2022)]] (path-space ELBO, eq. 1) · [[Priors in Bayesian deep learning (Fortuin 2022)]] (VAE-prior ELBO, eqs. 12, 37).
- Sparse variational GP surrogate maximizes the ELBO with $m=100$ inducing points: [[Surrogate model]] (source: `up/surrogates/04_gpr_large_data.ipynb`).
- Derived in the book as $\mathrm{KL}(q\|p)=\log p(y)-\mathrm{ELBO}$, so maximizing the ELBO minimizes the KL; estimated by a sample average through reparameterization. (source: `inverse/vi/01_basics.md`; [[Variational inference]])
- Expected ELBO over $p(y)$ is the amortized objective, used for the [[Duffing oscillator]]. (source: `inverse/odes/03_dyn_system_multiple_traj.ipynb`)

**Covered in**: ASML book inverse/vi (ME 697 4.3)
**Sources**: `Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, `Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Variational inference]] · [[KL divergence]] · [[Amortized VI]]
