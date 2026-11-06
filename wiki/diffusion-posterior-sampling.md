---
type: method
area: ml
areas: [ml, bayesian]
source-ref: "Wang 2026, eqs. 7, 14-21"
---

# Conditioning generative priors (posterior sampling)

> [!algorithm] Three training-free variants (Wang 2026)
> Target $p_\theta(x|y)\propto p_\theta(x)\,p(y|x)$ with $p(y|x)\propto e^{-\frac12\|y-H(x)\|^2_{\Sigma^{-1}}}$ (eq. 7).
> - DPS: $\nabla\log p_\theta(x|y)\approx\nabla\log p_\theta(x)+\nabla\log p(y|\hat x_0)$, $\hat x_0$ the denoised estimate (eqs. 16-17).
> - Guided flow matching: $\frac{dx}{d\tau}=v_\theta+\lambda(\tau)\nabla\log p(y|\hat x)$ (eq. 18).
> - Source space: sample $x_0\sim p(x_0|y)\propto p_0(x_0)\,p(y|T_\theta(x_0))$, then $x_1=T_\theta(x_0)$ (eqs. 19-21). D-Flow SGLD (ref. 29, not read) samples this with SGLD.

> [!question]
> Wang gives no rule for choosing among the three (Sec. VII.C).

Wiki note: source-space conditioning has the same shape as PIFT — a prior pushed forward through a map, sampled with [[stochastic-gradient-langevin-dynamics]].

## Where it appears
- [[wang-2026-generative-priors-turbulence]].

**Sources**: `IFT/Wang - Generative priors for spatiotemporal turbulence.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[diffusion-models]] · [[flow-matching]] · [[information-field-theory]]
