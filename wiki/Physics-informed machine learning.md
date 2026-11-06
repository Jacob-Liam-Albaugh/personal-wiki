---
type: concept
area: physics-informed
areas: [physics-informed, ml, pde]
source-ref: "Karniadakis et al. 2021 review, Box 2 and §2-§5; Wiki note synthesis"
tags: [physics-informed, ml, pde, mechanics]
---

# Physics-informed machine learning

**Summary**: Learning methods that use prior physical, empirical or mathematical knowledge to improve training and generalization. The review separates three ways to inject it: through data, through architecture, and through the loss (source: review.pdf, p. 3-4, Box 2).

## The three biases

- **Observational bias**: data (or augmentation) that embody the physics. Simple but data hungry.
- **Inductive bias**: architectures that satisfy constraints exactly, such as equivariant or symplectic networks and hard-coded boundary conditions. Strict but limited to simple, known structure.
- **Learning bias**: soft penalties in the loss, e.g. a PDE residual in a [[PINN]]. Flexible but only approximate.

They can be mixed. Details: [[Physics-informed ML review (Karniadakis 2021)]].

## Where pages in this wiki sit

| Family | Idea | Pages |
|---|---|---|
| Learning bias (PDE residual) | residual of a known PDE in the loss | [[PINN]], [[PINNs (Raissi 2019)]] |
| Training of residual losses | loss balance, causality, [[Spectral bias]] | [[When and why PINNs fail (Wang 2022)]], [[Respecting causality (Wang 2022)]], [[Expert's guide to PINNs (Wang 2023)]], [[Neural tangent kernel]] |
| Inductive bias (mechanics) | energy-conserving structure | [[Hamiltonian neural network]], [[Lagrangian neural network]] |
| Inductive bias (continuous depth) | dynamics as a vector field | [[Neural ODE]] |
| Equation discovery | sparse dictionary regression | [[SINDy]] |
| Physics in the kernel | RKHS norm equals mechanical energy | [[Energy-based kernels for viscoelastic flow (Otto 2024)]] |
| Neural fields | parameter-conditioned implicit nets | [[Neural implicit flow]] |
| Bayesian reading | physics as a prior, soft penalty as MAP | [[Physics-informed prior]], [[Information field theory]] |

## Observations from the review

- Soft-penalty solutions correspond to a MAP estimate under a physics-based likelihood (review.pdf, p. 7).
- PINNs shine on inverse and ill-posed problems; well-posed forward problems are still better served by grid solvers (p. 8).
- Neural networks can be read as kernel methods with a learned kernel ([[Kernel methods]]).
- Wiki note: the same split (exact structure versus soft penalty) recurs in operator learning ([[Operator learning]]) and [[Equivariance]].

**Sources**: `papers/Physics Informed Architectures/Karniadakis, Lu, Kevrekidis, Perdikaris - Physics-Informed Machine Learning.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[PINN]] · [[Physics-informed ML review (Karniadakis 2021)]] · [[Neural ODE]] · [[SINDy]] · [[Hamiltonian neural network]]
- [[Lagrangian neural network]] · [[Neural implicit flow]] · [[Neural tangent kernel]] · [[Physics-informed prior]]
- [[Symbolic models from deep learning (Cranmer 2020)]].
