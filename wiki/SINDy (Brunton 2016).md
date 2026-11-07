---
type: paper
area: physics-informed
areas: [physics-informed, ml, optimization]
source-ref: "Brunton, Proctor, Kutz 2016, PNAS 113(15), eqs. 1-9"
tags: [physics-informed, ml, optimization]
authors: ["[[Steven L. Brunton]]", "[[Joshua L. Proctor]]", "[[J. Nathan Kutz]]"]
year: 2016
venue: "PNAS 113(15):3932-3937"
file: "papers/ML/Brunton, Proctor, Kutz - Discovering governing equations from data by sparse identification of nonlinear dynamical systems.pdf"
---

# SINDy (Brunton 2016)

**Summary**: Recasts discovery of governing equations as sparse regression. Time derivatives of the state are regressed on a library of candidate nonlinear functions, and sparsity keeps only the few terms that matter. This is the original [[SINDy]] paper; it scales better than genetic [[Symbolic regression]] and handles chaos, a fluid PDE reduced by POD, and parameterized bifurcations.

**Authors**: Steven L. Brunton, Joshua L. Proctor, J. Nathan Kutz · **Year**: 2016 · **File**: `papers/ML/Brunton, Proctor, Kutz - Discovering governing equations from data by sparse identification of nonlinear dynamical systems.pdf`

---

## Problem

Data are abundant but governing equations are often unknown (climate, neuroscience, epidemiology, finance). Symbolic regression ([[Eureqa (Schmidt 2009)]]) finds equations and balances complexity against accuracy, but "is expensive, does not scale well to large systems of interest, and may be prone to overfitting" (source: Brunton 2016, p. 1). Goal: find $f$ in $\dot x=f(x)$ (eq. 1, $x\in\mathbb R^n$) from measurements, assuming only that $f$ has few terms in some function basis.

## Method

> [!algorithm] SINDy
> Stack states and derivatives (rows are times):
> $X=[x^\top(t_1);\dots;x^\top(t_m)]$, $\dot X$ likewise.
> Build a library $\Theta(X)=[\,1\ \ X\ \ X^{P_2}\ \ X^{P_3}\cdots\sin X\ \cos X\cdots]$ (eq. 2), $m\times p$ with $m\gg p$. Solve for sparse $\Xi=[\xi_1\cdots\xi_n]$:
> $$\dot X=\Theta(X)\,\Xi\qquad(3)$$
> Each column is a separate optimization. The model is $\dot x^\top=\Theta(x^\top)\Xi$, i.e. $\dot x=\Xi^\top\Theta(x^\top)^\top$ (eqs. 4-5). With noise, $\dot X=\Theta(X)\Xi+\eta Z$ (eq. 6), $Z$ i.i.d. Gaussian.
>
> (source: Brunton 2016, eqs. 2-6, pp. 2-3)

- Solver: [[LASSO]] ($\ell_1$-regularized regression), or sequentially thresholded least squares (Code 1 in the SI, not in this PDF). LASSO may be expensive for very large data (p. 2).
- Derivatives: if only $X$ is available, $\dot X$ comes from numerical differentiation, with total-variation regularized derivatives to suppress noise (p. 2). Alternatively filter with the optimal singular-value hard threshold (p. 2).
- Normalize columns of $\Theta$ when entries of $X$ are small (SI).
- High-dimensional state: the library grows factorially in $n$, so first reduce with POD, a low-rank basis $\Psi$ ([[Proper orthogonal decomposition]]) (p. 2).
- Coordinates and basis matter: "we need the right coordinates and function basis to yield sparse dynamics" (p. 2). Time-delay coordinates can supply missing variables (SI sec. 4.5); learned coordinates are the later extension ([[SINDy autoencoders (Champion 2019)]]).
- Extensions: parameters appended as states with $\dot\mu=0$ (eq. 9, $\dot x=f(x;\mu)$); forcing $u(t)$ and time dependence $\dot t=1$ via $\dot x=f(x,u(t),t)$ (p. 4).

## Results

- **Lorenz** (eq. 7, $\sigma=10,\beta=8/3,\rho=28$): degree-5 polynomial library; correct terms found and coefficients within 0.03% of truth. Attractor reproduced; individual trajectories diverge by chaos, so attractor fidelity is the goal. Works with noisy state data (SI Fig. S7) (p. 3).
- **Cylinder wake, Re = 100**: POD modes 1-2 plus a shift mode give coordinates $(x,y,z)$. SINDy recovers the quadratic mean-field model (eq. 8): $\dot x=\mu x-\omega y+Axz$, $\dot y=\omega x+\mu y+Ayz$, $\dot z=-\lambda(z-x^2-y^2)$, with its parabolic slow manifold $z=x^2+y^2$. Experts took about 30 years to settle this form (Hopf bifurcation with cubic nonlinearity vs quadratic Navier-Stokes). If training data omit trajectories starting off the slow manifold, SINDy wrongly returns cubic terms (pp. 3-4).
- **Logistic map** $x_{k+1}=\mu x_k(1-x_k)+\eta_k$ (stochastic forcing) sampled at 10 values of $\mu$: parameters within 0.1%, bifurcation cascade reproduced (p. 4).
- **Hopf normal form** from noisy data at 8 values of $\mu$ with TV derivatives: correct limit-cycle amplitudes and growth rates (p. 4).

## Limitations

As stated by the authors:
- Depends on measurement variables, data quality and a sparsifying basis; fails when dynamics are not sparse in the chosen basis (SI Appendix B: Lorenz in nonlinear coordinates, glycolytic oscillator) (pp. 2, 5).
- Ill-suited to large $n$ without dimensionality reduction (p. 2).
- Failure is itself diagnostic information about coordinates and basis (p. 5).

Wiki note: the paper's code and SI (thresholded least squares, Appendices A-C) are not in the PDF; details above marked "SI" are cited from the main text only.

## Connections

- Builds on and replaces genetic search of [[Eureqa (Schmidt 2009)]] (cited as refs. 3-4) with convex sparse regression; see [[Symbolic regression]].
- Related to [[Dynamic mode decomposition]] ("linear dynamic regression", p. 3) and to [[Koopman operator]] theory; [[Deep Koopman (Lusch 2018)]] learns linearizing coordinates where SINDy keeps a nonlinear sparse model.
- Followed by [[SINDy autoencoders (Champion 2019)]] and [[SINDy delay autoencoders (Bakarji 2022)]].
- SINDy fits $f$ in the same way a [[Neural ODE]] does, but with a sparse linear-in-parameters library instead of a network.

%% refs:start %%
**Cited by in this wiki**: [[Deep Koopman (Lusch 2018)]], [[Energy-based kernels for viscoelastic flow (Otto 2024)]], [[IFT for engineering inverse problems (Alberts 2024)]], [[PINNs (Raissi 2019)]], [[PySR (Cranmer 2023)]], [[SINDy autoencoders (Champion 2019)]], [[SINDy delay autoencoders (Bakarji 2022)]], [[Symbolic models from deep learning (Cranmer 2020)]]
%% refs:end %%

**Sources**: `papers/ML/Brunton, Proctor, Kutz - Discovering governing equations from data by sparse identification of nonlinear dynamical systems.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[SINDy]] · [[LASSO]] · [[Symbolic regression]] · [[Proper orthogonal decomposition]]
- [[Eureqa (Schmidt 2009)]] · [[Deep Koopman (Lusch 2018)]] · [[Koopman operator]]
- [[SINDy autoencoders (Champion 2019)]] · [[SINDy delay autoencoders (Bakarji 2022)]] · [[Dynamic mode decomposition]]
