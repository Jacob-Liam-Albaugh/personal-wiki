---
type: concept
area: dsp
source-ref: "ECE 438 Topic DSP.4.A pp. 12-17, IP.2 aliasing"
tags: [signals]
---

# Aliasing

**Summary**: When a signal is sampled or downsampled too slowly, spectral replicas overlap and high frequencies masquerade as low ones. Once the overlap has happened it cannot be undone. The fix is a low-pass prefilter before sampling or downsampling.

## 1D mechanism
- If $\omega_s<2\omega_m$, replicas of $X(j\omega)$ overlap and add (see [[Sampling theorem]]). It also happens for non-bandlimited signals (DSP.4.A, pp. 12-13).
- $x(t)=\cos\omega_0t$ sampled with $\omega_s<2\omega_0$ looks like $\cos((\omega_s-\omega_0)t)$ (p. 13).
- Not recoverable afterwards (p. 14). Everyday cases: car wheels turning backwards on video (30 frames/s), and unfiltered image downsampling.
- DT: decimation $y[m]=x[mD]$ without the prefilter ($|\omega|\le\pi/D$) aliases (DSP.4.B, pp. 4-6).
- A DT frequency and the same frequency plus $2\pi$ are indistinguishable, see [[Discrete-time signal]].

> [!algorithm] Prefilter
> If $\omega_s$ cannot be raised, low-pass first with cutoff $\omega_0<\omega_s/2$. Losing the top frequencies knowingly beats letting them corrupt the low ones. (DSP.4.A, p. 17)

## 2D
Downsampling an image by 3 tiles the spectrum $3\times3$; the replicas pile onto the central piece. Unfiltered downsampling shows aliasing energy on an extension of the main lobe; a hard ideal filter rings, so a non-ideal filter is better. Moral: always filter before downsampling (IP.2 aliasing, pp. 3-11).

**Sources**: `Digital Signal Processing/Topic DSP.4.A Sampling CT.pdf`, `Digital Signal Processing/Topic DSP.4.B Sampling DT.pdf`, `Digital Signal Processing/Topic IP.2 aliasing-ece438-250328-share.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 DSP.4.A - Sampling CT]] · [[ECE438 DSP.4.B - Sampling DT]] · [[ECE438 IP.2 - Aliasing]] · [[ECE438 L17 - Anti-aliasing prefilter and non-ideal interpolation]] · [[ECE438 L26 - Continuous-space FT and aliasing in images]]
- [[Sampling theorem]] · [[Digital filter]] · [[Fourier transform]] · [[DTFT]] · [[Spatial filtering]]
