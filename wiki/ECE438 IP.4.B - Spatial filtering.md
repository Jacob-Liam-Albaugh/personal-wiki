---
type: lecture
area: dsp
source-ref: "Topic IP.4.B, pp. 1-12"
course: ece438
lecture: IP.4.B
tags: [signals]
---

# ECE438 IP.4.B - Spatial filtering

**Summary**: Linear spatial filtering as 2D convolution (or correlation) with a small kernel, border handling, DC preservation, separability, frequency analysis of image filters with the 2D DSFT, and nonlinear (median, order-statistic) filters. Reading: Gonzalez and Woods, sections 3.4-3.6, 4.6 and following.

**File**: `Digital Signal Processing/Topic IP.4.B spatial filtering Apr 4, 2025.pdf`

---

## Topics
- Low-pass filters: smoothing, blurring, noise reduction, "like" integration. High-pass filters: edge detection and sharpening, "like" differentiation, because edges are high-frequency content (p. 1).
- 2D discrete Fourier transform; directional filters that respond strongly to different edge orientations; nonlinear filters such as the median.

## Key results
> [!definition] Linear spatial filtering (p. 1)
> Output pixel $g(x,y)$ is a weighted sum of input pixels in the neighbourhood of the corresponding location; equivalent to 2D [[Convolution]]. Notation: $f(m,n)$ input, $g(m,n)$ output, $h(m,n)$ filter coefficients (impulse response).
> $$g(m,n)=\sum_k\sum_\ell h(k,\ell)\,f(m-k,\,n-\ell)$$
> or, as 2D correlation with $h'$:
> $$g(m,n)=\sum_{k'}\sum_{\ell'}h'(k',\ell')\,f(m+k',\,n+\ell')$$
> with $h(k,\ell)=h'(-k,-\ell)$. A convolutional neural network really performs correlation, not convolution; fine if self-consistent. If $h$ is symmetric in both $k$ and $\ell$ the distinction is unnecessary (p. 3).

> [!assumption] Dealing with image borders (p. 3)
> At least three options:
> 1. Compute $g(m,n)$ only where the shifted filter overlaps $f$ completely (smaller $g$).
> 2. Extend the image with zeros.
> 3. Extend by replicating boundary pixels.
>
> Options 2 and 3 keep the same number of pixels. The worked example uses replication, centring the filter at each pixel of interest.

> [!definition] DC preserving (p. 5)
> If $f(m,n)=c$ everywhere, then
> $$g(m,n)=c\sum_k\sum_\ell h(m-k,n-\ell)$$
> so a filter is DC preserving if $\sum_k\sum_\ell h(k,\ell)=1$; then $g=c$ and flat regions are kept.

> [!definition] Separable filter (p. 5)
> $h(k,\ell)=h_1(k)\,h_2(\ell)$. Then it can be implemented by filtering first along one dimension, then the other, 1D each.

> [!theorem] Frequency-domain analysis (p. 9)
> 2D discrete-space Fourier transform (DSFT):
> $$F(\mu,\nu)=\sum_m\sum_nf(m,n)\,e^{-j(m\mu+n\nu)}$$
> $$f(m,n)=\frac1{(2\pi)^2}\int_{-\pi}^{\pi}\!\int_{-\pi}^{\pi}F(\mu,\nu)\,e^{j(m\mu+n\nu)}\,d\mu\,d\nu$$
> Units: radians/pixel. A horizontal edge in space appears as a vertical band in frequency through $(0,0)$. $F$ is $2\pi$-periodic in both variables. Convolution property: $f*g\leftrightarrow F(\mu,\nu)G(\mu,\nu)$. See [[DTFT]] for the 1D version.

## Examples
> [!example] Smoothing filter, border and DC (pp. 3-5)
> Image values in $\{0,1\}$ on a 6x6 grid, filter $h=\frac1{16}\begin{bmatrix}1&2&1\\2&4&2\\1&2&1\end{bmatrix}$ (symmetric). Computed by hand with replication: $g(4,1)=16/16=1$ (flat region), $g(4,4)=4/16$. Observations: the filter smooths edges (large differences between adjacent pixels) and preserves DC (flat regions stay flat). It is separable: $h=h_1(k)h_2(\ell)$ with $\frac14[1,2,1]$ in each direction.

> [!example] Edge-detecting filter (pp. 5-7)
> $h=\frac19\begin{bmatrix}-1&-1&-1\\-1&8&-1\\-1&-1&-1\end{bmatrix}$. Same image: $g(2,3)=5/9$, $g(4,1)=0$, $g(4,4)=-3/9$. Observations: large response at edges; no response when the input is constant (because $\sum h=0$); the filter is not separable.

> [!example] DSFT of the smoothing filter (p. 11)
> $$H_1(\mu)=\tfrac14e^{j\mu}+\tfrac12+\tfrac14e^{-j\mu}=\tfrac12(1+\cos\mu)$$
> $$H(\mu,\nu)=\tfrac14(1+\cos\mu)(1+\cos\nu)$$
> A low-pass filter; $H(0,0)=1$ so DC preserving.

> [!example] DSFT of the edge filter (p. 11)
> Not separable, but $h=\delta(k,\ell)-h_2(k)h_2(\ell)$ with $h_2=\frac13[1,1,1]$ (a 3-point box). Then
> $$H(\mu,\nu)=1-H_2(\mu)H_2(\nu)$$
> $$H_2(\mu)=\tfrac13(1+2\cos\mu)$$
> $H_2$ equals $-1/3$ at $\mu=\pi$ and has zeros at $\pm2\pi/3$. $H$ is a high-pass filter and $H(0,0)=1-1\cdot1=0$, so not DC preserving (p. 13).

> [!algorithm] Nonlinear spatial filtering (p. 13)
> Why: linear smoothing filters can overly smear desired features while removing noise; depending on the noise, a nonlinear filter may remove it without damaging the signal.
> $$g(m,n)=\operatorname*{median}_{k,\ell\in\eta}f(m+k,\,n+\ell)$$
> $\eta$ defines the neighbourhood. Median is the 50th percentile: pixel locations in the neighbourhood do not matter, only values; sort and take the middle. Other order-statistic filters: min (0th percentile), max (100th), and the alpha-trimmed mean (delete the $\alpha/2$ lowest and highest values, then average).

## Connections
- This is the image version of the 1D [[LTI system]] / [[Digital filter]] story; the convolution theorem is [[Convolution]] with [[DTFT]].
- Intensity (pointwise) transformations: [[ECE438 IP.4.A - Histograms]]. Filtering in the frequency domain with the 2D DFT: [[DFT]], [[FFT]].
- Wiki note: the sheet writes the 3x3 output of the second example only at three pixels; other pixel values on the grid are not reproduced here.

**Sources**: `Digital Signal Processing/Topic IP.4.B spatial filtering Apr 4, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 IP.4.A - Histograms]] · [[Convolution]] · [[Digital filter]] · [[DTFT]] · [[DFT]] · [[Spatial filtering]]
