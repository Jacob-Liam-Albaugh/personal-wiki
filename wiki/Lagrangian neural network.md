---
type: method
area: physics-informed
areas: [physics-informed, ml, mechanics]
source-ref: "Cranmer et al. 2020, eqs. 3-6"
tags: [physics-informed, mechanics, ml]
---

# Lagrangian neural network

> [!definition] Lagrangian neural network (LNN)
> A network $L_\theta(q,\dot q)\in\mathbb R$ used as the Lagrangian. Accelerations follow from Euler-Lagrange:
> $$\ddot q=(\nabla_{\dot q}\nabla_{\dot q}^{\top}L)^{-1}\big[\nabla_q L-(\nabla_q\nabla_{\dot q}^{\top}L)\,\dot q\big].$$
>
> (source: LNNs.pdf, eq. 6, p. 3)

**Intuition**: the Lagrangian formalism works in any generalized coordinates, so the model needs no canonical momentum. The price is a Hessian inverse of the network, computed with [[Automatic differentiation]] (JAX), and the need for smooth activations (softplus, not ReLU).

## Compared with neighbours (source: LNNs.pdf, Table 1, p. 2)
- Plain net: no exact conservation law.
- [[Hamiltonian neural network]]: exact conservation, but needs canonical coordinates.
- DeLaN (Lutter 2019): arbitrary coordinates but kinetic energy restricted to $\dot q^\top M(q)\dot q$.
- LNN: arbitrary Lagrangian, arbitrary coordinates.

## Variants
- Lagrangian graph network: sum a learned Lagrangian density over neighbourhoods; applied to the 1D wave equation. See [[Graph neural network]].

## Where it appears
- [[LNNs (Cranmer 2020)]] — origin and experiments.
- [[Neural ODE]] — LNN is a Neural ODE once $\ddot q$ is integrated.

**Sources**: `papers/Physics Informed Architectures/Cranmer, Greydanus, Ho - LNNs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Hamiltonian neural network]] · [[Neural ODE]] · [[HNNs (Greydanus 2019)]] · [[Physics-informed machine learning]] · [[Graph neural network]]
