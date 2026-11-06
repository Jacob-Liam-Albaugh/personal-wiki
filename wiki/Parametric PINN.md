---
type: method
area: me697
areas: [me697, pde, operators]
source-ref: "ME 697 book, pinns/parametric"
tags: [physics-informed, operators, pde, uq]
---

# Parametric PINN

A [[PINN]] that takes PDE parameters $\xi$ as extra input, so one training run covers a whole family of problems.

For a single solve a numerical method is cheaper; for a family of solves, one network trained over the parameter distribution amortizes the cost (source: pinns/intro.md: PINNs can build surrogates of scientific models given as ODEs or PDEs).

> [!definition] Parametric PINN ansatz (parametric_example.ipynb)
> For parameters $\xi$ with density $p(\xi)$, build the network from learned basis functions:

$$
N(x,\xi;\theta) = \sum_{i=1}^{m} b_i(\xi;\theta)\,\phi_i(x;\theta).
$$

The $b_i$ ("branch") depend on $\xi$ only and come from a branch network. The $\phi_i$ ("trunk") are learned basis functions of $x$. This is the split of a [[Neural operator]] of DeepONet type.

> [!algorithm] Loss
> Average the PDE residual over the parameter law $p(\xi)$:

$$
\mathcal J = \int \big\| \mathcal L_\xi N(\cdot,\xi) - f \big\|^2\, p(\xi)\, d\xi.
$$

In the notation of the ansatz, with $\mathcal L_\xi$ the PINN loss at parameter $\xi$,

$$
\mathcal L(\theta) = \int \mathcal L_\xi(\theta)\,p(\xi)\,d\xi.
$$

Sample $(x,\xi)$ jointly and minimize with [[Adam]] using unbiased gradient estimates: draw a few $\xi$ and a fresh set of collocation points each step. The integral over $\xi$ makes the loss an expectation over a joint (collocation point, parameter) distribution, so the unbiasedness argument of [[PINN]] carries over unchanged (Wiki note).

> [!example] Poisson with amplitude parameter
> On $[0,1]^2$ solve
> $$
> -\Delta u = 2\pi^2\,\xi\,\sin(\pi x)\sin(\pi y).
> $$
>
> The exact solution is $u=\xi\sin(\pi x)\sin(\pi y)$ (checked with sympy).
> - Boundary: $u = x(1-x)y(1-y)\,N$, class `EnforceDirichletZeroBoundarySquare`.
> - Model `ParametricModel`: $m=10$ branch MLPs (width 32, depth 3, scalar in and out) and 10 trunks (32 [[Fourier features]] followed by an MLP).
> - Training: 128 collocation points and 2 values of $\xi$ per step, 1000 iterations, about 2.5 minutes.
> - Result "pretty good"; more iterations would fit better (source: parametric_example.ipynb).

## Notes
- The trained network is a surrogate for the parametric solution map, usable for uncertainty propagation ([[Surrogate model]]).
- Once trained, sample $\xi\sim p(\xi)$ and evaluate $N$: uncertainty propagation without a solver. Same trunk-branch idea as [[DeepONet]]; the physics loss replaces paired data. See [[Operator learning]].
- Physics-informed neural operators: `physics-informed_nops.ipynb` has only a title in the book.

> [!example] Homework 7 problem 3, part C
> Parametric neo-Hookean problem with the applied displacement $\delta\in[0,0.5]$ as network input, see [[PINN]].

**Covered in**: ASML book pinns/parametric (ME 697 5.2); homework 7
**Sources**: `advanced-scientific-machine-learning/book/pinns/parametric`, `advanced-scientific-machine-learning/book/pinns/intro.md`, `pinns/parametric/parametric_example.ipynb`, `pinns/parametric/physics-informed_nops.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[PINN]] · [[Neural operator]] · [[Surrogate model]] · [[Physics-informed machine learning]]
