---
type: method
area: ml
areas: [ml, stochastic]
source-ref: "Wang 2026, eqs. 3-5"
---

# Diffusion models (score-based SDE view)

> [!algorithm] Forward / reverse SDE (Wang 2026, eqs. 3-4)
> $$dx=f(x,\tau)\,d\tau+g(\tau)\,dW,\qquad \text{DDPM: }f=-\tfrac12\beta(\tau)x,\ g=\sqrt{\beta(\tau)}$$
> $$dx=[f-g^2 s_\theta(x,\tau)]\,d\tau+g\,d\bar W,\qquad s_\theta\approx\nabla_x\log p_\tau(x).$$

> [!definition] Probability-flow ODE (eq. 5)
> $dx=\big(f-\tfrac12g^2\nabla_x\log p_\tau\big)d\tau$ has the same marginals as the reverse SDE.

## Related methods
- [[flow-matching]] — learn a velocity field instead of a score.
- [[diffusion-posterior-sampling]] — condition a trained prior on data.
- The SDE framework is Song et al. (Wang ref. 14), cited, not read.

## Where it appears
- [[wang-2026-generative-priors-turbulence]].

**Sources**: `IFT/Wang - Generative priors for spatiotemporal turbulence.pdf`.
**Last updated**: 2026-11-06
