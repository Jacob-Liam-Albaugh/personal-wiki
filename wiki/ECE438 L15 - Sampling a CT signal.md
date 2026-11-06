---
type: lecture
area: dsp
source-ref: "L15 Feb 19, 2025, front page"
course: ece438
lecture: L15
tags: [signals]
---

# ECE438 L15 - Sampling a CT signal

**Summary**: Lecture 15 front page: recap of the FFT and digital filter $H_d(e^{j\omega})$, then the start of sampling a continuous-time signal, with a quiz.

**Sources**: `Digital Signal Processing/front page/L15 Feb 19, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: FFT; digital filter/system $H_d(e^{j\omega})$
- This time: Sampling a CT signal; quiz
(source: L15 Feb 19, 2025.pdf, p. 1)

## Review and notes

- Given the input-output relationship of a system, find $H(e^{j\omega})$. Preferred method: take the DTFT of both sides.
- Relies on the DTFT time-shift property, $x[n-n_0]\leftrightarrow e^{-j\omega n_0}X(e^{j\omega})$.
- Relies on the DTFT convolution property, $y[n]=x[n]*h[n]\leftrightarrow Y(e^{j\omega})=X(e^{j\omega})H(e^{j\omega})$.
(source: L15 Feb 19, 2025.pdf, p. 1)

## Related pages
- [[ECE438 DSP.3.E - FFT]] · [[ECE438 DSP.4.A - Sampling CT]] · [[DTFT]] · [[Convolution]] · [[Digital filter]] · [[Sampling theorem]]
