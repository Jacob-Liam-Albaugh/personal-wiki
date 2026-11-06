---
type: lecture
area: dsp
source-ref: "L16 Feb 21, 2025, front page"
course: ece438
lecture: L16
tags: [signals]
---

# ECE438 L16 - Impulse-train sampling in the frequency domain

**Summary**: Lecture 16 front page: impulse-train sampling of a CT signal, analysed now in the frequency domain after the time-domain analysis of the previous lecture.

**Sources**: `Digital Signal Processing/front page/L16 Feb 21, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: Framework for sampling CT to DT; impulse-train sampling, time-domain analysis
- This time: Impulse-train sampling, frequency-domain analysis
(source: L16 Feb 21, 2025.pdf, p. 1)

## Review and notes

- Time domain: $x_p(t)=x_c(t)p(t)=x_d(nT)p(t)$, the continuous-time connection to the DT signal $x_d(nT)$. A reconstruction block maps $x_p(t)$ to $y_c(t)$.
- Frequency-domain analysis depends on the CTFT pair $X(j\omega)=\int x(t)e^{-j\omega t}dt$ and $x(t)=\frac{1}{2\pi}\int X(j\omega)e^{j\omega t}d\omega$.
- The impulse train $p(t)=\sum_k\delta(t-kT)$ has $P(j\omega)=\frac{2\pi}{T}\sum_k\delta(\omega-\frac{2\pi k}{T})$.
- Multiplication in time becomes convolution in frequency: $x_1(t)x_2(t)\leftrightarrow\frac{1}{2\pi}X_1(j\omega)*X_2(j\omega)$.
(source: L16 Feb 21, 2025.pdf, p. 1)

## Logistics

- Exams returned: average 79, max 100.
(source: L16 Feb 21, 2025.pdf, p. 1)

## Related pages
- [[ECE438 DSP.4.A - Sampling CT]] · [[Sampling theorem]] · [[Fourier transform]] · [[Aliasing]] · [[Convolution]]
