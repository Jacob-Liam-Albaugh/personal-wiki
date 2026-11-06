---
type: method
area: physics-informed
areas: [physics-informed, ift]
source-ref: "Alberts & Bilionis 2023, eqs. 28-32, pp. 15-17"
tags: [physics-informed, ml, pde]
---

# Physics-informed neural networks (PINN) and B-PINN

> [!theorem] PINN as a PIFT MAP estimate (Alberts & Bilionis 2023, eqs. 28-30)
> With a flat prior on network weights $\theta$ and constant partition function, the PINN loss equals the parameter information Hamiltonian when $r_d=s/(2\sigma^2)$ and $r_p=\beta$. With physics parameters $\lambda$, $-\log p(\theta,\lambda|d)$ also has $\log Z(\lambda)+H(\lambda)$, which the PINN loss drops.

> [!theorem] When a B-PINN matches PIFT (eqs. 31-32)
> A B-PINN uses a fictitious zero-residual likelihood with noise $\sigma_r$ and a Gaussian weight prior. Its posterior equals PIFT's iff collocation points are shared, $\sigma_\theta=\infty$, and
> $$\sigma_r^2=n/(2\beta).$$

**Intuition**: B-PINN posteriors collapse as collocation points $n\to\infty$ (Bayesian asymptotics); PIFT's spread is set by $\beta$ and stays.

