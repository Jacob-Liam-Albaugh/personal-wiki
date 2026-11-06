---
type: method
area: physics-informed
areas: [physics-informed, ml, optimization]
source-ref: "Chen et al. 2018, §2, eqs. 3-5, Alg. 1"
tags: [physics-informed, optimization, ml]
---

# Adjoint sensitivity method

> [!algorithm] Gradients through an ODE solve
> For $L(z(t_1))$ with $z$ solving $\dot z=f(z,t,\theta)$ define the adjoint $a(t)=\partial L/\partial z(t)$. Then
> $$\dot a(t)=-a(t)^{\top}\frac{\partial f}{\partial z}$$
> $$\frac{dL}{d\theta}=-\int_{t_1}^{t_0}a(t)^{\top}\frac{\partial f}{\partial\theta}\,dt$$
> Integrate $[z,\,a,\,\partial L/\partial\theta]$ backwards from $t_1$ to $t_0$ with one solver call.
>
> (source: Neural ODEs.pdf, eqs. 4-5, Alg. 1, pp. 2-3)

**Intuition**: the adjoint is the instantaneous chain rule. It runs backwards in time, so the forward pass need not store activations; $z(t)$ is recomputed along the way. Memory is $O(1)$ in depth; cost is linear in problem size, and the solver controls the numerical error. The needed vector-Jacobian products are supplied by [[Automatic differentiation]].

## Points to note
- Alternative: differentiate through the solver's operations (high memory, extra error).
- Forward sensitivity analysis (used in Stan) is quadratic in the number of variables; adjoint is linear (source: Neural ODEs.pdf, §7, p. 9).
- With several observation times the backward solve is split and the adjoint is jumped at each observation.
- Backward reconstruction of $z$ can drift; checkpointing stores selected forward states.
- Wiki note: the idea is Pontryagin-era optimal control (cited p. 2); the paper's contribution is the generic vector-Jacobian formulation inside deep-learning AD.

## Where it appears
- [[Neural ODEs (Chen 2018)]] — derivation and Algorithm 1.
- [[Neural ODE]] — training method.

**Sources**: `Physics Informed Architectures/Chen, Rubanova, Bettencourt, Duvenaud - Neural ODEs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Neural ODE]] · [[Automatic differentiation]] · [[Neural ODEs (Chen 2018)]] · [[Gradient descent]]
