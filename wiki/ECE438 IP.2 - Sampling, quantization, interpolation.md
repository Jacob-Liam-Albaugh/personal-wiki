---
type: lecture
area: dsp
source-ref: "Topic IP.2 (sampling, quantization, representation), pp. 1-17"
course: ece438
lecture: IP.2
tags: [signals]
---

# ECE438 IP.2 - Sampling, quantization, interpolation

**Summary**: Digital image formation (sampling plus quantization), what resolution and bit depth do to visual quality, and spatial-domain image interpolation (nearest neighbour, bilinear, bicubic) used for geometric transformations. Readings are from Gonzalez and Woods, ch. 2.

**File**: `Digital Signal Processing/Topic IP.2 Sampling, quantization, interpolation Mar 23, 2025 .pdf`

---

## Topics
- Effect of spatial resolution $(M,N)$ and bit depth $L=2^k$ on visual impact (p. 1).
- Interpolation as a modified perspective in the pixel domain; the Fourier view comes after 2D Fourier methods (pp. 1, 11, 13).
- Geometric transformations: spatial transform of coordinates plus intensity interpolation (pp. 15-17).

## Key results
> [!definition] Sampling and quantization of an image (p. 1)
> A continuous image is projected onto a sensor array (a pattern of photons hitting the sensor). Sampling digitizes the coordinate values; quantization digitizes the amplitude values. The origin is $(m,n)=(0,0)$.

> [!definition] Resolution (p. 3)
> Several formal and informal definitions exist, not all consistent: "smallest discernible detail", "resolving power of a lens". One measure is dots per unit measure, in the US dpi (dots per inch).
> - Newspapers: 75 dpi
> - Magazines: 133 dpi
> - Glossy brochures: 175 dpi
> - Image-processing book: 2400 dpi
> Image size (number of pixels) alone is not enough.

> [!theorem] Effects seen in Gonzalez and Woods figures
> - Range of pixel values (Fig. 2.20): saturation clips all values above the top level; noise gives a grainy texture (p. 5).
> - Reduced spatial resolution at fixed display size gives graininess, then a checkerboard pattern (Fig. 2.23, p. 7).
> - Reduced bit depth: high contrast is possible at high depth; at 16, 8, 4, 2 levels false contouring appears and the image becomes dull and washed out (Fig. 2.24, p. 9).

> [!algorithm] Nearest-neighbour interpolation (p. 11)
> Find the pixel in the original image nearest to the desired location $(x',y')$ and use its intensity:
> $$v(x',y')=f\big(\lfloor x'+\tfrac12\rfloor,\ \lfloor y'+\tfrac12\rfloor\big)$$
> That is $f(\mathrm{round}(x'),\mathrm{round}(y'))$. Somewhat analogous to sample-and-hold (see [[Sampling theorem]]), with a time shift, in 2D.

> [!algorithm] Bilinear interpolation (p. 11)
> Take the four nearest original pixels $f_1,\dots,f_4$ and weight them by $x/y$ distance. With $d_1+d_2=1$ and $d_3+d_4=1$:
> $$v=(1-d_1)(1-d_3)f_1+(1-d_1)(1-d_4)f_3$$
> $$\quad+(1-d_2)(1-d_3)f_2+(1-d_2)(1-d_4)f_4$$
> Two readings: linear interpolation along rows then columns (or vice versa); or weight each $f_i$ by the area of the opposite rectangle (for example the coefficient of $f_4$ is $A_4=d_1d_3=(1-d_2)(1-d_4)$).

> [!algorithm] Bicubic interpolation (p. 13)
> Bilinear approximates a surface between 4 points with lines (or does two sets of linear interpolation, each with 2 points). Bicubic uses 16 points to approximate a surface with a third-order polynomial.
> - More computation; preserves fine detail better than bilinear.
> - May overshoot: sharp edges cause negative values, seen as a halo around edges, equivalently ringing artifacts.

> [!algorithm] Geometric transformation (pp. 15-17)
> Rubber-sheet transformations (stretching and scaling) have two parts: (a) a spatial transformation of the coordinates, (b) intensity interpolation to assign values to the transformed pixels.
> $$\begin{bmatrix}x'\\y'\end{bmatrix}=T\begin{bmatrix}x\\y\end{bmatrix}$$
> Example: $(x',y')=(x/2,\,y/2)$ shrinks the image in both dimensions. An affine transformation (scaling, translation, rotation, shearing) preserves straight lines and planes:
> $$\begin{bmatrix}x'\\y'\end{bmatrix}=T\begin{bmatrix}x\\y\end{bmatrix}+\begin{bmatrix}\Delta x\\\Delta y\end{bmatrix}$$
> Forward mapping can send two pixels to the same location and leave others unmapped. Inverse mapping computes, for each $(x',y')$, the source location, then interpolates:
> $$\begin{bmatrix}x\\y\end{bmatrix}=T^{-1}\begin{bmatrix}x'-\Delta x\\y'-\Delta y\end{bmatrix}$$
> Black regions often remain in the final image (p. 17).

## Examples
- Fig. 2.27 (p. 13): an image reduced to 72 dpi and zoomed back to 930 dpi; nearest neighbour is blocky, bilinear is smoother, bicubic keeps most detail.
- Zoom from 128x128, 64x64, 32x32 to 1024x1024, nearest neighbour (top row) versus bilinear (bottom row) (p. 15).

## Connections
- Interpolation here is the pixel-domain version of ideal reconstruction in [[Sampling theorem]]; the frequency view and visual impact of [[Aliasing]] come in [[ECE438 IP.2 - Aliasing]].
- Bit-depth reduction is scalar [[Quantization]].
- Interpolation kernels are 2D [[Convolution]] filters ([[Digital filter]]).

**Sources**: `Digital Signal Processing/Topic IP.2 Sampling, quantization, interpolation Mar 23, 2025 .pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 IP.1 - Image processing overview]] · [[ECE438 IP.2 - Aliasing]] · [[Quantization]] · [[Sampling theorem]] · [[Aliasing]] · [[Convolution]] · [[Digital filter]]
