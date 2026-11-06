---
type: concept
area: me697
areas: [me697, gp]
tags: [uq, gp, ml, optimization]
---

# Surrogate model

**Summary**: A cheap statistical model fitted to runs of an expensive simulator or experiment, then used in its place for prediction, optimization, sensitivity analysis and uncertainty propagation.

---

## Workflow (01)
> [!algorithm] Surrogate workflow (01)
> 1. Training data from the expensive model $f$ at a space-filling design ([[Latin hypercube sampling]] or Sobol sequence).
> 2. Separate validation data, also space-filling.
> 3. Choose a model: polynomial regression / generalized linear model, GP regression, or a neural network.
> 4. Train.
> 5. Validate (mean squared error); if poor, add data and retrain.
> 6. Test on a third set with more diagnostics; if poor, change the model (step 3).
> 7. Use it: prediction, optimization, sensitivity analysis, uncertainty propagation, later inverse problems.

## Families
- **Generalized linear model**: $\hat f(x)=\sum_iw_i\phi_i(x)$ with polynomial, radial or [[Polynomial chaos]] bases.
- **GP regression**: [[Gaussian process]] prior, hyperparameters by marginal likelihood, cost cubic in the data size. Sparse variational GPs with inducing points scale further.
- **Neural network**: an MLP is good from about 2,000 points on the autoinjector data.

## Diagnostics
Parity plot and RMSE for the mean; for GPs the standardized errors
$$e_i=\frac{y_i-m(x_i)}{\sigma(x_i)}$$
should look standard normal (histogram, QQ plot, residuals).

## Variants
- Cheap plus expensive models: [[Multi-fidelity modeling]].
- Choose where to sample next: [[Active learning]].
- Function-valued inputs: [[Operator learning]].
- Built-in symmetry: [[Equivariance]].

## Gaussian-process surrogates
- kernel choice by structure, and automatic kernel search, are in [[Duvenaud thesis (Duvenaud 2014)]]; fast GP regression at O(N m^2) in low dimension is in [[Reduced-rank GPs (Greengard 2022)]].

## Where it appears
- Case 2 of the book's classical inverse problem (legacy codes) requires a differentiable surrogate. (source: `inverse/basics/01_classic_formulation.md`; [[Bayesian inverse problems]])

## Details from the autoinjector study (book, surrogates 01-04)
- **GP regression**: zero-mean prior, squared-exponential kernel, hyperparameters by marginal likelihood. Cost is cubic in the number of training points, impractical beyond about 5,000. Remedies: sparse GP with inducing points (Hensman et al. 2015), Kronecker structure for grid inputs with separable kernels (Bilionis et al. 2013).
- **Preprocessing**: standardize inputs; log-transform skewed outputs, then standardize.
- **Data size**: the MLP (5 hidden layers of 100, Adam $10^{-3}$, 5000 iterations, batch 128) is good from about 2,000 points and already reasonable at 500. Exact GPs need only a few hundred points for most outputs; needle displacement needs more data or built-in inductive bias.
- **Exact GP failure**: inverting the $n\times n$ covariance is $O(n^3)$, so the full training set crashes. The sparse variational GP maximizes the [[ELBO]] and inverts only the $m\times m$ inducing covariance, cost $O(bm^2+m^3)$ for minibatch $b$ and $m=100$.
- **Use**: Sobol indices from the surrogate show injection time is very sensitive to viscosity and needle diameter, somewhat to needle length and spring force, and insensitive to the rest. The book stresses this would not have been feasible with the true model ([[Sobol indices]]).

> [!example] Autoinjector model
> Replicates Sree et al. 2023 (biomechanical injection model). 10 inputs (viscosity, fill volume, air-gap height, needle length and diameter, spring force and constant, three tissue parameters kappa5-7); 4 outputs (needle displacement, injection time, max acceleration, max deceleration). Thousands of runs supplied by the authors.

> [!question] Open
> The book asks whether training the approximate GP on everything is worth the cost, and for other large datasets that would benefit.

> [!example] Homework 4, Branin (source: homework/04_homework.ipynb)
> Wrap the Branin legacy code, build a surrogate, compare random design against [[Active learning]], optimize, then go multi-fidelity ([[Multi-fidelity modeling]]).

Wiki notes:
- The exact-GP hyperparameters in the notebook are fitted by Adam on minibatches. The exact marginal likelihood of a random subset treats the subset as the whole dataset, so this is a biased stochastic objective, not the unbiased minibatch estimate used for sparse variational GPs.
- Workflow step 5 loops back to retraining while adding data, so the validation set is reused across iterations; that is why a separate test set (step 6) is kept.

**Covered in**: ASML book up/surrogates (ME 697 2.3); homework 4
**Sources**: `courses/ME 697/advanced-scientific-machine-learning/book/up/surrogates/01_basics_of_surrogate_models.md`, `02_nn_surrogates.ipynb`, `03_gp_surrogates.ipynb`, `04_gpr_large_data.ipynb`, `courses/ME 697/advanced-scientific-machine-learning/book/up/surrogates/intro.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Gaussian process]] · [[Sobol indices]] · [[Sensitivity analysis]] · [[Variational inference]] · [[ELBO]]
- [[Multi-fidelity modeling]] · [[Active learning]]
- [[Multi-fidelity Gaussian process]], [[Kernel composition]], [[Kernel methods]].
