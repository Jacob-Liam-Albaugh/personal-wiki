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

## Related / multiresolution lectures
- Course treatment: [[ECE438 IP.7 - Multiresolution image processing]], [[ECE438 L38 - Gaussian and Laplacian pyramids]], [[ECE438 L39 - Dyadic filter banks and wavelets]], [[ECE438 L40 - Wavelets and images, final exam logistics]]; filtering background in [[Digital filter]]. (source: Digital Signal Processing/Topic IP.7 Multiresolution image processing Apr 18, 2025.pdf)

**Sources**: Strang, Bull. AMS 1993.
**Last updated**: 2026-11-06

---

## Related pages
- [[Wavelets vs Fourier (Strang 1993)]]
- [[Fourier transform]]
- [[FFT]]
- [[DFT]]
- [[Convolution]]
- [[Karhunen-Loève expansion]]
