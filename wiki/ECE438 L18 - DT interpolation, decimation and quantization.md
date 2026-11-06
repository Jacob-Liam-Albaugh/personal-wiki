---
type: lecture
area: dsp
source-ref: "L18 Feb 26, 2025, front page"
course: ece438
lecture: L18
tags: [signals]
---

# ECE438 L18 - DT interpolation, decimation and quantization

**Summary**: Lecture 18 front page: DT interpolation and decimation, first look at quantization, and a quiz on CT sampling.

**Sources**: `Digital Signal Processing/front page/L18 Feb 26, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: Anti-aliasing prefilter; non-ideal reconstruction; CT to DT frequency scaling
- This time: DT interpolation and decimation; quantization; quiz on CT sampling
(source: L18 Feb 26, 2025.pdf, p. 1)

## Review and notes

- Pre-filter with an ideal LPF of cutoff $\omega_s/2$ to avoid aliasing.
- Interpolation can be modelled as applying a non-ideal LPF to the samples.
- CT frequency $\omega$ and DT frequency $\Omega$ are related by $\Omega=\omega T$. DT is periodic in $\Omega$ with period $2\pi$; sampled CT is periodic in $\omega$ with period $2\pi/T=\omega_s$.
(source: L18 Feb 26, 2025.pdf, p. 1)

## Related pages
- [[ECE438 DSP.4.A - Sampling CT]] · [[ECE438 DSP.4.B - Sampling DT]] · [[ECE438 DSP.5 - Quantization]] · [[Quantization]] · [[Aliasing]] · [[Sampling theorem]] · [[Digital filter]]
