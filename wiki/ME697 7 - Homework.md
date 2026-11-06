---
type: lecture
area: me697
areas: [me697]
course: me697
lecture: homework
source-ref: "ME 697 book, homework/00_intro and 01-07 (problem statements only; no solutions in the notebooks)"
tags: [ml, software, uq, bayesian, inverse-problems, physics-informed]
---

# ME697 7 - Homework

**Summary**: Overview of the seven ME 697 homework notebooks: what each covers and which wiki page carries its problems as `> [!example]` callouts. The notebooks hold problem statements only, with empty answer cells. Each homework is 100 points, problems not equally weighted (source: homework/01_homework.ipynb).
**File**: `advanced-scientific-machine-learning/book/homework/`

---

## Topics
`00_intro.md`: review the lecture first; "the code you need can typically be found in the lecture notebooks".

| HW | Modules | Problems | Callouts placed on |
|---|---|---|---|
| 1 | 1-2 | recursion vs iteration, `foldl`, `lax.scan` Fibonacci, logistic map, autoencoder on MNIST | [[ME697 1.1 - Functional programming in JAX]], [[ME697 1.4 - Optimization]] |
| 2 | 3 | Duffing local sensitivity, strange attractor, GP view, Sobol indices | [[ME697 2.1 - Sensitivity analysis]] |
| 3 | 3 | Pythagoras in Hilbert spaces, $\ell^2$ isomorphism, orthogonal polynomials, Lorenz PCE | [[ME697 2.2 - Polynomial chaos]] |
| 4 | 3 | surrogate of a legacy code (Branin), active learning, multi-fidelity, permutation group | [[ME697 2.3 - Surrogates]], [[ME697 2.5 - Active learning]], [[Equivariance]] |
| 5 | 4 | POD derivation, POD of fluid flow, KL permeability model, Darcy FNO | [[Proper orthogonal decomposition]], [[Karhunen-Loève expansion]], [[Neural operator]] |
| 6 | 5 | why Metropolis works, VI mathematics, PK model calibration | [[Markov chain Monte Carlo]], [[Variational inference]], [[KL divergence]] |
| 7 | 5-6 | partially observed Lorenz with SINDy, noisy SINDy, neo-Hookean PINN | [[SINDy]], [[PINN]], [[Dynamic mode decomposition]] |

The homework 7 header also lists "Module 7: SDEs" in a comment, but no module 7 problem exists.

## Key results
Nothing is derived here; the problems point at results on the pages above.

**Homework 1.** Fibonacci without loops (tail recursion), `foldl` and its use for sum and product, `lax.scan` plus `jit`. Logistic map $x_{n+1}=r\,x_n(1-x_n)$ vectorized over $r$ and $x_0$, output shape `(1000, 100, 10000)`, period-doubling plot. Autoencoder with latent dimension 2 (two hidden layers of 128 ReLU units, Equinox, Optax, Adam $10^{-3}$, batch 32), plots of reconstructions and of the latent space, then a 10-component Gaussian mixture fitted to the latent space and sampled.

**Homework 2.** Duffing oscillator $\ddot x+\delta\dot x+\alpha x+\beta x^3=\gamma\cos\omega t$. Parameters $\alpha=1$, $\beta=5$, $\gamma=8$, $\delta=0.02$, $\omega=0.5$ for the attractor. Local sensitivity with $\theta\sim N(\mu,\Sigma)$ gives credible intervals and a Gaussian-process view with covariance

$$
\mathrm{Cov}[x(t),x(0)] = \nabla_\theta x(t)\,\Sigma\,\nabla_\theta x(0)^T.
$$

Then map $\theta_i$ to uniform $\xi_i$ via CDFs and compute Sobol indices on $[0,30]$ with step 0.1.

