---
type: paper
area: physics-informed
areas: [physics-informed, ml, mechanics]
source-ref: "Cranmer, Greydanus, Hoyer, Battaglia, Spergel, Ho 2020, ICLR workshop, eqs. 2-8"
tags: [physics-informed, mechanics, ml]
authors: ["[[Miles Cranmer]]", "[[Sam Greydanus]]", "[[Stephan Hoyer]]", "[[Peter Battaglia]]", "[[David Spergel]]", "[[Shirley Ho]]"]
year: 2020
venue: "ICLR 2020 workshop (arXiv 2003.04630)"
file: "papers/Physics Informed Architectures/Cranmer, Greydanus, Ho - LNNs.pdf"
---

# Lagrangian Neural Networks (Cranmer 2020)

**Summary**: Learn a black-box Lagrangian $L_\theta(q,\dot q)$ with a network and recover accelerations by solving the Euler-Lagrange equation numerically with automatic differentiation. Unlike [[HNNs (Greydanus 2019)]], no canonical momenta are needed, so it works in arbitrary coordinates. Shown on a double pendulum, a relativistic particle, and a 1D wave equation via a Lagrangian graph network.

**Authors**: Miles Cranmer, Sam Greydanus, Stephan Hoyer, Peter Battaglia, David Spergel, Shirley Ho · **Year**: 2020 · **File**: `papers/Physics Informed Architectures/Cranmer, Greydanus, Ho - LNNs.pdf`

---

## Problem

Hamiltonian networks require canonical coordinates obeying the Poisson bracket relations
$$\{q_i,q_j\}=0,\quad\{p_i,p_j\}=0,\quad\{q_i,p_j\}=\delta_{ij}$$
(eq. 1, p. 2), but many datasets give $p_i\ne m\dot q_i$. Deep Lagrangian Networks (DeLaN, Lutter 2019) assume kinetic energy $T=\dot q^\top M(q)\dot q$, which excludes e.g. a charged particle in a magnetic field or a relativistic particle (p. 3).

## Method

Action $S=\int_{t_0}^{t_1}(T-V)\,dt$ (eq. 2); stationarity gives the Euler-Lagrange equation $\frac{d}{dt}\frac{\partial L}{\partial\dot q_j}=\frac{\partial L}{\partial q_j}$ (eq. 3, p. 3).

> [!algorithm] Dynamics from a parametric Lagrangian
> Expanding the time derivative by the chain rule (eq. 5):
> $$(\nabla_{\dot q}\nabla_{\dot q}^{\top}L)\,\ddot q+(\nabla_{q}\nabla_{\dot q}^{\top}L)\,\dot q=\nabla_q L.$$
> Solving for the acceleration (eq. 6):
> $$\ddot q=(\nabla_{\dot q}\nabla_{\dot q}^{\top}L)^{-1}\big[\nabla_q L-(\nabla_q\nabla_{\dot q}^{\top}L)\,\dot q\big].$$
> The loss compares predicted $\ddot x$ with the true one. The pseudoinverse is used to avoid singular Hessians; cost is $O(d^3)$ in the number of coordinates $d$. Appendix A gives a few lines of JAX.
>
> (source: LNNs.pdf, eqs. 4-6, p. 3-4, App. A) See [[Lagrangian neural network]].

Practical choices (p. 4): four layers, 500 hidden units, batch size 32, decaying learning rate from $10^{-3}$. Because the Hessian of the network is taken, the second derivative of the activation matters: ReLU is a poor choice, softplus won a search over ReLU$^2$, ReLU$^3$, tanh, sigmoid, softplus. A custom initialization scheme is in Appendix C.

**Lagrangian graph network** (§5): total Lagrangian $L=\sum_i L_{\mathrm{density}}(\{\phi_j,\dot\phi_j\}_{j\in I_i})$ over neighbour groups (eq. 7), with $\ddot\phi$ from eq. 8. For a 1D grid the Hessian is sparse; it needs 5 forward-over-backward passes and linear-time inversion.

## Results

- **Double pendulum** (pp. 4-5): 600,000 random initial conditions, accelerations as targets. Final losses 7.3 (LNN) vs 7.4 ($\times10^{-2}$) baseline. Mean energy discrepancy (40 initial conditions, 100 steps) was 8% of max potential energy for the baseline and 0.4% for the LNN.
- **Relativistic particle**, $L=((1-\dot q^2)^{-1/2}-1)+gq$ with canonical momentum $\dot q(1-\dot q^2)^{-3/2}$: HNN fails on non-canonical inputs $(q,\dot q)$, succeeds with canonical coordinates; LNN learns from arbitrary coordinates as accurately as the canonical HNN (Fig. 3).
- **1D wave equation** with periodic boundary: the graph version fits the dynamics and almost exactly conserves total energy (Fig. 4).

## Limitations

- Needs the Hessian $\nabla_{\dot q}\nabla^\top_{\dot q}L$ to be invertible; pseudoinverse used (p. 4).
- $O(d^3)$ inverse per step; sparsity exploited only in the graph variant.
- Activation and initialization are sensitive because of second derivatives (p. 4).
- Wiki note: the paper reports only simulated, noise-free systems and compares to energy-drift, not to long-horizon trajectory accuracy beyond the pendulum; no friction or forcing is treated.

## Connections

- Direct response to [[HNNs (Greydanus 2019)]]; Table 1 (p. 2) positions LNN against plain nets, [[Neural ODEs (Chen 2018)]], HNN and DeLaN.
- Exploits [[Automatic differentiation]] of Hessians (JAX).
- The graph variant is a [[Graph neural network]].
- See [[Hamiltonian neural network]], [[Lagrangian neural network]], [[Physics-informed machine learning]].

%% refs:start %%
**Cites in this wiki**: [[Glorot init (Glorot 2010)]], [[HNNs (Greydanus 2019)]], [[Neural ODEs (Chen 2018)]], [[Symbolic models from deep learning (Cranmer 2020)]]
**Cited by in this wiki**: [[Symbolic models from deep learning (Cranmer 2020)]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Cranmer, Greydanus, Ho - LNNs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Lagrangian neural network]] · [[Hamiltonian neural network]] · [[Neural ODE]] · [[Graph neural network]]
- [[HNNs (Greydanus 2019)]] · [[Neural ODEs (Chen 2018)]] · [[Physics-informed machine learning]]
