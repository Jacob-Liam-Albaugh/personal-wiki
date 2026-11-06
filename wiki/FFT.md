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
> $G$ and $H$ are $N/2$-point DFTs of the even and odd samples. Periodicity and $W_N^{k+N/2}=-W_N^k$ give the second half for free, for $k<N/2$:
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

## Where it appears
- Lecture notes: [[ECE438 DSP.3.E - FFT]].
- Fast linear [[Convolution]]: [[ECE438 DSP.3.D - Convolution with DFT]]. Image spectra use a 2D FFT: [[ECE438 IP.2 - Aliasing]].

**Sources**: `Digital Signal Processing/Topic DSP.3.E the FFT Feb 12, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DFT]] · [[DTFT]] · [[Fourier transform]] · [[Convolution]] · [[Digital filter]] · [[Spectral leakage]]
