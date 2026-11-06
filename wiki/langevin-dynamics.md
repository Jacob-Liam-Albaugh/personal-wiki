---
type: definition
area: stochastic
source-ref: "Zhang, Wilson, De Sa 2022, eq. 1, App. B eq. 6; Welling & Teh 2011, eq. 3"
---

# Langevin dynamics

> [!definition] Overdamped Langevin SDE
> $$d\theta=-\nabla U(\theta)\,dt+\sqrt2\,dW_t,\qquad \pi\propto e^{-U}\ \text{stationary.}$$
> Euler-Maruyama (unadjusted Langevin): $\theta_{k+1}=\theta_k-\alpha\nabla U(\theta_k)+\sqrt{2\alpha}\,\xi_{k+1}$.
>
> (source: `IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`, eq. 1)

- With MH correction it is MALA; Welling & Teh use it as the proposal (eq. 3).
- With noisy gradients $\nabla U+\zeta_k$ (Low-precision App. B, eq. 6) it covers [[stochastic-gradient-langevin-dynamics]].

> [!theorem] Non-asymptotic $W_2$ bound (Dalalyan & Karagulyan 2019, Thm 4; restated in Zhang et al. 2022 App. B)
> For $m$-strongly convex, $M$-smooth $U$, gradient bias $\delta$ and variance $\sigma^2$:
> $$W_2(\mu_K,\pi)\le(1-\alpha m)^KW_2(\mu_0,\pi)+1.65\tfrac Mm(\alpha d)^{1/2}+\tfrac{\delta\sqrt d}m+\tfrac{\sigma^2(\alpha d)^{1/2}}{1.65M+\sigma\sqrt m}.$$

In score-based generation the gradient comes from a learned score, $\nabla\log p\approx s_\theta$. SMLD samples with annealed Langevin steps, and the [[diffusion-models#Predictor-corrector sampler|PC sampler]] uses Langevin as its corrector (Song et al. 2021, Algs. 4-5).

## Where it appears
- [[song-2021-score-sde]].
- [[welling-2011-sgld]] · [[zhang-2020-cyclical-sg-mcmc]] · [[zhang-2020-amagold]] · [[zhang-2022-low-precision-sgld]].

**Sources**: `IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`, `IFT/Welling - Bayesian Learning via Stochastic Gradient Langevin Dynamics.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[wasserstein-distance]] · [[stochastic-gradient-hmc]]