**Homework 3.** Pythagoras $\|x+y\|^2=\|x\|^2+\|y\|^2$ for orthogonal $x,y$ and its $n$-term form; the map $T:H\to\ell^2$ from an orthonormal basis is linear, onto, one-to-one and preserves the inner product. Orthogonal polynomials for $\Xi\sim\exp(1)$ with `orthojax`, projection of $\sin$, mean and variance of $\sin(\Xi)$. Lorenz system ($\sigma=10$, $\beta=8/3$, $\rho=28$) with $x(0)\sim N(0,0.1)$, $y(0)\sim N(5,0.1)$, $z(0)\sim N(20,0.1)$: PCE surrogate, mean and variance versus Monte Carlo, three predictions, densities at $t=1,2,5,10$ from 100,000 samples.

**Homework 4.** Legacy-code wrapper around the Branin function, initial design, surrogate, random versus active-learning data, optimization, multi-fidelity. Permutation group $S_n$, cycles, transpositions, permutation matrices, and a faithful complex $2\times2$ representation of $S_3$.

**Homework 5.** POD operator $R\phi=\langle(\phi^\dagger u)u\rangle$: kernel form, linear, bounded, continuous, self-adjoint, positive semi-definite, spectral facts. POD of 2D Navier-Stokes velocity magnitude (Wang and Perdikaris data, arXiv:2203.07404): energy captured, modes, uncorrelated coefficients, reconstruction. KL model of oil-reservoir permeability on $[0,356]\times[0,670]$ m, positive and conditioned on a geologist's estimate. Darcy flow $\nabla\cdot(K\nabla p)=f$: train a Fourier neural operator, then propagate uncertainty from a noisy $24\times24$ permeability measurement smoothed with a GP.

**Homework 6.** Detailed balance implies stationarity; the Metropolis-Hastings kernel satisfies it. Rank-$k$ covariance parameterization is positive semi-definite, multi-point convexity, Jensen's inequality, non-negativity of $D_{KL}(p\|q)$. Two-compartment pharmacokinetic model for IV bolus acetaminophen: log posterior, prior predictive, MAP, MCMC, mean-field and full-rank Gaussian VI.

**Homework 7.** Partially observed Lorenz: SINDy fails on the observed coordinate; build the Hankel matrix, SVD to three dimensions, SINDy of degree 5 on the principal components. SINDy with noisy data and no derivatives (numerical differentiation from the `derivative` package). Neo-Hookean PINN on $[0,1]^2$ with energy

$$
E_b = \int \Big\{\tfrac12\Big(\sum_{ij}F_{ij}^2-2\Big) - \ln\det F + 50\,(\ln\det F)^2\Big\}\,dx\,dy.
$$

Parts: $\delta=0.1$, then $\delta=0.5$ via continuation (transfer learning), then the parametric problem over $\delta\in[0,0.5]$ with the loss integrated over $\delta$.

## Examples
> [!example] How the callouts are used
> Each concept or method page above gets a short `> [!example]` callout naming the homework problem, its setup and the page's idea it exercises, via the staged edits file. No solutions are in the source.

## Connections
- Modules: [[ME697 1.1 - Functional programming in JAX]] through [[ME697 6.3 - Calibration of stochastic models]].
- The homework 7 PINN uses the energy form of [[ME697 5.1 - PINN basics]] ([[Energy functional]]) and the parametric idea of [[ME697 5.2 - Parametric PINNs]].

**Wiki note**: homework 7 problem 3 names a stored-energy functional, so it is the energy loss of [[Energy functional]] with a nonlinear hyperelastic energy. Homework 6 problem 1 part B should be read with the Metropolis-Hastings page [[Metropolis-Hastings correction]].

**Sources**: `advanced-scientific-machine-learning/book/homework/00_intro.md`, `01_homework.ipynb` through `07_homework.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 5.1 - PINN basics]] · [[ME697 6.3 - Calibration of stochastic models]] · [[ME697 2.1 - Sensitivity analysis]] · [[ME697 2.2 - Polynomial chaos]] · [[ME697 ROM - SVD, PCA and POD]]
- [[PINN]] · [[SINDy]] · [[Proper orthogonal decomposition]] · [[Markov chain Monte Carlo]] · [[Variational inference]]
