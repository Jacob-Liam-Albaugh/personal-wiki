---
type: example
area: me697
areas: [me697, me539]
source-ref: "ASML (ME 697); Intro SciML (ME 539)"
tags: [uq, ml, bayesian, inverse-problems, signals, sampling, mcmc]
data-origin: [simulated, synthetic, analytic]
tasks: [uncertainty propagation, surrogate modelling, sensitivity analysis, inverse problem and calibration, system identification, state estimation, sampling]
uses: 10
---

# Duffing oscillator examples

**Summary**: 10 uses in ASML (ME 697) and Intro SciML (ME 539). Data: simulated, synthetic, analytic. Tasks: uncertainty propagation, surrogate modelling, sensitivity analysis, inverse problem and calibration, system identification, state estimation, sampling.

**Covered in**: ASML (ME 697), Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/polynomial_chaos/07_pce_dynamical_system.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Duffing oscillator with random initial state (PCE)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/polynomial_chaos/07_pce_dynamical_system.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: uncertainty propagation / surrogate modelling
- **Technique**: PCE Legendre total degree 5 with Smolyak sparse grid level 5 ('F2') vs MC 100,000 samples
- **Data origin**: simulated
- **Forward model**: x'=v, v'=gamma cos(omega t)-delta v-alpha x-beta x^3, alpha=1, beta=5, gamma=0.37, delta=0.1, omega=1; x(0),v(0)~N(0,0.1^2) mapped from Xi~U[-1,1]^2 by normal ppf; t in [0,10], 2000 points; Diffrax Tsit5 in JAX
- **Unknown dimension**: 2
- **Data dimension**: 2 states x 2000 times
- **Ground truth**: MC reference
- **What makes it hard**: nonlinear oscillator; PC accuracy degrades with larger initial variance
- **Libraries**: JAX, Diffrax, orthojax, py-design
- **References**: Bilionis et al. 2013 (cited in 08_limitations.md)
- **Notes**: Timings: PC 5.01 ms per loop vs MC 5.19 s per loop (two timeit outputs; PC vs MC assignment inferred from order, unclear). Sobol indices mentioned.

## Duffing oscillator local sensitivity

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/sensitivity_analysis/03_example_ode.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: sensitivity analysis / uncertainty propagation
- **Technique**: local (first-order) sensitivity: Y~GP(y(mu), J Sigma J^T) via jax.jacobian and einsum; Sigma=diag((0.05 mu)^2); compared against 1,000,000-sample MC with vmap
- **Data origin**: simulated
- **Forward model**: Duffing x'=v, v'=gamma cos(omega t)-delta v-alpha x-beta x^3, theta=(alpha,beta,gamma,delta,omega)=(1,5,0.37,0.1,1), x0=v0=0, t in [0,50], 2000 points, Diffrax Tsit5, jit+jacobian in JAX
- **Unknown dimension**: 5
- **Data dimension**: 2 x 2000
- **Ground truth**: MC with 1e6 samples
- **What makes it hard**: limit cycle; linearisation fails at longer times
- **Libraries**: JAX, Diffrax, NumPy
- **Notes**: Good at early times (first 200 steps), progressively wrong over 1000 steps.

## Duffing oscillator global sensitivity (Sobol indices)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/sensitivity_analysis/08_global_sensitivity_analysis.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: sensitivity analysis
- **Technique**: Sobol first-order and total indices via SALib (Saltelli sampling, N=512, calc_second_order False for S1 and True for ST), per time step
- **Data origin**: simulated
- **Forward model**: Same Duffing system, theta=(1,5,0.37,0.1,1), x0=v0=0, t in [0,50] with 500 save points, Tsit5, vmap in JAX; each parameter varied +-1% uniformly
- **Unknown dimension**: 5
- **Data dimension**: 2 x 500
- **Ground truth**: none; indices should sum to 1
- **What makes it hard**: interactions and numerical error
- **Libraries**: JAX, Diffrax, SALib
- **Notes**: Early on gamma dominates, later omega. First-order sums fall below 1 (interactions); total sums sometimes exceed 1 (sampling error).

