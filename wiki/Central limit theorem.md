---
type: theorem
area: math
areas: [math, ift, bayesian]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 3 (largenumbers.rst)"
tags: [bayesian, mechanics]
---

# Central limit theorem

> [!theorem] Sums of many independent terms are Gaussian
> If y = x_1 + … + x_N with the x_i iid, mean μ_x and standard deviation σ_x, then for large N y is approximately Gaussian with
> ```
> mean = N μ_x
> σ_y  = √N σ_x
> ```
> (source: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/largenumbers.rst`)

**Intuition**: the mean grows like N but the spread only like √N, so relative fluctuations die off as 1/√N. Large systems look deterministic.

## Example (ch. 3)
N two-state units with m "up": Ω(m) = N!/(m!(N−m)!), mean N/2, variance N/4, σ/⟨m⟩ = 1/√N. At N ≈ 10^26 the fluctuations are unmeasurable, which is why thermodynamic quantities have sharp values.

## Where it appears
- [[Statistical entropy]]: sharpness of macrostates.
- [[Fluctuation-dissipation theorem]]: the integrated random force is Gaussian, so the Langevin noise is a [[Wiener process]].
- Wiki note **[unverified]**: the Bayesian analogue (Bernstein-von Mises) makes posteriors Gaussian with width ∝ 1/√n as data grow, which is when the [[Laplace approximation]] is accurate.

**Covered in**: Eastman statmech ch. 3 (Large numbers); Enßlin IT & IFT ch. 4 §4.1 (p. 71)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/largenumbers.rst`, `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

## Why Gaussians recur (Enßlin)
The book lists the CLT, maximum entropy for known mean and covariance, and mathematical convenience as the three reasons to prefer Gaussians (source: Ensslin - Information Theory & Information Field Theory.pdf, §4.1, p. 71; PDF page). See [[Multivariate Gaussian]] and [[Maximum entropy principle]].

---

## Related pages
- [[Gaussian process]] · [[Brownian motion]]
- [[Multivariate Gaussian]] · [[Maximum entropy principle]]
