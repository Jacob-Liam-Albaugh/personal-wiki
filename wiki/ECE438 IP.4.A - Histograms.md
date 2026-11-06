---
type: lecture
area: dsp
source-ref: "Topic IP.4.A, pp. 1-12"
course: ece438
lecture: IP.4.A
tags: [signals]
---

# ECE438 IP.4.A - Histograms

**Summary**: Intensity transformations (gray-level mapping) as point operations; image histogram as a probability mass function; a worked 4x4 mapping example; contrast stretching; histogram equalization with a CDF-based proof. Figures are from Gonzalez and Woods, ch. 3.

**File**: `Digital Signal Processing/Topic IP.4.A Histograms Apr 2, 2025.pdf`

---

## Topics
- Histogram adjustments (intensity transformations, gray-level mapping): contrast stretching and histogram equalization (p. 1).
- Applications: contrast enhancement, gamut mapping (gamma correction for displays), high dynamic range imaging (tone mapping) (p. 1).

## Key results
> [!definition] Gray-scale transformation (p. 1)
> $s=T(r)$ with $r=f(x,y)$: a point operation applied to each pixel independent of other pixel values.

> [!definition] Histogram and normalized histogram (p. 1)
> $$h_f(b)=\#\{(m,n):f(m,n)=b\}$$
> $$p_f(b)=\frac{h_f(b)}{MN}=\frac1{MN}\sum_{m=0}^{M-1}\sum_{n=0}^{N-1}\delta\big(f(m,n)-b\big)$$
> for $0\le b\le255$. This is the fraction of times gray level $b$ appears, $\Pr(f(m,n)=b)$. Properties: $0\le p_f(b)\le1$ and $\sum_{b=0}^{255}p_f(b)=1$, so it is a probability mass function.

> [!example] Worked mapping, $M=N=4$, $K=3$ bits (p. 5)
> Levels $0,\dots,7$. Image $f$ (rows):
> - 2 2 3 3
> - 2 3 3 4
> - 3 3 4 4
> - 3 4 4 5
>
> $h_f$: levels 2, 3, 4, 5 have 3/16, 7/16, 5/16, 1/16. Mapping $T(b)$: $0,1,2\to0$; $3\to2$; $4\to6$; $5,6,7\to7$. Output $g$:
> - 0 0 2 2
> - 0 2 2 6
> - 2 2 6 6
> - 2 6 6 7
>
> This makes small values smaller (darker) and large values larger, increasing contrast; it can be implemented by table lookup. The output histogram is $h_g$ at levels 0, 2, 6, 7 with 3/16, 7/16, 5/16, 1/16.
> $$p_g(b)=\sum_{b':\,b=T(b')}p_f(b')$$
> In English: sum over those $b'$ for which $b=T(b')$.

> [!definition] Typical transformations (p. 5)
> Any shape is possible: thresholding, logarithmic, identity, exponential, negative, contrast stretch. Typical goal: improve contrast in regions where more detail is preferred (image enhancement).

> [!algorithm] Contrast stretching (p. 7)
> Adjust the range of the histogram to span linearly a range of pixel values.
> - Pick min and max $c,d$ in the original image and corresponding new values $k,l$.
> - Adjust linearly:
> $$g=(f-c)\,\frac{l-k}{d-c}+k$$
> Example: choose $c,d$ at the 5% and 95% points to prevent one outlier from affecting the output too much. Requires someone to specify $c,d$.

> [!algorithm] Histogram equalization (p. 7)
> Force the image to have a uniform histogram; parameter-free. With the CDF
> $$c_f(b)=\sum_{\ell=0}^{b}p_f(\ell),\quad b=0,\dots,255$$
> the new image is
> $$g=\mathrm{round}\big(255\,c_f(f)\big)$$
> and the histogram of $g$ is now (approximately) uniform.

> [!theorem] Why it works (p. 7)
> Suppose $T$ maps $h_f$ to a uniform histogram. Using the CDF of $g$:
> $$P(g\le b)=P\big(T(f)\le b\big)$$
> $$=P\big(f\le T^{-1}(b)\big)$$
> $$=c_f\big(T^{-1}(b)\big)$$
> For this to be a uniform CDF it must equal $b$ (on the normalized scale), so $T=c_f$.
> In practice the transformed pmf is only mostly uniform, because all pixels with $f(m,n)=b$ must map to the same value in $g$ (p. 9). Pictorially, equal-area slices of the pdf map to equal-width bins.

> [!algorithm] Locally adaptive variants (p. 9)
> One popular method is CLAHE (Contrast Limited Adaptive Histogram Equalization).

## Examples
- Fig. 3.24 (p. 3): image and histogram, mass concentrated at dark levels.
- Fig. 3.16 (p. 3): dark, light, low-contrast and high-contrast images with their histograms.
- Fig. 3.20 (p. 9): Fig. 3.16 images before and after equalization; the equalized histograms are spread out.
- Fig. 3.22 (p. 11): Phoenix Lander image equalized. Fig. 3.25 (p. 11): the equalization transformation $T(r_k)$ from the histogram of Fig. 3.24(b), equalized image and histogram.

## Connections
- The normalized histogram is a pmf, so equalization is the probability integral transform in discrete form; compare scalar [[Quantization]] where the input density matters.
- Intensity transformations are pointwise; neighbourhood operations are in [[ECE438 IP.4.B - Spatial filtering]].
- Wiki note: because $T$ is non-decreasing but pixels with equal value cannot be split, the output histogram can only approximate uniform (the source says this, p. 9).

**Sources**: `Digital Signal Processing/Topic IP.4.A Histograms Apr 2, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 IP.4.B - Spatial filtering]] · [[ECE438 IP.2 - Sampling, quantization, interpolation]] · [[Quantization]] · [[Histogram equalization]]
