---
type: overview
area: me697
areas: [me697, me539]
source-ref: "ASML (ME 697) book and Intro SciML (ME 539) notebooks"
tags: [uq, inverse-problems, bayesian, sampling, ml]
---

# Examples catalogue

**Summary**: Every worked example and dataset in the two Bilionis books, 136 notebook uses grouped into 60 examples. Pick a task below to see which examples the books use for it. Intro-book toy examples (coin flips, basic probability) are left out. A further 47 examples from lab papers, with source and data links, are in [[#Examples from lab papers]]. A further 51 planned examples that fill the gaps in the [[Dynamical systems table]] are in [[#Planned examples]].

**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book`, `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks`. Raw rows: `wiki/examples/examples.csv`.
**Last updated**: 2026-11-19

---

## By task

### Active learning
[[Active learning test functions]] · [[Branin function]]

### Classification
[[MNIST digits]] · [[Handwritten digits (sklearn)]] · [[Tetris shapes (e3nn)]] · [[HMX drop-weight sensitivity]] · [[CIFAR10]] · [[Steel plates faults]] · [[Floor vibration activity recognition]]

### Clustering
[[MNIST digits]] · [[Steel plates faults]]

### Dimensionality reduction
[[MNIST digits]] · [[SVD image compression]] · [[KLE of Gaussian processes]] · [[Navier-Stokes POD (Wang-Perdikaris)]] · [[SPE10 permeability field]] · [[Steel plates faults]]

### Distribution fitting
[[Fatigue life of 6061-T6 aluminium]] · [[Lake Michigan waves]]

### Dynamical simulation
[[Logistic map]]

### Generative
[[MNIST digits]]

### Inverse problem and calibration
[[Duffing oscillator examples]] · [[Catalysis kinetics]] · [[Gamma density (Laplace)]] · [[Cars on a bumpy road]] · [[Planar arm inverse kinematics]] · [[Harmonic oscillator identifiability]] · [[PK two-compartment IV bolus]] · [[Trailer on a rough road]] · [[Coal mining disasters]] · [[Challenger O-ring]] · [[California earthquakes]] · [[A to B to C reaction]]

### Operator learning
[[Antiderivative operator (DeepONet)]] · [[Burgers 1D operator benchmark]] · [[Darcy flow FNO]]

### Optimization
[[Optimizer test problems]] · [[Branin function]] · [[Bayesian optimisation 1D test function]]

### Physics-informed
[[Manufactured 2D Poisson]] · [[Parametric Poisson]] · [[Neo-Hookean hyperelasticity PINN]] · [[Lagaris benchmarks]]

### Regression
[[Optimizer test problems]] · [[Sparse regression (lasso and ridge)]] · [[Spectral bias 1D regression]] · [[Branin function]] · [[Motorcycle crash (mcycle)]] · [[Challenger O-ring]] · [[MD stress-strain curve]] · [[Chwirut1 ultrasonic calibration]] · [[Airfoil self-noise]]

### Sampling
[[Duffing oscillator examples]] · [[Banana density]] · [[Cars on a bumpy road]] · [[Coal mining disasters]] · [[Challenger O-ring]]

### Sensitivity analysis
[[Duffing oscillator examples]] · [[Lorenz system examples]] · [[Autoinjector FE surrogate]]

### State estimation
[[Duffing oscillator examples]] · [[Object tracking point mass]] · [[Forced damped oscillator (Kalman)]]

### Stochastic simulation
[[Gaussian random walk 2D]] · [[Brownian motion, bridge and sheet]]

### Surrogate modelling
[[Duffing oscillator examples]] · [[Polynomial chaos 1D test functions]] · [[Autoinjector FE surrogate]] · [[Multi-fidelity 2D synthetic function]] · [[Stochastic cylinder flow (multi-fidelity)]] · [[Stochastic 1D heat equation]] · [[Branin function]]

### System identification
[[Duffing oscillator examples]] · [[Lorenz system examples]] · [[Cylinder flow Re 100 (DMD)]] · [[Harmonic oscillator identifiability]] · [[SINDy toy systems]] · [[Tumour growth (GBM)]] · [[Treasury yield (Vasicek)]]

### Uncertainty propagation
[[Duffing oscillator examples]] · [[Lorenz system examples]] · [[Polynomial chaos 1D test functions]] · [[Exponential decay ODE with random inputs]] · [[Stochastic 1D heat equation]] · [[Darcy flow FNO]] · [[Trailer on a rough road]] · [[Robert-Casella integral]]

### Variational inference
[[Autoinjector FE surrogate]] · [[Catalysis kinetics]] · [[Planar arm inverse kinematics]] · [[Challenger O-ring]]

## Real data
[[MNIST digits]] · [[Handwritten digits (sklearn)]] · [[SVD image compression]] · [[Catalysis kinetics]] · [[Tumour growth (GBM)]] · [[Treasury yield (Vasicek)]] · [[SPE10 permeability field]] · [[Darcy flow FNO]] · [[PK two-compartment IV bolus]] · [[Motorcycle crash (mcycle)]] · [[HMX drop-weight sensitivity]] · [[CIFAR10]] · [[Coal mining disasters]] · [[Challenger O-ring]] · [[Fatigue life of 6061-T6 aluminium]] · [[Lake Michigan waves]] · [[California earthquakes]] · [[Steel plates faults]] · [[Chwirut1 ultrasonic calibration]] · [[Airfoil self-noise]] · [[Floor vibration activity recognition]]

## All examples

**How to judge it**: the "suggested" columns are a rule by task that follows lab practice on [[Lab evaluation metrics]] (first two tasks only); they are not what the notebook does. The lab-paper columns are what each paper reports, taken from that page. `examples.csv` holds the same in `metric`, `compared_against` and `judging_basis`. Added 2026-11-22.

| Example | Data | Tasks | Book | Uses | How to judge it (suggested) |
|---|---|---|---|---|---|
| [[A to B to C reaction]] | simulated | inverse problem and calibration | intro | 1 | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Active learning test functions]] | synthetic | active learning | asml | 2 | error vs number of evaluations |
| [[Airfoil self-noise]] | real | regression | intro | 1 | held-out RMSE; KS on PIT if probabilistic |
| [[Antiderivative operator (DeepONet)]] | none | operator learning | asml | 1 | relative L2 on held-out inputs |
| [[Autoinjector FE surrogate]] | simulated | sensitivity analysis, surrogate modelling, variational inference | asml | 3 | indices vs analytic or Monte Carlo values; relative L2 and R² vs the solver |
| [[Banana density]] | analytic | sampling | asml | 3 | split R-hat and ESS; match to the known density |
| [[Bayesian optimisation 1D test function]] | analytic, synthetic | optimization | intro | 2 | distance to the optimum vs evaluations |
| [[Branin function]] | simulated, analytic | surrogate modelling, optimization, active learning, regression | asml, intro | 2 | relative L2 and R² vs the solver; distance to the optimum vs evaluations |
| [[Brownian motion, bridge and sheet]] | analytic | stochastic simulation | asml | 1 | KS between simulated and observed distributions |
| [[Burgers 1D operator benchmark]] | none | operator learning | asml | 1 | relative L2 on held-out inputs |
| [[CIFAR10]] | real | classification | intro | 1 | held-out accuracy or AUC |
| [[California earthquakes]] | real | inverse problem and calibration | intro | 1 | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Cars on a bumpy road]] | synthetic | sampling, inverse problem and calibration | asml | 1 | split R-hat and ESS; match to the known density; posterior match to a NUTS reference; KS on PIT of predictions |
| [[Catalysis kinetics]] | real | inverse problem and calibration, variational inference | asml | 3 | posterior match to a NUTS reference; KS on PIT of predictions; KS vs NUTS samples |
| [[Challenger O-ring]] | real | sampling, inverse problem and calibration, regression, variational inference | intro | 2 | split R-hat and ESS; match to the known density; posterior match to a NUTS reference; KS on PIT of predictions |
| [[Chwirut1 ultrasonic calibration]] | real | regression | intro | 1 | held-out RMSE; KS on PIT if probabilistic |
| [[Coal mining disasters]] | real | sampling, inverse problem and calibration | intro | 1 | split R-hat and ESS; match to the known density; posterior match to a NUTS reference; KS on PIT of predictions |
| [[Cylinder flow Re 100 (DMD)]] | simulated | system identification | asml | 1 | recovered parameters; RMSE on a held-out trajectory |
| [[Darcy flow FNO]] | simulated, real | operator learning, uncertainty propagation | asml | 2 | relative L2 on held-out inputs; error of output mean and variance vs Monte Carlo |
| [[Duffing oscillator examples]] | simulated, synthetic, analytic | uncertainty propagation, surrogate modelling, sensitivity analysis, inverse problem and calibration, system identification, state estimation, sampling | asml, intro | 10 | error of output mean and variance vs Monte Carlo; relative L2 and R² vs the solver |
| [[Exponential decay ODE with random inputs]] | analytic | uncertainty propagation | asml | 3 | error of output mean and variance vs Monte Carlo |
| [[Fatigue life of 6061-T6 aluminium]] | real | distribution fitting | intro | 1 | KS on PIT with a Q-Q plot |
| [[Floor vibration activity recognition]] | real | classification | intro | 1 | held-out accuracy or AUC |
| [[Forced damped oscillator (Kalman)]] | simulated | state estimation | intro | 2 | state RMSE; interval coverage (PICP) |
| [[Gamma density (Laplace)]] | analytic | inverse problem and calibration | asml | 1 | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Gaussian random walk 2D]] | synthetic | stochastic simulation | asml | 1 | KS between simulated and observed distributions |
| [[HMX drop-weight sensitivity]] | real | classification | intro | 4 | held-out accuracy or AUC |
| [[Handwritten digits (sklearn)]] | real | classification | intro | 1 | held-out accuracy or AUC |
| [[Harmonic oscillator identifiability]] | synthetic | inverse problem and calibration, system identification | asml | 1 | posterior match to a NUTS reference; KS on PIT of predictions; recovered parameters; RMSE on a held-out trajectory |
| [[KLE of Gaussian processes]] | analytic | dimensionality reduction | asml | 2 | reconstruction error |
| [[Lagaris benchmarks]] | analytic | physics-informed | intro | 2 | relative L2 vs exact or solver; PDE residual |
| [[Lake Michigan waves]] | real | distribution fitting | intro | 1 | KS on PIT with a Q-Q plot |
| [[Logistic map]] | analytic | dynamical simulation | asml | 1 | trajectory error vs a reference solver |
| [[Lorenz system examples]] | simulated, analytic, synthetic | uncertainty propagation, sensitivity analysis, system identification | asml | 5 | error of output mean and variance vs Monte Carlo; indices vs analytic or Monte Carlo values |
| [[MD stress-strain curve]] | simulated | regression | intro | 1 | held-out RMSE; KS on PIT if probabilistic |
| [[MNIST digits]] | real | classification, dimensionality reduction, generative, clustering | asml, intro | 7 | held-out accuracy or AUC; reconstruction error |
| [[Manufactured 2D Poisson]] | analytic | physics-informed | asml | 3 | relative L2 vs exact or solver; PDE residual |
| [[Motorcycle crash (mcycle)]] | real | regression | intro | 3 | held-out RMSE; KS on PIT if probabilistic |
| [[Multi-fidelity 2D synthetic function]] | synthetic | surrogate modelling | asml | 1 | relative L2 and R² vs the solver |
| [[Navier-Stokes POD (Wang-Perdikaris)]] | simulated | dimensionality reduction | asml | 1 | reconstruction error |
| [[Neo-Hookean hyperelasticity PINN]] | analytic | physics-informed | asml | 1 | relative L2 vs exact or solver; PDE residual |
| [[Object tracking point mass]] | synthetic | state estimation | intro | 2 | state RMSE; interval coverage (PICP) |
| [[Optimizer test problems]] | synthetic, analytic | regression, optimization | asml | 8 | held-out RMSE; KS on PIT if probabilistic; distance to the optimum vs evaluations |
| [[PK two-compartment IV bolus]] | real | inverse problem and calibration | asml | 1 | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Parametric Poisson]] | analytic | physics-informed | asml | 1 | relative L2 vs exact or solver; PDE residual |
| [[Planar arm inverse kinematics]] | synthetic | inverse problem and calibration, variational inference | asml | 1 | posterior match to a NUTS reference; KS on PIT of predictions; KS vs NUTS samples |
| [[Polynomial chaos 1D test functions]] | analytic | surrogate modelling, uncertainty propagation | asml | 5 | relative L2 and R² vs the solver; error of output mean and variance vs Monte Carlo |
| [[Robert-Casella integral]] | analytic | uncertainty propagation | intro | 7 | error of output mean and variance vs Monte Carlo |
| [[SINDy toy systems]] | simulated | system identification | asml | 3 | recovered parameters; RMSE on a held-out trajectory |
| [[SPE10 permeability field]] | real | dimensionality reduction | asml | 1 | reconstruction error |
| [[SVD image compression]] | real | dimensionality reduction | asml | 2 | reconstruction error |
| [[Sparse regression (lasso and ridge)]] | synthetic | regression | asml | 1 | held-out RMSE; KS on PIT if probabilistic |
| [[Spectral bias 1D regression]] | synthetic | regression | asml | 1 | held-out RMSE; KS on PIT if probabilistic |
| [[Steel plates faults]] | real | dimensionality reduction, classification, clustering | intro | 2 | reconstruction error; held-out accuracy or AUC |
| [[Stochastic 1D heat equation]] | simulated | uncertainty propagation, surrogate modelling | asml, intro | 3 | error of output mean and variance vs Monte Carlo; relative L2 and R² vs the solver |
| [[Stochastic cylinder flow (multi-fidelity)]] | simulated | surrogate modelling | asml | 1 | relative L2 and R² vs the solver |
| [[Tetris shapes (e3nn)]] | synthetic | classification | asml | 1 | held-out accuracy or AUC |
| [[Trailer on a rough road]] | analytic, none | uncertainty propagation, inverse problem and calibration | intro | 2 | error of output mean and variance vs Monte Carlo; posterior match to a NUTS reference; KS on PIT of predictions |
| [[Treasury yield (Vasicek)]] | real | system identification | asml | 1 | recovered parameters; RMSE on a held-out trajectory |
| [[Tumour growth (GBM)]] | real | system identification | asml | 1 | recovered parameters; RMSE on a held-out trajectory |

## Examples from lab papers

Examples used in papers by Ilias, Alex, Max, Atharva, Abhishek, Motahareh and Wesley, sorted by spatial dimension. Links were collected by web search on 2026-11-19 and the downloads were not inspected **[unverified]**. "none found" means no public link turned up.

### No spatial dimension

| Example | Over time? | Who | Source | Data / code | In the books | Judged by (in the paper) | Compared against |
|---|---|---|---|---|---|---|---|
| Synthetic OU process with hidden mean | yes | Max, Alex, Ilias | [Diesel PM as OU process (2026)](https://arxiv.org/abs/2603.12356) | [code](https://github.com/PredictiveScienceLab/ou-pm-paper) |  | KS on PIT, Q-Q, σ-band coverage, NRMSE | sparse GP, deep-kernel GP, NN, LSTM, gradient-boosted trees |
| Cummins B6.7L particulate matter | yes | Max, Alex, Ilias | [Diesel PM as OU process (2026)](https://arxiv.org/abs/2603.12356) | none found (proprietary) |  | KS on PIT, Q-Q, σ-band coverage, NRMSE | sparse GP, deep-kernel GP, NN, LSTM, gradient-boosted trees |
| Cummins turbocharger and NOx | yes | Ilias | [Koopman turbine (2022)](https://arxiv.org/abs/2204.10421), [NOx causal GP (2024)](https://arxiv.org/abs/2410.18424), [NOx calibration (2025)](https://arxiv.org/abs/2511.18178) | none found (proprietary) |  | NRMSE, R², MAPE; RMSE, tail percentiles, Q-Q; RMSE, tail percentiles | NARX; RBF GP, ECM sensor; uncalibrated GP |
| Space-habitat thermal twin, 17 states | yes | Ilias | [Bayesian thermal digital twin (2026)](https://arxiv.org/abs/2609.04614) | none found (promised on acceptance) |  | configuration accuracy, posterior probability of the health state, first detection time, time-to-critical 95% interval vs truth, run time; held-out 95% intervals by eye | synthetic truth and one testbed scenario; no other method |
| Pressure leak, synthetic and steel box | yes | Motahareh | [Leakage severity with EKF (2025)](https://doi.org/10.2514/1.J063825) | none found (synthetic case regenerable from stated parameters) |  | detection time, NRMSE, PICP, PINAW | plain EKF |
| Pressure chamber leak | yes | Motahareh | [Rapid leakage estimation (2023)](https://arxiv.org/abs/2212.03372) | none found |  | MAPE, runtime, evaluations | brute-force search |
| HARSH habitat testbed | yes | Motahareh, Ilias | [Communication delays in habitats (2026)](https://ntrs.nasa.gov/citations/20260005281) | none found (data DOI promised, not found) |  | resilience measures HRM, DMN, ABM | delay and interruption settings |
| Motorcycle crash, 94 points | yes | Alex, Ilias | [Mercer-kernel BNN priors (2025)](https://arxiv.org/abs/2510.23745) | [mcycle in R MASS](https://stat.ethz.ch/R-manual/R-devel/library/MASS/html/mcycle.html) | [[Motorcycle crash (mcycle)]] | KS vs GP samples, covariance error | true GP, i.i.d. BNN prior |
| Mauna Loa CO2 | yes | Alex, Ilias | [Mercer-kernel BNN priors (2025)](https://arxiv.org/abs/2510.23745) | [NOAA record](https://gml.noaa.gov/ccgg/trends/) (may differ from the series the paper used) |  | KS vs GP samples, covariance error | true GP, i.i.d. BNN prior |
| NASA fibrous insulation k(T), 51 temperatures | no | Alex, Ilias | [Mercer-kernel BNN priors (2025)](https://arxiv.org/abs/2510.23745) | [NASA report](https://ntrs.nasa.gov/citations/20240003609), [CSV in repo](https://github.com/PredictiveScienceLab/IFT-Thermal-Conductivity-Experiments) |  | KS vs GP samples, covariance error | true GP, i.i.d. BNN prior |
| Damage location (EIT) and 4-DoF arm | no | Ilias | [Amortized VI for inverse problems (2023)](https://arxiv.org/abs/2305.20004) | [code and notebooks](https://github.com/PredictiveScienceLab/paper-2023-inverse-map-karumuri) | [[Planar arm inverse kinematics]] | KS vs NUTS, re-simulation error | NUTS |
| Murine skin hyperelasticity | no | Ilias | [Generative hyperelasticity (2023)](https://arxiv.org/abs/2310.03745) | [data and code](https://github.com/tajtac/node_diffusion) |  | total variation distance | Gaussian mixture, KDE |
| Oxidation curves, 407 | yes | Ilias | [Oxidation mass uptake (2023)](https://arxiv.org/abs/2310.15083) | [refoxdb on nanoHUB](https://nanohub.org/tools/refoxdb/) |  | BIC rank of the original authors' model among 42 fitted models (top for 29%, top three for 44% of 130 alloys at 2.5% noise); MSE and R² per model | the models chosen by the original authors |
| Refractory alloy active learning | no | Ilias | [Alloy active learning (2025)](https://arxiv.org/abs/2512.15958) | [refoxdb](https://nanohub.org/tools/refoxdb/) (new measurements in the paper supplement) |  | measured 24 h mass gain at 1000°C against a 1 mg/cm² target; GP prediction ± σ vs measurement, by eye, for 30 alloys in six batches; two follow-up alloys predicted 0.93 and 0.79, measured 4.76 and 5.87 mg/cm² | own measurements only; starts from 81 literature alloys; no other method |
| Nitrate kinetics | yes | Ilias | [Variational reformulation of inverse problems (2014)](https://arxiv.org/abs/1410.5522) | [code](https://github.com/ebilionis/variational-reformulation-of-inverse-problems) | [[Catalysis kinetics]] | 95% CI, evaluations, wall-clock | MALA, published values |
| Thermal preferences | no | Ilias | [Unimodal GP thermal preferences (2019)](https://arxiv.org/abs/1903.09094) | [code](https://github.com/nawalgao/GPPrefElicit) (survey data not released) |  | distance to optimum, hit rate | random search, logistic regression, SVM |
| Synthetic design functions | no | Ilias | [BODE (2018)](https://arxiv.org/abs/1807.09979), [Bayesian sequential design (2019)](https://arxiv.org/abs/1912.07366) | [BODE code](https://github.com/piyushpandita92/bode), [AdaptiveSDOE](https://github.com/piyushpandita92/AdaptiveSDOE) (AdaptiveSDOE matched by author, not linked in the paper) |  | convergence to the true quantity of interest | uncertainty sampling, EI, PI |
| Steel wire drawing | no | Ilias | [Multi-objective optimization on a budget (2017)](https://arxiv.org/abs/1706.01665) | [toy code only](https://github.com/piyushpandita92/pydes) (simulator not public) |  | Pareto front, Vorob'ev expectation and symmetric deviation, by eye | Monte Carlo reference Pareto front (synthetic); 100-sample average only for wire drawing; no other method |
| Lorenz and Hopf (SINDy) | yes | Atharva, Ilias | [Coding-agent paper replication (2026)](https://arxiv.org/abs/2607.02134) | [replication repo](https://github.com/PredictiveScienceLab/paper-replication-paper), [PySINDy](https://github.com/dynamicslab/pysindy) | [[SINDy toy systems]] | targets matched, discrepancy ratio | the source papers' numbers |
| Dual-moon posterior | no | Wesley | [GitHub repo only, no paper](https://github.com/wesleyjholt/multimodal-examples) | [repo](https://github.com/wesleyjholt/multimodal-examples) |  | none stated in the repository | none stated |
| CF-PEI tensile tests | no | Ilias | [Fiber orientation inference (2022)](https://arxiv.org/abs/2202.12881) | none found |  | surrogate MSE, Q-Q, coverage by eye | experiments only |
| WCA dimer, LJ38, 2D toy potential | no | Ilias | [Free energy by KL minimization (2010)](https://arxiv.org/abs/1011.2416) | none found |  | free-energy curve vs reference, by eye; reduction in KL divergence per added kernel | analytic free energy (toy); dimer potential (WCA); own 1D run vs integrated 2D surface (LJ38); no other method |
| 50 state-capital temperatures | yes | Ilias | [Bayesian reduced-order models (2010)](https://arxiv.org/abs/1001.2753) | none found (paper's link not opened, likely dead) |  | normalized error in identified parameters; posterior mean and 5-95% quantiles vs exact, by eye | reference parameter values, switching linear dynamical system, exact heat-equation solution |

### 1D

| Example | Over time? | Who | Source | Data / code | In the books | Judged by (in the paper) | Compared against |
|---|---|---|---|---|---|---|---|
| Steady heat and cubic nonlinear equation | no | Alex, Ilias | [Physics-informed IFT (2023)](https://arxiv.org/abs/2301.07609) | [code and observation CSVs](https://github.com/PredictiveScienceLab/pift-paper-2023) |  | trust β vs injected model-form error | ground truth |
| Elliptic PDE, log-normal conductivity | no | Ilias | [Simulator-free SPDE solver (2019)](https://arxiv.org/abs/1902.05200) | [code](https://github.com/PredictiveScienceLab/variational-elliptic-SPDE) (data on Purdue SharePoint, not opened) | [[Stochastic 1D heat equation]] | relative L2, R², moment errors | finite-volume solver |
| Heat equation, Wiener-Levy conductivity | no | Ilias | [Amortized VI for inverse problems (2023)](https://arxiv.org/abs/2305.20004) | [code and notebooks](https://github.com/PredictiveScienceLab/paper-2023-inverse-map-karumuri) |  | KS vs NUTS, re-simulation error | NUTS |
| Burgers and Schrodinger (Raissi PINNs) | yes | Atharva, Ilias | [Coding-agent paper replication (2026)](https://arxiv.org/abs/2607.02134) | [Raissi PINNs data](https://github.com/maziarraissi/PINNs) |  | targets matched, discrepancy ratio | the source papers' numbers |
| Poisson with Brownian bridge prior | no | Alex, Ilias | [Brownian bridge prior for Poisson (2025)](https://arxiv.org/abs/2503.00213) | none found | [[Brownian motion, bridge and sheet]] | none (proof) | none |
| Heat equation, probabilistic solver | no | Ilias | [Probabilistic PDE solvers (2016)](https://arxiv.org/abs/1607.03526) | none found |  | predicted discretization error (2σ) vs exact absolute error, by eye | exact solution, fine finite-difference solve |
| Granular crystal chain (placement uncertain) | yes | Ilias | [GP dimensionality reduction (2016)](https://arxiv.org/abs/1602.04550), [Deep active subspaces (2019)](https://arxiv.org/abs/1902.10527) | [py-aspgp](https://github.com/PredictiveScienceLab/py-aspgp) (repo matched by name) |  | RMSE, recovered subspace | gradient-based active subspaces |

### 2D

| Example | Over time? | Who | Source | Data / code | In the books | Judged by (in the paper) | Compared against |
|---|---|---|---|---|---|---|---|
| Elliptic PDE, log-normal and channelized fields | no | Ilias | [Simulator-free SPDE solver (2019)](https://arxiv.org/abs/1902.05200) | [code](https://github.com/PredictiveScienceLab/variational-elliptic-SPDE), [channelized data](https://github.com/cics-nd/pde-surrogate) |  | relative L2, R², moment errors | finite-volume solver |
| Elliptic PDE, DNN surrogate | no | Ilias | [Deep UQ (2018)](https://arxiv.org/abs/1802.00850) | [code](https://github.com/rohitkt10/deep-uq-paper) |  | relative error, R², mean and std field error | finite-volume solver, Monte Carlo |
| Elliptic PDE, active subspaces | no | Ilias | [GP dimensionality reduction (2016)](https://arxiv.org/abs/1602.04550), [Deep active subspaces (2019)](https://arxiv.org/abs/1902.10527) | [py-aspgp](https://github.com/PredictiveScienceLab/py-aspgp), [dataset repo](https://github.com/paulcon/as-data-sets) (dataset folder may have moved) |  | RMSE, recovered subspace | gradient-based active subspaces |
| Allen-Cahn, bimodal (steady placement uncertain) | no | Alex, Ilias | [Physics-informed IFT (2023)](https://arxiv.org/abs/2301.07609) | [notebook](https://github.com/PredictiveScienceLab/pift-paper-2023) |  | trust β vs injected model-form error | ground truth |
| Insulation thermal conductivity, ABAQUS twin | yes | Alex, Ilias | [IFT thermal conductivity (2026)](https://arxiv.org/abs/2601.15427) | [data and code](https://github.com/PredictiveScienceLab/IFT-Thermal-Conductivity-Experiments) (ABAQUS licence needed) |  | MSE and max error, 95% CI | NASA reference conductivity |
| Navier-Stokes cylinder wake (Raissi PINNs) | yes | Atharva, Ilias | [Coding-agent paper replication (2026)](https://arxiv.org/abs/2607.02134) | [Raissi PINNs data](https://github.com/maziarraissi/PINNs) | [[Cylinder flow Re 100 (DMD)]] | targets matched, discrepancy ratio | the source papers' numbers |
| Contaminant source (time placement uncertain) | yes | Ilias | [Variational reformulation of inverse problems (2014)](https://arxiv.org/abs/1410.5522) | [code](https://github.com/ebilionis/variational-reformulation-of-inverse-problems) |  | 95% CI, evaluations, wall-clock | MALA, published values |
| Skin flaps | no | Ilias | [Reconstructive surgery GP (2020)](https://arxiv.org/abs/2010.02800) | [repo](https://bitbucket.org/abuganzatepole/gp_anisotropy) (repo contents not opened) |  | relative L2, share under 0.1 | finite-element solves |
| Poisson, analytic | no | Alex, Ilias | [MAP uniqueness in PIFT (2024)](https://arxiv.org/abs/2401.14224) | none found | [[Manufactured 2D Poisson]] | none (proof) | none |
| Electromagnet PINN | no | Ilias | [Parametric magnetostatics PINN (2022)](https://arxiv.org/abs/2202.04041) | none found |  | relative L2 percentiles, force error | finite-element solver |
| Oil well placement on SPE10 (placement uncertain) | no | Ilias | [Extended expected improvement (2016)](https://arxiv.org/abs/1604.01147) | none found (SPE10's public home not looked up) | [[SPE10 permeability field]] | 95% bounds on the optimum and maximum EEI vs iteration, by eye | known optimum of two synthetic problems; none for the oil-well problem; no other method |

### 3D

| Example | Over time? | Who | Source | Data / code | In the books | Judged by (in the paper) | Compared against |
|---|---|---|---|---|---|---|---|
| Brindise in-vitro aneurysm flow | yes | Atharva, Abhishek, Ilias | [3D particle reconstruction (2024)](https://doi.org/10.1088/1361-6501/ad6624), [UOT particle tracking (2024)](https://arxiv.org/abs/2407.04583) | [particle velocimetry](https://doi.org/10.4231/M5F1-QC84), [MRI](https://doi.org/10.4231/C6DE-N845), [CFD](https://doi.org/10.4231/5RW6-4Z50) (Purdue PURR, CC0; zips not inspected) |  | yield and reliability rates; detection rate, ghost fraction, RMS pixel error [unverified] | own ablations; synthetic truth, Poiseuille flow |
| Aneurysm growth, 19 public aneurysms | yes | Atharva, Ilias | [Aneurysm growth detection (2026)](https://arxiv.org/abs/2604.06649) | [OpenNeuro ds005096](https://openneuro.org/datasets/ds005096) (paper does not say which 19) |  | AUC, Cohen's κ, LOOCV, ICC | volumetric clinical rule, three raters |
| Aneurysm growth, UCSF 42 | yes | Atharva, Ilias | [Aneurysm growth detection (2026)](https://arxiv.org/abs/2604.06649) | none found (not public) |  | AUC, Cohen's κ, LOOCV, ICC | volumetric clinical rule, three raters |
| Synthetic aneurysm CFD, Poiseuille tube, in-vivo patient | yes | Atharva, Abhishek, Ilias | [SMURF 4D-flow MRI (2025)](https://arxiv.org/abs/2505.12494), [VAST 4D-flow MRI (2026)](https://arxiv.org/abs/2601.13393) | none found |  | Dice, surface distance, divergence and momentum residuals; Dice, Jaccard, RMSE, SSIM, divergence | MedSAM2, Tempus; PCD, SDM, CFD |
| Burgers vortex, 3,000 particles | yes | Atharva, Ilias | [UOT particle tracking (2024)](https://arxiv.org/abs/2407.04583) | none found (generated in the paper) |  | yield and reliability rates | own ablations |
| Pipe flow, Re 630 | yes | Atharva | [3D particle reconstruction (2024)](https://doi.org/10.1088/1361-6501/ad6624) | none found (journal's data statement not read) |  | detection rate, ghost fraction, RMS pixel error [unverified] | synthetic truth, Poiseuille flow |

## Planned examples

Not built yet. Each fills a gap in the [[Dynamical systems table]] and has its own page. Every link was opened by script on 2026-11-19; "resolved" means the page loaded, not that the contents were read. Models and papers on the pages are **[unverified]**.

| Example | Gap filled | Data | Links | Link check | How to judge it (suggested) |
|---|---|---|---|---|---|
| [[Lévy-process asset returns]] | Jump process | real | [Kenneth French daily market factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions; KS between simulated and observed distributions |
| [[Lévy option-smile calibration]] | Jump process | real | [CBOE delayed SPX option chain](https://cdn.cboe.com/api/global/delayed_quotes/options/_SPX.json) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Merton and Kou jump-diffusion]] | Jump noise | real | [Kenneth French daily market factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [FRED SP500 (last 10 years)](https://fred.stlouisfed.org/series/SP500) | FRED SP500 (last 10 years): timed out for a script; open in a browser | posterior match to a NUTS reference; KS on PIT of predictions; KS between simulated and observed distributions |
| [[Bates stochastic volatility with jumps]] | Jump noise | real | [FRED VIXCLS](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [Kenneth French daily market factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip) | FRED VIXCLS: timed out for a script; open in a browser | posterior match to a NUTS reference; KS on PIT of predictions; state RMSE; interval coverage (PICP) |
| [[Intraday jumps (Bitcoin 1-minute)]] | Jump noise | real | [Binance public klines](https://data.binance.vision/data/spot/daily/klines/BTCUSDT/1m/BTCUSDT-1m-2024-01-02.zip) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Nagel-Schreckenberg traffic]] | Cellular automaton | real | [NGSIM vehicle trajectories](https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions; trajectory error vs a reference solver |
| [[Wildfire spread cellular automaton]] | Cellular automaton | real | [NIFC fire perimeters](https://data-nifc.opendata.arcgis.com/datasets/nifc::wfigs-interagency-fire-perimeters/about); [Grieshop and Wikle 2023](https://arxiv.org/abs/2306.03214) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions; trajectory error vs a reference solver |
| [[RC thermal network (ecobee homes)]] | Hybrid / non-smooth | real | [ecobee Donate Your Data (OSTI record)](https://www.osti.gov/biblio/1854924) | all resolved | recovered parameters; RMSE on a held-out trajectory; state RMSE; interval coverage (PICP) |
| [[RC thermal network (NIST Net-Zero house)]] | Hybrid / non-smooth | real | [NIST Net-Zero data](https://pages.nist.gov/netzero/data.html) | all resolved | recovered parameters; RMSE on a held-out trajectory; state RMSE; interval coverage (PICP) |
| [[RC thermal network (Twin Houses)]] | Hybrid / non-smooth | real | [Twin Houses, Fraunhofer (CC BY-SA 4.0)](https://fordatis.fraunhofer.de/handle/fordatis/161); [Twin Houses experiment 1, Strathclyde (CC BY 4.0)](https://pureportal.strath.ac.uk/en/datasets/twin-houses-empirical-dataset-experiment-1) | all resolved | recovered parameters; RMSE on a held-out trajectory |
| [[Dry friction (EMPS rig)]] | Hybrid / non-smooth | real | [EMPS benchmark](https://www.nonlinearbenchmark.org/benchmarks/emps); [nonlinear_benchmarks loader](https://github.com/MaartenSchoukens/nonlinear_benchmarks) | all resolved | recovered parameters; RMSE on a held-out trajectory |
| [[Stick-slip laboratory earthquake]] | Hybrid / non-smooth | real | [LANL earthquake data on Kaggle](https://www.kaggle.com/c/LANL-Earthquake-Prediction/data); [Johnson et al. 2021](https://doi.org/10.1073/pnas.2011362118) | LANL earthquake data on Kaggle: page loads; download needs a Kaggle login; Johnson et al. 2021: publisher bot wall (403); not read | state RMSE; interval coverage (PICP) |
| [[Stochastic PDEs in time]] | SPDE in time | synthetic | [torchspde](https://github.com/crispitagorico/torchspde); [OSF copy](https://osf.io/ahn6v/); [Neural SPDEs paper](https://arxiv.org/abs/2110.10249) | OSF copy: page loads, but the OSF API asks for a login; may be private | KS between simulated and observed distributions; relative L2 on held-out inputs |
| [[Ammonia inversion (double-well tunnelling)]] | Quantum | real | [JPL catalogue entry 17002](https://spec.jpl.nasa.gov/ftp/pub/catalog/doc/d017002.cat) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Rabi oscillation (trapped ion)]] | Quantum | real | [Zenodo record 15797402](https://zenodo.org/records/15797402) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Kuramoto oscillators (power grid)]] | Interacting particles | real | [Power grid frequency database](https://osf.io/by5hu/); [Rydin Gorjão et al. 2020](https://arxiv.org/abs/2006.01771) | all resolved | recovered parameters; RMSE on a held-out trajectory; posterior match to a NUTS reference; KS on PIT of predictions |
| [[Flocking (schooling fish)]] | Interacting particles | real | [Schooling-fish trajectories, Zenodo 10890112](https://zenodo.org/records/10890112); [Paper](https://arxiv.org/abs/2305.17108); [Chimney swift flock (3D, 897 MB)](https://zenodo.org/record/5084183); [Jülich pedestrian archive](https://ped.fz-juelich.de/da/doku.php) | all resolved | recovered parameters; RMSE on a held-out trajectory |
| [[Fermi-Pasta-Ulam-Tsingou chain]] | Interacting particles | synthetic | [Dauxois 2008 (history)](https://arxiv.org/abs/0801.1590) | all resolved | trajectory error vs a reference solver |
| [[Double pendulum]] | Conservative | real | [IBM double pendulum chaotic dataset](https://developer.ibm.com/exchanges/data/all/double-pendulum-chaotic/) | IBM double pendulum chaotic dataset: landing page loads, but the project page is gone and the download host does not resolve; the data may no longer be downloadable | recovered parameters; RMSE on a held-out trajectory; trajectory error vs a reference solver |
| [[Two-body orbit (S2 star)]] | Conservative | real | [Gillessen et al. 2017](https://arxiv.org/abs/1611.09144); [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Hénon-Heiles]] | Conservative | synthetic | none | no links | trajectory error vs a reference solver |
| [[Old Faithful eruptions (Markov chain)]] | Markov chain | real | [R faithful](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/faithful.html) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Wet and dry day rainfall chain]] | Markov chain | real | [NOAA GHCN-Daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions; KS between simulated and observed distributions |
| [[Ion-channel gating (hidden Markov model)]] | Markov chain | real | [R ionChannelData](https://rolfturner.r-universe.dev/ionChannelData) | R ionChannelData: page refuses scripts (403); the r-universe API confirms the package, version 0.0-3 | state RMSE; interval coverage (PICP); posterior match to a NUTS reference; KS on PIT of predictions |
| [[Earthquake counts (Poisson hidden Markov model)]] | Markov chain | real | [hmmlearn example with the counts](https://hmmlearn.readthedocs.io/en/stable/auto_examples/plot_poisson_hmm.html) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Ising model (retina spikes)]] | Markov chain | real | [ISTA record 5562](https://research-explorer.ista.ac.at/record/5562) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions; split R-hat and ESS; match to the known density |
| [[Earthquake aftershocks (Hawkes, ETAS)]] | Point process | real | [USGS ComCat API](https://earthquake.usgs.gov/fdsnws/event/1/); [R PtProcess catalogues](https://cran.r-project.org/web/packages/PtProcess/index.html); [R ETAS fitter](https://cran.r-project.org/web/packages/ETAS/index.html) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Nicholson's blowflies (delayed logistic)]] | Delay / memory | real | [pomp blowflies](https://kingaa.github.io/manuals/pomp/html/blowflies.html) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions; recovered parameters; RMSE on a held-out trajectory |
| [[ENSO delayed oscillator]] | Delay / memory | real | [NOAA CPC indices](https://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Mackey-Glass]] | Delay / memory | synthetic | none | no links | trajectory error vs a reference solver |
| [[Generalised Langevin equation]] | Delay / memory | synthetic | none | no links | KS between simulated and observed distributions; recovered parameters; RMSE on a held-out trajectory |
| [[Power-grid swing dynamics]] | Differential-algebraic | real | [ISO-NE oscillation cases](https://web.eecs.utk.edu/~kaisun/Oscillation/actualcases.html) | all resolved | recovered parameters; RMSE on a held-out trajectory |
| [[Tennessee Eastman process]] | Differential-algebraic | synthetic | [Rieth et al. dataset, Harvard Dataverse](https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId=doi:10.7910/DVN/6C3JR1) | all resolved | state RMSE; interval coverage (PICP); held-out accuracy or AUC |
| [[Constrained pendulum and RLC circuit]] | Differential-algebraic | synthetic | none | no links | trajectory error vs a reference solver |
| [[Tides (quasi-periodic)]] | Quasi-periodic | real | [NOAA CO-OPS API](https://api.tidesandcurrents.noaa.gov/api/prod/) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Blazhko RR Lyrae stars]] | Quasi-periodic | real | [Kepler at MAST](https://archive.stsci.edu/missions-and-data/kepler) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Sunspot cycle]] | Quasi-periodic | real | [SILSO data files](https://www.sidc.be/SILSO/datafiles) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Torus flow, circle map and standard map]] | Quasi-periodic | synthetic | none | no links | trajectory error vs a reference solver |
| [[FitzHugh-Nagumo (neuron voltage)]] | Multiscale / stiff | real | [Allen Cell Types database](https://celltypes.brain-map.org/) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions; recovered parameters; RMSE on a held-out trajectory |
| [[Oregonator (Belousov-Zhabotinsky reaction)]] | Multiscale / stiff | real | [Lathrop and Kostelich series (UMD)](https://complex.umd.edu/data.html) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions; recovered parameters; RMSE on a held-out trajectory |
| [[Stiff ODE test problems]] | Multiscale / stiff | synthetic | none | no links | trajectory error vs a reference solver |
| [[Van der Pol oscillator]] | Canonical | synthetic | [Silverbox benchmark](https://www.nonlinearbenchmark.org/benchmarks/silverbox); [Circuit paper, no data](https://arxiv.org/abs/1904.11289) | all resolved | recovered parameters; RMSE on a held-out trajectory; trajectory error vs a reference solver |
| [[Lotka-Volterra (lynx and hare)]] | Canonical | real | [Stan CSV, 1900-1920](https://raw.githubusercontent.com/stan-dev/example-models/master/knitr/lotka-volterra/hudson-bay-lynx-hare.csv); [R pelt, 1845-1935](https://tsibbledata.tidyverts.org/reference/pelt.html); [Stan case study](https://mc-stan.org/learn-stan/case-studies/lotka-volterra-predator-prey.html) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[SIR epidemic (boarding school influenza)]] | Canonical | real | [Boarding-school influenza data](https://r-packages.io/datasets/influenza_england_1978_school); [Eyam plague 1666 (8 rows)](https://rdrr.io/cran/MultiBD/man/Eyam.html) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Double-well SDE (ice-core record)]] | Canonical | real | [NGRIP d18O (NOAA)](https://www.ncei.noaa.gov/pub/data/paleo/icecore/greenland/summit/ngrip/gicc05-20yr.txt) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions; recovered parameters; RMSE on a held-out trajectory |
| [[Kuramoto-Sivashinsky]] | Canonical | synthetic | none | no links | trajectory error vs a reference solver; relative L2 on held-out inputs |
| [[Wave equation]] | Canonical | real | [Bowed cello string, Zenodo 1302894](https://doi.org/10.5281/zenodo.1302894); [SAGE seismic data centre](https://ds.iris.edu/ds/nodes/dmc/data/) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions |
| [[Fisher-KPP (scratch assay)]] | Canonical | real | [BINNs repository](https://github.com/jlager/BINNs); [Lagergren et al. 2020](https://arxiv.org/abs/2005.13073) | all resolved | posterior match to a NUTS reference; KS on PIT of predictions; relative L2 vs exact or solver; PDE residual |
| [[Gray-Scott]] | Canonical | synthetic | [xmorphia reference patterns](https://www.mrob.com/pub/comp/xmorphia/) | all resolved | trajectory error vs a reference solver |
| [[Korteweg-de Vries]] | Canonical | synthetic | none | no links | trajectory error vs a reference solver |
| [[Lorenz 96]] | Canonical | synthetic | [DAPPER](https://github.com/nansencenter/DAPPER) | all resolved | state RMSE; interval coverage (PICP); trajectory error vs a reference solver |

## Related pages
- [[Dynamical systems table]]
- [[Planned and stub examples]]
