---
type: definition
area: stochastic
source-ref: "Zhang, Wilson, De Sa 2022, eq. 1, App. B eq. 6; Welling & Teh 2011, eq. 3"
tags: [sampling, mcmc]
---

# Langevin dynamics

> [!definition] Overdamped Langevin SDE
> $$d\theta=-\nabla U(\theta)\,dt+\sqrt2\,dW_t,\qquad \pi\propto e^{-U}\ \text{stationary.}$$
> Euler-Maruyama (unadjusted Langevin): $\theta_{k+1}=\theta_k-\alpha\nabla U(\theta_k)+\sqrt{2\alpha}\,\xi_{k+1}$.
>
> (source: `papers/IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`, eq. 1)

- With MH correction it is MALA; Welling & Teh use it as the proposal (eq. 3).
- With noisy gradients $\nabla U+\zeta_k$ (Low-precision App. B, eq. 6) it covers [[SGLD]].

> [!theorem] Non-asymptotic $W_2$ bound (Dalalyan & Karagulyan 2019, Thm 4; restated in Zhang et al. 2022 App. B)
> For $m$-strongly convex, $M$-smooth $U$, gradient bias $\delta$ and variance $\sigma^2$:
> $$W_2(\mu_K,\pi)\le(1-\alpha m)^KW_2(\mu_0,\pi)+1.65\tfrac Mm(\alpha d)^{1/2}+\tfrac{\delta\sqrt d}m+\tfrac{\sigma^2(\alpha d)^{1/2}}{1.65M+\sigma\sqrt m}.$$

In score-based generation the gradient comes from a learned score, $\nabla\log p\approx s_\theta$. SMLD samples with annealed Langevin steps, and the [[Diffusion models#Predictor-corrector sampler|PC sampler]] uses Langevin as its corrector (Song et al. 2021, Algs. 4-5).

## Where it appears
- [[Score SDE (Song 2021)]].
- [[NCSNv2 (Song 2020)]]: annealed Langevin with step size and step count set from a closed-form variance ratio (Prop. 3).
- [[Path Integral Sampler (Zhang 2022)]]: PIS-Grad modulates the Langevin drift so the SDE reaches the target at finite $T$ (eq. 15).
- [[SGLD (Welling 2011)]] · [[Cyclical SG-MCMC (Zhang 2020)]] · [[AMAGOLD (Zhang 2020)]] · [[Low-precision SGLD (Zhang 2022)]].
- The noise term is increments of a [[Wiener process]]; origin in [[Brownian motion]] and [[Brownian movement (Einstein 1905)]].
- [[Ornstein-Uhlenbeck process]] is the linear-drift Langevin/SDE case with a Gaussian stationary law; [[Euler-Maruyama method]] is the discretization used to simulate it (source: sinverse/sodes). [[Stochastic differential equation]] gives the general setting.
- Wiki note: the book's SDE chapter does not mention Langevin sampling; the link is the shared SDE form $dX=b\,dt+\sigma\,dW$.
- The noise term is increments of a [[Wiener process]]; origin in [[Brownian motion]] and [[Brownian movement (Einstein 1905)]].

## Riemannian extension
- Girolami 2011 defines the manifold Langevin diffusion with metric G(theta), and MMALA as its discretization with a Metropolis correction (source: Girolami 2011, §3). Link [[Riemannian manifold HMC]].

**Covered in**: Eastman statmech ch. 7 (Friction and dissipation: physical Langevin equation)
**Sources**: `papers/IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`, `papers/IFT/Welling - Bayesian Learning via Stochastic Gradient Langevin Dynamics.pdf`, Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/friction.rst`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Wasserstein distance]] · [[SGHMC]]
- Book sampler progression: random-walk MH, [[Hamiltonian Monte Carlo]], [[NUTS]] ([[Markov chain Monte Carlo]]). Wiki note: Langevin methods are the gradient-only relative; the book does not treat them in Part 4.
- [[Fluctuation-dissipation theorem]] (why the noise is √2 at kT = 1) · [[Equipartition theorem]] · [[Boltzmann distribution]] · [[Ergodicity]]
