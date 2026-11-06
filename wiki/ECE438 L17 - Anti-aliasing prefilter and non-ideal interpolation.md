---
type: lecture
area: dsp
source-ref: "L17 Feb 24, 2025, front page"
course: ece438
lecture: L17
tags: [signals]
---

# ECE438 L17 - Anti-aliasing prefilter and non-ideal interpolation

**Summary**: Lecture 17 front page: Nyquist reconstruction recap, then the anti-aliasing prefilter, non-ideal interpolation, CT to DT frequency, and DT interpolation and decimation.

**Sources**: `Digital Signal Processing/front page/L17 Feb 24, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: Sampling in the frequency domain; Nyquist theorem; ideal reconstruction in frequency and time domains; aliasing (single cosine)
- This time: Anti-aliasing prefilter; non-ideal interpolation; relating CT and DT frequency; DT interpolation; DT decimation
(source: L17 Feb 24, 2025.pdf, p. 1)

## Review and notes

- CT sampling creates replicates in frequency.
- A bandlimited signal can be perfectly reconstructed from its samples if $\omega_s>2\omega_m$, where $X(j\omega)=0$ for $\omega>\omega_m$.
- The ideal reconstruction filter is an ideal low-pass filter; it is not realizable (not causal, infinite support in time).
- Aliasing occurs if $\omega_s<2\omega_m$.
(source: L17 Feb 24, 2025.pdf, p. 1)

## Logistics

- Next time: quantization and a quiz.
(source: L17 Feb 24, 2025.pdf, p. 1)

## Related pages
- [[Sampling theorem]] · [[Aliasing]] · [[ECE438 DSP.4.A - Sampling CT]] · [[ECE438 DSP.4.B - Sampling DT]] · [[Digital filter]]
