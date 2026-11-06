---
type: method
area: ml
areas: [ml]
source-ref: "Tancik et al. 2020, §4-5"
tags: [ml, signals, gp]
---

# Fourier features

**Summary**: A fixed sinusoidal embedding $\gamma(v)$ applied to the inputs before an MLP. It lets the network fit high-frequency functions of low-dimensional inputs by making its effective kernel stationary and bandwidth-tunable.

> [!algorithm] Random Fourier feature input map
> Sample $B\in\mathbb{R}^{m\times d}$ with entries $N(0,\sigma^2)$, then use
> $$\gamma(v) = \left[\cos(2\pi B v),\ \sin(2\pi B v)\right]$$
> as the network input. Tune $\sigma$ on validation data (source: Tancik 2020, §6).

## Key points

- The book's PINN variant (no $2\pi$) feeds
$$\phi(x) = [\cos(Bx);\ \sin(Bx)].$$
  Here $B$ is frozen (Equinox `eqx.partition` with a filter spec) with entries $N(0,\sigma^2)$. Wang et al. suggest $\sigma\in[1,10]$ for PINNs; the run uses 100 features and $\sigma=6$ (source: spectral_bias.ipynb).
- Small $\sigma$ underfits (smooth), large $\sigma$ overfits (noisy, aliased). The scale matters more than the sampling family (Tancik 2020, Fig. 4).
- The induced kernel $\sum_j a_j^2\cos(2\pi b_j^{\top}\Delta v)$ is shift-invariant. This is the classical random Fourier feature approximation of a stationary kernel; see [[Random features model]] and [[Kernel methods]].
- NeRF's "positional encoding" is the deterministic, axis-aligned variant with log-spaced frequencies (source: Tancik 2020, §6).
- Fixes [[Spectral bias]]. Alternative: periodic activations ([[SIREN]]).

**Covered in**: ASML book pinns/basics (ME 697 5.1)
**Sources**: `papers/ML/Tanicik, Srinivasan, Midenhall, et. al. - Fourier Features Let Netowrks Learn High Frequency Functions in Low Dimensional Domains.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Fourier features (Tancik 2020)]]
- [[Spectral bias]]
- [[SIREN]]
- [[Neural tangent kernel]]
- [[Random features model]]
- [[Kernel methods]]
- [[Fourier transform]]
