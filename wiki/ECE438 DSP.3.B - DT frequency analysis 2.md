---
type: lecture
area: dsp
source-ref: "Topic DSP.3.B, pp. 1-9"
course: ece438
lecture: DSP.3.B
tags: [signals]
---

# ECE438 DSP.3.B - DT frequency analysis 2

**Summary**: Two results about the [[DFT]]: keeping only $m<N$ projections gives the best approximation in the least-squares sense, and the DFT is a matrix multiplication by the symmetric matrix $\mathbf W_N$ of roots of unity.

**File**: `Digital Signal Processing/Topic DSP.3.B DT frequency analysis Part 2 Jan 31, 2025.pdf`

---

## Topics
- **Approximating with fewer basis vectors (pp. 2-4)**: given an orthogonal basis $\{g_k\}$ of $\mathbb C^N$ and $x=\sum_k a_kg_k$, approximate by $\hat x=\sum_{k=1}^m b_kg_k$, $m<N$. Which $b_k$ minimize $\|x-\hat x\|$? How to pick the best basis is not explored.
- **Matrix form (pp. 5-8)**: with $W_N=e^{-j2\pi/N}$ an $N$th root of unity ($W_N^N=1$), analysis and synthesis read
  $$X(k)=\sum_{n=0}^{N-1}x[n]\,W_N^{kn}$$
  $$x[n]=\frac1N\sum_{k=0}^{N-1}X(k)\,W_N^{-kn}$$
- Each term is nonzero in general, so one output needs $N$ complex multiplications and $N-1$ additions; all $N$ outputs need $N^2$ multiplications and $N(N-1)$ additions. This motivates [[ECE438 DSP.3.E - FFT]]. Useful identity: $W_N^{k+N/2}=-W_N^k$.

## Key results
> [!theorem] Truncated projection is the best approximation
> For $\mathcal G=\mathrm{span}\{g_1..g_m\}$, the choice $b_k=a_k=\langle x,g_k\rangle/\langle g_k,g_k\rangle$ minimizes $\|x-\hat x\|$ over $\mathcal G$.
> Proof: $(x-\hat x)\perp\mathcal G$, so for any other $f\in\mathcal G$ Pythagoras gives
> $$\|x-f\|^2=\|x-\hat x\|^2+\|\hat x-f\|^2\ge\|x-\hat x\|^2$$
> The $a_k$ are unique. (source: p. 4)

> [!theorem] DFT matrix
> Let $\mathbf X=\mathbf W_N\mathbf x$ with $[\mathbf W_N]_{kn}=W_N^{kn}$ (symmetric). Then
> $$\mathbf x=\tfrac1N\mathbf W_N^{*}\mathbf X,\qquad \mathbf W_N\mathbf W_N^{*}=N\mathbf I_N$$
> so $\mathbf W_N$ is orthogonal but not quite unitary (it needs the $1/\sqrt N$ scaling). (source: pp. 7-8)

## Examples
> [!example] $N=4$ (p. 9)
> $W_4=-j$, $W_4^2=-1$, $W_4^3=j$, $W_4^4=1$. For $\mathbf x=(0,1,2,3)^T$,
> $$\mathbf X=\mathbf W_4\mathbf x=(6,\;-2+2j,\;2,\;-2-2j)^T$$
> with $\mathbf W_4$ having rows $(1,1,1,1)$, $(1,-j,-1,j)$, $(1,-1,1,-1)$, $(1,j,-1,-j)$.

Wiki note: the third coefficient is $0-1+2-3=-2$ (row $(1,-1,1,-1)$), not $2$ as written on the slide. The exam 1 review gives $-2$ too. See [[DFT]].

## Connections
- Continues [[ECE438 DSP.3.A - DT frequency analysis 1]]. Truncating the basis is the idea behind transform coding in [[ECE438 IP.5 - Image transforms and wavelets]] and [[ECE438 IP.6 - Image compression]].

**Sources**: `Digital Signal Processing/Topic DSP.3.B DT frequency analysis Part 2 Jan 31, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DFT]] · [[FFT]] · [[DTFT]] · [[Fourier transform]] · [[ECE438 DSP.3.C - More on DFT]]
