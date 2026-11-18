---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [uq, ml, vi, bayesian]
data-origin: [simulated]
tasks: [sensitivity analysis, surrogate modelling, variational inference]
uses: 3
---

# Autoinjector FE surrogate

**Summary**: 3 uses in ASML (ME 697). Data: simulated. Tasks: sensitivity analysis, surrogate modelling, variational inference.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/up/surrogates/02_nn_surrogates.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Autoinjector FE model surrogate (neural network + Sobol)

`text_books/advanced-scientific-machine-learning/book/up/surrogates/02_nn_surrogates.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: surrogate modelling; sensitivity analysis
- **Technique**: Equinox MLP (width 100, depth 5), Adam lr 1e-3, batch 128, 5000 iterations, 10% validation split; inputs standardized, injection time and max acceleration log-transformed then standardized; dataset sizes 100/1000/2500/5000/9000 tried; Sobol indices via SALib (N=512, calc_second_order=False) on the N=9000 surrogate
- **Data**: Samples of a multi-hour finite-element biomechanical model of an autoinjector (Sree et al. 2023). 10 inputs: mu (viscosity), fill_volume, hGap0, lNeedle, dNeedle, FSpring0, kSpring, kappa5, kappa6, kappa7. 4 outputs: needle displacement (m), injection time (s), max acceleration (m/s^2), max deceleration (m/s^2).
- **Data origin**: simulated
- **Data file**: data/autoinjector_surrogate/training_data.xlsx (10000 rows x 14 cols, first col index) and test_data.xlsx (500 x 14)
- **Forward model**: Expensive FE autoinjector model, treated as black box mapping 10 inputs to 4 outputs; not available as code in the notebook.
- **Unknown dimension**: 10 inputs
- **Data dimension**: 4 outputs per sample; 10000 training, 500 test
- **Ground truth**: held-out test set of 500 FE samples; no numeric RMSE in the notebook text
- **What makes it hard**: expensive simulator, 10 inputs with very different sensitivities, multi-output
- **Libraries**: jax (x64), equinox, optax, SALib, pandas
- **References**: Sree et al. 2023, https://doi.org/10.1016/j.jmbbm.2023.105695
- **Notes**: Notebook says surrogate is 'pretty good' at 2000+ points. Sobol result: injection time very sensitive to viscosity and needle diameter, somewhat to needle length and spring force. Input bounds are used for Sobol sampling: 10 inputs (viscosity [1,20], fill volume [1,1.05], air gap [4,5], needle length [8,15.9], needle diameter [0.133,0.21], spring force [18,36], spring constant [150,250], kappa5 [0,3], kappa6 [0,4], kappa7 [0,0.1])

## Autoinjector FE model surrogate (exact GP)

`text_books/advanced-scientific-machine-learning/book/up/surrogates/03_gp_surrogates.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: surrogate modelling
- **Technique**: independent ARD RBF GP per output (tinygp): log_amplitude, 10 log_lengthscales, log_noise_variance; hyperparameters by minibatch Adam on negative marginal likelihood (lr 1e-2, 1000 iterations, batch 100) using 200 points; diagnostics: parity, standardized errors, QQ, residuals; convergence study N=50,100,200,500,1000,2000
- **Data**: Samples of a multi-hour finite-element biomechanical model of an autoinjector (Sree et al. 2023). 10 inputs: mu (viscosity), fill_volume, hGap0, lNeedle, dNeedle, FSpring0, kSpring, kappa5, kappa6, kappa7. 4 outputs: needle displacement (m), injection time (s), max acceleration (m/s^2), max deceleration (m/s^2).
- **Data origin**: simulated
- **Data file**: same autoinjector xlsx files, loaded from GitHub raw URLs
- **Forward model**: Expensive FE autoinjector model, treated as black box mapping 10 inputs to 4 outputs; not available as code in the notebook.
- **Unknown dimension**: 10 inputs, 12 GP hyperparameter values per output
- **Data dimension**: 4 outputs; up to 2000 training points
- **Ground truth**: held-out test set of 500
- **What makes it hard**: O(n^3) GP cost limits N
- **Libraries**: jax, tinygp, optax, pandas
- **References**: Sree et al. 2023, https://doi.org/10.1016/j.jmbbm.2023.105695
- **Notes**: Notebook: most outputs need only a few hundred points; needle displacement needs more data or inductive biases. Possible bug: the convergence loop builds GPs with trained_params from the 200-point fit rather than the per-N fits.

## Autoinjector FE model surrogate (sparse variational GP)

`text_books/advanced-scientific-machine-learning/book/up/surrogates/04_gpr_large_data.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: surrogate modelling (large data)
- **Technique**: sparse variational GP, GPJax 0.9.3: VariationalGaussian with 100 inducing points, ELBO, Adam lr 1e-3, 50000 iterations, batch 32; trained on one output (needle_displacement_m). Exact GP on all 10000 points crashes (O(n^3)); that cell is commented out
- **Data**: Samples of a multi-hour finite-element biomechanical model of an autoinjector (Sree et al. 2023). 10 inputs: mu (viscosity), fill_volume, hGap0, lNeedle, dNeedle, FSpring0, kSpring, kappa5, kappa6, kappa7. 4 outputs: needle displacement (m), injection time (s), max acceleration (m/s^2), max deceleration (m/s^2).
- **Data origin**: simulated
- **Data file**: same autoinjector xlsx files (training_data.xlsx 10000 x 14)
- **Forward model**: Expensive FE autoinjector model, treated as black box mapping 10 inputs to 4 outputs; not available as code in the notebook.
- **Unknown dimension**: 10 inputs
- **Data dimension**: 1 output used; 10000 training points
- **Ground truth**: intended held-out test set
- **What makes it hard**: large N for GPs
- **Libraries**: jax, gpjax 0.9.3, optax
- **References**: Sree et al. 2023, https://doi.org/10.1016/j.jmbbm.2023.105695
- **Notes**: Bug: test_data_url points at training_data.xlsx so 'test' equals train. Inducing points are 100 linspaced per feature (on a diagonal), not space-filling.

## Related pages
- [[Examples catalogue]]
- [[Variational inference]] · [[ELBO]] · [[Sobol indices]] · [[Gaussian process]] · [[Surrogate model]] · [[Sensitivity analysis]] · [[Adam]]
