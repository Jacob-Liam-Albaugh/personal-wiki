---
type: method
area: me697
areas: [me697, pde, operators]
source-ref: "ME 697 book, pinns/parametric"
tags: [physics-informed, operators, pde, uq]
---

# Parametric PINN

A [[PINN]] that takes PDE parameters $\xi$ as extra input, so one training run covers a whole family of problems.

> [!definition] Branch-trunk ansatz (source: pinns/parametric)

$$
N(x,\xi) = \sum_i b_i(\xi)\,\phi_i(x).
$$

The coefficients $b_i(\xi)$ come from a branch network and the basis $\phi_i(x)$ from a trunk network, as in a [[Neural operator]] of DeepONet type.

> [!algorithm] Loss
> Average the PDE residual over the parameter law $p(\xi)$:

$$
\mathcal J = \int \big\| \mathcal L_\xi N(\cdot,\xi) - f \big\|^2\, p(\xi)\, d\xi.
$$

Sample $(x,\xi)$ jointly and minimize as for a standard PINN.

> [!example] Poisson with uncertain coefficient
> The book trains on a Poisson problem with a parameterized coefficient and compares against the forward solves (source: pinns/parametric). See [[ME697 5.2 - Parametric PINNs]] for the setup and numbers.

## Notes
- The trained network is a surrogate for the parametric solution map, usable for uncertainty propagation ([[Surrogate model]]).
- HW7 asks for a PINN parametric over $\delta\in[0,0.5]$ for a neo-Hookean solid ([[ME697 7 - Homework]]).

**Sources**: `advanced-scientific-machine-learning/book/pinns/parametric`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 5.2 - Parametric PINNs]] · [[PINN]] · [[Neural operator]] · [[Surrogate model]] · [[Physics-informed machine learning]]
