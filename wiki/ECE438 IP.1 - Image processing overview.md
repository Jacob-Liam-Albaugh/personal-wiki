---
type: lecture
area: dsp
source-ref: "Topic IP.1, pp. 1-8"
course: ece438
lecture: IP.1
tags: [signals]
---

# ECE438 IP.1 - Image processing overview

**Summary**: Course roadmap for the image-processing half of ECE 438, following Gonzalez and Woods (4th ed.), plus basic definitions: image as a function, illumination times reflectance, imaging geometry, digital image, bit depth, colour images.

**File**: `Digital Signal Processing/Topic IP.1 Image processing overview Mar 23, 2025.pdf`

---

## Topics
- **Scope (p. 1)**: the notes connect topics to "Digital Image Processing", 4th ed., Gonzalez and Woods, as a six-week whirlwind tour. The sheet is headed "Topic IP.0" in the handwriting. Figures like the textbook's Fig. 1.23 (fundamental steps in digital image processing) always come from Gonzalez and Woods; chapters on morphological processing and pattern classification are crossed out (p. 2).
- **High-level outline (p. 3)**:
  - A. continuous-space analysis, Fourier analysis, image acquisition ([[ECE438 IP.3 - Continuous-space FT]])
  - B. discrete-space and digital images: sampling, quantization, bit planes, geometric transformations ([[ECE438 IP.2 - Sampling, quantization, interpolation]])
  - C. intensity transformations, spatial filtering, enhancement, some feature extraction ([[ECE438 IP.4.A - Histograms]], [[ECE438 IP.4.B - Spatial filtering]])
  - D. frequency analysis and the 2D DFT
  - E. image reconstruction and the Radon transform
  - F. wavelets and image transforms ([[ECE438 IP.5 - Image transforms and wavelets]], [[ECE438 IP.7 - Multiresolution image processing]])
  - G. image compression ([[ECE438 IP.6 - Image compression]])
  - Other topics not covered here: human visual system, segmentation, feature extraction, classification, colour spaces, computer vision.

## Key results
> [!definition] Image in continuous space (p. 4)
> $f(x,y)$ with $x,y\in\mathbb R$. A natural image has $0\le f<\infty$, proportional to the energy captured by a physical sensor. It depends on (a) the source illumination incident on the scene and (b) the illumination reflected by scene objects:
> $$f(x,y)=i(x,y)\,r(x,y)$$
> Illumination $0\le i<\infty$ depends on the light on the scene. Reflectance $0\le r\le1$ depends on the objects in the scene, from total absorption ($0$) to total reflectance ($1$).

> [!definition] Digital image (pp. 5-7)
> $f(m,n)$ with $m,n\in\mathbb Z$, quantized so values come from a finite set. Each $f(m,n)$ is a pixel (picture element). If sampled densely enough, the visual system merges pixels so the picture appears continuous.
> - Binary image: $0$ or $1$ (or $0$ and $255$).
> - Grayscale image: scalar value, range $0\to1$ or $0\to255$.
> - Bit depth: number of bits per image value; typical 8-bit and 1-bit, medical sometimes 10 or 12 bits.
> - Colour image: vector-valued, e.g. $f(m,n)=(f_r,f_g,f_b)$. RGB is "a relatively poor" colour space but common in consumer products (p. 8).

## Key remarks
- **Imaging geometry (p. 6)**: a point light source illuminates an object, reflected rays pass through a lens onto the image plane (sensor). Image projection reduces the dimension of the scene from 3D to 2D; that information is lost and very difficult to recover. Image coordinates: origin $(0,0)$ at the top-left, $x$ down rows, $y$ across columns.
- **Warning (p. 8)**: OpenCV reads images as BGR, not RGB; if an image looks odd, swap colour space.

## Connections
- The 1D theory (sampling, [[Quantization]], [[Fourier transform]], [[Digital filter]]) extends to 2D in the later lectures; the sampling theory is [[Sampling theorem]] and [[Aliasing]].

**Sources**: `Digital Signal Processing/Topic IP.1 Image processing overview Mar 23, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Discrete-time signal]] · [[Quantization]] · [[Sampling theorem]] · [[Aliasing]] · [[Fourier transform]]
