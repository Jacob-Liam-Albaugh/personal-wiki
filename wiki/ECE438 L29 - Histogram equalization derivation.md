---
type: lecture
area: dsp
source-ref: "L29 Apr 4, 2025, front page"
course: ece438
lecture: L29
tags: [signals]
---

# ECE438 L29 - Histogram equalization derivation

**Summary**: Lecture 29 front page: gray-scale mapping for enhancement, the derivation of histogram equalization, then spatial filtering and the discrete-space 2D FT.

**Sources**: `Digital Signal Processing/front page/L29 Apr 4, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: Gray-scale mappings; histogram equalization
- This time: A little more spatial filtering (smoothing, edge detection); discrete-space 2D FT
(source: L29 Apr 4, 2025.pdf, p. 1)

## Review and notes

- Gray-scale mapping $g(m,n)=T(f(m,n))$ is for enhancement. It improves contrast for better visual detail and is useful for creating High Dynamic Range images from several low dynamic range images (tone mapping).
- Histogram equalization uses $T(b)=C_f(b)$, the CDF of $f$, so $g(m,n)=C_f(f(m,n))$. The result is the CDF of a uniform random variable on $0\le g\le1$.
- Derivation: $C_g(b)=b$ is required, and
(source: L29 Apr 4, 2025.pdf, p. 1)

$$C_g(b)=P(g\le b)=P(T(f)\le b)=P(f\le T^{-1}(b))=C_f(T^{-1}(b))$$

so $T(b)=C_f(b)$ is required.

## Related pages
- [[ECE438 IP.4.A - Histograms]] · [[ECE438 IP.4.B - Spatial filtering]] · [[Histogram equalization]] · [[Spatial filtering]]
