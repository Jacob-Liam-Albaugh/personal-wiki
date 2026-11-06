---
type: method
area: physics-informed
areas: [physics-informed, ift]
source-ref: "Alberts & Bilionis 2023, eqs. 28-32, pp. 15-17"
tags: [physics-informed, ml, pde]
---

# Physics-informed neural networks (PINN) and B-PINN

> [!theorem] PINN as a PIFT MAP estimate (Alberts & Bilionis 2023, eqs. 28-30)
> With a flat prior on network weights $\theta$ and constant partition function, the PINN loss equals the parameter information Hamiltonian when $r_d=s/(2\sigma^2)$ and $r_p=\beta$. With physics parameters $\lambda$, $-\log p(\theta,\lambda|d)$ also has $\log Z(\lambda)+H(\lambda)$, which the PINN loss drops.

> [!theorem] When a B-PINN matches PIFT (eqs. 31-32)
> A B-PINN uses a fictitious zero-residual likelihood with noise $\sigma_r$ and a Gaussian weight prior. Its posterior equals PIFT's iff collocation points are shared, $\sigma_\theta=\infty$, and
> $$\sigma_r^2=n/(2\beta).$$

**Intuition**: B-PINN posteriors collapse as collocation points $n\to\infty$ (Bayesian asymptotics); PIFT's spread is set by $\beta$ and stays.

## Where it appears
- [[PIFT (Alberts 2023)]] — derivations.
- [[IFT thermal conductivity (Alberts 2026)]] — contrast; cites Hao & Bilionis (neural information field filter, not read) for B-PINN's poor extrapolation.

## Queued sources
`Physics Informed/` holds the PINN literature; see [[sources]].

**Sources**: `IFT/Bilionis, Alberts - IFT.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Physics-informed prior]] · [[Information field theory]]
