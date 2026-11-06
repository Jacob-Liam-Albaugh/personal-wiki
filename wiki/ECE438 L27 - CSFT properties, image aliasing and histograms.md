---
type: lecture
area: dsp
source-ref: "L27 Mar 31, 2025, front page"
course: ece438
lecture: L27
tags: [signals]
---

# ECE438 L27 - CSFT properties, image aliasing and histograms

**Summary**: Lecture 27 front page: CSFT properties, radial symmetry, aliasing in images and the start of histograms.

**Sources**: `Digital Signal Processing/front page/L27 Mar 31, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: Continuous-space FT; special functions (sinusoids, rect, circ) and their CSFT
- This time: CSFT properties; aliasing in images; histograms
(source: L27 Mar 31, 2025.pdf, p. 1)

## Review and notes

- The CSFT pair is $F(u,v)=\iint f(x,y)e^{-j2\pi xu}e^{-j2\pi yv}dx\,dy$ and the inverse with $e^{+j2\pi(xu+yv)}$ over $u,v$. It can be applied in 1D, then the next dimension.
- Radial symmetry: the function depends only on $r=\sqrt{x^2+y^2}$, not on $\theta=\tan^{-1}(y/x)$. The CSFT of a radially symmetric function is radially symmetric.
- Why show images: to connect the math to what you see.
(source: L27 Mar 31, 2025.pdf, p. 1)

## Related pages
- [[ECE438 IP.3 - Continuous-space FT]] · [[ECE438 IP.2 - Aliasing]] · [[ECE438 IP.4.A - Histograms]] · [[Fourier transform]] · [[Aliasing]]
