---
type: method
area: ml
source-ref: "Wang 2026, eq. 6"
---

# Flow matching

> [!algorithm] (Wang 2026, eq. 6)
> Learn $v_\theta$ so that $\frac{dx}{d\tau}=v_\theta(x,\tau)$ transports $x_0\sim p_0$ to $x_1\sim p_{\text{data}}$.

Examples cited by Wang: conditional flow matching for near-wall turbulence (ref. 27), patch-additive flow matching (ref. 56). Neither read.

Wiki note: the deterministic [[diffusion-models#Probability-flow ODE|probability-flow ODE]] of Song et al. 2021 is also a velocity field that transports noise to data. There the velocity is built from the score; flow matching learns it directly.

## Where it appears
- [[wang-2026-generative-priors-turbulence]].

**Sources**: `IFT/Wang - Generative priors for spatiotemporal turbulence.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[diffusion-models]] · [[diffusion-posterior-sampling]]
