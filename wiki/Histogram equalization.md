---
type: method
area: dsp
source-ref: "ECE 438 Topic IP.4.A, pp. 1-11; probability mini review"
tags: [signals]
---

# Histogram equalization

**Summary**: A parameter-free gray-level mapping that forces an image's histogram to be (approximately) uniform, using the image's own CDF as the mapping. It is the probability integral transform applied to pixel values.

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

> [!example] 4x4, 3-bit image
> Levels 2, 3, 4, 5 have frequencies 3/16, 7/16, 5/16, 1/16; the point map sends $0,1,2\to0$, $3\to2$, $4\to6$, $5,6,7\to7$. (IP.4.A, p. 5, a general mapping example.)

Variants: contrast stretching with chosen percentiles $c,d$ (needs parameters); CLAHE for local adaptation (IP.4.A, pp. 7-9).

**Sources**: `Digital Signal Processing/Topic IP.4.A Histograms Apr 2, 2025.pdf`, `Digital Signal Processing/Probability mini review Apr 11, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 IP.4.A - Histograms]] · [[ECE438 L29 - Histogram equalization derivation]] · [[ECE438 L28 - Gray-scale transformations and spatial filters]]
- [[Spatial filtering]] · [[Quantization]] · [[Image compression]] · [[Discrete-time signal]]
