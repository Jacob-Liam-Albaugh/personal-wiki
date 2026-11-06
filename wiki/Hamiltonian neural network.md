---
type: method
area: physics-informed
areas: [physics-informed, ml, mechanics]
source-ref: "Greydanus et al. 2019, eqs. 1-3"
tags: [physics-informed, mechanics, ml]
---

# Hamiltonian neural network

> [!definition] Hamiltonian neural network (HNN)
> A network $H_\theta(q,p)\in\mathbb R$ whose symplectic gradient is the dynamics:
> $$\dot q=\frac{\partial H_\theta}{\partial p},\qquad \dot p=-\frac{\partial H_\theta}{\partial q}.$$
> Trained by regressing these onto observed $(\dot q,\dot p)$ (eq. 3 of the paper).
>
> (source: HNNs.pdf, eqs. 2-3, pp. 2-3)

**Intuition**: instead of learning the vector field, learn the energy and differentiate it. A field built as a symplectic gradient automatically keeps $H_\theta$ constant along trajectories and preserves phase-space volume (Liouville), so rollouts are exactly reversible. The learned $H_\theta$ equals the true energy only up to a constant, which is physically harmless.

## Properties
- Conserves the learned $H_\theta$ exactly in continuous time; numerically only as well as the integrator.
- Needs canonical coordinates $(q,p)$; with an autoencoder, an auxiliary loss pushes latent halves to behave canonically (source: [[HNNs (Greydanus 2019)]], eq. 7).
- Cannot represent dissipation: friction must be modelled separately.
- Adding energy by moving along $(\partial H/\partial q,\partial H/\partial p)$ gives counterfactuals.

## Failure modes
- Non-canonical inputs, e.g. relativistic particle with $(q,\dot q)$: HNN fails, [[Lagrangian neural network]] succeeds (source: [[LNNs (Cranmer 2020)]], Fig. 3).

## Where it appears
- [[HNNs (Greydanus 2019)]] — origin.
- [[LNNs (Cranmer 2020)]] — baseline and contrast.
- [[Neural ODE]] — HNN is a Neural ODE with a structured vector field.

**Sources**: `papers/Physics Informed Architectures/Greydanus, Dzamba, Yosinski - HNNs.pdf`, `Cranmer, Greydanus, Ho - LNNs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Lagrangian neural network]] · [[Neural ODE]] · [[Physics-informed machine learning]] · [[PINN]] · [[Equivariance]]
