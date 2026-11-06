---
type: lecture
area: dsp
source-ref: "Topic DSP.5, pp. 1-11"
course: ece438
lecture: DSP.5
tags: [signals]
---

# ECE438 DSP.5 - Quantization

**Summary**: Quantization maps real sample values to one of $L$ levels. Covers uniform quantizers and their error ($\Delta^2/12$, 6.02 dB per bit) and the MSE-optimal nonuniform quantizer (Lloyd-Max), found iteratively.

**File**: `Digital Signal Processing/Topic DSP.5 Quantization Feb 23, 2025.pdf`

---

## Topics
- **Why (p. 1)**: a computer cannot take real values. [[Quantization]] is a non-invertible, nonlinear mapping into one of $L$ discrete levels. Outline: uniform quantization, its error, nonuniform optimal quantization.
- **Quantizer mapping (p. 2)**: $L+1$ decision thresholds (break points) $x_1,\dots,x_{L+1}$ and $L$ reconstruction (quantization) levels $q_1,\dots,q_L$. Typically memoryless, the same for all $n$:
$$Q\{x\}=q_k\quad\text{if}\quad x_k<x<x_{k+1}$$
All inputs in an interval map to the same output level.
- **Definitions (p. 3)**: the step size is the distance between break points. A uniform quantizer has equal step sizes, a nonuniform one does not. For processing one typically uses a uniform quantizer with $L$ a power of 2. For compression, transmission and storage, a nonuniform quantizer may do better and $L$ can be anything. If one $q_k=0$ it is a mid-tread or dead-zone quantizer; if one $x_k=0$ it is mid-rise. Dead-zone quantizers are often preferred because small variations around zero may be unimportant.
- **Uniform (p. 3)**: $\Delta=x_{k+1}-x_k$ for all $k$, and typically $\Delta=q_{k+1}-q_k$. Overload occurs when $x>x_{L+1}$ or $x<x_1$; design the quantizer so this rarely happens, and scale the signal before quantizing if needed.

## Key results
> [!definition] Quantization error and SQNR (p. 4)
> Treat $x[n]$ as a stationary random process, so each time step is a random variable $X$, with output $Y=Q\{X\}$ and error $U=Q\{X\}-X$.
> $$\mathrm{MSQE}=E[U^2]=E[(Y-X)^2]$$
> $$\mathrm{SQNR}=10\log_{10}\frac{E[X^2]}{E[U^2]}$$
> For a uniform quantizer, $U$ is modelled as a noise term added to $X$. If $-\Delta/2<U<\Delta/2$ it is granular noise; if $X$ is outside the quantizer range it is overload noise.

> [!assumption] Four assumptions for the uniform quantizer (p. 5)
> 1. Each $U$ is uniform on $(-\Delta/2,\Delta/2]$.
> 2. $\{U_n\}$ is a stationary white noise sequence.
> 3. $U_n$ is uncorrelated with $X_n$.
> 4. $\{X_n\}$ is zero-mean and stationary.
> Model: $Y=X+U$. These are fairly accurate when $\Delta$ is small and $X$ changes "non slowly".

> [!theorem] Uniform quantizer error (pp. 5-6)
> With density $1/\Delta$ on $(-\Delta/2,\Delta/2)$:
> $$E[U^2]=\frac1\Delta\int_{-\Delta/2}^{\Delta/2}u^2\,du=\frac{\Delta^2}{12}$$
> Take $X\in[-A,A]$, $\Delta=2A/2^\ell$ and $L=2^\ell$. Both $X$ and $U$ are zero-mean, so
> $$\mathrm{SQNR}=20\log_{10}\sigma_X-10\log_{10}\frac{\Delta^2}{12}=C+6.02\,\ell$$
> SQNR increases by 6.02 dB for every extra bit ($20\log_{10}2\approx6.02$). No overload noise is assumed; any signal distribution is allowed.

> [!algorithm] Optimal (Lloyd-Max) quantizer (pp. 7-11)
> Uniform quantization is optimal in some sense when there are many levels and variable-length (Huffman-like) coding is used, or when the source is uniformly distributed; otherwise there is no reason to assume it. Intuition: finer regions where the signal is likely, coarser where unlikely (e.g. a Gaussian $X$ is more likely within $\pm\Delta/2$ than between $3\sigma-\Delta$ and $3\sigma$).
> Assume the pdf $f_X(x)$ has no delta functions and no gaps. Minimize
> $$\mathrm{MSQE}=\sum_{k=1}^L\int_{x_k}^{x_{k+1}}(q_k-x)^2f_X(x)\,dx$$
> Setting $\partial/\partial q_k=0$:
> $$q_k=\frac{\int_{x_k}^{x_{k+1}}x\,f_X(x)\,dx}{\int_{x_k}^{x_{k+1}}f_X(x)\,dx}=E[X\mid x_k<X<x_{k+1}]$$
> the centroid of the $k$th interval, the best level for a given partition. Setting $\partial/\partial x_k=0$ (with $x_1=-\infty$, $x_{L+1}=\infty$):
> $$x_k=\frac{q_{k-1}+q_k}{2}$$
> the midpoint between levels, the best break point for given levels. There is generally no closed-form solution; solve iteratively (Lloyd and Max), usually empirically from data samples:
> 0. sample typical data; 1. choose starting levels $q_k$; 2. set break points midway between levels; 3. replace each $q_k$ with the mean of the data samples in its interval; 4. repeat steps 2 and 3 until the change is below a threshold. It may help to run it a few times with different starting values (p. 11).

## Connections
- Quantization follows sampling in the A/D chain: [[ECE438 DSP.4.A - Sampling CT]]. Images: [[ECE438 IP.2 - Sampling, quantization, interpolation]]; compression with entropy coding: [[ECE438 IP.6 - Image compression]].
- Wiki note: the centroid and midpoint conditions are the alternating steps of one-dimensional k-means. **[unverified]** link not made in the source.

**Sources**: `Digital Signal Processing/Topic DSP.5 Quantization Feb 23, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Quantization]] · [[Sampling theorem]] · [[Discrete-time signal]] · [[Digital filter]]
