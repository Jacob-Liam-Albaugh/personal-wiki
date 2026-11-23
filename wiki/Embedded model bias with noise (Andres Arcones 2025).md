---
type: paper
area: bayesian
areas: [bayesian, inverse-problems]
source-ref: "Andrés Arcones, Weiser, Koutsourelakis, Unger 2026, Data-Centric Engineering 7:e7"
tags: [bayesian, inverse-problems, uq, mcmc]
authors: ["[[Daniel Andrés Arcones]]", "[[Martin Weiser]]", "[[Phaedon-Stelios Koutsourelakis]]", "[[Jörg F. Unger]]"]
year: 2026
venue: "Data-Centric Engineering 7:e7 (2026), doi:10.1017/dce.2025.10035; preprint arXiv:2410.12037"
file: "[[papers/Bayesian/Andres Arcones, Weiser, Koutsourelakis, Unger - Embedded Model Form Uncertainty Quantification with Measurement Noise for Bayesian Model Calibration.pdf]]"
---

# Embedded model bias with noise (Andres Arcones 2025)

**Summary**: Calibrating a wrong model with only a noise term gives an overconfident posterior, and an external Kennedy-O'Hagan discrepancy cannot be carried to other quantities of interest (QoIs). The paper puts the model error inside a parameter as an additive Gaussian, θ̃ = θ_m + δ, and fits the predicted mean and variance to data. It adds measurement noise to Sargsyan's ABC and independent-normal likelihoods and proposes two new ones (GMM, RGMM). Pushing the full posterior through the model gives honest uncertainty on an unobserved QoI.

**Authors**: Daniel Andrés Arcones, Martin Weiser, Phaedon-Stelios Koutsourelakis, Jörg F. Unger (BAM Berlin, TU Munich, Zuse Institute Berlin) · **Year**: 2026 · **File**: [[papers/Bayesian/Andres Arcones, Weiser, Koutsourelakis, Unger - Embedded Model Form Uncertainty Quantification with Measurement Noise for Bayesian Model Calibration.pdf]] · **Code**: probeye (BAMResearch, Python) · **Data**: Zenodo 10.5281/zenodo.15720780

**Version**: the journal version, titled "Embedded model form uncertainty quantification with measurement noise for Bayesian model calibration" (received 23 June 2025, accepted 9 December 2025, CC-BY). The arXiv v2 preprint is kept as [[papers/Bayesian/Andres Arcones, Weiser, Koutsourelakis, Unger - Embedded Model Bias Quantification with Measurement Noise for Bayesian Model Calibration.pdf|the preprint]]. Equation numbers below follow the journal version.

Wiki note: the first author's surname is "Andrés Arcones" (the paper cites its own earlier work that way); the filename drops the accent.

---

## Problem

Data are explained as model plus model error plus noise (eq. 1):

```
y = f(θ, x)
  + ε_model
  + ε_noise
```

- With only ε_noise, the posterior of a misspecified model concentrates on the best-fitting value as data grow. Its credible intervals do not cover the data, citing Bernstein-von Mises and Kleijn-van der Vaart 2012 (pp. 2-3). See [[Central limit theorem]].
- Kennedy-O'Hagan adds a GP discrepancy to the output ([[Multi-fidelity modeling]]). It fixes predictions of the observed quantity only, and the discrepancy can trade off against θ ([[Identifiability]]).
- The alternative is to embed the error in the parameters (Sargsyan 2015, 2019; Pernot calls it parameter uncertainty inflation). The error then flows through the physics into any other output. See [[Embedded model inadequacy]].

## Method

> [!definition] Additive embedding (eqs. 7-8)
> ```
> θ̃ = θ_m + δ(θ_b)
> δ ~ N(0, diag(θ_b))
> ```
> θ_m is the parameter mean and θ_b the model-error scale; both are inferred.
>
> (source: file, §2.2)

- Sargsyan 2019 writes θ̃ as a [[Polynomial chaos]] expansion with inferred coefficients (eq. 6). The explicit form is easier to read and needs a smaller PCE (p. 5).
- **Forward model**: a stochastic θ̃ makes f(θ̃, x) random. A PCE in the germ of δ, fitted by pseudo-spectral Gauss quadrature (Algorithm 1, chaospy), gives its moments straight from the coefficients:
  ```
  μ_i  = α_i0              (15)
  σ_i² = Σ_{j≥1} α_ij²     (16)
  ```
- **Versus hierarchical Bayes** (§2.4): the embedded posterior π(θ_m, θ_b | y) never samples θ̃. The [[Hierarchical Bayesian model]] version (Fig. 1) samples θ̃ per data point with a deterministic f. Pernot and Cailliez 2017 found the ABC-embedded version better (p. 7).
- **Sampler**: emcee stretch-move ensemble [[Markov chain Monte Carlo]], stopped at an estimated effective sample size of 837 (App. A).

