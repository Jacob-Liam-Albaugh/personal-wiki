---
type: paper
area: physics-informed
areas: [physics-informed, pde, inverse-problems]
source-ref: "Raissi, Perdikaris, Karniadakis 2019, J. Comput. Phys., eqs. 1-28"
tags: [physics-informed, pde, inverse-problems, ml]
authors: ["[[Maziar Raissi]]", "[[Paris Perdikaris]]", "[[George Em Karniadakis]]"]
year: 2019
venue: "Journal of Computational Physics (preprint dated 26 Oct 2018)"
file: "papers/Physics Informed Architectures/Karniadakis, Raissi, Perdikaris - PINNs - Physics-Informed Neural Networks.pdf"
---

# Physics-informed neural networks (Raissi 2019)

**Summary**: Defines the PINN: a neural network $u(t,x)$ whose derivatives are taken by [[Automatic differentiation]] to form the PDE residual $f$, with both trained by one mean-squared loss on data plus residual at collocation points. Two classes of problems (data-driven solution, data-driven discovery of PDE parameters) and two time-handling schemes (continuous, discrete Runge-Kutta). See [[PINN]] for the Bayesian reading.

**Authors**: Maziar Raissi, Paris Perdikaris, George E. Karniadakis · **Year**: 2019 · **File**: `papers/Physics Informed Architectures/Karniadakis, Raissi, Perdikaris - PINNs - Physics-Informed Neural Networks.pdf` (the file name puts Karniadakis first; the paper's byline is Raissi, Perdikaris, Karniadakis)

---

## Problem setup

Parametrized nonlinear PDE for a latent solution $u(t,x)$ (source: PINNs.pdf, eq. 1, p. 4):
$$u_t+\mathcal N[u;\lambda]=0,\quad x\in\Omega,\ t\in[0,T].$$
Burgers is the running case: $\mathcal N[u;\lambda]=\lambda_1uu_x-\lambda_2u_{xx}$ (see [[Burgers equation]]). Two tasks: (1) *data-driven solution*, with $\lambda$ fixed; (2) *data-driven discovery*, find $\lambda$ from data (pp. 3-4). Earlier Gaussian-process approaches are limited by linearization and local time-stepping and by prior assumptions (p. 3; see [[Gaussian process]]).

## Continuous-time model (§3.1)

Define the residual network
$$f:=u_t+\mathcal N[u]\quad(\text{eq. 3}).$$
Both $u$ and $f$ share parameters; $f$ is built by chain rule through $u$ with [[Automatic differentiation]]. Training loss:
$$\mathrm{MSE}=\mathrm{MSE}_u+\mathrm{MSE}_f\quad(\text{eq. 4}).$$
$$\mathrm{MSE}_u=\tfrac1{N_u}\sum_i|u(t_u^i,x_u^i)-u^i|^2$$
$$\mathrm{MSE}_f=\tfrac1{N_f}\sum_i|f(t_f^i,x_f^i)|^2$$
$\mathrm{MSE}_u$ fits initial and boundary data; $\mathrm{MSE}_f$ enforces the PDE at collocation points (p. 5). Small data (hundreds to a few thousand points) is optimized with full-batch L-BFGS; no convergence guarantee, but empirically fine when the PDE is well posed (p. 6). The residual term acts as a regularizer against over-fitting (p. 9).

For discovery (§4.1, eq. 14) the same construction with $f:=u_t+\mathcal N[u;\lambda]$ turns $\lambda$ into trainable parameters of the PINN.

## Discrete-time model (§3.2, §4.2)

Collocation-free alternative for the large-gap case. A $q$-stage implicit Runge-Kutta step (eq. 7) is encoded by a network with $q+1$ outputs $u^{n+c_i}(x)$ and $u^{n+1}(x)$; the loss is a sum of squared errors on data at $t^n$ (eqs. 9-13). Wiki note: because of the Runge-Kutta structure, only the last layer grows with $q$ (footnote 1, p. 12).

Truncation error is $O(\Delta t^{2q})$; the KdV example chooses $q$ by
$$q=\tfrac12\,\frac{\log\epsilon}{\log\Delta t}\quad(\text{eq. 28}),$$
so that the temporal error reaches machine precision $\epsilon$ (p. 21).

## Experiments

| Case | Setup | Result |
|---|---|---|
| Schrodinger (eq. 5), continuous | $N_0=50$, $N_b=50$, $N_f=20{,}000$, 5 layers x 100, tanh | relative $L^2$ error $1.97\times10^{-3}$ (p. 10) |
| Allen-Cahn (eq. 12), discrete | $N_n=200$ at $t=0.1$, predict $t=0.9$ in one step $\Delta t=0.8$, $q=100$ | relative $L^2$ error $6.99\times10^{-3}$ (p. 14) |
| Navier-Stokes cylinder wake (eqs. 15-19), $Re=100$ | $N=5000$ (1% of data), 9 layers x 20, stream function $\psi$ plus pressure $p$ | $\lambda_1,\lambda_2$ error 0.078%, 4.67% clean; 0.17%, 5.70% with 1% noise (p. 17) |
| KdV (eq. 27), discrete discovery | snapshots at $t=0.2,0.8$, $N_n=199,201$, $\Delta t=0.6$ | $\lambda$ errors 0.023%, 0.006% clean; 0.057%, 0.017% at 1% noise (p. 22) |

Notes on Navier-Stokes: assuming $u=\psi_y$, $v=-\psi_x$ makes the continuity equation hold identically; pressure is recovered up to a constant with no pressure data (p. 17). Burgers (App. A: $u_t+uu_x-(0.01/\pi)u_{xx}=0$, $N_u=100$, 9 layers x 20, 3021 parameters) is the sensitivity-study testbed, with a sharp internal layer near $t=0.4$ and error tables over data size, depth and width (pp. 25-29).

## Limitations stated by the authors (§5, p. 24)

- Not a replacement for finite elements or spectral methods, which meet robustness and efficiency standards from 50 years of development (p. 23).
- Open questions: how deep/wide, how much data, why no bad local optima for $\lambda$, vanishing gradients with higher-order operators, initialization, loss choice, uncertainty quantification. Settings that worked for one equation could fail on another.
- Many collocation points are needed in high dimensions (p. 9), the motivation for the discrete-time model.
- Wiki note: the failure modes the authors left open are analyzed in [[When and why PINNs fail (Wang 2022)]] (NTK view), [[Respecting causality (Wang 2022)]] and [[Expert's guide to PINNs (Wang 2023)]].

## Connections

- Exact enforcement of invariants "by construction at the prior level" (App. A, p. 26) is the origin of the [[Physics-informed machine learning]] framing.
- Alternative view: [[Physics-informed prior]] / [[Information field theory]]; the loss as a MAP objective in [[PINN]].
- Neural fields vs operators: [[NIF (Pan 2023)]], [[Operator learning]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[AlexNet (Krizhevsky 2012)]], [[Bayesian DenseED surrogate (Zhu 2018)]], [[SINDy (Brunton 2016)]], [[Tensor basis NN turbulence (Ling 2016)]], [[Universal approximation (Hornik 1989)]]
**Cited by in this wiki**: [[Cardiac activation PINN (Sahli Costabal 2020)]], [[Cardiovascular flow PINNs (Kissas 2020)]], [[Expert's guide to PINNs (Wang 2023)]], [[FNO (Li 2021)]], [[Neural operator (Kovachki 2022)]], [[Respecting causality (Wang 2022)]], [[SINDy delay autoencoders (Bakarji 2022)]], [[SIREN paper (Sitzmann 2020)]], [[When and why PINNs fail (Wang 2022)]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Karniadakis, Raissi, Perdikaris - PINNs - Physics-Informed Neural Networks.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[PINN]] · [[Automatic differentiation]] · [[Burgers equation]] · [[Navier-Stokes equations]] · [[Physics-informed machine learning]]
- [[When and why PINNs fail (Wang 2022)]] · [[Respecting causality (Wang 2022)]] · [[Expert's guide to PINNs (Wang 2023)]] · [[Neural tangent kernel]]
- Applications building on it: [[Hidden fluid mechanics (Raissi 2020)]] · [[Cardiovascular flow PINNs (Kissas 2020)]] · [[Cardiac activation PINN (Sahli Costabal 2020)]]
