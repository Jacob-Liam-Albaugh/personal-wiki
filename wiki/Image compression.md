---
type: concept
area: dsp
source-ref: "ECE 438 Topic IP.6; Reibman DL 08 slides"
tags: [signals]
---

# Image compression

**Summary**: Reducing the bits needed for an image through entropy coding, prediction and transform coding, with fidelity judged by metrics such as MSE and PSNR. The Reibman slides show why PSNR alone is a poor guide to visual quality.

## Pipeline
Entropy and Huffman coding, spatial prediction, block transform coding (DCT, JPEG) and multiresolution coding are laid out in [[ECE438 IP.6 - Image compression]], [[ECE438 L34 - Image compression basics]], [[ECE438 L35 - Huffman coding, entropy and spatial prediction]], [[ECE438 L36 - Fidelity, block transform coding and JPEG]]. Keeping few transform coefficients is the best-approximation idea from the [[DFT]]; the amplitude side is [[Quantization]].

> [!definition] PSNR
> $$\mathrm{PSNR}=10\log_{10}\frac{L^2}{\mathrm{MSE}}$$
> (source: Topic IP.6, objective fidelity metrics)

## Reibman examples: why PSNR is not enough
> [!example] PSNR versus rate, JPEG-2000, two test images
> Plot of PSNR against bits per pixel (axis 0 to 0.1) for "Harbor" and "Bridge". Harbor rises from about 25 dB at the lowest rate to about 39 dB at 0.1 bpp; Bridge from about 19 dB to about 29 dB. Values read off the plot, except the labelled ones: Harbor 25.35 dB (lowest rate) and 34.61 dB (0.05 bpp); Bridge 19.09 dB and 25.25 dB at the same two rates. The same codec gives much lower PSNR on the texture-rich Bridge image.
>
> (source: reibman_purdue08-examples.pdf, pp. 1-6, slides "PSNR for image encoding: JPEG-2000")

> [!example] Why not PSNR: shift, and equal PSNR on unlike images
> Example 1: a 2-pixel shifted copy of the Harbor image has a relative PSNR of 20.11 dB, though the two look identical (pp. 7-8). Example 4: a resized version of Harbor is also shown against the original (pp. 9-10). Example 5: a heavily blurred Harbor at 25.36 dB and a good-looking Bridge at 25.25 dB have almost equal PSNR but very different quality (p. 11).
>
> (source: reibman_purdue08-examples.pdf, pp. 7-11)

Lesson: PSNR compares pixels, so it penalises harmless geometric changes and is content-dependent. Wiki note: the slide text gives no explanation for example 4 beyond the images; the reading of the resizing is mine. **[unverified]**

**Sources**: `Digital Signal Processing/Topic IP.6 Image compression Apr 23, 2025.pdf`, `Digital Signal Processing/reibman_purdue08-examples.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 IP.6 - Image compression]] · [[ECE438 L37 - Block transform coding and multiresolution processing]] · [[ECE438 IP.7 - Multiresolution image processing]]
- [[Quantization]] · [[DFT]] · [[Wavelet transform]] · [[Histogram equalization]] · [[Principal component analysis]] · [[Karhunen-Loève expansion]]
