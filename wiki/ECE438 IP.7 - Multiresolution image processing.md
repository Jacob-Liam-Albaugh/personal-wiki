---
type: lecture
area: dsp
source-ref: "Digital Signal Processing/Topic IP.7 Multiresolution image processing Apr 18, 2025.pdf (ECE 438 handwritten slides)"
course: ece438
lecture: IP.7
tags: [signals]
---

# ECE438 IP.7 - Multiresolution image processing

**Summary**: Gaussian and Laplacian pyramids, space/frequency tiling, and the two-channel dyadic filter bank with its z-domain aliasing and distortion conditions (the route to wavelets).

**File**: `Digital Signal Processing/Topic IP.7 Multiresolution image processing Apr 18, 2025.pdf`

---

## Topics
- Motivation: objects do not appear at a fixed pixel size; appearance depends on distance and object size (source: Topic IP.7 Multiresolution image processing Apr 18, 2025.pdf, p. 1).
- Angular frequency (p. 2).
- Gaussian pyramid, REDUCE and EXPAND (p. 3-6).
- Laplacian pyramid (p. 6).
- Space/frequency tiling and dyadic filter banks (p. 7-10).
- z-domain analysis: no-aliasing and no-distortion constraints (p. 11-14).
- Applications named: compression, denoising, edge/feature extraction (not covered in depth) (p. 1).

## Key results

> [!definition] Angular frequency
> An eye or camera at distance $d$ sees an object of height $h$ at angle $\theta$:
> $$\tan(\theta/2) = \frac{h/2}{d}$$
> $$\theta = 2\tan^{-1}\frac{h}{2d} \approx \frac{h}{d}\quad(\theta\text{ small})$$
> For content at $f_s$ cycles per picture height, the visual frequency is
> $$f_\theta \approx \frac{f_s}{\theta} = \frac{\pi d}{180\,h}\,f_s$$
> so frequencies seen by the eye depend on distance and size (p. 2).

> [!algorithm] Gaussian pyramid (Burt and Adelson 1981)
> Make several versions of an image at different resolutions by iterating two steps: smooth with a Gaussian filter, then downsample by 2. Details get blurred at each level; $g_0$ is the original, $g_1,g_2,\dots$ follow.
> To save computation, filter only the pixels retained:
> $$g_{\ell+1} = \mathrm{REDUCE}(g_\ell) = \sum_i\sum_j h(m,n)\,g_\ell(2i-m,\,2j-n)$$
> Typical constraints on $h$: separable, symmetric, DC preserving.
> Drawn as a pyramid of sizes $N\times N$, $\tfrac N2\times\tfrac N2$, $\tfrac N4\times\tfrac N4$; it needs $4/3$ as many values as the original image (p. 3-4).
> REDUCE shows which lower-level pixels form an upper-level pixel. Uses: hierarchical edge detection, feature extraction, SIFT (p. 5).

> [!algorithm] Laplacian pyramid
> Built on the Gaussian pyramid but stores differences between adjacent levels instead of smoothed images:
> $$L_\ell = g_\ell - \mathrm{EXPAND}(g_{\ell+1})$$
> $L_\ell$ holds the details missing from $g_{\ell+1}$. Many values are zero or small, so bits can be reduced.
> EXPAND interpolates the lower level (higher resolution) from the upper (lower resolution) level; for a 5x5 filter it uses neighbouring coarse pixels at the missing positions.
> Reconstruct:
> $$g_\ell = L_\ell + \mathrm{EXPAND}(g_{\ell+1})$$
> (p. 5-6).

> [!definition] Space/frequency tiling (1-D, conceptual)
> A pixel-domain representation is exact in space, with no frequency information. A transform-domain representation is exact in frequency but not in space. One cannot be precise in both. Block-based coding gains some spatial localisation.
> A dyadic filter bank tiles the plane with narrow-in-space cells at high frequency and wide-in-space cells at low frequency: precise low-frequency measurement needs many samples, while a few pixels suffice to flag a big change (p. 7-9).
> Example: pixel-domain analysis shows where a signal changed rapidly, Fourier shows high frequencies exist but not where, wavelets give both better (p. 8).

