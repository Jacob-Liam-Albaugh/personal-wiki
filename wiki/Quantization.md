---
type: method
area: dsp
source-ref: "ECE 438 Topic DSP.5, pp. 1-11; probability mini review"
tags: [signals]
---

# Quantization

**Summary**: Mapping continuous amplitudes to $L$ discrete levels, a non-invertible nonlinear step that follows sampling in A/D conversion. Uniform quantizers gain about 6 dB of SQNR per bit; the Lloyd-Max quantizer adapts break points and levels to the input density.

> [!definition] Quantizer
> Break points $x_1<\dots<x_{L+1}$ and levels $q_1,\dots,q_L$:
> $$Q\{x\}=q_k\quad\text{if}\ x_k<x<x_{k+1}$$
> Uniform if all step sizes $\Delta$ are equal. Overload occurs outside $[x_1,x_{L+1}]$.
>
> (source: Topic DSP.5, pp. 2-3)

> [!theorem] Uniform quantizer noise
> Model $Y=X+U$ with $U$ uniform on $(-\Delta/2,\Delta/2]$, white, uncorrelated with $X$. Then
> $$E[U^2]=\frac{\Delta^2}{12}$$
> $$\mathrm{SQNR}=10\log_{10}\frac{E[X^2]}{E[U^2]}=C+6.02\,\ell$$
> for $\ell$ bits ($L=2^\ell$, $\Delta=2A/2^\ell$). Accurate for small $\Delta$.
>
> (source: Topic DSP.5, pp. 4-6)

> [!algorithm] Lloyd-Max
> Minimise $\mathrm{MSQE}=\sum_k\int_{x_k}^{x_{k+1}}(q_k-x)^2f_X(x)dx$. Two necessary conditions:
> $$q_k=E[X\mid x_k<X<x_{k+1}]$$
> $$x_k=\tfrac12(q_{k-1}+q_k)$$
> Levels are centroids, break points are midpoints. Iterate: start levels, set midpoints, recompute centroids from data, repeat until change is small. Try several starting values.
>
> (source: Topic DSP.5, pp. 7-11)

Wiki note: the alternation is 1D k-means. **[unverified]** link not made in the source.

> [!example] Probability mini review: pmf, CDF, pdf of an image
> Image $f$ with pmf $p_f(b)=P(f(m,n)=b)$, $\sum_bp_f(b)=1$. CDF $c_f(b)=P(f\le b)$ rises from 0 to 1. The pdf $p_f(b)=\frac{d}{db}c_f(b)$ is not a probability but integrates to one over $[b_1,b_2]$ to give one; useful for normalised pixels in $[0,1]$. These are the densities the quantizer minimises over.
>
> (source: Probability mini review Apr 11, 2025.pdf, p. 1)

For images, quantization is bit depth; entropy coding of quantized values is in [[Image compression]].

## Terminology and assumptions
A computer cannot take real values, so quantization is a non-invertible, nonlinear map into one of $L$ levels with $L+1$ decision thresholds (break points) and $L$ reconstruction levels. Typically it is memoryless, the same for all $n$ (source: Topic DSP.5, pp. 1-2; L20 Mar 3, 2025.pdf, p. 1).

The step size is the distance between break points: uniform quantizers have equal steps, nonuniform ones do not. For processing one typically uses a uniform quantizer with $L$ a power of 2. For compression, transmission and storage a nonuniform quantizer may do better and $L$ can be anything. If one $q_k=0$ it is a mid-tread or dead-zone quantizer; if one $x_k=0$ it is mid-rise. Dead-zone quantizers are often preferred because small variations around zero may be unimportant. For a uniform quantizer $\Delta=x_{k+1}-x_k$ and typically $\Delta=q_{k+1}-q_k$; overload occurs when $x>x_{L+1}$ or $x<x_1$, so design it to occur rarely, scaling the signal first if needed (source: Topic DSP.5, p. 3).

Treat $x[n]$ as a stationary random process, so each time step is a random variable $X$ with $Y=Q\{X\}$ and error $U=Q\{X\}-X$:
$$\mathrm{MSQE}=E[U^2]=E[(Y-X)^2]$$
If $-\Delta/2<U<\Delta/2$ the error is granular noise; if $X$ is outside the quantizer range it is overload noise (source: Topic DSP.5, p. 4).

> [!assumption] Four assumptions for the uniform quantizer
> 1. Each $U$ is uniform on $(-\Delta/2,\Delta/2]$.
> 2. $\{U_n\}$ is a stationary white noise sequence.
> 3. $U_n$ is uncorrelated with $X_n$.
> 4. $\{X_n\}$ is zero-mean and stationary.
> These are fairly accurate when $\Delta$ is small and $X$ changes non-slowly; the model is $Y=X+U$. They give $E[U^2]=\Delta^2/12$ for any input distribution without delta functions (L20), and with $X\in[-A,A]$, $\Delta=2A/2^\ell$:
> $$\mathrm{SQNR}=20\log_{10}\sigma_X-10\log_{10}\frac{\Delta^2}{12}=C+6.02\,\ell$$
> since $20\log_{10}2\approx6.02$ dB per extra bit, with no overload noise assumed.
>
> (source: Topic DSP.5, pp. 5-6)

## When uniform is optimal, and Lloyd-Max intuition
Uniform quantization is optimal in some sense when there are many levels and variable-length (Huffman-like) coding is used, or when the source is uniformly distributed; otherwise there is no reason to assume it. The intuition for Lloyd-Max is finer regions where the signal is likely and coarser where unlikely (e.g. a Gaussian $X$ is more likely within $\pm\Delta/2$ than between $3\sigma-\Delta$ and $3\sigma$). The derivation assumes a pdf $f_X$ without delta functions or gaps. Setting $\partial\mathrm{MSQE}/\partial q_k=0$ gives the centroid
$$q_k=\frac{\int_{x_k}^{x_{k+1}}xf_X(x)dx}{\int_{x_k}^{x_{k+1}}f_X(x)dx}$$
and setting $\partial/\partial x_k=0$ (with $x_1=-\infty$, $x_{L+1}=\infty$) gives $x_k=(q_{k-1}+q_k)/2$. There is generally no closed form, so the solution is iterated empirically from data: sample typical data, choose starting levels, set break points midway, replace each $q_k$ with the mean of the samples in its interval, repeat until the change is small, possibly from several starting values (source: Topic DSP.5, pp. 7-11; L21 Mar 5, 2025.pdf, p. 1).

## Images
Bit depth is quantization of pixel amplitude, $L=2^k$ levels. Reducing it at a fixed display size produces false contouring and a dull, washed-out look at 16, 8, 4, 2 levels; see [[Digital image]] (source: Topic IP.2 Sampling, quantization, interpolation, Fig. 2.24).

**Covered in**: ECE 438 DSP.5, L19-L21 (Topic DSP.5 Quantization; L19 Feb 28, L20 Mar 3, L21 Mar 5, 2025 front pages); image bit depth from IP.2
**Sources**: `courses/ECE 438/Topic DSP.5 Quantization Feb 23, 2025.pdf`, `courses/ECE 438/Probability mini review Apr 11, 2025.pdf`, `courses/ECE 438/front page/L19 Feb 28, 2025.pdf`, `courses/ECE 438/front page/L20 Mar 3, 2025.pdf`, `courses/ECE 438/front page/L21 Mar 5, 2025.pdf`, `courses/ECE 438/Topic IP.2 Sampling, quantization, interpolation Mar 23, 2025 .pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sampling theorem]] · [[Histogram equalization]] · [[Image compression]] · [[Discrete-time signal]] · [[Digital filter]] · [[Digital image]]
