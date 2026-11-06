---
type: lecture
area: dsp
source-ref: "Topic DSP.3.D, pp. 1-8"
course: ece438
lecture: DSP.3.D
tags: [signals]
---

# ECE438 DSP.3.D - Convolution with DFT

**Summary**: Computing a linear [[Convolution]] through the [[DFT]]. Multiplying DFTs gives circular convolution, which equals linear convolution only after zero padding; long signals are handled in chunks by overlap-add or overlap-save.

**File**: `Digital Signal Processing/Topic DSP.3.D Convolution with DFT Feb 9, 2025.pdf`

---

## Topics
- **DTFT convolution theorem (p. 2)**: $x_1[n]*x_2[n]\leftrightarrow X_1(e^{j\omega})X_2(e^{j\omega})$, "linear" or "aperiodic" convolution. For an [[LTI system]], $y=\mathcal F^{-1}\{XH\}$, but the DTFT is continuous in $\omega$ so it cannot be evaluated directly on a computer. Using the DFT instead is "not necessarily" correct.
- **DFT convolution theorem (p. 3)**: product of DFTs corresponds to circular (periodic, cyclic) convolution, with the dual property for products in time.
- **Zero padding (p. 6)** and **chunked processing (pp. 7-8)**.

## Key results
> [!theorem] DFT convolution theorem
> $$x_1[n]\circledast x_2[n]=\sum_{k=0}^{N-1}x_1[k]\,x_2[(n-k)\bmod N]\;\leftrightarrow\;X_1[k]X_2[k]$$
> $$x_1[n]x_2[n]\;\leftrightarrow\;\tfrac1N X_1[k]\circledast X_2[k]$$
> The circular sum depends on $N$. Simplest picture: periodically extend one sequence and do an ordinary convolution over one interval of length $N$. (source: p. 3)

> [!theorem] Zero padding makes circular equal linear
> If $x$ has length $L$ and $h$ has length $K$, pad both to length $N\ge L+K-1$. Then there is no overlap/corruption and circular convolution equals linear convolution. Recipe: zero pad $x$ and $h$, take DFTs, multiply, inverse DFT. This works for any length but is not real-time, since it needs memory and delay to store the whole signal. (source: p. 6)

> [!algorithm] Overlap-add (p. 7)
> Split $x$ into non-overlapping chunks $x_r[n]$ of length $L$ (nonzero for $rL\le n<(r+1)L$). Then $y=\sum_r x_r*h$, and each $x_r*h$ has $L+K-1$ nonzero samples, so neighbouring outputs overlap in $K-1$ samples that are added. For each chunk: zero pad $x_r$ and $h$ (the DFT of $h$ is computed once), multiply, inverse DFT, add to the stored output, output and discard $L$ elements, store $K-1$.

> [!algorithm] Overlap-save (p. 8)
> Split into overlapping (longer) chunks, $rL\le n<(r+1)L+K$. Apply circular convolution with no zero padding. Part of each result (the end) is valid and part (the beginning) is corrupted by wrap-around; discard the corrupted part and output the valid part. The notes give a quick overview and point to the textbook.

## Examples
> [!example] Circular vs linear, $N=5$ (pp. 4-6)
> $x[n]=1$ for $0\le n\le3$, $0$ for $n=4$; $h[n]=1$ for $0\le n\le2$, $0$ for $n=3,4$; both periodic with $N=5$. Circular convolution (computed $n=0,1$ graphically, then $2,3,4$):
> $$y[n]=\begin{cases}2&n=0,1,4\\3&n=2,3\end{cases}$$
> The linear convolution is a triangular pulse (two rectangles convolved), which differs only at the wrap-around, "the beginning, for $n=0$". Wiki note: the full linear result has $L+K-1=6$ samples, $1,2,3,3,2,1$; the sheet lists values up to $n=4$ and plots a small tail at $n=5$.

## Connections
- Complexity of the underlying DFT is addressed in [[ECE438 DSP.3.E - FFT]]; the time-domain method is in [[ECE438 DSP.2 - DT systems]].
- Practical filtering with these methods: [[Digital filter]].

**Sources**: `Digital Signal Processing/Topic DSP.3.D Convolution with DFT Feb 9, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Convolution]] · [[DFT]] · [[DTFT]] · [[FFT]] · [[LTI system]] · [[Digital filter]]
