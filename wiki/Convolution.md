---
type: definition
area: dsp
source-ref: "ECE 438 Topic DSP.2, DSP.3.D; exam 1 review; ECE 301 equation sheet"
tags: [signals]
---

# Convolution

**Summary**: The operation that gives the output of an [[LTI system]] from its input and impulse response. It becomes a product under the [[Fourier transform]], [[DTFT]] and [[Z-transform]], and a circular convolution under the [[DFT]]. In 2D it is [[Spatial filtering]].

## Definition
> [!definition] Convolution sum
> $$(x*h)[n]=\sum_{k=-\infty}^{\infty}x[k]\,h[n-k]$$
> Commutative: $x*h=h*x$. (source: Topic DSP.2, p. 9)

Recipe (DSP.2, p. 11): flip and shift one signal, write the other as a function of $k$, find the overlap regions as $n$ varies, sum in each region with its own bounds. For finite-duration signals of lengths $L$ and $K$ the result has $L+K-1$ samples.

## Transform-domain forms
| Domain | Convolution becomes |
|---|---|
| [[DTFT]] | $X_1(e^{j\omega})X_2(e^{j\omega})$ |
| [[Z-transform]] | $X(z)H(z)$, ROC at least $R_1\cap R_2$ |
| [[Fourier transform]] (CT) | $X(j\omega)Y(j\omega)$ |
| [[DFT]] | circular convolution, $X_1[k]X_2[k]$ |

(source: Topic DSP.3.D, pp. 2-3; ece301final_equation-sheet.pdf, pp. 5, 7; Topic DSP.6, p. 12)

> [!theorem] Linear from circular
> Pad both sequences with zeros to length $N\ge L+K-1$, then circular equals linear. Long inputs use overlap-add or overlap-save. (source: Topic DSP.3.D, pp. 6-8)

## Examples
> [!example] Exam 1 review: finite-duration convolution
> $x=\{2,3,1\}$ and $h=\{1,-2,3\}$ on $n=0,1,2$. The output is nonzero from $n=0$ to $4$. Sum bounds for fixed $n$:
> $$y[n]=\sum_{k=\max(0,n-2)}^{\min(n,2)}x[k]\,h[n-k]$$
> Result: $y=\{2,\,-1,\,1,\,7,\,3\}$ for $n=0..4$.
> Check: $y[3]=3\cdot3+1\cdot(-2)=7$ and $y[4]=1\cdot3=3$.
>
> (source: exam_1_review_transcribed.pdf, pp. 10-11)

> [!example] Convolution of $u[n]$ with $2^{-|n|}$
> $y[n]=2^{n+1}$ for $n\le0$ and $3-2^{-n}$ for $n>0$. (source: Topic DSP.2, pp. 11-13)

CT convolution uses the same flip-and-shift rules as the time transformations on [[Discrete-time signal]].

## Circular convolution
> [!theorem] DFT convolution theorem
> $$x_1[n]\circledast x_2[n]=\sum_{k=0}^{N-1}x_1[k]\,x_2[(n-k)\bmod N]\;\leftrightarrow\;X_1[k]X_2[k]$$
> $$x_1[n]x_2[n]\;\leftrightarrow\;\tfrac1N X_1[k]\circledast X_2[k]$$
> The circular sum depends on $N$. Simplest picture: periodically extend one sequence and do an ordinary convolution over one interval of length $N$.
>
> (source: Topic DSP.3.D, p. 3)

The DTFT theorem $x_1*x_2\leftrightarrow X_1X_2$ gives "linear" convolution, so $y=\mathcal F^{-1}\{XH\}$ for an [[LTI system]], but the DTFT is continuous in $\omega$ and cannot be evaluated directly on a computer. Using the DFT instead is not necessarily correct unless the signals are zero padded (source: Topic DSP.3.D, p. 2).

Zero padding recipe: pad $x$ (length $L$) and $h$ (length $K$) to $N\ge L+K-1$, take DFTs, multiply, inverse DFT. It works for any length but is not real-time, since it needs memory and delay to hold the whole signal (source: Topic DSP.3.D, p. 6). The cost of the underlying transform is addressed by the [[FFT]].

> [!algorithm] Overlap-add
> Split $x$ into non-overlapping chunks $x_r[n]$ of length $L$ (nonzero for $rL\le n<(r+1)L$). Then $y=\sum_rx_r*h$, and each $x_r*h$ has $L+K-1$ nonzero samples, so neighbouring outputs overlap in $K-1$ samples that are added. For each chunk: zero pad $x_r$ and $h$ (the DFT of $h$ is computed once), multiply, inverse DFT, add to the stored output, output and discard $L$ elements, store $K-1$.
>
> (source: Topic DSP.3.D, p. 7)

> [!algorithm] Overlap-save
> Split into overlapping, longer chunks, $rL\le n<(r+1)L+K$. Apply circular convolution with no zero padding. The end of each result is valid and the beginning is corrupted by wrap-around; discard the corrupted part and output the valid part.
>
> (source: Topic DSP.3.D, p. 8)

> [!example] Circular vs linear, $N=5$
> $x[n]=1$ for $0\le n\le3$, $0$ for $n=4$; $h[n]=1$ for $0\le n\le2$, $0$ for $n=3,4$; both periodic with $N=5$. Circular convolution (computed for $n=0,1$ graphically, then $2,3,4$):
> $$y[n]=\begin{cases}2&n=0,1,4\\3&n=2,3\end{cases}$$
> The linear convolution is a triangular pulse (two rectangles convolved) and differs only at the wrap-around. The full linear result has $L+K-1=6$ samples, $1,2,3,3,2,1$; the sheet lists values up to $n=4$ and plots a small tail at $n=5$.
>
> (source: Topic DSP.3.D, pp. 4-6)

**Covered in**: ECE 438 DSP.3.D (Topic DSP.3.D Convolution with DFT); convolution recipe from DSP.2
**Sources**: `Digital Signal Processing/Topic DSP.2 DT systems UPDATED Jan 22, 2025.pdf`, `Digital Signal Processing/Topic DSP.3.D Convolution with DFT Feb 9, 2025.pdf`, `Digital Signal Processing/exam_1_review_transcribed.pdf`, `Digital Signal Processing/301 Review/ece301final_equation-sheet.pdf`, `Digital Signal Processing/301 Review/Topic 2.2 time transformations.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[LTI system]] · [[Digital filter]] · [[FFT]] · [[Spatial filtering]] · [[Discrete-time signal]]
