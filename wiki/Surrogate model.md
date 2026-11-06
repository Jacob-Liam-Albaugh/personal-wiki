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
1. Training data from the true model on a space-filling design ([[Latin hypercube sampling]] or Sobol).
2. Separate validation data.
3. Pick a family: generalized linear model, GP, or neural network.
4. Train. 5. Validate; add data if poor. 6. Test on a third set; change model if poor.
7. Use it.

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
- Case 2 of the book's classical inverse problem (legacy codes) requires a differentiable surrogate. (source: `inverse/basics/01_classic_formulation.md`; [[ME697 4.1 - Classical and Bayesian inverse problems]])

**Sources**: `advanced-scientific-machine-learning/book/up/surrogates/01_basics_of_surrogate_models.md`, `02_nn_surrogates.ipynb`, `03_gp_surrogates.ipynb`, `04_gpr_large_data.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Gaussian process]] · [[Sobol indices]] · [[Sensitivity analysis]] · [[Variational inference]] · [[ELBO]]
- [[ME697 2.3 - Surrogates]] · [[ME697 2.4 - Multi-fidelity modeling]] · [[ME697 2.5 - Active learning]]
- [[Multi-fidelity Gaussian process]], [[Kernel composition]], [[Kernel methods]].