## Duffing oscillator system identification

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/inverse/odes/03_dyn_system_multiple_traj.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Bayesian system identification
- **Technique**: Full-rank Gaussian VI baseline (2000 steps, 5 MC, lr 1e-2) vs amortized VI (NeuralNetworkEncoder trunk + mu/cov heads, 1000 steps, minibatch 5 trajectories, 6 MC, lr 1e-4) trained on prior-simulated trajectories with divergence filtering (pos>5, vel>10, acc>50 dropped, 1.3x oversampling)
- **Data**: Acceleration observations, 376 time points, t in [0,15] dt 0.04, noise sigma_meas=1.0 known; truth theta=(x0,v0,wn,xi,beta)=(0.5,0.1,3.0,0.2,0.0)
- **Data origin**: simulated
- **Forward model**: x'=v, v'=-2 xi wn v - wn^2 x - beta x^3 + gamma sin(omega t), gamma=0.8, omega=1.25; JAX diffrax Heun dt 0.04, float32
- **Unknown dimension**: 5
- **Data dimension**: 376
- **Ground truth**: true theta known
- **What makes it hard**: Nonlinear forced oscillator; diverging prior draws
- **Libraries**: jax, diffrax, equinox, optax
- **Notes**: Priors: x0,v0~N(0,1), beta~N(0,0.5^2), wn~LogN(1.2,0.3^2), xi~LogN(-1.9,0.6^2). VI reconstructs trajectory accurately, AVI slightly worse; timings in plot labels.

## Stochastic Duffing oscillator state-space (filtering)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/sinverse/fs/02_filter.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: filtering / prediction
- **Technique**: Bootstrap particle filter, 10,000 particles, then forward prediction
- **Data**: 400 points on t in [0,40], first 200 used for training; noisy position only.
- **Data origin**: synthetic
- **Forward model**: Stochastic Duffing: dx=v dt, dv=(-delta v - alpha x - beta x^3 + gamma cos(omega t))dt + noise; omega=1.2, alpha=-1, beta=1, delta=0.3, gamma=0.5, sigma_x=0.01, sigma_v=0.05; x0=(1,0); position observed with noise s=0.1, dt=0.1. Euler-Maruyama in JAX.
- **Unknown dimension**: 2-dim latent state per step
- **Data dimension**: 200 noisy positions
- **Ground truth**: True simulated trajectory
- **What makes it hard**: Nonlinear, chaotic-regime forcing; predictions degrade
- **Libraries**: jax, dax
- **Notes**: dax (JAX state-space package)

## Stochastic Duffing oscillator state-space (smoothing)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/sinverse/fs/03_smoother.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: filtering/smoothing
- **Technique**: Bootstrap filter 10,000 particles + backward smoother 1000 samples
- **Data**: Same system, t in [0,20].
- **Data origin**: synthetic
- **Forward model**: Stochastic Duffing: dx=v dt, dv=(-delta v - alpha x - beta x^3 + gamma cos(omega t))dt + noise; omega=1.2, alpha=-1, beta=1, delta=0.3, gamma=0.5, sigma_x=0.01, sigma_v=0.05; x0=(1,0); position observed with noise s=0.1, dt=0.1.
- **Unknown dimension**: 2-dim latent state per step
- **Ground truth**: True simulated trajectory
- **What makes it hard**: Nonlinear latent dynamics
- **Libraries**: jax, dax

