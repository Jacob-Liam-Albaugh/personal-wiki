---
type: method
area: ml
areas: [ml]
source-ref: "Sitzmann et al. 2020, §3"
tags: [ml, physics-informed, signals]
---

# SIREN

**Summary**: A sinusoidal representation network: an MLP whose activation is $\sin$, with a variance-preserving initialization. It fits signals and their derivatives and can be supervised through PDE constraints alone.

> [!algorithm] SIREN layer and init
> $$\phi(x) = \sin(\omega_0 W x + b)\quad\text{(first layer, } \omega_0 = 30)$$
> $$\phi(x) = \sin(W x + b)\quad\text{(hidden), } w \sim U(-\sqrt{6/n}, \sqrt{6/n})$$
> (source: Sitzmann 2020, §3.2)

## Key points

- Derivatives of a SIREN are SIRENs, so derivative-based losses (Poisson, Eikonal, Helmholtz) stay well behaved.
- Sidesteps [[Spectral bias]] through periodic activations instead of a [[Fourier features]] input map. Wiki note: a SIREN's first layer is itself a learned sinusoidal feature map.
- Used as a PDE solver representation in the same spirit as [[PINN]].
- Sensitive to the initialization scale: $\omega_0$ sets the starting bandwidth.

**Sources**: `ML/Sitzmann - SIREN - Implicit Neural Representations with Periodic Activation Functions.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SIREN paper (Sitzmann 2020)]]
- [[Spectral bias]]
- [[Fourier features]]
- [[PINN]]
- [[Weight initialization]]
