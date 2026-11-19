---
type: overview
area: me697
areas: [me697, me539]
source-ref: "ASML (ME 697) book and Intro SciML (ME 539) notebooks"
tags: [uq, inverse-problems, bayesian, sampling, ml]
---

# Examples catalogue

**Summary**: Every worked example and dataset in the two Bilionis books, 136 notebook uses grouped into 60 examples. Pick a task below to see which examples the books use for it. Intro-book toy examples (coin flips, basic probability) are left out. A further 47 examples from lab papers, with source and data links, are in [[#Examples from lab papers]].

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

| Example | Data | Tasks | Book | Uses |
|---|---|---|---|---|
| [[A to B to C reaction]] | simulated | inverse problem and calibration | intro | 1 |
| [[Active learning test functions]] | synthetic | active learning | asml | 2 |
| [[Airfoil self-noise]] | real | regression | intro | 1 |
| [[Antiderivative operator (DeepONet)]] | none | operator learning | asml | 1 |
| [[Autoinjector FE surrogate]] | simulated | sensitivity analysis, surrogate modelling, variational inference | asml | 3 |
| [[Banana density]] | analytic | sampling | asml | 3 |
| [[Bayesian optimisation 1D test function]] | analytic, synthetic | optimization | intro | 2 |
| [[Branin function]] | simulated, analytic | surrogate modelling, optimization, active learning, regression | asml, intro | 2 |
| [[Brownian motion, bridge and sheet]] | analytic | stochastic simulation | asml | 1 |
| [[Burgers 1D operator benchmark]] | none | operator learning | asml | 1 |
| [[CIFAR10]] | real | classification | intro | 1 |
| [[California earthquakes]] | real | inverse problem and calibration | intro | 1 |
| [[Cars on a bumpy road]] | synthetic | sampling, inverse problem and calibration | asml | 1 |
| [[Catalysis kinetics]] | real | inverse problem and calibration, variational inference | asml | 3 |
| [[Challenger O-ring]] | real | sampling, inverse problem and calibration, regression, variational inference | intro | 2 |
| [[Chwirut1 ultrasonic calibration]] | real | regression | intro | 1 |
| [[Coal mining disasters]] | real | sampling, inverse problem and calibration | intro | 1 |
| [[Cylinder flow Re 100 (DMD)]] | simulated | system identification | asml | 1 |
| [[Darcy flow FNO]] | simulated, real | operator learning, uncertainty propagation | asml | 2 |
| [[Duffing oscillator examples]] | simulated, synthetic, analytic | uncertainty propagation, surrogate modelling, sensitivity analysis, inverse problem and calibration, system identification, state estimation, sampling | asml, intro | 10 |
| [[Exponential decay ODE with random inputs]] | analytic | uncertainty propagation | asml | 3 |
| [[Fatigue life of 6061-T6 aluminium]] | real | distribution fitting | intro | 1 |
| [[Floor vibration activity recognition]] | real | classification | intro | 1 |
| [[Forced damped oscillator (Kalman)]] | simulated | state estimation | intro | 2 |
| [[Gamma density (Laplace)]] | analytic | inverse problem and calibration | asml | 1 |
| [[Gaussian random walk 2D]] | synthetic | stochastic simulation | asml | 1 |
| [[HMX drop-weight sensitivity]] | real | classification | intro | 4 |
| [[Handwritten digits (sklearn)]] | real | classification | intro | 1 |
| [[Harmonic oscillator identifiability]] | synthetic | inverse problem and calibration, system identification | asml | 1 |
| [[KLE of Gaussian processes]] | analytic | dimensionality reduction | asml | 2 |
| [[Lagaris benchmarks]] | analytic | physics-informed | intro | 2 |
| [[Lake Michigan waves]] | real | distribution fitting | intro | 1 |
| [[Logistic map]] | analytic | dynamical simulation | asml | 1 |
| [[Lorenz system examples]] | simulated, analytic, synthetic | uncertainty propagation, sensitivity analysis, system identification | asml | 5 |
| [[MD stress-strain curve]] | simulated | regression | intro | 1 |
| [[MNIST digits]] | real | classification, dimensionality reduction, generative, clustering | asml, intro | 7 |
| [[Manufactured 2D Poisson]] | analytic | physics-informed | asml | 3 |
| [[Motorcycle crash (mcycle)]] | real | regression | intro | 3 |
| [[Multi-fidelity 2D synthetic function]] | synthetic | surrogate modelling | asml | 1 |
| [[Navier-Stokes POD (Wang-Perdikaris)]] | simulated | dimensionality reduction | asml | 1 |
| [[Neo-Hookean hyperelasticity PINN]] | analytic | physics-informed | asml | 1 |
| [[Object tracking point mass]] | synthetic | state estimation | intro | 2 |
| [[Optimizer test problems]] | synthetic, analytic | regression, optimization | asml | 8 |
| [[PK two-compartment IV bolus]] | real | inverse problem and calibration | asml | 1 |
| [[Parametric Poisson]] | analytic | physics-informed | asml | 1 |
| [[Planar arm inverse kinematics]] | synthetic | inverse problem and calibration, variational inference | asml | 1 |
| [[Polynomial chaos 1D test functions]] | analytic | surrogate modelling, uncertainty propagation | asml | 5 |
| [[Robert-Casella integral]] | analytic | uncertainty propagation | intro | 7 |
| [[SINDy toy systems]] | simulated | system identification | asml | 3 |
| [[SPE10 permeability field]] | real | dimensionality reduction | asml | 1 |
| [[SVD image compression]] | real | dimensionality reduction | asml | 2 |
| [[Sparse regression (lasso and ridge)]] | synthetic | regression | asml | 1 |
| [[Spectral bias 1D regression]] | synthetic | regression | asml | 1 |
| [[Steel plates faults]] | real | dimensionality reduction, classification, clustering | intro | 2 |
| [[Stochastic 1D heat equation]] | simulated | uncertainty propagation, surrogate modelling | asml, intro | 3 |
| [[Stochastic cylinder flow (multi-fidelity)]] | simulated | surrogate modelling | asml | 1 |
| [[Tetris shapes (e3nn)]] | synthetic | classification | asml | 1 |
| [[Trailer on a rough road]] | analytic, none | uncertainty propagation, inverse problem and calibration | intro | 2 |
| [[Treasury yield (Vasicek)]] | real | system identification | asml | 1 |
| [[Tumour growth (GBM)]] | real | system identification | asml | 1 |

## Examples from lab papers

Examples used in papers by Ilias, Alex, Max, Atharva, Abhishek, Motahareh and Wesley, sorted by spatial dimension. Links were collected by web search on 2026-11-19 and the downloads were not inspected **[unverified]**. "none found" means no public link turned up.

### No spatial dimension

| Example | Over time? | Who | Source | Data / code | In the books |
|---|---|---|---|---|---|
| Synthetic OU process with hidden mean | yes | Max, Alex, Ilias | [Diesel PM as OU process (2026)](https://arxiv.org/abs/2603.12356) | [code](https://github.com/PredictiveScienceLab/ou-pm-paper) |  |
| Cummins B6.7L particulate matter | yes | Max, Alex, Ilias | [Diesel PM as OU process (2026)](https://arxiv.org/abs/2603.12356) | none found (proprietary) |  |
| Cummins turbocharger and NOx | yes | Ilias | [Koopman turbine (2022)](https://arxiv.org/abs/2204.10421), [NOx causal GP (2024)](https://arxiv.org/abs/2410.18424), [NOx calibration (2025)](https://arxiv.org/abs/2511.18178) | none found (proprietary) |  |
| Space-habitat thermal twin, 17 states | yes | Ilias | [Bayesian thermal digital twin (2026)](https://arxiv.org/abs/2609.04614) | none found (promised on acceptance) |  |
| Pressure leak, synthetic and steel box | yes | Motahareh | [Leakage severity with EKF (2025)](https://doi.org/10.2514/1.J063825) | none found (synthetic case regenerable from stated parameters) |  |
| Pressure chamber leak | yes | Motahareh | [Rapid leakage estimation (2023)](https://arxiv.org/abs/2212.03372) | none found |  |
| HARSH habitat testbed | yes | Motahareh, Ilias | [Communication delays in habitats (2026)](https://ntrs.nasa.gov/citations/20260005281) | none found (data DOI promised, not found) |  |
| Motorcycle crash, 94 points | yes | Alex, Ilias | [Mercer-kernel BNN priors (2025)](https://arxiv.org/abs/2510.23745) | [mcycle in R MASS](https://stat.ethz.ch/R-manual/R-devel/library/MASS/html/mcycle.html) | [[Motorcycle crash (mcycle)]] |
| Mauna Loa CO2 | yes | Alex, Ilias | [Mercer-kernel BNN priors (2025)](https://arxiv.org/abs/2510.23745) | [NOAA record](https://gml.noaa.gov/ccgg/trends/) (may differ from the series the paper used) |  |
| NASA fibrous insulation k(T), 51 temperatures | no | Alex, Ilias | [Mercer-kernel BNN priors (2025)](https://arxiv.org/abs/2510.23745) | [NASA report](https://ntrs.nasa.gov/citations/20240003609), [CSV in repo](https://github.com/PredictiveScienceLab/IFT-Thermal-Conductivity-Experiments) |  |
| Damage location (EIT) and 4-DoF arm | no | Ilias | [Amortized VI for inverse problems (2023)](https://arxiv.org/abs/2305.20004) | [code and notebooks](https://github.com/PredictiveScienceLab/paper-2023-inverse-map-karumuri) | [[Planar arm inverse kinematics]] |
| Murine skin hyperelasticity | no | Ilias | [Generative hyperelasticity (2023)](https://arxiv.org/abs/2310.03745) | [data and code](https://github.com/tajtac/node_diffusion) |  |
| Oxidation curves, 407 | yes | Ilias | [Oxidation mass uptake (2023)](https://arxiv.org/abs/2310.15083) | [refoxdb on nanoHUB](https://nanohub.org/tools/refoxdb/) |  |
| Refractory alloy active learning | no | Ilias | [Alloy active learning (2025)](https://arxiv.org/abs/2512.15958) | [refoxdb](https://nanohub.org/tools/refoxdb/) (new measurements in the paper supplement) |  |
| Nitrate kinetics | yes | Ilias | [Variational reformulation of inverse problems (2014)](https://arxiv.org/abs/1410.5522) | [code](https://github.com/ebilionis/variational-reformulation-of-inverse-problems) | [[Catalysis kinetics]] |
| Thermal preferences | no | Ilias | [Unimodal GP thermal preferences (2019)](https://arxiv.org/abs/1903.09094) | [code](https://github.com/nawalgao/GPPrefElicit) (survey data not released) |  |
| Synthetic design functions | no | Ilias | [BODE (2018)](https://arxiv.org/abs/1807.09979), [Bayesian sequential design (2019)](https://arxiv.org/abs/1912.07366) | [BODE code](https://github.com/piyushpandita92/bode), [AdaptiveSDOE](https://github.com/piyushpandita92/AdaptiveSDOE) (AdaptiveSDOE matched by author, not linked in the paper) |  |
| Steel wire drawing | no | Ilias | [Multi-objective optimization on a budget (2017)](https://arxiv.org/abs/1706.01665) | [toy code only](https://github.com/piyushpandita92/pydes) (simulator not public) |  |
| Lorenz and Hopf (SINDy) | yes | Atharva, Ilias | [Coding-agent paper replication (2026)](https://arxiv.org/abs/2607.02134) | [replication repo](https://github.com/PredictiveScienceLab/paper-replication-paper), [PySINDy](https://github.com/dynamicslab/pysindy) | [[SINDy toy systems]] |
| Dual-moon posterior | no | Wesley | [GitHub repo only, no paper](https://github.com/wesleyjholt/multimodal-examples) | [repo](https://github.com/wesleyjholt/multimodal-examples) |  |
| CF-PEI tensile tests | no | Ilias | [Fiber orientation inference (2022)](https://arxiv.org/abs/2202.12881) | none found |  |
| WCA dimer, LJ38, 2D toy potential | no | Ilias | [Free energy by KL minimization (2010)](https://arxiv.org/abs/1011.2416) | none found |  |
| 50 state-capital temperatures | yes | Ilias | [Bayesian reduced-order models (2010)](https://arxiv.org/abs/1001.2753) | none found (paper's link not opened, likely dead) |  |

### 1D

| Example | Over time? | Who | Source | Data / code | In the books |
|---|---|---|---|---|---|
| Steady heat and cubic nonlinear equation | no | Alex, Ilias | [Physics-informed IFT (2023)](https://arxiv.org/abs/2301.07609) | [code and observation CSVs](https://github.com/PredictiveScienceLab/pift-paper-2023) |  |
| Elliptic PDE, log-normal conductivity | no | Ilias | [Simulator-free SPDE solver (2019)](https://arxiv.org/abs/1902.05200) | [code](https://github.com/PredictiveScienceLab/variational-elliptic-SPDE) (data on Purdue SharePoint, not opened) | [[Stochastic 1D heat equation]] |
| Heat equation, Wiener-Levy conductivity | no | Ilias | [Amortized VI for inverse problems (2023)](https://arxiv.org/abs/2305.20004) | [code and notebooks](https://github.com/PredictiveScienceLab/paper-2023-inverse-map-karumuri) |  |
| Burgers and Schrodinger (Raissi PINNs) | yes | Atharva, Ilias | [Coding-agent paper replication (2026)](https://arxiv.org/abs/2607.02134) | [Raissi PINNs data](https://github.com/maziarraissi/PINNs) |  |
| Poisson with Brownian bridge prior | no | Alex, Ilias | [Brownian bridge prior for Poisson (2025)](https://arxiv.org/abs/2503.00213) | none found | [[Brownian motion, bridge and sheet]] |
| Heat equation, probabilistic solver | no | Ilias | [Probabilistic PDE solvers (2016)](https://arxiv.org/abs/1607.03526) | none found |  |
| Granular crystal chain (placement uncertain) | yes | Ilias | [GP dimensionality reduction (2016)](https://arxiv.org/abs/1602.04550), [Deep active subspaces (2019)](https://arxiv.org/abs/1902.10527) | [py-aspgp](https://github.com/PredictiveScienceLab/py-aspgp) (repo matched by name) |  |

### 2D

| Example | Over time? | Who | Source | Data / code | In the books |
|---|---|---|---|---|---|
| Elliptic PDE, log-normal and channelized fields | no | Ilias | [Simulator-free SPDE solver (2019)](https://arxiv.org/abs/1902.05200) | [code](https://github.com/PredictiveScienceLab/variational-elliptic-SPDE), [channelized data](https://github.com/cics-nd/pde-surrogate) |  |
| Elliptic PDE, DNN surrogate | no | Ilias | [Deep UQ (2018)](https://arxiv.org/abs/1802.00850) | [code](https://github.com/rohitkt10/deep-uq-paper) |  |
| Elliptic PDE, active subspaces | no | Ilias | [GP dimensionality reduction (2016)](https://arxiv.org/abs/1602.04550), [Deep active subspaces (2019)](https://arxiv.org/abs/1902.10527) | [py-aspgp](https://github.com/PredictiveScienceLab/py-aspgp), [dataset repo](https://github.com/paulcon/as-data-sets) (dataset folder may have moved) |  |
| Allen-Cahn, bimodal (steady placement uncertain) | no | Alex, Ilias | [Physics-informed IFT (2023)](https://arxiv.org/abs/2301.07609) | [notebook](https://github.com/PredictiveScienceLab/pift-paper-2023) |  |
| Insulation thermal conductivity, ABAQUS twin | yes | Alex, Ilias | [IFT thermal conductivity (2026)](https://arxiv.org/abs/2601.15427) | [data and code](https://github.com/PredictiveScienceLab/IFT-Thermal-Conductivity-Experiments) (ABAQUS licence needed) |  |
| Navier-Stokes cylinder wake (Raissi PINNs) | yes | Atharva, Ilias | [Coding-agent paper replication (2026)](https://arxiv.org/abs/2607.02134) | [Raissi PINNs data](https://github.com/maziarraissi/PINNs) | [[Cylinder flow Re 100 (DMD)]] |
| Contaminant source (time placement uncertain) | yes | Ilias | [Variational reformulation of inverse problems (2014)](https://arxiv.org/abs/1410.5522) | [code](https://github.com/ebilionis/variational-reformulation-of-inverse-problems) |  |
| Skin flaps | no | Ilias | [Reconstructive surgery GP (2020)](https://arxiv.org/abs/2010.02800) | [repo](https://bitbucket.org/abuganzatepole/gp_anisotropy) (repo contents not opened) |  |
| Poisson, analytic | no | Alex, Ilias | [MAP uniqueness in PIFT (2024)](https://arxiv.org/abs/2401.14224) | none found | [[Manufactured 2D Poisson]] |
| Electromagnet PINN | no | Ilias | [Parametric magnetostatics PINN (2022)](https://arxiv.org/abs/2202.04041) | none found |  |
| Oil well placement on SPE10 (placement uncertain) | no | Ilias | [Extended expected improvement (2016)](https://arxiv.org/abs/1604.01147) | none found (SPE10's public home not looked up) | [[SPE10 permeability field]] |

### 3D

| Example | Over time? | Who | Source | Data / code | In the books |
|---|---|---|---|---|---|
| Brindise in-vitro aneurysm flow | yes | Atharva, Abhishek, Ilias | [3D particle reconstruction (2024)](https://doi.org/10.1088/1361-6501/ad6624), [UOT particle tracking (2024)](https://arxiv.org/abs/2407.04583) | [particle velocimetry](https://doi.org/10.4231/M5F1-QC84), [MRI](https://doi.org/10.4231/C6DE-N845), [CFD](https://doi.org/10.4231/5RW6-4Z50) (Purdue PURR, CC0; zips not inspected) |  |
| Aneurysm growth, 19 public aneurysms | yes | Atharva, Ilias | [Aneurysm growth detection (2026)](https://arxiv.org/abs/2604.06649) | [OpenNeuro ds005096](https://openneuro.org/datasets/ds005096) (paper does not say which 19) |  |
| Aneurysm growth, UCSF 42 | yes | Atharva, Ilias | [Aneurysm growth detection (2026)](https://arxiv.org/abs/2604.06649) | none found (not public) |  |
| Synthetic aneurysm CFD, Poiseuille tube, in-vivo patient | yes | Atharva, Abhishek, Ilias | [SMURF 4D-flow MRI (2025)](https://arxiv.org/abs/2505.12494), [VAST 4D-flow MRI (2026)](https://arxiv.org/abs/2601.13393) | none found |  |
| Burgers vortex, 3,000 particles | yes | Atharva, Ilias | [UOT particle tracking (2024)](https://arxiv.org/abs/2407.04583) | none found (generated in the paper) |  |
| Pipe flow, Re 630 | yes | Atharva | [3D particle reconstruction (2024)](https://doi.org/10.1088/1361-6501/ad6624) | none found (journal's data statement not read) |  |

## Related pages
- [[Dynamical systems table]]
- [[Planned and stub examples]]
