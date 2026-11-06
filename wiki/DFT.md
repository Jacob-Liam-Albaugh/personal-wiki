---
type: definition
area: dsp
source-ref: "ECE 438 Topic DSP.3.A-3.D; exam 1 review"
tags: [signals]
---

# DFT

**Summary**: The discrete Fourier transform maps $N$ samples to $N$ frequency coefficients. It is a change of basis to complex sinusoids, a matrix multiplication, and samples of the [[DTFT]] of the same data. [[FFT]] computes it fast.

## Definition
> [!definition] DFT pair
> With $W_N=e^{-j2\pi/N}$ and $k,n=0,\dots,N-1$:
> $$X(k)=\sum_{n=0}^{N-1}x(n)\,W_N^{kn}$$
> $$x(n)=\frac1N\sum_{k=0}^{N-1}X(k)\,W_N^{-kn}$$
>
> (source: Topic DSP.3.A, p. 2; DSP.3.B, pp. 5-8)

The DTFS coefficients of ECE 301 are the same up to a $1/N$ factor, but the DFT is applied to any signal (DSP.3.A, p. 2).

## Why it works
> [!theorem] Orthogonality
> The vectors $s_k[n]=e^{j2\pi kn/N}$ satisfy $\langle s_k,s_l\rangle=N\delta_{kl}$. So $X(k)=\langle x,s_k\rangle$ are projection coefficients, and the DFT is a change of coordinates from the sample basis to the sinusoid basis. (source: Topic DSP.3.A, pp. 10-12)

Keeping only $m<N$ coefficients gives the best least-squares approximation, the idea behind transform coding (DSP.3.B, p. 4).

## Matrix form
> [!theorem] DFT matrix
> $$\mathbf X=\mathbf W_N\mathbf x,\qquad \mathbf x=\tfrac1N\mathbf W_N^{*}\mathbf X$$
> $\mathbf W_N$ is symmetric, $[\mathbf W_N]_{kn}=W_N^{kn}$, and $\mathbf W_N\mathbf W_N^*=N\mathbf I$. Orthogonal columns but not unitary without a $1/\sqrt N$ scale.
>
> (source: Topic DSP.3.B, pp. 7-8)

> [!example] Exam 1 review: 4-point DFT as a matrix
> $\mathbf W_4$ has rows $(1,1,1,1)$, $(1,-j,-1,j)$, $(1,-1,1,-1)$, $(1,j,-1,-j)$. For $\mathbf x=(0,1,2,3)^T$:
> $$\mathbf X=(6,\ -2+2j,\ -2,\ -2-2j)^T$$
> The inverse $\mathbf x=\frac14\mathbf W_4^*\mathbf X$ returns $(0,1,2,3)^T$; row 1 gives $\frac14(6-2+2j-2-2-2j)=0$ and row 2 gives $\frac14\cdot4=1$. The matrix is fixed for a given $N$.
>
> (source: exam_1_review_transcribed.pdf, pp. 3-5)

Wiki note: Topic DSP.3.B, p. 9, lists the third coefficient of this same example as $2$; the exam review and direct computation ($0-1+2-3$) give $-2$. The review itself notes its answer differs slightly from the notes.

## Relation to the DTFT
Truncate to $N$ samples and sample $\omega_k=2\pi k/N$: that is the DFT of the truncated signal (DSP.3.C, p. 3). A sinusoid not at a bin frequency spreads over every bin, see [[Spectral leakage]]. Zero padding samples the same DTFT more densely and does not remove leakage.

Product of DFTs is circular convolution; zero pad to $N\ge L+K-1$ for linear (DSP.3.D, pp. 3-6), see [[Convolution]].

**Sources**: `Digital Signal Processing/Topic DSP.3.A DT frequency analysis Part 1 Jan 31, 2025.pdf`, `Digital Signal Processing/Topic DSP.3.B DT frequency analysis Part 2 Jan 31, 2025.pdf`, `Digital Signal Processing/Topic DSP.3.C more on DFT Feb 2, 2025.pdf`, `Digital Signal Processing/Topic DSP.3.D Convolution with DFT Feb 9, 2025.pdf`, `Digital Signal Processing/exam_1_review_transcribed.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 DSP.3.A - DT frequency analysis 1]] · [[ECE438 DSP.3.B - DT frequency analysis 2]] · [[ECE438 DSP.3.C - More on DFT]] · [[ECE438 DSP.3.D - Convolution with DFT]]
- [[FFT]] · [[DTFT]] · [[Fourier transform]] · [[Spectral leakage]] · [[Convolution]] · [[Z-transform]] · [[Digital filter]]
- [[Principal component analysis]] · [[Karhunen-Loève expansion]]
