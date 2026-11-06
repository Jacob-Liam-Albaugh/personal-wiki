---
type: concept
area: dsp
source-ref: "ECE 438 Topic DSP.4.B, DSP.6, IP.4.B"
tags: [signals]
---

# Digital filter

**Summary**: A discrete-time [[LTI system]] used to shape a signal's frequency content, described by its impulse response $h[n]$, frequency response $H(e^{j\omega})$ or transfer function $H(z)$. In this course the main jobs are interpolation, anti-alias prefiltering, and 2D image smoothing and sharpening.

## Descriptions
- Time: $y=h*x$, see [[Convolution]]. FIR if $h$ has finite length; IIR otherwise (DSP.6, p. 7).
- Frequency: $H(e^{j\omega})=H(z)|_{z=e^{j\omega}}$, see [[DTFT]].
- Rational form: $H(z)=\frac{\sum_ib_iz^{-i}}{1+\sum_ka_kz^{-k}}$ from the difference equation; zeros and poles shape the response; poles inside the unit circle for a stable causal filter ([[Z-transform]]).

## Ideal filters used here
> [!definition] Interpolation and decimation filters
> Interpolate by $L$ (after zero insertion):
> $$H(e^{j\omega})=L\ \text{for}\ |\omega|<\pi/L,\ 0\ \text{else}$$
> $$h[n]=\mathrm{sinc}(n/L)$$
> Decimate by $D$ (prefilter): $H=1$ for $|\omega|\le\pi/D$.
> Rate change $L/D$: one filter with gain $L$ and cutoff $\min(\pi/D,\pi/L)$.
>
> (source: Topic DSP.4.B, pp. 2-8)

It is easier to build a good low-pass digitally than in analog, so interpolate by $L$ in DT and use a cheaper CT reconstruction filter (DSP.4.B, p. 1). Ideal filters are non-causal and ring; practical filters trade this off, see [[Aliasing]] and [[Sampling theorem]].

## 2D spatial filters
Linear spatial filtering is 2D convolution with a small kernel $h(k,\ell)$. DC preserving if $\sum h=1$; separable if $h=h_1(k)h_2(\ell)$ (IP.4.B, p. 5). Smoothing kernel $\frac1{16}\begin{bmatrix}1&2&1\\2&4&2\\1&2&1\end{bmatrix}$ has response $\frac12(1+\cos\mu)$ per axis (p. 11); the edge kernel with centre $8/9$ sums to zero. See [[Spatial filtering]].

## Implementation
Direct convolution, or via the [[DFT]]/[[FFT]] with zero padding and overlap-add or overlap-save for long signals (see [[Convolution]]).

**Covered in**: ECE 438 DSP.4.A, DSP.4.B, DSP.6, IP.4.B (filtering content, held on Sampling theorem, Z-transform and Spatial filtering)
**Sources**: `courses/ECE 438/Topic DSP.4.B Sampling DT.pdf`, `courses/ECE 438/Topic DSP.6 z-transforms March 7, 2025.pdf`, `courses/ECE 438/Topic IP.4.B spatial filtering Apr 4, 2025.pdf`, `courses/ECE 438/Topic DSP.4.A Sampling CT.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[LTI system]] · [[Convolution]] · [[Z-transform]] · [[DTFT]] · [[FFT]] · [[Spatial filtering]] · [[Aliasing]] · [[Wavelet transform]] · [[Sampling theorem]]
