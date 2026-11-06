---
type: lecture
area: dsp
source-ref: "L31 Apr 9, 2025, front page"
course: ece438
lecture: L31
tags: [signals]
---

# ECE438 L31 - Non-linear filters and the 2D DSFT

**Summary**: Lecture 31 front page: low-pass and high-pass filters in the DFT domain, non-linear filters, a quiz, and the start of 2D image transforms.

**Sources**: `Digital Signal Processing/front page/L31 Apr 9, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: High-pass filter; 2D DFT (discrete-space FT); LP filter DFT; HP filter DFT
- This time: Non-linear filters; quiz; 2D image transforms
(source: L31 Apr 9, 2025.pdf, p. 1)

## Review and notes

- LP filters smooth edges; HP filters have strong responses at edges.
- Discrete-space FT: $F(\mu,\nu)=\sum_m\sum_n f(m,n)e^{-j(m\mu+n\nu)}$, with $\mu,\nu$ in radians per pixel (or per sample), periodic in both $\mu$ and $\nu$.
- Inverse: $f(m,n)=\frac{1}{(2\pi)^2}\int_{-\pi}^{\pi}\int_{-\pi}^{\pi}F(\mu,\nu)e^{j(m\mu+n\nu)}d\mu\,d\nu$.
- Convolution: $f(m,n)*g(m,n)\leftrightarrow F(\mu,\nu)G(\mu,\nu)$ (2D DFT).
(source: L31 Apr 9, 2025.pdf, p. 1)

## Related pages
- [[ECE438 IP.4.B - Spatial filtering]] · [[Spatial filtering]] · [[DTFT]] · [[DFT]] · [[Convolution]] · [[ECE438 IP.5 - Image transforms and wavelets]]
