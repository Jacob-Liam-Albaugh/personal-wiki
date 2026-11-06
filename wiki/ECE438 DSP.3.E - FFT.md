---
type: lecture
area: dsp
source-ref: "Topic DSP.3.E, pp. 1-9"
course: ece438
lecture: DSP.3.E
tags: [signals]
---

# ECE438 DSP.3.E - FFT

**Summary**: The radix-2 decimation-in-time [[FFT]]. Splitting the sum into even and odd samples turns one $N$-point [[DFT]] into two $N/2$-point DFTs plus twiddle factors, and iterating gives $N\log_2 N$ cost.

**File**: `Digital Signal Processing/Topic DSP.3.E the FFT Feb 12, 2025.pdf`

---

## Topics
- **Goal (p. 1)**: implement the FFT. Cost table, $N^2$ versus $N\log N$ (source: p. 1):

| $\log_2 N$ | $N$ | $N^2$ | $N\log N$ |
|---|---|---|---|
| 3 | 8 | 64 | 24 |
| 4 | 16 | 256 | 64 |
| 6 | 64 | 4096 | 384 |
| 8 | 256 | 65536 | 2084 |
| 10 | 1024 | ~1,048,000 | 10240 |

- **Properties of $W_N^{kn}=e^{-j2\pi kn/N}$ to exploit (p. 1)**:
$$W_N^{k(N-n)}=W_N^{-kn}=(W_N^{kn})^*$$
$$W_N^{kn}=W_N^{k(n+N)}=W_N^{(k+N)n}$$
$$W_N^2=W_{N/2}$$
- **Decimation**: decompose $x[n]$ (in time) or $X[k]$ (in frequency) into smaller subsequences. This lecture does decimation in time. Assume $N=2^p$; otherwise zero pad, which only samples the [[DTFT]] more finely (source: p. 1).

## Key results
> [!algorithm] Even/odd split (pp. 2-3)
> Split the DFT sum over even and odd $n$, with $n=2r$ and $n=2r+1$:
> $$X[k]=\sum_{r=0}^{N/2-1}x[2r]\,W_N^{2rk}+W_N^k\sum_{r=0}^{N/2-1}x[2r+1]\,W_N^{2rk}$$
> Since $W_N^{2rk}=W_{N/2}^{rk}$:
> $$X[k]=G[k]+W_N^kH[k]$$
> $G$ is the $N/2$-point DFT of the even samples, $H$ that of the odd samples. $W_N^k$ is the twiddle factor (a linear phase, i.e. a time shift). By itself this changes nothing in operation count.

> [!theorem] Periodicity gives the second half for free (p. 5)
> $G[k]$ and $H[k]$ have period $N/2$:
> $$G[k+N/2]=G[k],\quad H[k+N/2]=H[k]$$
> and $W_N^{k+N/2}=-W_N^k$ because $e^{-j\pi}=-1$. So for $k=0,\dots,N/2-1$:
> $$X[k]=G[k]+W_N^kH[k]$$
> $$X[k+N/2]=G[k]-W_N^kH[k]$$
> The product $W_N^kH[k]$ is reused, so the odd-indexed second half needs no extra multiplies.

> [!algorithm] Butterfly and stages (pp. 6-7)
> Butterfly: add, and subtract, the twiddled odd branch, with one multiply by $W_N^k$. One step reduces an $N$-point DFT to two $N/2$-point DFTs plus $N/2$ complex multiplies. Iterate until a 2-point DFT, $W_2=e^{-j\pi}=-1$, with basis vectors $(1,1)$ and $(1,-1)$. Each stage costs $N/2$ multiplies (some trivial, $W_N^0=1$), and there are $\log_2 N$ stages.

> [!algorithm] Input reordering (p. 8)
> Inputs must be bit-reversed so data flows smoothly. For $N=8$, index $0,1,2,3,4,5,6,7$ is read in the order $0,4,2,6,1,5,3,7$.

> [!theorem] Matrix form (p. 9, not covered in detail)
> $$\mathbf W_N=\begin{bmatrix}I_{N/2}&D_{N/2}\\I_{N/2}&-D_{N/2}\end{bmatrix}\begin{bmatrix}\mathbf W_{N/2}&0\\0&\mathbf W_{N/2}\end{bmatrix}P$$
> $P$ is the even-odd permutation matrix, $I_{N/2}$ the identity, and $D_{N/2}$ is diagonal with entries $1,W_N,\dots,W_N^{N/2-1}$.

## Connections
- Wiki note: the table lists 2084 for $N=256$; $256\cdot 8=2048$. Likely a transcription slip on the sheet.
- The speedup is what makes FFT-based [[Convolution]] practical: [[ECE438 DSP.3.D - Convolution with DFT]].
- Frequency analysis context: [[ECE438 DSP.3.A - DT frequency analysis 1]].

**Sources**: `Digital Signal Processing/Topic DSP.3.E the FFT Feb 12, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[FFT]] · [[DFT]] · [[DTFT]] · [[Fourier transform]] · [[Convolution]] · [[Digital filter]]