### Likelihoods (§2.5, Table 1)

All four match the predicted mean μ_i and standard deviation σ_i to the data. σ_N is the known noise.

> [!algorithm] ABC with noise (eq. 24)
> ```
> log L = Σ_i [
>   -(μ_i - y_i)² / (2σ_N²)
>   -(σ_i + σ_N
>     - γ|μ_i - y_i|)² / (2ε²) ]
> γ = √(π/2)
> ```
> Without noise (eq. 21, Sargsyan) the first term uses ε and γ = 1. The paper's γ = √(π/2) comes from the half-normal mean: E|r| = σ√(2/π) (eq. 22). The noise version follows Wilkinson 2013 (§2.5.2, eq. 23). Eq. 24 assumes additive homoscedastic Gaussian noise; other noise models are left for future work.

> [!algorithm] Independent normal, IN (eq. 26)
> ```
> y_i ~ N(μ_i, σ_i² + σ_N²)
> ```
> Sargsyan's eq. 25 without σ_N.

> [!algorithm] Global moment matching, GMM (eqs. 27-40)
> Treat the residuals u_i = y_i - μ_i as draws from one equal-weight mixture F = (1/n) Σ N(0, σ_i² + σ_N²). It has mean 0 and variance
> ```
> σ_F² = mean_i(σ_i²) + σ_N²
> ```
> By Cochran's theorem, the sample mean ū and sample variance s² of the residuals should satisfy
> ```
> ū ~ N(0, σ_F²/n)
> n s²/σ_F² ~ χ²_{n-1}
> ```
> The likelihood is the product of these two densities (eqs. 36, 38, 39).

> [!algorithm] Relative GMM, RGMM (eqs. 41-49)
> GMM applied to the scaled residuals
> ```
> r_i = (y_i - μ_i)
>     / √(σ_i² + σ_N²)
> ```
> so σ_F = 1. Meant for strongly heteroscedastic errors, where a few high-variance points would dominate GMM.

Wiki note: the GMM sample variance (eq. 35) divides Σ(u_i - ū)² by n-1, the RGMM one (eq. 46) by n (checked against the page). The χ² statement n s²/σ_F² ~ χ²_{n-1} is exact for the divide-by-n form. The arXiv v2 printed this variance with no square and no mean subtracted; the journal version fixes that.

- **Noise check (App. B)**: if the prescribed σ_N exceeds the residuals, the moment-matching likelihoods prefer *larger* residuals so σ_i + σ_N can match them. The posterior then drifts away from the true system. App. B derives this from the gradient and Hessian of the noisy ABC log-likelihood (eqs. B2-B9): the Hessian is negative definite, and Table B1 sorts the behaviour into seven cases by how the mean residual compares with the mean predicted deviation. Inferring σ_N as a latent parameter is possible for the noisy moment-matching likelihood (p. 13).

### Pushing to QoIs (§2.7)

- Usual practice (Huan 2017, Sargsyan 2019) pushes only the MAP (θ̂_m, θ̂_b) through f. That keeps the model-error spread θ_b but drops the posterior spread, correlations and other modes.
- The paper pushes every posterior sample through f, or through another QoI g that shares the parameters. Each sample gives a predictive distribution, so μ_P, σ_P and a z-value each get their own posterior distribution.
- The predictive variance does not shrink to zero with more data, because it keeps the model-error spread.

## Results

> [!example] Linear model (§3.1)
> Data y = θx + ε_N with θ ~ N(4, 1) redrawn for each point and σ_true = 0.01, 120 points on [0.4, 1]. Embedding θ* = t + δ_b with δ_b ~ N(0, σ_b²). A degree-1 Hermite PCE is exact here.
>
> Posterior (Table 2; truth t = 4, σ_b = 1):
>
> | Likelihood | t mean ± std | σ_b mean ± std |
> |---|---|---|
> | ABC | 3.93 ± 0.00 | 1.03 ± 0.00 |
> | GMM | 3.95 ± 0.13 | 0.89 ± 0.15 |
> | RGMM | 3.97 ± 0.13 | 1.03 ± 0.14 |
> | IN | 3.95 ± 0.09 | 1.00 ± 0.06 |
>
> - ABC is near-exact up to ε and is the only one whose interval misses the truth: it fits this dataset's moments exactly.
> - z-value of the point y(1.0) = 5.04 is below 1.96 for every likelihood. Without the embedding (noise only) it is 104.
> - Over 20 datasets ABC's t varies most and needs the most variable chain length. GMM underestimates σ_b because the shared-mixture assumption fails on a small dataset (Figs. 5-6).

