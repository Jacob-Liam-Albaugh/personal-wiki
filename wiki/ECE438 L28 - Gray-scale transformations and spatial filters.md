---
type: lecture
area: dsp
source-ref: "L28 Apr 2, 2025, front page"
course: ece438
lecture: L28
tags: [signals]
---

# ECE438 L28 - Gray-scale transformations and spatial filters

**Summary**: Lecture 28 front page: 2D sinusoids and aliasing recap, then gray-scale transformations, histogram equalization, contrast stretching and spatial filters.

**Sources**: `Digital Signal Processing/front page/L28 Apr 2, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: 2D sinusoids; sampling and aliasing in 2D images; intro to histograms
- This time: Gray-scale transformations; histogram equalization and contrast stretching; spatial filters
(source: L28 Apr 2, 2025.pdf, p. 1)

## Review and notes

- A 2D sinusoid $A\cos(2\pi(u_0x+v_0y)+\theta)$ is constant along $u_0x+v_0y=c$ in the spatial domain. In the frequency domain there are two deltas, and the line between them is perpendicular to the peaks in the spatial domain.
- Aliasing in images can be readily seen with proper analysis: apply a Blackman window plus FFT. Always filter before downsampling.
- Notation: $h_f(b)$ is the histogram of image $f$, $P_f(b)$ its probability mass function.
(source: L28 Apr 2, 2025.pdf, p. 1)

## Related pages
- [[ECE438 IP.4.A - Histograms]] · [[ECE438 IP.4.B - Spatial filtering]] · [[Histogram equalization]] · [[Spatial filtering]] · [[Aliasing]] · [[Spectral leakage]]
