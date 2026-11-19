---
type: example
area: me697
areas: [me697, me539]
source-ref: "ASML (ME 697); Intro SciML (ME 539)"
tags: [uq, ml]
data-origin: [simulated]
tasks: [uncertainty propagation, surrogate modelling]
uses: 3
---

# Stochastic 1D heat equation

**Summary**: 3 uses in ASML (ME 697) and Intro SciML (ME 539). Data: simulated. Tasks: uncertainty propagation, surrogate modelling.

**Covered in**: ASML (ME 697), Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/hup/funcin/05_up_example.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Stochastic 1D heat equation, point QoI

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/hup/funcin/05_up_example.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: uncertainty propagation; surrogate modelling
- **Technique**: ARD GP from KLE coefficients xi to u(0.5) (Adam lr 1e-2, 1000 iterations, batch 100), then UQ by sampling 2000 xi through the GP
- **Data**: 200 FiPy solves at random xi; 80/20 train/test split.
- **Data origin**: simulated
- **Data file**: none (solved in notebook)
- **Forward model**: Steady 1D heat equation d/dx(c du/dx) = 0 on [0,1], u(0)=1, u(1)=0, with c = exp(KLE of a GP), kernel 0.5\*ExpSquared(scale=0.1), nq=1000, alpha=0.95; FiPy finite volume, nx=500 (not differentiable, not JAX).
- **Unknown dimension**: KLE coefficients xi (number unclear, outputs not saved)
- **Data dimension**: 1 scalar QoI u(x=0.5) per solve; 200 solves
- **Ground truth**: held-out 20% of solves
- **What makes it hard**: lognormal conductivity random field
- **Libraries**: fipy, jax, tinygp, optax
- **Notes**: Text says time t=0.5 instead of x=0.5 (typo).

## Stochastic 1D heat equation, full-field output

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/hup/funcin/06_up_hout_example.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: uncertainty propagation; surrogate modelling (high-dimensional output)
- **Technique**: KLE input (alpha 0.95) + PCA of outputs (alpha 0.95) + one GP per PCA coefficient (hyperparameters as in 05); 1000 samples give mean and 2.5%/97.5% quantile bands
- **Data**: 100 FiPy solves, 90/10 split; field on nx=500 grid.
- **Data origin**: simulated
- **Data file**: none (solved in notebook)
- **Forward model**: Steady 1D heat equation d/dx(c du/dx) = 0 on [0,1], u(0)=1, u(1)=0, with c = exp(KLE of a GP), kernel 0.5\*ExpSquared(scale=0.1), nq=1000, alpha=0.95; FiPy finite volume, nx=500 (not differentiable, not JAX).
- **Unknown dimension**: KLE coefficients xi
- **Data dimension**: 500-point temperature field per solve
- **Ground truth**: held-out 10% of solves
- **What makes it hard**: field-valued output
- **Libraries**: fipy, jax, tinygp, optax
- **Notes**: PCA energy computed with cumsum(s), not s^2.

## Random-conductivity rod, steady 1D heat (uncertainty propagation through BVP)

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/10 - Quantify Uncertainty in Monte Carlo Estimates/hands-on-10.4.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: uncertainty propagation
- **Technique**: plain Monte Carlo over random rods; running mean and 95% interval for T(0.5); median and 2.5/97.5 percentile bands over x
- **Data**: 1000 temperature profiles T(x) on 500 finite-volume cells (shape 1000 x 501 incl. faceValues), each for a freshly sampled random rod.
- **Data origin**: simulated
- **Data file**: steady_state_heat_N=1000.txt (written by the notebook via np.savetxt; not stored in data/)
- **Forward model**: d/dx( c(x) dT/dx ) = 0 on [0,1] m, T(0)=400 C, T(1)=4 C. c(x) piecewise constant: D~Poisson(100) segments, breakpoints sorted U(0,1), material Categorical(0.3,0.7) with conductivities 0.045 (fiberglass) and 38 W/m/K (steel). Solved with FiPy finite volume (nx=500); not JAX, not differentiable.
- **Unknown dimension**: random field c(x): D (~100) + D-1 breakpoints + D material labels
- **Data dimension**: 501 temperature values per sample
- **Ground truth**: E[T(0.5)] taken as (400+4)/2=202 in plot (red line); no reference otherwise
- **What makes it hard**: random piecewise-constant coefficient with 3 orders of magnitude contrast (0.045 vs 38); high output variance (notebook needs N>=16 sigma^2/eps^2 samples, 'a big number' for eps=1), motivates surrogates
- **Libraries**: numpy, scipy.stats, fipy, matplotlib
- **Notes**: Rod class demo sample uses conductivities 0.3/0.8 but the RandomRod used for MC uses 0.045/38. Exercise: P(T(0.5)>300 C). Data file not shipped.

## Related pages
- [[Examples catalogue]]
- [[Karhunen-Loève expansion]] · [[Principal component analysis]] · [[Gaussian process]] · [[Surrogate model]] · [[Poisson and Laplace equations]] · [[Adam]]
