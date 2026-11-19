---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [bayesian, inverse-problems, vi]
data-origin: [real]
tasks: [inverse problem and calibration, variational inference]
uses: 3
---

# Catalysis kinetics

**Summary**: 3 uses in ASML (ME 697). Data: real. Tasks: inverse problem and calibration, variational inference.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/inverse/basics/02_classic_example.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Catalysis kinetics (classical calibration)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/inverse/basics/02_classic_example.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Parameter calibration (point estimate)
- **Technique**: Adam (lr 0.1, 100 its) on scaled squared loss 0.5\*sum(((f-y)/500)^2); x=log(180 k); no uncertainty
- **Data**: Real nitrate-reduction catalysis time series, 7 rows x 6 cols (Time, NO3, NO2, N2, NH3, N2O); t=0,30,...,180 min, mmol/L; row0 = (500,0,0,0,0), last row = (13.54,6.11,309.50,27.26,62.54) for NO3,NO2,N2,NH3,N2O
- **Data origin**: real
- **Data file**: data/catalysis.csv (GitHub raw URL in notebook)
- **Forward model**: Linear ODE dz/dt = A(k) z, 6 species (X unobserved intermediate), rates k1..k5; JAX/diffrax Tsit5 (differentiable)
- **Unknown dimension**: 5 rates (x0 init has shape 6)
- **Data dimension**: 7x5 array flattened = 35 (includes t=0 row); 30 informative
- **Ground truth**: none
- **What makes it hard**: Mass not conserved in data, motivating unobserved X; ODE-solver in the loop
- **Libraries**: jax, diffrax, optax, pandas
- **References**: Katsounaros 2012; Tsilifis 2014 Example 3.1 (arXiv 1410.5522)
- **Notes**: Bug: t_exp = dataframe index 0..6 (not minutes) while k=exp(x)/180; x0 has 6 entries for 5 parameters. Questions on seeds and far-away starts.

## Catalysis kinetics (Bayesian Laplace, known and unknown noise)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/inverse/basics/05_laplace_example.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Bayesian inverse problem
- **Technique**: MAP via Adam (lr 0.1, 300 its) + Laplace covariance from finite-difference (eps 1e-5) Jacobian/Hessian, jitter 1e-6; prior x~N(0,10^2 I), noise sigma=5 known; then unknown noise theta=log sigma with Jeffreys prior 1/sigma, joint 7 unknowns; 50 posterior samples pushed through ODE
- **Data**: Real nitrate-reduction catalysis time series, 7 rows x 6 cols (Time, NO3, NO2, N2, NH3, N2O); t=0,30,...,180 min, mmol/L; row0 = (500,0,0,0,0), last row = (13.54,6.11,309.50,27.26,62.54) for NO3,NO2,N2,NH3,N2O
- **Data origin**: real
- **Data file**: data/catalysis.csv (GitHub raw URL in notebook)
- **Forward model**: Linear ODE dz/dt = A(k) z, 6 species (X unobserved intermediate), rates k1..k5; JAX/diffrax Tsit5 (differentiable)
- **Unknown dimension**: 5 rates (6-entry x0) ; 5+1 noise in second part
- **Data dimension**: 7x5=35 (as in classical notebook)
- **Ground truth**: none
- **What makes it hard**: Gaussian approximation of ODE-based posterior; epistemic vs aleatory
- **Libraries**: jax, diffrax, optax
- **References**: Katsounaros 2012; Tsilifis 2014 Example 3.1 (arXiv 1410.5522)
- **Notes**: Same t_exp index bug. Noise part: sampling uses mu instead of mu_noise; var_post_sigma indexes Sigmas not Sigmas_noise. Autodiff Hessian through diffrax not used. Questions on sigma 1-20, gamma.

## Catalysis kinetics (full-rank Gaussian VI)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/inverse/vi/02_catalysis.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Bayesian inverse problem
- **Technique**: Reparameterised-ELBO full-rank Gaussian VI (27 params: 6 mean + 21 Cholesky), Adam lr 5e-2, batch 5, 3000 its, optax.apply_if_finite; priors via transform: k=exp(2.0 x), sigma^2~Exp(1/0.005) through normal CDF
- **Data**: Same catalysis data, t>0 rows only: 6 times (30..180 min) x 5 species; scaled t/180, conc/500
- **Data origin**: real
- **Data file**: data/catalysis.csv
- **Forward model**: Linear ODE dz/dt = A(k) z, 6 species (X unobserved intermediate), rates k1..k5; JAX/diffrax Tsit5 (differentiable), with DirectAdjoint (Hessian-compatible) and Event NaN guard
- **Unknown dimension**: 5 log-rates + noise variance = 6
- **Data dimension**: 30 = 5 species x 6 times
- **Ground truth**: none (no reference MCMC)
- **What makes it hard**: Solver blow-up for extreme parameter draws
- **Libraries**: jax, diffrax, optax
- **References**: Katsounaros 2012; Tsilifis 2014 Example 3.1 (arXiv 1410.5522)
- **Notes**: Posterior correlation heatmap, 50 posterior trajectories. Questions on lambda, gamma, starting points.

## Related pages
- [[Examples catalogue]]
- [[Markov chain Monte Carlo]] · [[Variational inference]] · [[ELBO]] · [[Catalysis problem]] · [[Adam]] · [[Adjoint sensitivity method]]
