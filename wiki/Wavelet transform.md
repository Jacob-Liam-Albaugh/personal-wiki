---
type: concept
area: math
areas: [math, ml]
source-ref: "Strang 1993, §1-5"
tags: [signals]
---

# Wavelet transform

**Summary**: Expansion of a signal in an orthogonal basis built from translations and dilations of one function. Unlike sines and cosines, the basis functions are local, so coefficients reflect structure in space or time as well as scale.

---

## Definition

Choose a scaling function $\phi$ and a wavelet $W$. The basis is

$$W_{jk}(x)=W(2^jx-k)$$

and the transform maps $f$ to its coefficients $b_{jk}$ in this basis. The simplest case is the Haar wavelet (source: Strang 1993, §1, p. 2).

## Multiresolution

Nested spaces $V_j\subset V_{j+1}$ with $V_{j+1}=V_j\oplus W_j$. The wavelet space $W_j$ holds the detail lost in going from level $j+1$ to $j$ (source: Strang 1993, §3).

The scaling function satisfies the dilation equation

$$\phi(x)=\sum_kc_k\,\phi(2x-k)$$

and the wavelet reuses the $c_k$ with alternating signs (source: Strang 1993, eqs. 7-8).

## Why use it

- Local basis: a signal that vanishes beyond some point only involves the basis functions that reach it (source: Strang 1993, p. 2).
- Fast: the fast wavelet transform is $O(n)$, against $O(n\log n)$ for the [[FFT]] (source: Strang 1993, p. 4).
- Approximation order: Daubechies wavelets with $2p$ coefficients reproduce polynomials up to degree $p-1$, with error $O(h^p)$ (source: Strang 1993, eq. 14).
- Compression: coefficients are mostly near zero for a good basis. Wavelets compete with the Fourier-based JPEG standard (source: Strang 1993, §6).

## Versus Fourier

| | Fourier | Wavelet |
|---|---|---|
| Support | global | local |
| Cost | $\tfrac12 n\log_2n$ | $O(n)$ |
| Strength | exact frequency | position and scale |
| Weakness | local features need many terms | smooth functions need high order |

Wiki note: this table condenses the paper's discussion; the cost figures are from the paper (pp. 3-4).

## Appearance elsewhere

Wiki note: the multiscale idea shows up in [[Group equivariant CNNs (Cohen 2016)]] only by analogy, as another way of building structure into a basis. The Karhunen-Loève basis ([[Karhunen-Loève expansion]]) is the data-adapted counterpart of a fixed basis like wavelets.

## Multiresolution image processing
Objects do not appear at a fixed pixel size; appearance depends on distance and object size. Applications include compression, denoising and edge or feature extraction (source: Topic IP.7 Multiresolution image processing Apr 18, 2025.pdf, p. 1).

> [!definition] Angular frequency
> An eye or camera at distance $d$ sees an object of height $h$ at angle $\theta$:
> $$\tan(\theta/2)=\frac{h/2}{d},\qquad\theta=2\tan^{-1}\frac h{2d}\approx\frac hd$$
> Content at $f_s$ cycles per picture height has visual frequency
> $$f_\theta\approx\frac{f_s}{\theta}=\frac{\pi d}{180\,h}\,f_s$$
> so frequencies seen by the eye depend on distance and size.
>
> (source: IP.7, p. 2)

> [!algorithm] Gaussian pyramid (Burt and Adelson 1981)
> Iterate: smooth with a Gaussian filter, then downsample by 2; $g_0$ is the original and each level is blurrier. Filter only the retained pixels:
> $$g_{\ell+1}=\mathrm{REDUCE}(g_\ell)=\sum_i\sum_jh(m,n)\,g_\ell(2i-m,\,2j-n)$$
> Typical constraints on $h$: separable, symmetric, DC preserving (see [[Spatial filtering]]). Sizes $N\times N,\ \tfrac N2\times\tfrac N2,\dots$ need $4/3$ as many values as the image. Uses: hierarchical edge detection, feature extraction, SIFT.
>
> (source: IP.7, pp. 3-5; L39 Apr 30, 2025.pdf, p. 1)

> [!algorithm] Laplacian pyramid
> Store differences between adjacent Gaussian levels:
> $$L_\ell=g_\ell-\mathrm{EXPAND}(g_{\ell+1}),\qquad g_\ell=L_\ell+\mathrm{EXPAND}(g_{\ell+1})$$
> $L_\ell$ holds the detail missing from $g_{\ell+1}$; many values are zero or small, so bits can be saved. EXPAND interpolates the finer level from the coarser (a 5x5 filter uses neighbouring coarse pixels at the missing positions). The result is one blurry image plus many difference images. Gaussian and Laplacian pyramids are both overcomplete.
>
> (source: IP.7, pp. 5-6; L39, p. 1)

