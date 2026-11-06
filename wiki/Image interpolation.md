---
type: method
area: dsp
source-ref: "ECE 438 Topic IP.2, pp. 11-17"
tags: [signals]
---

# Image interpolation

**Summary**: Assigning pixel values at non-grid locations, used for resizing and geometric transforms. The spatial-domain methods are nearest neighbour, bilinear and bicubic; they are the pixel-domain counterpart of ideal reconstruction in the [[Sampling theorem]].

> [!algorithm] Nearest-neighbour interpolation
> Use the intensity of the original pixel nearest the desired location $(x',y')$:
> $$v(x',y')=f\big(\lfloor x'+\tfrac12\rfloor,\ \lfloor y'+\tfrac12\rfloor\big)=f(\mathrm{round}(x'),\mathrm{round}(y'))$$
> Roughly sample-and-hold with a shift, in 2D.
>
> (source: Topic IP.2 Sampling, quantization, interpolation, p. 11)

> [!algorithm] Bilinear interpolation
> Weight the four nearest pixels $f_1,\dots,f_4$ by distance, with $d_1+d_2=1$ and $d_3+d_4=1$:
> $$v=(1-d_1)(1-d_3)f_1+(1-d_1)(1-d_4)f_3$$
> $$\quad+(1-d_2)(1-d_3)f_2+(1-d_2)(1-d_4)f_4$$
> Equivalent to linear interpolation along rows then columns (or the reverse), or to weighting each $f_i$ by the area of the opposite rectangle (the weight of $f_4$ is $A_4=d_1d_3=(1-d_2)(1-d_4)$).
>
> (source: IP.2, p. 11)

> [!algorithm] Bicubic interpolation
> Fits a third-order polynomial surface through 16 points, where bilinear uses lines through 4. More computation, better fine detail. It may overshoot: sharp edges give negative values, seen as a halo or ringing around edges.
>
> (source: IP.2, p. 13)

> [!example] Zooming figures
> Fig. 2.27: an image reduced to 72 dpi and zoomed to 930 dpi is blocky with nearest neighbour, smoother with bilinear and keeps most detail with bicubic (p. 13). Zooms from 128x128, 64x64, 32x32 to 1024x1024, nearest neighbour above bilinear (p. 15).

## Geometric transformations
> [!algorithm] Rubber-sheet transformation
> Two parts: (a) a spatial transformation of coordinates and (b) intensity interpolation to assign values to the transformed pixels.
> $$\begin{bmatrix}x'\\y'\end{bmatrix}=T\begin{bmatrix}x\\y\end{bmatrix}$$
> For example $(x',y')=(x/2,y/2)$ shrinks both dimensions. An affine transformation (scaling, translation, rotation, shearing) preserves straight lines and planes:
> $$\begin{bmatrix}x'\\y'\end{bmatrix}=T\begin{bmatrix}x\\y\end{bmatrix}+\begin{bmatrix}\Delta x\\\Delta y\end{bmatrix}$$
> Forward mapping can send two pixels to one location and leave others unmapped. Inverse mapping computes the source for each output location, then interpolates:
> $$\begin{bmatrix}x\\y\end{bmatrix}=T^{-1}\begin{bmatrix}x'-\Delta x\\y'-\Delta y\end{bmatrix}$$
> Black regions often remain in the result.
>
> (source: IP.2, pp. 15-17)

The interpolation kernels are 2D [[Convolution]] filters ([[Digital filter]]). Shrinking without a low-pass prefilter causes [[Aliasing]]; the frequency-domain view follows [[Fourier transform]] in 2D. Background on images: [[Digital image]].

**Covered in**: ECE 438 IP.2 (Sampling, quantization, interpolation), pp. 11-17 (courses/ECE 438/Topic IP.2 Sampling, quantization, interpolation Mar 23, 2025 .pdf)
**Sources**: `courses/ECE 438/Topic IP.2 Sampling, quantization, interpolation Mar 23, 2025 .pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Digital image]] · [[Sampling theorem]] · [[Aliasing]] · [[Quantization]] · [[Convolution]] · [[Digital filter]] · [[Fourier transform]]
