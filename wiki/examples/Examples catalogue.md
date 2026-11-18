---
type: overview
area: me697
areas: [me697, me539]
source-ref: "ASML (ME 697) book and Intro SciML (ME 539) notebooks"
tags: [uq, inverse-problems, bayesian, sampling, ml]
---

# Examples catalogue

**Summary**: Every worked example and dataset in the two Bilionis books, 136 notebook uses grouped into 60 examples. Pick a task below to see which examples the books use for it. Intro-book toy examples (coin flips, basic probability) are left out.

**Sources**: `text_books/advanced-scientific-machine-learning/book`, `text_books/intro-to-scientific-machine-learning/notebooks`. Raw rows: `wiki/examples/examples.csv`.
**Last updated**: 2026-11-18

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

## Related pages
- [[Planned and stub examples]]
