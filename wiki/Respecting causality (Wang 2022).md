---
type: paper
area: physics-informed
areas: [physics-informed, pde]
source-ref: "Wang, Sankaran, Perdikaris, arXiv:2203.07404 (14 Mar 2022)"
tags: [physics-informed, pde, optimization, ml]
authors: ["[[Sifan Wang]]", "[[Shyam Sankaran]]", "[[Paris Perdikaris]]"]
year: 2022
venue: "arXiv:2203.07404"
file: "papers/Physics Informed Architectures/Wang, Sankaran, Perdikaris - Respecting Causality is All You Need for Training PINNs.pdf"
---

# Respecting causality is all you need for training PINNs (Wang 2022)

**Summary**: Continuous-time [[PINN]]s trained by gradient descent fit late times before early times, violating temporal causality. Weighting each time slice's residual by the exponential of the cumulative earlier residual forces the network to resolve the solution in order, and made PINNs work for the first time on the chaotic Lorenz system, chaotic Kuramoto-Sivashinsky and 2D decaying turbulence (source: causality.pdf, abstract, p. 1).

**Authors**: Sifan Wang, Shyam Sankaran, Paris Perdikaris · **Year**: 2022

---

## Problem and diagnosis (§2)

PDE with initial and boundary conditions (eqs. 2.1-2.3, p. 3):
$$u_t+\mathcal N[u]=0,\quad u(0,x)=g(x),\quad \mathcal B[u]=0.$$
Composite loss (eq. 2.4):
$$L=\lambda_{ic}L_{ic}+\lambda_{bc}L_{bc}+\lambda_rL_r.$$
Case study: Allen-Cahn $u_t-0.0001u_{xx}+5u^3-5u=0$ with $u(x,0)=x^2\cos\pi x$ (eqs. 2.8-2.11). A tanh MLP (4 layers x 128) with exact periodic BCs and 200,000 Adam iterations gets stuck at an intermediate state: relative $L^2$ error 49.87% (Fig. 1, p. 5; Table 1 lists 4.98e-1 for the original formulation).

Why: split the residual by time slice,
$$L_r(t,\theta)=\tfrac1{N_x}\sum_j\big|\partial_tu_\theta+\mathcal N[u_\theta]\big|^2(t,x_j).$$
Discretizing $\partial_t$ by forward Euler shows $L_r(t_i)$ depends on $u_\theta(t_i)$ and $u_\theta(t_{i-1})$ (eq. 2.16, p. 4). Minimizing all slices at once can drive $L_r(t_i)$ small while earlier predictions are still wrong, so a small residual is meaningful only if earlier times are already accurate (p. 4).

Implicit bias: with the empirical NTK of the residual, $K_\theta(t)_{ij}=\langle\partial_\theta R(t,x_i),\partial_\theta R(t,x_j)\rangle$ (eq. 2.17), the temporal convergence rate is
$$C(t)=\mathrm{Tr}(K_\theta(t))/N_t\quad(\text{Def. 2.1}).$$
$C(t)$ is larger for larger $t$, so late-time residuals converge first (Fig. 2, p. 5). This builds on the [[Neural tangent kernel]] analysis in [[When and why PINNs fail (Wang 2022)]].

## Causal training (§3)

Weighted residual loss (eq. 3.1):
$$L_r(\theta)=\tfrac1{N_t}\sum_{i}w_i\,L_r(t_i,\theta).$$
$$w_i=\exp\Big(-\epsilon\sum_{k<i}L_r(t_k,\theta)\Big)\quad(\text{eq. 3.2})$$
A slice only gets weight once all earlier slices have small residual. $\epsilon$ is the causality parameter (p. 6). The initial-condition loss is treated as the residual at $t=0$ (p. 7).