> [!algorithm] Two-channel filter bank
> $x[n]$ goes through analysis filters $H_0$ (low pass) and $H_1$ (high pass), each followed by $\downarrow2$, then $\uparrow2$ and synthesis filters $G_0$, $G_1$, summed to $\hat x[n]$. All filters FIR.
> For images, apply separably, rows then columns, giving subbands LL (blurry image), LH (horizontal details), HL (vertical details), HH (diagonal details) (p. 9).
> The cascade applies the bank recursively to the low-pass branch. It is a complete representation: exactly as many samples as the original. The lowest branch is an image; the others are difference images (p. 10).
> Haar example: $H_0=[1\ \ 1]^T$, $H_1=[1\ -1]^T$; the cascade applies step-shaped basis functions at successively higher scales (p. 10).

> [!theorem] Perfect reconstruction conditions
> Up and down sampling in z:
> $$X_u(z) = X_d(z^L)$$
> $$X_d(z) = \frac1D\sum_{r=0}^{D-1}X\big(z^{1/D}e^{-j2\pi r/D}\big)$$
> With $L=D=2$, combined down/up sampling gives
> $$X_u(z) = \tfrac12\big[X(z)+X(-z)\big]$$
> The full bank:
> $$\hat X(z) = \tfrac12\big[G_0H_0+G_1H_1\big]X(z)$$
> $$\qquad+\ \tfrac12\big[G_0(z)H_0(-z)+G_1(z)H_1(-z)\big]X(-z)$$
> The first term is distortion, the second aliasing. Allowing a delay, $\hat x[n]=x[n-\ell]$:
> - No aliasing: $G_0(z)H_0(-z)+G_1(z)H_1(-z)=0$.
> - No distortion: $G_0(z)H_0(z)+G_1(z)H_1(z)=2z^{-\ell}$.
> One alias-cancelling choice: $G_0(z)=H_1(-z)$ and $G_1(z)=-H_0(-z)$, so for given $H_0$, $H_1$ the $G$s are prescribed. With $H_0=[a\ b\ c]$, $H_1=[p\ q\ r\ s\ t]$ this gives $G_0=[p\ -q\ r\ -s\ t]$ and $G_1=[a\ -b\ c]$.
> Then with $P_0(z)=H_0(z)G_0(z)$ the no-distortion condition becomes
> $$P_0(z)-P_0(-z) = 2z^{-\ell}$$
> a single constraint on $P_0$, plus the $G_0$-$H_1$ and $G_1$-$H_0$ relations. Beyond this, $P_0$ can be chosen for zero phase (symmetric), simple $\pm1$ values, orthogonality, and so on (p. 11-14).
> Good choices: $H_0$ low pass and $H_1$ high pass, hence $G_1$ low pass and $G_0$ high pass.

## Examples
> [!example] Space/frequency intuition (p. 8)
> $f[n]$ with a short burst: pixel-domain analysis locates the burst but not its frequency; Fourier analysis shows high frequency but not where; the wavelet filter bank gives both, better.

> [!example] Haar filter bank (p. 10)
> The Haar wavelet seen in [[ECE438 IP.5 - Image transforms and wavelets]] arises as $H_0=[1\ 1]^T$, $H_1=[1\ -1]^T$ in the cascade.

## Connections
- Down- and up-sampling in the z-domain reuse [[ECE438 DSP.4.B - Sampling DT]] and [[ECE438 DSP.6 - z-transforms]] ([[Z-transform]]); the aliasing term is [[Aliasing]] from decimation.
- The Gaussian filter and DC-preserving constraint come from [[ECE438 IP.4.B - Spatial filtering]] and [[Spatial filtering]].
- Haar and JPEG-2000 wavelets: [[Wavelet transform]], [[ECE438 IP.5 - Image transforms and wavelets]], [[ECE438 IP.6 - Image compression]].
- Wiki note: the filter bank is a [[Digital filter]] structure; the time-frequency tradeoff echoes [[Spectral leakage]] and window length.

**Sources**: Digital Signal Processing/Topic IP.7 Multiresolution image processing Apr 18, 2025.pdf
**Last updated**: 2026-11-06

---

## Related pages
[[Wavelet transform]] | [[ECE438 IP.5 - Image transforms and wavelets]] | [[ECE438 IP.6 - Image compression]] | [[Aliasing]] | [[Z-transform]] | [[Digital filter]] | [[Spatial filtering]] | [[ECE438 IP.4.B - Spatial filtering]]
