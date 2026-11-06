---
type: method
area: me697
areas: [me697, uq]
tags: [uq, pde, optimization]
---

# Local sensitivity analysis of ODEs

**Summary**: Propagates a small Gaussian uncertainty in the parameters or initial state of an ODE through its solution using one Jacobian $\nabla_\theta x$. The first-order solution is a Gaussian process, so one solve and one derivative replace many Monte Carlo runs.

---

## Setup
IVP $\dot x=f(x,t,\theta)$, $x(0)=x_0(\theta)$, with $\theta\approx\mathcal N(\mu,\Sigma)$.
Taylor expansion of $x(t;\theta)$ about $\mu$ gives, to first order,
$$X\sim\mathrm{GP}\big(x(t;\mu),\,c(t,t')\big)$$
$$c(t,t')=\nabla_\theta x(t;\mu)\,\Sigma\,\nabla_\theta x(t';\mu)^T$$
(source: `up/sensitivity_analysis/01_theory.md`).

## Getting the Jacobian (02)
1. **Autodiff through the solver**: `jax.jacobian` of a Diffrax solve (Duffing example, 03).
2. **Sensitivity ODE**: with $S=\nabla_\theta x$,
$$\dot S=\nabla_x f\,S+\nabla_\theta f$$
$$S(0)=\nabla_\theta x_0(\theta)$$
Solve the original IVP, then this linear one with the same solver.

## When it works
- Small input uncertainty, $f$ differentiable in $\theta$, non-chaotic system.
- Duffing with 5% parameter noise: tracks Monte Carlo for a while, then drifts since the solution is not linear in $\theta$ (03).
- Lorenz: a blob of std $10^{-3}$ spreads over the attractor; mean and variance fail, the variance first (04).

## Wiki notes
- The book calls the sensitivity ODE the "method of adjoints". It is the forward sensitivity equation. The adjoint method runs backward in time and is cheaper for many parameters and a scalar output.
- Higher accuracy keeping nonlinearity: [[Polynomial chaos]].

**Sources**: `advanced-scientific-machine-learning/book/up/sensitivity_analysis/01_theory.md`, `02_diff_ode.md`, `03_example_ode.ipynb`, `04_example_lorenz.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sensitivity analysis]] · [[Sobol indices]] · [[Polynomial chaos]] · [[Gaussian process]]
- [[Automatic differentiation]] · [[ME697 1.3 - Differentiation]] · [[ME697 2.1 - Sensitivity analysis]]