- Weights are functions of $\theta$ but gradients are stopped through them (`lax.stop_gradient` in JAX) and the extra cost is negligible (Algorithm 1 remarks 2-3, p. 8).
- Stopping criterion: stop when $\min_i w_i>\delta$ with $\delta\in(0,1)$; weights start at zero except $t=0$ and rise to 1 as training converges (p. 6).
- Sensitivity to $\epsilon$: too small fails to enforce late times, too large makes activation hard. Remedy: anneal through an increasing sequence. Recommended: $\lambda_{ic}=10^3$, $\delta=0.99$, $\epsilon\in\{10^{-2},10^{-1},1,10,100\}$ (p. 8).
- Relation to others: similar to adaptive time sampling (Wight et al.), which needs hand-designed densities, and complementary to time marching, since causality can still be violated inside a window (pp. 8-9).
- Applicable to any physics-informed pipeline, including physics-informed [[DeepONet]] and neural operators (p. 8).

Allen-Cahn results (Table 1, p. 6), relative $L^2$ error:

| Method | Error |
|---|---|
| Raissi original | 4.98e-1 |
| Adaptive time sampling | 2.33e-2 |
| Self-attention | 2.10e-2 |
| Time marching | 1.68e-2 |
| Causal (MLP) | 1.43e-3 |
| Causal (modified MLP) | 1.39e-4 |

## Practical additions (§4)

- **Modified MLP**: two encoders $U,V$ of the input merged into each hidden layer by gating, $H^{(l+1)}=(1-Z^{(l)})\odot U+Z^{(l)}\odot V$ (p. 9).
- **Exact periodic BCs** via a Fourier embedding $v(x)=(1,\cos\omega x,\sin\omega x,\dots,\cos m\omega x,\sin m\omega x)$ (Dong et al.), so any network of $v(x)$ is periodic. See [[Fourier features]].
- **Taylor-mode [[Automatic differentiation]]** for high-order derivatives (needed for Kuramoto-Sivashinsky); 3-5x training speed-up over reverse mode in their test (pp. 10, 12).
- **Data parallelism** across GPUs with `jax.pmap`; weak-scaling efficiency above 99% (p. 15).

## Benchmarks (§5)

All use modified MLP, tanh, Glorot init, Adam, exponential decay, plus time marching (p. 10).

| Problem | Setup | Relative $L^2$ error |
|---|---|---|
| Lorenz (sigma=3, rho=28, beta=8/3, T=20) | start [1,1,1] | x 1.139e-2, y 1.656e-2, z 7.038e-3 (p. 11) |
| Kuramoto-Sivashinsky, regular | alpha=5, beta=0.5, gamma=0.005, T=1 | 3.49e-4 (p. 12) |
| Kuramoto-Sivashinsky, chaotic | alpha=100/16, T=0.5 | 2.46e-2 in text, 2.26e-2 in Fig. 9 caption (p. 13) |
| 2D Navier-Stokes decaying turbulence, Re=100, T=1 | no training data | u 3.90e-2, v 2.61e-2, w 3.53e-2 (p. 14) |

Limits: for the chaotic KS case with $u_0=\cos x(1+\sin x)$ to $T=0.9$, the transition to chaos near $t=0.4$ is captured but error exceeds 10% after $t=0.8$; long-time integration remains a PINN weakness (p. 13). Removing the stopping criterion gave slightly lower losses but worse predictions (p. 11).

Wiki note: the two KS error values (2.46e-2 vs 2.26e-2) disagree inside the paper; the page reports both.

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Cardiac activation PINN (Sahli Costabal 2020)]], [[Cardiovascular flow PINNs (Kissas 2020)]], [[Glorot init (Glorot 2010)]], [[Hidden fluid mechanics (Raissi 2020)]], [[NTK (Jacot 2018)]], [[PINNs (Raissi 2019)]], [[Physics-informed ML review (Karniadakis 2021)]], [[When and why PINNs fail (Wang 2022)]]
**Cited by in this wiki**: [[Expert's guide to PINNs (Wang 2023)]]
**Software cited**: [[software#DeepXDE|DeepXDE]], [[software#JAX|JAX]], [[software#Matplotlib|Matplotlib]], [[software#NumPy|NumPy]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Wang, Sankaran, Perdikaris - Respecting Causality is All You Need for Training PINNs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[PINN]] · [[PINNs (Raissi 2019)]] · [[When and why PINNs fail (Wang 2022)]] · [[Expert's guide to PINNs (Wang 2023)]]
- [[Neural tangent kernel]] · [[Navier-Stokes equations]] · [[Physics-informed machine learning]] · [[Adam]]
