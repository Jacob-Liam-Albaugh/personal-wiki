---
type: lecture
area: dsp
source-ref: "L30 Apr 7, 2025, front page"
course: ece438
lecture: L30
tags: [signals]
---

# ECE438 L30 - High-pass filtering, 2D DSFT and median filtering

**Summary**: Lecture 30 front page: a high-pass filter, the 2D DFT (DSFT) and median filtering, with 2D convolution review.

**Sources**: `Digital Signal Processing/front page/L30 Apr 7, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: Spatial (2D) filtering: mechanics, boundary operations, a low-pass smoothing filter
- This time: Another filter (high pass); 2D DFT = DSFT; median filtering
(source: L30 Apr 7, 2025.pdf, p. 1)

## Review and notes

- 2D convolution: $y(m,n)=\sum_k\sum_l h(k,l)\,x(m-k,n-l)$. Watch the boundaries.
- DC preserving if $\sum_k\sum_l h(l,k)=1$. Separable if $h(l,k)=h_1(l)h_2(k)$.
(source: L30 Apr 7, 2025.pdf, p. 1)

## Logistics

- Next time: quiz on histograms and gray-scale mapping, and 2D filtering.
(source: L30 Apr 7, 2025.pdf, p. 1)

## Related pages
- [[ECE438 IP.4.B - Spatial filtering]] · [[Spatial filtering]] · [[Convolution]] · [[DFT]] · [[Fourier transform]]
