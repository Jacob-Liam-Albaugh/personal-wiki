---
type: method
area: stochastic
source-ref: "Zhang, Cooper, De Sa 2020, eq. 1, Alg. 1"
---

# Stochastic-gradient HMC (and HMC)

> [!definition] HMC (AMAGOLD eq. 1, p. 3)
> Sample $(\theta,r)\sim e^{-U(\theta)-\|r\|^2/(2\sigma^2)}$ by the flow $d\theta=\sigma^{-2}r\,dt$, $dr=-\nabla U\,dt$ and momentum resampling. L2MC adds friction and noise.

> [!algorithm] SGHMC inner step, leapfrog form (AMAGOLD Alg. 1, p. 2)
> $$r_{t+\frac12}=\frac{(1-\epsilon\beta)r_{t-\frac12}-\epsilon\nabla\tilde U(\theta_t)+\eta_t}{1+\epsilon\beta},\quad \eta_t\sim\mathcal N(0,4\epsilon\beta\sigma^2I),\quad \theta_{t+1}=\theta_t+\epsilon\sigma^{-2}r_{t+\frac12}.$$
> No MH step, so biased; Chen et al. 2014 (cited) introduced it.

## Where it appears
- [[zhang-2020-amagold]] — the biased baseline AMAGOLD corrects.
- [[zhang-2020-cyclical-sg-mcmc]] — second base kernel.
- [[zhang-2022-low-precision-sgld]] — prior art (Ferianc et al., cited).

**Sources**: `IFT/Ruqi Zhang - AMAGOLD.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[amagold]] · [[langevin-dynamics]] · [[stochastic-gradient-mcmc]]