> [!definition] Space/frequency tiling
> A pixel-domain representation is exact in space with no frequency information; a transform-domain one is exact in frequency but not in space. Block coding gains some localisation. A dyadic filter bank tiles the plane with narrow-in-space cells at high frequency and wide cells at low frequency: precise low-frequency measurement needs many samples, while a few pixels suffice to flag a big change.
>
> (source: IP.7, pp. 7-9)

> [!example] Space/frequency intuition
> For $f[n]$ with a short burst, pixel-domain analysis locates the burst but not its frequency, Fourier analysis shows high frequency but not where, and the wavelet filter bank gives both, better (IP.7, p. 8). The tradeoff echoes [[Spectral leakage]] and window length.

> [!algorithm] Two-channel filter bank
> $x[n]$ passes through analysis filters $H_0$ (low pass) and $H_1$ (high pass), each followed by $\downarrow2$, then $\uparrow2$ and synthesis filters $G_0,G_1$, summed to $\hat x[n]$. All filters FIR ([[Digital filter]]). For images apply it separably, rows then columns, giving subbands LL (blurry image), LH (horizontal detail), HL (vertical detail) and HH (diagonal detail). The cascade recurses on the low-pass branch; it is a complete representation with exactly as many samples as the original (the lowest branch is an image, the others difference images). Haar: $H_0=[1\ \ 1]^T$, $H_1=[1\ -1]^T$, giving step-shaped basis functions at successively higher scales (see [[Image transforms]]).
>
> (source: IP.7, pp. 9-10; L38 Apr 28, 2025.pdf, p. 1)

> [!theorem] Perfect reconstruction conditions
> Up and down sampling in z (reusing [[Sampling theorem]] and [[Z-transform]]):
> $$X_u(z)=X_d(z^L),\qquad X_d(z)=\frac1D\sum_{r=0}^{D-1}X\big(z^{1/D}e^{-j2\pi r/D}\big)$$
> With $L=D=2$, down then up gives $\tfrac12[X(z)+X(-z)]$. The full bank:
> $$\hat X(z)=\tfrac12\big[G_0H_0+G_1H_1\big]X(z)+\tfrac12\big[G_0(z)H_0(-z)+G_1(z)H_1(-z)\big]X(-z)$$
> The first term is distortion, the second aliasing (see [[Aliasing]]). Allowing a delay, $\hat x[n]=x[n-\ell]$:
> - No aliasing: $G_0(z)H_0(-z)+G_1(z)H_1(-z)=0$.
> - No distortion: $G_0(z)H_0(z)+G_1(z)H_1(z)=2z^{-\ell}$.
> One alias-cancelling choice is $G_0(z)=H_1(-z)$, $G_1(z)=-H_0(-z)$; for $H_0=[a\ b\ c]$ and $H_1=[p\ q\ r\ s\ t]$ this gives $G_0=[p\ -q\ r\ -s\ t]$ and $G_1=[a\ -b\ c]$. With $P_0(z)=H_0(z)G_0(z)$ the no-distortion condition becomes
> $$P_0(z)-P_0(-z)=2z^{-\ell}$$
> a single constraint on $P_0$, which can further be chosen for zero phase (symmetric), simple $\pm1$ values, orthogonality, and so on. Good choices: $H_0$ low pass and $H_1$ high pass, hence $G_1$ low pass and $G_0$ high pass.
>
> (source: IP.7, pp. 11-14)

Compression with wavelets (JPEG-2000) is on [[Image compression]].



**Covered in**: ECE 438 IP.7, L38-L40 (Digital Signal Processing/Topic IP.7 Multiresolution image processing Apr 18, 2025.pdf)
**Sources**: Strang, Bull. AMS 1993, Digital Signal Processing/Topic IP.7 Multiresolution image processing Apr 18, 2025.pdf, `Digital Signal Processing/front page/L38 Apr 28, 2025.pdf`, `Digital Signal Processing/front page/L39 Apr 30, 2025.pdf`, `Digital Signal Processing/front page/L40 May 2, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Wavelets vs Fourier (Strang 1993)]] · [[Fourier transform]] · [[FFT]] · [[DFT]] · [[Convolution]] · [[Karhunen-Loève expansion]] · [[Digital filter]] · [[Spatial filtering]] · [[Image compression]] · [[Image transforms]] · [[Aliasing]] · [[Z-transform]]
