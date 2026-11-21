---
type: method
area: bayesian
areas: [bayesian, inverse-problems]
source-ref: "Andrés Arcones et al. 2025, arXiv:2410.12037v2, §2"
tags: [bayesian, inverse-problems, uq]
---

# Embedded model inadequacy

> [!definition] Embedded model inadequacy
> Make a model parameter random, with a distribution whose spread is inferred, so the model's output is a distribution. Then calibrate by matching its mean and variance to the data:
> ```
> θ̃ = θ_m + δ
> δ ~ N(0, diag(θ_b))
> y_i ≈ f(θ̃, x_i)
> ```
> Infer (θ_m, θ_b). The model-error spread θ_b sits inside the physics.
>
> (source: `papers/Bayesian/Andres Arcones, Weiser, Koutsourelakis, Unger - Embedded Model Bias Quantification with Measurement Noise for Bayesian Model Calibration.pdf`, eqs. 7-8)

**Intuition**: A wrong model fitted with only a noise term gives a posterior that shrinks to one parameter value as data grow, and its error bars stop covering the data. An external discrepancy term (Kennedy-O'Hagan) fixes predictions of the measured quantity but says nothing about anything else. Spreading a parameter instead lets the model's own physics carry the error to every output, including quantities never measured.

## How it is computed

- f(θ̃, x) is random, so each likelihood call needs its mean μ_i and standard deviation σ_i. A [[Polynomial chaos]] expansion in δ gives both from its coefficients.
- The likelihood then compares (μ_i, σ_i) with the data. Four options are compared in [[Embedded model bias with noise (Andres Arcones 2025)]]:
  - ABC: per-point moment matching with tolerance ε.
  - Independent normal: y_i ~ N(μ_i, σ_i² + σ_N²).
  - GMM: pooled residual mean and variance through Cochran's theorem.
  - RGMM: GMM on variance-scaled residuals.
- **Prediction**: push every posterior sample (θ_m, θ_b) through the model. Pushing only the MAP keeps θ_b but drops the posterior spread.

## Variants

- Sargsyan et al. 2015, 2019: θ̃ as a PCE with inferred coefficients (cited in the source above, not ingested).
- Pernot: "parameter uncertainty inflation"; Pernot and Cailliez 2017 compare it with hierarchical Bayes (cited, not ingested).
- Hierarchical form: sample θ̃ per data point with a deterministic model ([[Hierarchical Bayesian model]]).

## Failure modes

> [!failure] Errors the model cannot reach
> An offset or outlier that no parameter value reproduces biases θ_m and inflates θ_b. The embedding only spans the model's own output range (§4).

> [!failure] Overstated noise
> If the prescribed σ_N is larger than the residuals, moment matching favours worse fits so the predicted spread matches (App. C).

## Where it appears

- [[Embedded model bias with noise (Andres Arcones 2025)]]: additive Gaussian embedding, noise-aware ABC and IN likelihoods, new GMM and RGMM likelihoods. Tested on a linear toy and a reinforced-concrete heat problem.

**Sources**: `papers/Bayesian/Andres Arcones, Weiser, Koutsourelakis, Unger - Embedded Model Bias Quantification with Measurement Noise for Bayesian Model Calibration.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Embedded model bias with noise (Andres Arcones 2025)]]
- [[Model-form error detection]]
- [[Hierarchical Bayesian model]]
- [[Polynomial chaos]]
- [[Multi-fidelity modeling]]
- [[Bayesian inverse problems]]
- [[Identifiability]]
