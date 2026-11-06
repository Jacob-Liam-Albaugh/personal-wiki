---
type: method
area: stochastic
areas: [stochastic, bayesian]
source-ref: "Zhang et al. 2020 (ICLR), eq. 1, Alg. 1, Thms 1-2"
tags: [sampling, mcmc, bayesian]
---

# Cyclical SG-MCMC

> [!algorithm] Cosine step schedule (Zhang et al. 2020, eq. 1, Alg. 1)
> $$\alpha_k=\frac{\alpha_0}2\Big[\cos\Big(\frac{\pi\,\mathrm{mod}(k-1,\lceil K/M\rceil)}{\lceil K/M\rceil}\Big)+1\Big]$$
> $M$ cycles over $K$ steps. With $r(k)=\mathrm{mod}(k-1,\lceil K/M\rceil)/\lceil K/M\rceil$: exploration (large steps, temperature $T=0$, i.e. SGD) while $r(k)<\beta$, sampling ($T=1$) after. Collect samples only in sampling stages.

**Intuition**: each cycle's large steps jump to a new mode, small steps sample it. Tempering: $\pi_T\propto e^{-U/T}$.

> [!theorem] Theorems 1-2 (Zhang et al. 2020)
> Thm 1: bias $O\big(\frac1{\alpha_0K}+\alpha_0\big)$, MSE $O\big(\frac1{\alpha_0K}+\alpha_0^2\big)$.
> Thm 2: a $W_2$ bound to the target (constant $C_1$ to the first power per App. D.1; main-text exponents garbled in extraction, **[unverified]**).

## Where it appears
- [[Cyclical SG-MCMC (Zhang 2020)]] — defines it.
- [[Low-precision SGLD (Zhang 2022)]] — cSGLD with 7 cycles in low precision.

**Sources**: `papers/IFT/Ruqi Zhang - Cyclical Stochastic Gradient MCMC.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SGLD]] · [[Bayesian model averaging]] · [[Wasserstein distance]]
