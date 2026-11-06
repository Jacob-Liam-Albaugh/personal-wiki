---
type: method
area: stochastic
areas: [stochastic, bayesian, ift]
source-ref: "Welling & Teh 2011, eqs. 1-4, 9-11"
tags: [sampling, mcmc, bayesian]
---

# Stochastic gradient Langevin dynamics (SGLD)

> [!algorithm] SGLD (Welling & Teh 2011, eq. 4)
> $$\Delta\theta_t=\frac{\epsilon_t}2\Big(\nabla\log p(\theta_t)+\frac Nn\sum_{i=1}^n\nabla\log p(x_{ti}|\theta_t)\Big)+\eta_t,\qquad \eta_t\sim\mathcal N(0,\epsilon_t)$$
> with Robbins-Monro steps $\sum_t\epsilon_t=\infty$, $\sum_t\epsilon_t^2<\infty$ (eq. 2). No Metropolis-Hastings step.

**Intuition**: SGD (Robbins-Monro, eq. 1) plus noise of variance equal to the step. Early on gradient noise dominates and it optimizes; as $\epsilon_t\to0$ the injected noise dominates and it samples, and the MH rejection rate goes to zero.

## Notation used in this wiki
This wiki writes SGLD as Welling-Teh do: drift $\frac\epsilon2\nabla\log p$, noise variance $\epsilon$. Equivalent forms:
| Paper | Form |
|---|---|
| Zhang, Wilson, De Sa 2022 (eq. 1) | $\theta_{k+1}=\theta_k-\alpha\tilde\nabla U+\sqrt{2\alpha}\,\xi$, $U=-\log p(\theta|D)$; i.e. $\alpha=\epsilon/2$ |
| Alberts et al. 2026 (eq. 7) | Welling-Teh form, $\epsilon_t=\alpha_1/(t+\alpha_2)^{\alpha_3}$ |
| Alberts & Bilionis 2023 (eq. 22) | $\theta_{t+1}=\theta_t-\epsilon_t\nabla H+\eta_t$, noise written $\mathcal N(0,\sqrt{\epsilon_t})$ — **[unverified]** whether $\sqrt{\epsilon_t}$ is a std or a typo; with no ½ on the gradient the matching noise variance is $2\epsilon_t$ |

## Details (Welling & Teh)
- Sampling threshold (eqs. 9-10): switch from optimization to sampling when injected noise dominates the minibatch-gradient noise.
- Posterior expectations are step-weighted: $\hat{\mathbb E}[f]=\sum_t\epsilon_tf(\theta_t)/\sum_t\epsilon_t$ (eq. 11).
- Preconditioning (§3.2): $\Delta\theta=\frac\epsilon2M(\cdots)+\eta$, $\eta\sim\mathcal N(0,\epsilon M)$; $M=F^{-1}$ is Amari's natural gradient (Wiki note).

## In the lab papers
- [[PIFT (Alberts 2023)]]: energy gradient by importance sampling $X\sim q$, $n=b=1$, $\alpha_1=0.51$; unsuitable for multimodal posteriors. Hyperparameters via [[Nested SGLD]].
- [[IFT thermal conductivity (Alberts 2026)]]: $\alpha_2=0.01$, $\alpha_3=0.51$, $\alpha_1=0.1/\beta$.
- [[Stochastic differential equation]] supplies the SDE background (Itô calculus, [[Brownian motion]]).

## Where it appears
- [[SGLD (Welling 2011)]] (introduces it) · [[Cyclical SG-MCMC (Zhang 2020)]] · [[Low-precision SGLD (Zhang 2022)]] · the two IFT papers above · [[Diffusion posterior sampling]] (D-Flow SGLD, cited).
- [[Euler-Maruyama method]] is the same discretization as the SGLD update with a gradient drift (Wiki note; the book does not state the connection) (source: sinverse/sodes).

**Sources**: `papers/IFT/Welling - Bayesian Learning via Stochastic Gradient Langevin Dynamics.pdf`, `papers/IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`, `papers/IFT/Bilionis, Alberts - IFT.pdf`, `papers/IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Langevin dynamics]] · [[SG-MCMC]] · [[Metropolis-Hastings correction]]
- [[RMHMC (Girolami 2011)]]: MMALA is the Riemannian Langevin step (source: Girolami 2011, §3).
- [[Brownian motion]], [[Wiener process]].
