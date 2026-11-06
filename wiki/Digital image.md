---
type: concept
area: dsp
source-ref: "ECE 438 Topic IP.1, IP.2; lectures L24-L26"
tags: [signals]
---

# Digital image

**Summary**: A digital image is a sampled and quantised version of a continuous-space image: a 2D array of pixels with a finite set of values. Spatial resolution, bit depth and interpolation decide its visual quality. The course follows Gonzalez and Woods (4th ed.) as a six-week tour.

## Continuous and digital images
> [!definition] Image in continuous space
> $f(x,y)$ with $x,y\in\mathbb R$. A natural image has $0\le f<\infty$, proportional to the energy captured by a physical sensor, and depends on the source illumination $i$ and the reflectance $r$ of scene objects:
> $$f(x,y)=i(x,y)\,r(x,y)$$
> with $0\le i<\infty$ and $0\le r\le1$ (total absorption to total reflectance).
>
> (source: Topic IP.1 Image processing overview Mar 23, 2025.pdf, p. 4)

> [!definition] Digital image
> $f(m,n)$ with $m,n\in\mathbb Z$, quantised to a finite set of values; each value is a pixel. The same symbol $f$ is used for continuous-space and digital images. $(M,N)$ is the size and $L=2^k$ the number of quantisation levels. If sampled densely enough the visual system merges pixels into a continuous picture.
> - Binary image: 0 or 1 (or 0 and 255).
> - Grayscale: scalar, 0 to 1 or 0 to 255.
> - Bit depth: bits per value; typically 8 or 1, medical sometimes 10 or 12.
> - Colour: vector valued, $\mathbf f(m,n)=(f_r,f_g,f_b)$. RGB is a relatively poor colour space but common in consumer products.
>
> (source: IP.1, pp. 5-8; L25 Mar 26, 2025.pdf, p. 1)

Imaging geometry: a point source illuminates an object, reflected rays pass through a lens onto the image plane (sensor). The projection reduces the scene from 3D to 2D, losing information that is very difficult to recover. Image coordinates have origin $(0,0)$ at the top left, with $x$ down the rows and $y$ across the columns (IP.1, p. 6). Warning: OpenCV reads images as BGR, not RGB; swap the colour space if an image looks odd (IP.1, p. 8).

## Sampling, quantisation and resolution
Sampling digitises the coordinates and quantisation ([[Quantization]]) digitises the amplitude of the pattern of photons hitting the sensor array (source: Topic IP.2 Sampling, quantization, interpolation, p. 1).

> [!definition] Resolution
> Several inconsistent definitions exist: "smallest discernible detail", "resolving power of a lens". One measure is dots per inch (dpi): newspapers 75, magazines 133, glossy brochures 175, the image-processing book 2400. Pixel count alone is not enough: more pixels do not mean better resolution, and any resizing (interpolation) affects viewing.
>
> (source: IP.2, p. 3; L26 Mar 26, 2025.pdf, p. 1)

> [!example] Effects in Gonzalez and Woods figures
> - Fig. 2.20 (pixel-value range): saturation clips values above the top level; noise gives a grainy texture.
> - Fig. 2.23 (spatial resolution at fixed display size): graininess, then a checkerboard pattern.
> - Fig. 2.24 (bit depth): at 16, 8, 4, 2 levels false contouring appears and the image becomes dull and washed out.
>
> (source: IP.2, pp. 5-9)

English terms for these artifacts (checkerboard, jaggies, false contouring) overlap and are often imprecise. Undersampling causes [[Aliasing]]; the 2D analysis is in [[Fourier transform]]. Resizing is covered in [[Image interpolation]].

## Course outline
A. continuous-space and Fourier analysis, acquisition ([[Fourier transform]]); B. sampling, quantisation, bit planes, geometric transforms ([[Image interpolation]]); C. intensity transformations, spatial filtering, enhancement ([[Histogram equalization]], [[Spatial filtering]]); D. frequency analysis and the 2D DFT ([[DFT]]); E. reconstruction and the Radon transform; F. wavelets and image transforms ([[Image transforms]], [[Wavelet transform]]); G. compression ([[Image compression]]). Not covered: human visual system, segmentation, classification, colour spaces, computer vision (IP.1, p. 3). Fig. 1.23 (fundamental steps in digital image processing) and similar figures come from the textbook; morphological processing and pattern classification chapters are crossed out (IP.1, pp. 1-2).

**Covered in**: ECE 438 IP.1, IP.2 (resolution and bit depth), L24, L25, L26 (courses/ECE 438/Topic IP.1 Image processing overview Mar 23, 2025.pdf)
**Sources**: `courses/ECE 438/Topic IP.1 Image processing overview Mar 23, 2025.pdf`, `courses/ECE 438/Topic IP.2 Sampling, quantization, interpolation Mar 23, 2025 .pdf`, `courses/ECE 438/front page/L24 Mar 24, 2025.pdf`, `courses/ECE 438/front page/L25 Mar 26, 2025.pdf`, `courses/ECE 438/front page/L26 Mar 26, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Image interpolation]] · [[Quantization]] · [[Sampling theorem]] · [[Aliasing]] · [[Fourier transform]] · [[Discrete-time signal]] · [[Histogram equalization]] · [[Spatial filtering]] · [[Image transforms]] · [[Image compression]] · [[Wavelet transform]]
