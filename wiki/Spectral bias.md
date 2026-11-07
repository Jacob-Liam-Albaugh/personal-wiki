---
type: concept
area: ml
areas: [ml]
source-ref: "Rahaman et al. 2019; Tancik et al. 2020"
tags: [ml, optimization, signals]
---

# Spectral bias

**Summary**: Networks trained by gradient descent fit the low-frequency part of a target function first and the high-frequency part much later (source: Rahaman 2019, §3). Also called the frequency principle.

> [!definition] Spectral bias
> For a ReLU network the Fourier transform decays as a power of $|k|$, and the rate of change of the residual at frequency $k$ under gradient flow decays with $k$. Low $k$ therefore converges first, regardless of amplitude (source: Rahaman 2019, Thm 1, eq. 9).

Demo (spectral_bias.ipynb): the target is
$$f(x) = \sin(2\pi x) + 0.5\sin(16\pi x).$$
It is fitted from 1000 points with noise 0.1 by an MLP of width 128, depth 4, tanh, Adam, 300 epochs; the high-frequency part appears late.

## Why it matters

- It acts as implicit regularization: early stopping keeps the smooth part and drops high-frequency noise (Rahaman 2019, Exp. 3-4).
- It is a handicap for signals that need fine detail: images, shapes, PDE solutions with sharp features. Fixes:
  - [[Fourier features]] map inputs through sinusoids so the kernel is shift-invariant and bandwidth-tunable (source: Tancik 2020).
  - [[SIREN]] uses sine activations.
- Data-manifold shape matters: high frequencies on a complex manifold can be low frequencies in input space (Rahaman 2019, §4).
- Kernel-regime explanation: eigenvalues of the [[Neural tangent kernel]] decay with frequency, so high modes train slowly. Wiki note: this is the Tancik et al. argument.

**Covered in**: ASML book pinns/basics (ME 697 5.1)
**Sources**: `papers/ML/Rahaman et.al. - On the Spectrial Bias of NNs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Spectral bias (Rahaman 2019)]]
- [[Fourier features]]
- [[SIREN]]
- [[Neural tangent kernel]] · [[NTK (Jacot 2018)]] (eigenmode decay $e^{-\lambda_it}$, §5)
- [[Physics-informed machine learning]]
- [[Fourier transform]]
