---
type: method
area: dsp
source-ref: "ECE 438 Topic DSP.3.E, pp. 1-9"
tags: [signals]
---

# FFT

**Summary**: The fast Fourier transform computes the [[DFT]] in $O(N\log N)$ instead of $O(N^2)$ by splitting the sum into even and odd samples recursively. It is what makes [[Convolution]] by DFT, spectrum analysis and 2D transforms practical.

> [!algorithm] Radix-2 decimation in time
> Assume $N=2^p$ (else zero pad). With $W_N^2=W_{N/2}$,
> $$X[k]=G[k]+W_N^kH[k]$$
> $G$ and $H$ are $N/2$-point DFTs of the even and odd samples. Periodicity ($G[k+N/2]=G[k]$, $H[k+N/2]=H[k]$) and $W_N^{k+N/2}=-W_N^k$ give the second half for free, for $k<N/2$:
> $$X[k+N/2]=G[k]-W_N^kH[k]$$
>
> (source: Topic DSP.3.E, pp. 1-5)

- Butterfly: one multiply by the twiddle factor $W_N^k$, one add, one subtract. Iterate down to 2-point DFTs, $W_2=-1$ (pp. 6-7).
- Each stage costs about $N/2$ complex multiplies over $\log_2N$ stages, so $N\log_2N$ overall. Direct DFT needs $N^2$ multiplies and $N(N-1)$ additions (DSP.3.B, p. 8).
- Inputs are read in bit-reversed order, for $N=8$: $0,4,2,6,1,5,3,7$ (p. 8).
- Matrix form: $\mathbf W_N$ factors into a diagonal-twiddle butterfly matrix, two $\mathbf W_{N/2}$ blocks and an even-odd permutation (p. 9).

| $N$ | $N^2$ | $N\log_2N$ |
|---|---|---|
| 8 | 64 | 24 |
| 64 | 4096 | 384 |
| 1024 | about 1.05 million | 10240 |

Wiki note: the sheet's table prints 2084 for $N=256$; $256\cdot8=2048$.

Zero padding to a power of two only samples the [[DTFT]] more finely, it does not add information (p. 1).

## Twiddle-factor identities and derivation
With $W_N^{kn}=e^{-j2\pi kn/N}$ the properties exploited are (source: Topic DSP.3.E, p. 1):
$$W_N^{k(N-n)}=W_N^{-kn}=(W_N^{kn})^*$$
$$W_N^{kn}=W_N^{k(n+N)}=W_N^{(k+N)n}$$
$$W_N^2=W_{N/2}$$
Decimation decomposes $x[n]$ (in time) or $X[k]$ (in frequency) into smaller subsequences; this derivation is decimation in time.

Even/odd split with $n=2r$ and $n=2r+1$ (source: Topic DSP.3.E, pp. 2-3):
$$X[k]=\sum_{r=0}^{N/2-1}x[2r]W_N^{2rk}+W_N^k\sum_{r=0}^{N/2-1}x[2r+1]W_N^{2rk}$$
and $W_N^{2rk}=W_{N/2}^{rk}$ gives $X[k]=G[k]+W_N^kH[k]$. The twiddle factor $W_N^k$ is a linear phase, i.e. a time shift. By itself the split changes nothing in operation count; the saving comes from $G[k+N/2]=G[k]$, $H[k+N/2]=H[k]$ and $W_N^{k+N/2}=-W_N^k$ (because $e^{-j\pi}=-1$), so $W_N^kH[k]$ is computed once and reused for $X[k+N/2]$ (p. 5). The 2-point base case has $W_2=-1$ and basis vectors $(1,1)$, $(1,-1)$.

> [!theorem] Matrix factorization
> $$\mathbf W_N=\begin{bmatrix}I_{N/2}&D_{N/2}\\I_{N/2}&-D_{N/2}\end{bmatrix}\begin{bmatrix}\mathbf W_{N/2}&0\\0&\mathbf W_{N/2}\end{bmatrix}P$$
> $P$ is the even-odd permutation matrix, $I_{N/2}$ the identity, and $D_{N/2}$ is diagonal with entries $1,W_N,\dots,W_N^{N/2-1}$.
>
> (source: Topic DSP.3.E, p. 9, not covered in detail)

Fast linear [[Convolution]] by overlap-add and overlap-save relies on this speedup. Image spectra use a 2D FFT; see [[Aliasing]] for the display recipe.

**Covered in**: ECE 438 DSP.3.E (Topic DSP.3.E the FFT); Topic DSP.3.B cost count
**Sources**: `courses/ECE 438/Topic DSP.3.E the FFT Feb 12, 2025.pdf`, `courses/ECE 438/Topic DSP.3.B DT frequency analysis Part 2 Jan 31, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DFT]] · [[DTFT]] · [[Fourier transform]] · [[Convolution]] · [[Digital filter]] · [[Spectral leakage]] · [[Aliasing]]
