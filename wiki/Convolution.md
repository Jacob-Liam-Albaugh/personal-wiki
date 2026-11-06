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

CT convolution and the time-flip-shift rules: [[ECE438 301R 2.2 - Time transformations]].

**Sources**: `Digital Signal Processing/Topic DSP.2 DT systems UPDATED Jan 22, 2025.pdf`, `Digital Signal Processing/Topic DSP.3.D Convolution with DFT Feb 9, 2025.pdf`, `Digital Signal Processing/exam_1_review_transcribed.pdf`, `Digital Signal Processing/301 Review/ece301final_equation-sheet.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 DSP.2 - DT systems]] · [[ECE438 DSP.3.D - Convolution with DFT]] · [[ECE438 IP.4.B - Spatial filtering]]
- [[LTI system]] · [[Digital filter]] · [[FFT]] · [[Spatial filtering]] · [[Discrete-time signal]]
