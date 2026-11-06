---
type: method
area: stochastic
areas: [stochastic, ml]
source-ref: "Zhang, Wilson, De Sa 2022, p. 3, eq. 5, Algs. 1-2, Thms 1-3"
tags: [sampling, mcmc]
---

# Variance-corrected quantization (low-precision SGLD)

> [!definition] Fixed-point numbers (p. 3)
> $W$ bits, $F$ fractional: gap $\Delta=2^{-F}$, range $[-2^{W-F-1},\,2^{W-F-1}-2^{-F}]$. Deterministic rounding $Q_d$; stochastic rounding $Q_s$ is unbiased. Block floating point gap: $\Delta_W(\mu)=2^{E[\mu]-W+2}$ (eq. 7).

> [!algorithm] $Q_{vc}(\mu,v,\Delta)$ (Alg. 2, p. 6)
> Returns a grid-valued variable with mean exactly $\mu$ and variance exactly $v$: if $v>\Delta^2/4$ add $\mathcal N(0,(v-\Delta^2/4)I)$ and fix the remainder with a categorical; else stochastically round and add Cat$(0,v-v_s)$. Cat$(\mu,v)$ puts probabilities $\frac{v+\mu^2\pm\mu\Delta}{2\Delta^2}$ on $\pm\Delta$ (eq. 5).
> VC SGLDLP-L (Alg. 1): $\theta_{k+1}=Q_{vc}\big(\theta_k-\alpha Q_G(\tilde\nabla U(\theta_k)),\,2\alpha,\,\Delta_W\big)$.

**Intuition**: rounding noise is extra variance; subtract it from the Langevin noise so the total is still $2\alpha$.

> [!theorem] Theorems 1-3 (as $W_2$ bounds)
> - Thm 1, full-precision weights / low-precision gradients: error floor $O(\Delta_W^2)$.
> - Thm 2, naive low-precision weights: a $\alpha^{-1}\Delta_W^2$ term, which blows up as $\alpha\to0$.
> - Thm 3, variance-corrected: removes that term; constant $A=5v_0d$ or $\max(2\Delta_W\alpha G,4\alpha d)$; grouping of the $A/(\alpha m)$ term **[unverified]**.

## Where it appears
- [[Low-precision SGLD (Zhang 2022)]].

**Sources**: `papers/IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SGLD]] · [[Langevin dynamics]] · [[Wasserstein distance]]
