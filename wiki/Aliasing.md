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

### Recap and display recipe for images
Sampling a 1D signal too infrequently gives aliasing; it is eliminated if an ideal low-pass filter is applied first, and a non-ideal low-pass removes much of the high-frequency content and is far better than no filtering before downsampling. Pictures taken off the web (real-estate photos, a brick wall) show aliasing from poor resizing; the slides follow Reibman and Suthaharan (2008), a no-reference spatial aliasing measure for image resizing (source: Topic IP.2 aliasing slides, pp. 1-3).

> [!algorithm] How the spectrum is displayed
> Apply a Blackman window to a patch, take the 2D FFT, plot $\log|F(u,v)|$. Energy in the Fourier domain lies perpendicular to the image edges, but location is lost.
>
> (source: Topic IP.2 aliasing slides, p. 3)

> [!example] Downsampling by 3 and filtered versus unfiltered
> After downsampling by 3, the centre piece of the $3\times3$ tiling of the spectrum is the main component (the core); the other pieces pile on top of each other and add, and the actual spectrum of the downsampled patch shows this overlap (pp. 5-7). Comparing an ideally filtered with an unfiltered downsample, the aliasing energy lies clearly on an extension of the main lobe. The hard ideal filter causes ringing, used here only for illustration (pp. 7-9).

Lecture-27 note: aliasing of a sampled image is the same replica overlap in the 2D transform, using the bed-of-nails sampling model on [[Fourier transform]]. For the reconstruction side see [[Image interpolation]].

**Covered in**: ECE 438 IP.2 Aliasing (Topic IP.2 aliasing slides), DSP.4.A/B aliasing parts, L17, L26-L27 (aliasing in images)
**Sources**: `courses/ECE 438/Topic DSP.4.A Sampling CT.pdf`, `courses/ECE 438/Topic DSP.4.B Sampling DT.pdf`, `courses/ECE 438/Topic IP.2 aliasing-ece438-250328-share.pdf`, `courses/ECE 438/front page/L17 Feb 24, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sampling theorem]] · [[Digital filter]] · [[Fourier transform]] · [[DTFT]] · [[Spatial filtering]] · [[Image interpolation]]
