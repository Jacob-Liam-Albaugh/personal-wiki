---
type: method
area: dsp
source-ref: "ECE 438 Topic IP.4.A, pp. 1-11; probability mini review"
tags: [signals]
---

# Histogram equalization

**Summary**: A parameter-free gray-level mapping that forces an image's histogram to be (approximately) uniform, using the image's own CDF as the mapping. It is the probability integral transform applied to pixel values.

## Gray-scale transformations and histograms
Gray-level mapping (intensity transformation) improves contrast for enhancement, gamut mapping (gamma correction for displays) and tone mapping of several low-dynamic-range images into a high-dynamic-range one (source: Topic IP.4.A, p. 1; L29 Apr 4, 2025.pdf, p. 1).

> [!definition] Point operation
> $s=T(r)$ with $r=f(x,y)$, applied to each pixel independently of the others; in discrete form $g(m,n)=T(f(m,n))$. Any shape is possible: thresholding, logarithmic, identity, exponential, negative, contrast stretch.
>
> (source: Topic IP.4.A, pp. 1, 5)

> [!definition] Histogram and normalised histogram
> $$h_f(b)=\#\{(m,n):f(m,n)=b\}$$
> $$p_f(b)=\frac{h_f(b)}{MN}=\Pr\big(f(m,n)=b\big)$$
> for $0\le b\le255$, with $0\le p_f\le1$ and $\sum_bp_f(b)=1$, so $p_f$ is a probability mass function. The lecture notation is $h_f(b)$ for the histogram and $P_f(b)$ for the pmf (source: IP.4.A, p. 1; L28 Apr 2, 2025.pdf, p. 1).

> [!algorithm] Equalization
> Normalised histogram $p_f(b)=h_f(b)/MN$ is a pmf. CDF $c_f(b)=\sum_{\ell\le b}p_f(\ell)$. Then
> $$g=\mathrm{round}\big(255\,c_f(f)\big)$$
> The output histogram is only approximately flat, because all pixels with the same input value must map to the same output (IP.4.A, p. 9).
>
> (source: Topic IP.4.A, p. 7)

> [!theorem] Why $T=c_f$
> For the derived image $g=T(f)$, $T$ invertible:
> $$c_g(b)=P(g\le b)=P\big(T(f)\le b\big)$$
> $$=P\big(f\le T^{-1}(b)\big)=c_f\big(T^{-1}(b)\big)$$
> A uniform output needs $c_g(b)=b$ (normalised), so $T^{-1}=c_f^{-1}$, i.e. $T=c_f$.
>
> (source: Topic IP.4.A, p. 7; Probability mini review Apr 11, 2025.pdf, p. 1)

> [!example] Probability mini review: derived random variable
> The review defines pmf, CDF and pdf of an image, then the CDF of a derived image $g=T(f)$: rewrite $g$ as $T(f)$, change the set inside the probability without changing the event (the point is to move the inverse onto the threshold), and recognise a point on the CDF of $f$. Result: $c_g(b)=c_f(T^{-1}(b))$.
>
> (source: Probability mini review Apr 11, 2025.pdf, p. 1)

> [!example] Worked mapping, $M=N=4$, $K=3$ bits
> Levels $0,\dots,7$. Image $f$ (rows):
> - 2 2 3 3
> - 2 3 3 4
> - 3 3 4 4
> - 3 4 4 5
>
> Levels 2, 3, 4, 5 have frequencies 3/16, 7/16, 5/16, 1/16. Mapping $T(b)$: $0,1,2\to0$; $3\to2$; $4\to6$; $5,6,7\to7$. Output $g$:
> - 0 0 2 2
> - 0 2 2 6
> - 2 2 6 6
> - 2 6 6 7
>
> Small values get smaller and large values larger, raising contrast; implement as a table lookup. The output histogram has 3/16, 7/16, 5/16, 1/16 at levels 0, 2, 6, 7, and in general
> $$p_g(b)=\sum_{b':\,b=T(b')}p_f(b')$$
> (sum over those $b'$ for which $b=T(b')$).
>
> (source: Topic IP.4.A, p. 5)

> [!algorithm] Contrast stretching
> Map the range $[c,d]$ of the original linearly onto $[k,l]$:
> $$g=(f-c)\,\frac{l-k}{d-c}+k$$
> Choosing $c,d$ at the 5% and 95% points keeps one outlier from dominating. Someone has to specify $c,d$, unlike equalization.
>
> (source: Topic IP.4.A, p. 7)

Variants: CLAHE (Contrast Limited Adaptive Histogram Equalization) for local adaptation (IP.4.A, p. 9). Pictorially, equal-area slices of the pdf map to equal-width output bins.

> [!example] Figures from Gonzalez and Woods ch. 3
> - Fig. 3.24 (p. 3): image and histogram with mass concentrated at dark levels.
> - Fig. 3.16 (p. 3): dark, light, low-contrast and high-contrast images with histograms.
> - Fig. 3.20 (p. 9): the Fig. 3.16 images before and after equalization; equalized histograms spread out.
> - Fig. 3.22 (p. 11): Phoenix Lander image equalized. Fig. 3.25 (p. 11): the transformation $T(r_k)$ from the histogram of Fig. 3.24(b), with the equalized image and histogram.

Wiki note: $T$ is non-decreasing but equal-valued pixels cannot be split, so the output histogram only approximates uniform (IP.4.A, p. 9). Equalization is the probability integral transform in discrete form; compare scalar [[Quantization]], where the input density matters. Pointwise mappings contrast with the neighbourhood operations in [[Spatial filtering]].



**Covered in**: ECE 438 IP.4.A, L28, L29 (Digital Signal Processing/Topic IP.4.A Histograms Apr 2, 2025.pdf)
**Sources**: `Digital Signal Processing/Topic IP.4.A Histograms Apr 2, 2025.pdf`, `Digital Signal Processing/Probability mini review Apr 11, 2025.pdf`, `Digital Signal Processing/front page/L28 Apr 2, 2025.pdf`, `Digital Signal Processing/front page/L29 Apr 4, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Spatial filtering]] · [[Quantization]] · [[Image compression]] · [[Discrete-time signal]]
