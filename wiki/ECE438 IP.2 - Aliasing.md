---
type: lecture
area: dsp
source-ref: "Topic IP.2 aliasing (ECE301 slides after Reibman and Suthaharan 2008), pp. 1-11"
course: ece438
lecture: IP.2
tags: [signals]
---

# ECE438 IP.2 - Aliasing

**Summary**: Slides on aliasing in images, based on Reibman and Suthaharan (2008), a no-reference spatial aliasing measure for image resizing. Downsampling without a low-pass filter folds spectrum copies on top of the main lobe.

**File**: `Digital Signal Processing/Topic IP.2 aliasing-ece438-250328-share.pdf`

---

## Topics
- Pictures taken off the web (real-estate photos, a brick wall) show aliasing from poor resizing (p. 1).
- Aliasing in 2D: view an image patch and its Fourier spectrum before and after downsampling (pp. 3-9).

## Key results
> [!theorem] Aliasing recap (p. 3)
> - Sampling a 1D signal too infrequently gives aliasing.
> - Aliasing is eliminated if an ideal low-pass filter (LPF) is applied first to remove high frequencies.
> - A non-ideal LPF removes much of the high-frequency content and is far better than no filtering before downsampling.

> [!algorithm] How the spectrum is displayed (p. 3)
> Steps: apply a Blackman window to a patch, take the 2D FFT, plot $\log|F(u,v)|$. In the Fourier domain the energy is perpendicular to the image edges, but location is lost.

> [!example] Downsampling by 3 in the Fourier domain (p. 5)
> Image downsampled by 3: the centre piece of the 3x3 tiling of the spectrum is the main component (the core). The other pieces get piled on top of each other and added. The actual spectrum of the downsampled patch shows this overlap (p. 7).

> [!example] Filtered versus not filtered (pp. 7-9)
> - Left image (ideally) filtered, right not filtered before downsampling.
> - Aliasing energy lies clearly on an extension of the main lobe in the spectrum.
> - A hard "ideal" filter causes ringing artifacts, but is used here for illustration.

> [!theorem] Moral (p. 11)
> Always filter your images before you downsample. Ideal filters create a lot of ringing, so a non-ideal filter is actually better.

## Connections
- 1D theory: [[Aliasing]], [[Sampling theorem]], [[ECE438 DSP.4.A - Sampling CT]], [[ECE438 DSP.4.B - Sampling DT]] (decimation).
- The 2D spectrum is a 2D [[DFT]]/[[Fourier transform]]; filtering is [[Digital filter]] design.
- Companion lecture: [[ECE438 IP.2 - Sampling, quantization, interpolation]].

**Sources**: `Digital Signal Processing/Topic IP.2 aliasing-ece438-250328-share.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Aliasing]] · [[Sampling theorem]] · [[Digital filter]] · [[DFT]] · [[Fourier transform]] · [[ECE438 IP.2 - Sampling, quantization, interpolation]]
