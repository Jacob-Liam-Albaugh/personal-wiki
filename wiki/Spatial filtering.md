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

## Low-pass and high-pass
Low-pass filters smooth, blur and reduce noise ("like" integration); high-pass filters detect edges and sharpen ("like" differentiation), since edges are high-frequency content. Directional filters respond strongly to particular edge orientations (source: Topic IP.4.B, p. 1; L31 Apr 9, 2025.pdf, p. 1).

> [!definition] DC preserving and separable
> If $f(m,n)=c$ everywhere, $g(m,n)=c\sum_k\sum_\ell h(k,\ell)$, so a filter is DC preserving when $\sum_k\sum_\ell h(k,\ell)=1$. It is separable when $h(k,\ell)=h_1(k)h_2(\ell)$, so filtering along one axis then the other suffices.
>
> (source: Topic IP.4.B, p. 5; L30 Apr 7, 2025.pdf, p. 1)

> [!theorem] 2D discrete-space Fourier transform (DSFT)
> $$F(\mu,\nu)=\sum_m\sum_nf(m,n)\,e^{-j(m\mu+n\nu)}$$
> $$f(m,n)=\frac1{(2\pi)^2}\int_{-\pi}^{\pi}\!\int_{-\pi}^{\pi}F(\mu,\nu)\,e^{j(m\mu+n\nu)}\,d\mu\,d\nu$$
> Units radians per pixel, $2\pi$-periodic in both variables; $f*g\leftrightarrow F(\mu,\nu)G(\mu,\nu)$. A horizontal edge in space is a vertical band through $(0,0)$ in frequency. Low-pass filters smooth edges and high-pass filters respond strongly at them.
>
> (source: Topic IP.4.B, p. 9; L31 Apr 9, 2025.pdf, p. 1)

> [!example] Smoothing filter on a 6x6 binary image
> $h=\frac1{16}\begin{bmatrix}1&2&1\\2&4&2\\1&2&1\end{bmatrix}$ (symmetric), values in $\{0,1\}$, borders by replication with the filter centred on each pixel. Hand results: $g(4,1)=16/16=1$ (flat region), $g(4,4)=4/16$. The filter smooths edges and preserves DC. It is separable with $\frac14[1,2,1]$ in each direction.
>
> (source: Topic IP.4.B, pp. 3-5)

> [!example] Edge-detecting filter on the same image
> $h=\frac19\begin{bmatrix}-1&-1&-1\\-1&8&-1\\-1&-1&-1\end{bmatrix}$. Results: $g(2,3)=5/9$, $g(4,1)=0$, $g(4,4)=-3/9$. Large response at edges, none on constants because $\sum h=0$, and not separable.
>
> (source: Topic IP.4.B, pp. 5-7)

> [!example] DSFT of the smoothing filter
> $$H_1(\mu)=\tfrac14e^{j\mu}+\tfrac12+\tfrac14e^{-j\mu}=\tfrac12(1+\cos\mu)$$
> $$H(\mu,\nu)=\tfrac14(1+\cos\mu)(1+\cos\nu)$$
> Low-pass with $H(0,0)=1$.
>
> (source: Topic IP.4.B, p. 11)

> [!example] DSFT of the edge filter
> Not separable, but $h=\delta(k,\ell)-h_2(k)h_2(\ell)$ with $h_2=\frac13[1,1,1]$, so
> $$H(\mu,\nu)=1-H_2(\mu)H_2(\nu),\qquad H_2(\mu)=\tfrac13(1+2\cos\mu)$$
> $H_2=-1/3$ at $\mu=\pi$ with zeros at $\pm2\pi/3$. $H$ is high-pass and $H(0,0)=0$, so not DC preserving.
>
> (source: Topic IP.4.B, pp. 11-13)

> [!algorithm] Nonlinear spatial filtering
> Linear smoothing can smear desired features while removing noise; depending on the noise a nonlinear filter removes it without damaging the signal.
> $$g(m,n)=\operatorname*{median}_{k,\ell\in\eta}f(m+k,\,n+\ell)$$
> $\eta$ is the neighbourhood. The median (50th percentile) uses only the values, not their positions: sort and take the middle. Other order-statistic filters: min (0th percentile), max (100th), and the alpha-trimmed mean (drop the $\alpha/2$ lowest and highest values, average the rest).
>
> (source: Topic IP.4.B, p. 13; L30 Apr 7, 2025.pdf, p. 1)

Wiki note: the sheet gives the edge-filter output at only three pixels; other grid values are not reproduced. The 2D transform of the next topic is [[Image transforms]]; frequency-domain filtering uses the 2D [[DFT]] and [[FFT]]; the 1D version is [[DTFT]] and the system view is [[LTI system]] and [[Digital filter]].

Wiki note: low-pass filtering before downsampling is the 2D anti-aliasing prefilter ([[Aliasing]]); the pointwise counterpart is [[Histogram equalization]].

**Covered in**: ECE 438 IP.4.B, L28, L30, L31 (Digital Signal Processing/Topic IP.4.B spatial filtering Apr 4, 2025.pdf)
**Sources**: `Digital Signal Processing/Topic IP.4.B spatial filtering Apr 4, 2025.pdf`, `Digital Signal Processing/front page/L28 Apr 2, 2025.pdf`, `Digital Signal Processing/front page/L30 Apr 7, 2025.pdf`, `Digital Signal Processing/front page/L31 Apr 9, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Convolution]] · [[Digital filter]] · [[DTFT]] · [[DFT]] · [[Aliasing]] · [[Histogram equalization]] · [[Wavelet transform]] · [[Image transforms]] · [[LTI system]]
