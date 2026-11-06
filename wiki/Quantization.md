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

**Sources**: `Digital Signal Processing/Topic DSP.5 Quantization Feb 23, 2025.pdf`, `Digital Signal Processing/Probability mini review Apr 11, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 DSP.5 - Quantization]] · [[ECE438 L19 - Quantization]] · [[ECE438 L20 - Optimal quantization and the z-transform]] · [[ECE438 IP.2 - Sampling, quantization, interpolation]]
- [[Sampling theorem]] · [[Histogram equalization]] · [[Image compression]] · [[Discrete-time signal]] · [[Digital filter]]