## Duffing parameter identification by EM

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/sinverse/cali/02_em_example.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: system identification
- **Technique**: Expectation-maximisation with particle smoother (1000 particles, 100 M-step iterations, 100 EM iterations, lr 1e-3)
- **Data**: Duffing data as in filter notebook.
- **Data origin**: synthetic
- **Forward model**: Stochastic Duffing: dx=v dt, dv=(-delta v - alpha x - beta x^3 + gamma cos(omega t))dt + noise; omega=1.2, alpha=-1, beta=1, delta=0.3, gamma=0.5, sigma_x=0.01, sigma_v=0.05; x0=(1,0); position observed with noise s=0.1, dt=0.1.
- **Unknown dimension**: 4 (alpha, beta, delta, s)
- **Ground truth**: True alpha=-1, beta=1, delta=0.3, s=0.1
- **What makes it hard**: Starts at alpha=beta=delta=0, sigma0=2
- **Libraries**: jax, dax, optax
- **Notes**: Estimates alpha=-0.91, beta=0.93, delta=0.38, s=0.15; log-likelihood about 261. Printout mislabels true noise as 0.01.

## Duffing Bayesian calibration by particle MCMC

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/sinverse/cali/04_pmcmc_example.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Bayesian inverse problem
- **Technique**: Particle marginal Metropolis-Hastings, flat prior, 1000 particles, proposal_scale 0.01, 10000 iterations (381 s)
- **Data**: Duffing data as in filter notebook.
- **Data origin**: synthetic
- **Forward model**: Stochastic Duffing: dx=v dt, dv=(-delta v - alpha x - beta x^3 + gamma cos(omega t))dt + noise; omega=1.2, alpha=-1, beta=1, delta=0.3, gamma=0.5, sigma_x=0.01, sigma_v=0.05; x0=(1,0); position observed with noise s=0.1, dt=0.1.
- **Unknown dimension**: about 8 (alpha, beta, delta, log s, x0 mean, log sigma)
- **Ground truth**: True parameters known
- **What makes it hard**: Noisy likelihood estimate; slow
- **Libraries**: jax, dax
- **Notes**: Start alpha=-1.5, beta=1.5, delta=0.5, s=1.0. Posterior 'not amazing' but contains truth.

## Duffing oscillator sensitivity analysis

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/homework/02_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: sensitivity analysis
- **Technique**: Local sensitivity (theta mean (0.5,0.5,1,5,0.37,0.1,1), sd (0.025,0.025,0.01,0.05,0.0037,0.001,0.01)); Monte Carlo 1e5; GP view; Sobol indices via SALib
- **Data origin**: analytic
- **Forward model**: Duffing oscillator in strange-attractor regime alpha=1, beta=5, gamma=8, delta=0.02, omega=0.5; t in [0,30], dt 0.1.
- **Unknown dimension**: 7 uncertain inputs
- **Ground truth**: none
- **What makes it hard**: Chaotic regime
- **Libraries**: jax, SALib
- **Notes**: Problem 1.

## Bistable Duffing oscillator uncertainty propagation

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-02.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: forward uncertainty propagation
- **Technique**: Monte Carlo over F~N(0.001,0.005^2) with solve_ivp; predictive intervals; bootstrap
- **Data origin**: simulated
- **Forward model**: x''+0.4x'-x+x^3=F, x(0)=x'(0)=0, t in [0,20], 201 output times
- **Unknown dimension**: 1 (F)
- **Data dimension**: trajectory 201
- **Ground truth**: deterministic simulator
- **What makes it hard**: F=0 sits on unstable point, response bimodal
- **Libraries**: scipy
- **References**: Kovacic & Brennan 2011; Zhang et al. 2016 doi 10.1016/j.ijnonlinmec.2015.11.002

## Related pages
- [[Examples catalogue]]
- [[Markov chain Monte Carlo]] · [[Variational inference]] · [[Amortized VI]] · [[Particle filter]] · [[Particle MCMC]] · [[Expectation-maximization]] · [[Polynomial chaos]] · [[Sobol indices]] · [[Gaussian process]] · [[Surrogate model]] · [[Sensitivity analysis]] · [[Local sensitivity analysis of ODEs]] · [[Stochastic state-space model]] · [[Euler-Maruyama method]] · [[Duffing oscillator]]