## Where it appears
- [[PIFT (Alberts 2023)]] — derivations.
- [[IFT thermal conductivity (Alberts 2026)]] — contrast; cites Hao & Bilionis (neural information field filter, not read) for B-PINN's poor extrapolation.
- [[PINNs (Raissi 2019)]] — original continuous-time and discrete-time (implicit Runge-Kutta) formulations (source: Physics Informed Architectures/Karniadakis, Raissi, Perdikaris - PINNs - Physics-Informed Neural Networks.pdf).
- [[When and why PINNs fail (Wang 2022)]] — NTK analysis: boundary and residual loss blocks converge at different rates; adaptive weights from Tr(K) ratios; see [[Neural tangent kernel]].
- [[Respecting causality (Wang 2022)]] — causal weights along time; temporal convergence rate as a stopping criterion.
- [[Expert's guide to PINNs (Wang 2023)]] — training pipeline: non-dimensionalization, Fourier features, random weight factorization, loss balancing, curriculum.
- [[Physics-informed ML review (Karniadakis 2021)]] — PINN as a learning bias; soft penalty equals MAP under a physics likelihood (review, p. 7).
- Basics: residual loss, hard boundary conditions, [[Non-dimensionalization]] with Glorot init, Fourier features against [[Spectral bias]], and the [[Energy functional]] alternative (source: pinns/basics/forward.ipynb, energy.ipynb).
- [[Parametric PINN]]: branch-trunk ansatz $N=\sum_i b_i(\xi)\phi_i(x)$ with loss averaged over $p(\xi)$ (source: pinns/parametric).
- Inverse problems: see the section below (the book's notebooks are stubs).

## Forward problem (book, pinns/basics)
PINNs encode the physics through a regularization term added to the loss (source: pinns/intro.md). The book's toy problem is a steady heat equation with zero Dirichlet data.

> [!definition] Toy problem (forward.ipynb)
> Find $u$ on $[0,L_x]\times[0,L_y]$ with $u=0$ on the boundary:
> $$-k\,\Delta u = f.$$
> The source $f$ is derived with sympy from a chosen exact solution:
> $$u = u_0\sin^2(\pi x/L_x)\sin^2(\pi y/L_y).$$
> Values: $u_0=500$ K, $k=10$, $L_x=0.1$, $L_y=1.0$.

- **Boundary conditions by construction**: multiply the network by a function that vanishes on the boundary,
$$u(x,y) = x(1-x)\,y(1-y)\,\mathrm{MLP}(x,y;\theta).$$
- **Residual loss as an expectation**: with $X$ uniform on $\Omega$ (density $1/|\Omega|$),
$$\mathcal L(\theta) = \int_\Omega [\Delta u + f]^2\,dx = |\Omega|\;\mathbb E_X\big[(\Delta u + f)^2\big].$$
  Each step averages over 256 fresh random collocation points, so the gradient is unbiased. Optimizer: [[Adam]] at $10^{-3}$.
- **Architecture** (forward.ipynb): tanh activation, width 128-512, depth 3-5, Glorot init ([[Weight initialization]]).

> [!failure] Unscaled problem does not train
> With the physical $L_x, L_y, u_0$ the loss does not decrease. Glorot assumes inputs and outputs of order 1; the fix is [[Non-dimensionalization]], after which the model trains in 2000 iterations and reaches a good solution. "Very hard to achieve better error with plain MLPs."

> [!note] Not for forward problems
> The book states PINNs are not recommended for forward problems; classical solvers are more efficient (source: forward.ipynb). Their payoff is parametric and inverse problems, see [[Parametric PINN]].

- **Spectral bias**: the high-frequency part of a target is learned late; random [[Fourier features]] with $\sigma=6$ and 100 features are used in the PINN run.
- **Energy loss**: [[Energy functional]] uses only first derivatives; the book finds it less accurate than the residual loss (5000 iterations, Fourier MLP width 256).
- Follows Wang et al. 2023 (arXiv:2308.08468).

## Inverse problems (book, pinns/inverse)
The book's takeaway is that PINNs can pose and solve inverse problems (source: pinns/intro.md); its two inverse notebooks hold only titles, so nothing is derived there. The standard formulation (Wiki note): treat the unknown PDE parameter or field $\kappa$ as extra trainable variables and minimize
$$
\mathcal L(\theta,\kappa) = \mathcal L_{\text{data}} + \lambda\,\mathcal L_{\text{PDE}}(\theta,\kappa).
$$
The Bayesian version replaces the point estimate by a posterior over $(\theta,\kappa)$: a PINN is a MAP estimate under a [[Physics-informed prior]], and Bayesian PINNs use [[Bayesian neural networks]] inference. Whether the inverse problem is well posed is a question of [[Identifiability]]; see also [[Bayesian inverse problems]] and [[Markov chain Monte Carlo]] for sampling the posterior.

## PINN literature
The PINN literature is ingested under [[Physics-informed machine learning]] (five PINN pages plus the review).
- Book chapters pinns/basics, parametric, inverse are now ingested; remove from the queue.

## Examples

> [!example] Scaled residual PINN
> 2000 Adam iterations, about 17.5 s on an M1 and 8 s on an A100 (source: forward.ipynb).

> [!example] Fourier-feature PINN
> Takes 48 s on an M1 versus 13 s on an A100; loss compared with the plain MLP on a log scale (source: spectral_bias.ipynb).

> [!example] Homework 7, neo-Hookean PINN (source: homework/07_homework.ipynb)
> Train a PINN on $[0,1]^2$ minimizing a hyperelastic stored energy: $\delta=0.1$ first, then $\delta=0.5$ by continuation (transfer learning), then a parametric PINN over $\delta\in[0,0.5]$ with the loss integrated over $\delta$. See [[Energy functional]], [[Parametric PINN]], PINN.

The stored energy (homework 7, problem 3):

$$
E_b = \int \Big\{\tfrac12\Big(\sum_{ij}F_{ij}^2-2\Big) - \ln\det F + 50\,(\ln\det F)^2\Big\}\,dx\,dy.
$$

- Wiki note, forward.ipynb: the residual in the unscaled loss is written $\Delta u+f$, but the PDE is $-k\Delta u=f$, so $k$ is dropped. The toy-solution text has $\sin^2(10\pi y/L_y)$, the code has $\sin^2(\pi y/L_y)$. The text ansatz is $x(1-x)y(1-y)$, the code uses $x(L_x-x)y(L_y-y)$. The scaling cell builds `v_tu_xx`, `v_tu_yy` from the unscaled `u_xx`, `u_yy` rather than `tu_xx`, `tu_yy` **[unverified: read from the source cells, not re-run]**.
- Wiki note, energy.ipynb: the `tE_term1` code uses `kx` for both gradient terms; the $y$ term should use `ky`. Also $f_s$ is computed from the untrained model.
- Wiki note: the energy loss was less accurate than the residual loss in the book's Poisson example (source: pinns/basics/energy.ipynb).

**Covered in**: ASML book pinns/basics (ME 697 5.1); ASML book pinns/inverse (ME 697 5.3); homework 7
**Sources**: `IFT/Bilionis, Alberts - IFT.pdf`, `advanced-scientific-machine-learning/book/pinns/intro.md`, `pinns/basics/forward.ipynb`, `pinns/basics/spectral_bias.ipynb`, `pinns/basics/energy.ipynb`, `advanced-scientific-machine-learning/book/pinns/intro.md`, `pinns/inverse/01_pinns_inverse_example.ipynb`, `pinns/inverse/02_example_Bayesian_pinns.ipynb`, `homework/00_intro.md`, `homework/01_homework.ipynb through 07_homework.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Physics-informed prior]] · [[Information field theory]]
- [[Physics-informed machine learning]] · [[PINNs (Raissi 2019)]] · [[When and why PINNs fail (Wang 2022)]] · [[Respecting causality (Wang 2022)]] · [[Expert's guide to PINNs (Wang 2023)]] · [[Neural tangent kernel]] · [[Physics-informed ML review (Karniadakis 2021)]]
- [[SIREN]] (smooth derivatives for PDE losses, Sitzmann 2020 §4), [[Spectral bias]], [[Fourier features]].
- [[Poisson and Laplace equations]], [[Maxwell's equations]]: classical PDEs of electrostatics and electromagnetics that PINNs can solve (source: Electromagnetics/Lectures Slides/lect_12.pdf).
