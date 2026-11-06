---
type: method
area: dsp
source-ref: "ECE 438 Topic IP.4.B, pp. 1-11"
tags: [signals]
---

# Spatial filtering

**Summary**: Each output pixel is a function of a neighbourhood of input pixels. Linear versions are 2D [[Convolution]] with a small kernel; low-pass kernels smooth, high-pass kernels detect edges. Non-linear examples include the median filter.

> [!definition] Linear spatial filter
> $$g(m,n)=\sum_k\sum_\ell h(k,\ell)\,f(m-k,n-\ell)$$
> Correlation uses $f(m+k',n+\ell')$ with $h(k,\ell)=h'(-k,-\ell)$; a symmetric kernel makes them equal. CNNs actually compute correlation.
>
> (source: Topic IP.4.B, pp. 1-3)

- Borders: use only fully overlapping positions, extend with zeros, or replicate boundary pixels (p. 3).
- DC preserving: $\sum h=1$. Separable: $h=h_1(k)h_2(\ell)$, so two 1D passes (p. 5).
- Smoothing kernel $\frac1{16}[1\,2\,1;\,2\,4\,2;\,1\,2\,1]$ keeps flat regions and blurs edges; edge kernel $\frac19[-1\,\dots\,8\,\dots-1]$ gives zero on constants and a large response at edges, and is not separable (pp. 3-7).
- Frequency view: the 2D DSFT $F(\mu,\nu)=\sum_{m,n}f(m,n)e^{-j(m\mu+n\nu)}$, units radians per pixel, $2\pi$-periodic; $f*g\leftrightarrow FG$. A horizontal edge is a vertical band through the origin (p. 9). 1D version: [[DTFT]].
- Smoothing kernel response per axis: $\frac12(1+\cos\mu)$ (p. 11).

Wiki note: low-pass filtering before downsampling is the 2D anti-aliasing prefilter ([[Aliasing]]); the pointwise counterpart is [[Histogram equalization]].

**Sources**: `Digital Signal Processing/Topic IP.4.B spatial filtering Apr 4, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 IP.4.B - Spatial filtering]] · [[ECE438 L28 - Gray-scale transformations and spatial filters]] · [[ECE438 L30 - High-pass filtering, 2D DSFT and median filtering]] · [[ECE438 L31 - Non-linear filters and the 2D DSFT]]
- [[Convolution]] · [[Digital filter]] · [[DTFT]] · [[DFT]] · [[Aliasing]] · [[Histogram equalization]] · [[Wavelet transform]]
