---
type: definition
area: math
areas: [math, stochastic]
source-ref: "Zhang et al. 2020 (cyclical), Thm 2; Zhang, Wilson, De Sa 2022, Thms 1-3, App. E"
---

# Wasserstein-2 distance

> [!definition]
> $$W_2(\mu,\nu)=\Big(\inf_{J\in\mathcal J(\mu,\nu)}\int\|x-y\|_2^2\,dJ(x,y)\Big)^{1/2},$$
> $\mathcal J$ the couplings of $\mu,\nu$. Against a point mass: $W_2(\mu_K,\delta_{\theta^*})\le\mathbb E\|\bar\theta_K-\theta^*\|$ (Low-precision App. E).

## Where it appears
- [[cyclical-sg-mcmc]] (Thm 2) · [[variance-corrected-quantization]] (Thms 1-3) · [[langevin-dynamics]] (Dalalyan-Karagulyan bound).

**Sources**: `IFT/Ruqi Zhang - Cyclical Stochastic Gradient MCMC.pdf`, `IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`.
**Last updated**: 2026-11-06
