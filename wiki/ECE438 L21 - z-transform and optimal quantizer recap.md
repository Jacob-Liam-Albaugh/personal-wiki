---
type: lecture
area: dsp
source-ref: "L21 Mar 5, 2025, front page"
course: ece438
lecture: L21
tags: [signals]
---

# ECE438 L21 - z-transform and optimal quantizer recap

**Summary**: Lecture 21 front page: recap of the optimal (Lloyd-Max) quantizer conditions, then the z-transform, a quiz and exam logistics.

**Sources**: `Digital Signal Processing/front page/L21 Mar 5, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: Optimal quantization
- This time: z-transform; quiz
(source: L21 Mar 5, 2025.pdf, p. 1)

## Review and notes

- The optimal quantizer sets break points $x_k$ and reconstruction levels $q_k$ to minimize $\mathrm{MSQE}=E[(Q(x)-x)^2]$.
- Optimal break points are midway between the optimal reconstruction levels: $x_k=(q_{k-1}+q_k)/2$.
- Optimal reconstruction levels are at the centroid of the quantization interval:
(source: L21 Mar 5, 2025.pdf, p. 1)

$$q_k=E[X\mid x_k<X<x_{k+1}]$$

$$q_k=\frac{\int_{x_k}^{x_{k+1}}x f_X(x)\,dx}{\int_{x_k}^{x_{k+1}}f_X(x)\,dx}$$

## Logistics

- Exam next Wednesday in class, 50 minutes, TA proctoring.
(source: L21 Mar 5, 2025.pdf, p. 1)

## Related pages
- [[ECE438 DSP.5 - Quantization]] · [[Quantization]] · [[Z-transform]] · [[ECE438 DSP.6 - z-transforms]]