- **Noise misspecification** (Figs. 7-8, σ_N from 0.001 to 10): ABC is the most sensitive. Above σ_N ≈ 0.4 the prescribed noise exceeds the spread at some points and its parameters shift. Above σ_N = 1 the noise exceeds the spread at every point; the likelihood grows local optima and chains stop early. IN is the most robust; GMM and RGMM drift in t but keep narrow intervals.
- **Constant offset Δy** (eq. 55, Figs. 9-10, the model cannot reproduce it): t rises and σ_b inflates to cover the data. IN and RGMM move most, because low-variance points carry the most weight in them.
- **Outliers on a subset** (eq. 56, Figs. 11-12; offset 0 to 2 in 21 steps): ABC moves most, because it weighs every point equally.

> [!example] Reinforced concrete heat transfer (§3.2)
> - **Setup**: 2D transient heat equation on a 0.4 m square, solved with FE (20×20 linear elements, backward Euler, 5 min steps).
> - **Truth vs model**: the data come from concrete with a steel band (Voigt mixture, α = 5.61e-6 m²/s) and a noisy external temperature. The model is uniform concrete with constant external temperature.
> - **Inference**: α is inferred from four temperature sensors (20-220 min, σ_N = 0.2 K) with the embedding α = α_m + δ, δ ~ N(0, σ_b²), and a degree-2 PCE.
> - **QoI**: cumulative heat through the midline at 5000 min, which was never observed.
>
> Results (Table 5):
> - All likelihoods give α_m ≈ 1.27-1.32e-6, above concrete's 9.66e-7, because the steel speeds up conduction. σ_b is 1.3-2.4e-7.
> - Posterior bands cover the test sensors. The pushed heat distribution covers the true 91 338 J, with every z-value well below 1.96.
> - Without the embedding the heat prediction misses by more than 10 kJ with near-zero spread (Figs. 18-19).
> - ABC's posterior standard deviations are about 1e-13, again near-exact.

## Limitations

As stated by the authors (§4):
- The embedding only reaches outputs the model can produce. Offsets and outliers that no parameter value explains bias the parameters.
- The right likelihood depends on noise quality, outliers and heteroscedasticity, which are often not known in advance:
  - ABC is sensitive to σ_N and needs careful γ and ε.
  - RGMM and IN suffer from offsets near low-variance points.
  - GMM and RGMM need the shared-mixture assumption to hold.
- Residuals are treated as independent. Correlated residuals and correlated δ across several parameters are left for future work, as is a full comparison with hierarchical Bayes.
- Update cost goes up: one PCE fit per likelihood call.

Wiki notes:
- ε, the ABC tolerance, sets the posterior width directly. The paper takes ε = 1e-6, just above machine precision, and says larger ε inflates the posterior and has "no real fundament" (§3.3). So ABC's near-zero posterior spread reflects that tiny ε, not the information in the data.
- The z-test on QoIs checks coverage of a single held-out value. It is not a calibration check over many values.

## Connections

- **Same problem in IFT**: model-form error in [[Information field theory]]. There the trust β of a [[Physics-informed prior]] flags a wrong model ([[Model-form error detection]]); here the error lives in the parameters. Both aim to stop a misspecified posterior collapsing.
- **Hierarchical Bayes**: the hierarchical alternative is [[Hierarchical Bayesian model]]. Embedding is close to a hierarchical model with θ̃ marginalised by PCE moments instead of sampled.
- **External discrepancy**: the Kennedy-O'Hagan discrepancy lives on [[Multi-fidelity modeling]]. Its prediction-only scope is the paper's motivation.
- **Inverse-problem setting**: [[Bayesian inverse problems]], with a PDE forward model and a [[Polynomial chaos]] [[Surrogate model]].
- **Earlier work**: Sargsyan, Najm, Ghanem 2015 and Sargsyan, Huan, Najm 2019 (embedded PCE, ABC and IN likelihoods), cited, not ingested. Wu 2024 embeds the error inside a [[Kalman filter]].

%% refs:start %%
**Cites in this wiki**: [[Wiener-Askey chaos (Xiu 2002)]]
%% refs:end %%

**Sources**: `papers/Bayesian/Andres Arcones, Weiser, Koutsourelakis, Unger - Embedded Model Form Uncertainty Quantification with Measurement Noise for Bayesian Model Calibration.pdf` (45 pp., journal version); `papers/Bayesian/Andres Arcones, Weiser, Koutsourelakis, Unger - Embedded Model Bias Quantification with Measurement Noise for Bayesian Model Calibration.pdf` (37 pp., arXiv v2).
**Last updated**: 2026-11-23

---

## Related pages
- [[Embedded model inadequacy]]
- [[Model-form error detection]]
- [[Hierarchical Bayesian model]]
- [[Polynomial chaos]]
- [[Multi-fidelity modeling]]
- [[Bayesian inverse problems]]
- [[Identifiability]]
- [[Markov chain Monte Carlo]]
- [[Surrogate model]]
- [[Central limit theorem]]
