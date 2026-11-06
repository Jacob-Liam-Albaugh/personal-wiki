---
type: lecture
area: dsp
source-ref: "L20 Mar 3, 2025, front page"
course: ece438
lecture: L20
tags: [signals]
---

# ECE438 L20 - Optimal quantization and the z-transform

**Summary**: Lecture 20 front page: performance of a uniform quantizer, then optimal quantization and the start of the z-transform; quiz next time.

**Sources**: `Digital Signal Processing/front page/L20 Mar 3, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: Quantization and performance of a uniform quantizer
- This time: Optimal quantization; z-transform
(source: L20 Mar 3, 2025.pdf, p. 1)

## Review and notes

- A quantizer is a memoryless system $Y=Q(X)$ with $Y\in\{q_1,\dots,q_L\}$, and $Q(x)=q_k$ if $x_k<x<x_{k+1}$. It is a non-invertible mapping: once quantized, $X$ cannot be recovered.
- Quantization error $U$ is modelled by $Y=X+U$.
- For fine quantization (many levels) and a uniform quantizer with step size $\Delta$: $\mathrm{MSQE}=\Delta^2/12$. This holds for any input distribution (which has no delta functions).
- $\mathrm{SQNR}=C+6.02\,\ell$: SNR increases by 6.02 dB for every bit added to the quantizer.
(source: L20 Mar 3, 2025.pdf, p. 1)

## Logistics

- Next time: quiz on CT sampling and quantization.
(source: L20 Mar 3, 2025.pdf, p. 1)

## Related pages
- [[ECE438 DSP.5 - Quantization]] · [[Quantization]] · [[Z-transform]] · [[ECE438 DSP.6 - z-transforms]]
