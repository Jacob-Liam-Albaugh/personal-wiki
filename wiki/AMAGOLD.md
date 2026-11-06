---
type: method
area: stochastic
source-ref: "Zhang, Cooper, De Sa 2020, eqs. 2-6, Alg. 2, Thms 1-2"
tags: [sampling, mcmc, bayesian]
---

# AMAGOLD (amortized Metropolis adjustment)

> [!definition] Skew-reversibility (eqs. 2, 5)
> $\pi(x)G(x,y)=\pi(y^\star)G(y^\star,x^\star)$ for a measure-preserving involution $\star$, here $(\theta,r)^\star=(\theta,-r)$. Implies $\pi$ is stationary.

> [!algorithm] AMAGOLD (Alg. 2, p. 5)
> Run $T$ SGHMC leapfrog steps, accumulating
> $\rho_{t+\frac12}=\rho_{t-\frac12}+\tfrac12\epsilon\sigma^{-2}\nabla\tilde U_t(\theta_t)^\top(r_{t-\frac12}+r_{t+\frac12})$.
> Accept with probability $\min\big(1,\exp(U(\theta)-U(\theta^*)+\rho_{T-\frac12})\big)$; on reject flip momentum $r\leftarrow-r_{-\frac12}$.
> General form (eq. 3): $\tau=\min\big(1,\frac{\pi(y)}{\pi(x)}\prod_{t}\frac{P(x_{t+1},x_t;\zeta_t)}{P(x_t,x_{t+1};\zeta_t)}\big)$.

**Intuition**: one full-data energy evaluation per $T$ minibatch steps buys exactness.

> [!theorem] Theorem 1 (p. 5)
> The chain is reversible (momentum resampled) or skew-reversible, with stationary distribution $\pi$.

> [!theorem] Theorem 2 — spectral gap (p. 6)
> If $\mathbb E[(\nabla\tilde U-\nabla U)(\cdot)^\top]\preceq\frac{V^2}dI$, $\epsilon V^2\le4\sigma^2\beta d$, $c=1+\sqrt{\epsilon V^2/(16\sigma^2\beta Td^2)}$, then AMAGOLD with $(\epsilon,\sigma c^{-1/4},\beta c^{-1/2})$ has
> $$\gamma/\bar\gamma\ge\exp\Big(-\frac{\epsilon TV^2}{4\sigma^2\beta}-\sqrt{\epsilon TV^2/(\sigma^2\beta)}\Big),$$
> $\bar\gamma$ the full-gradient L2MC gap.

> [!proof]
> The library PDF has no appendix; proofs not available here.

## Where it appears
- [[AMAGOLD (Zhang 2020)]].

**Sources**: `papers/IFT/Ruqi Zhang - AMAGOLD.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SGHMC]] · [[Metropolis-Hastings correction]]
