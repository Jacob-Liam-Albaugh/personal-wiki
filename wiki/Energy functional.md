---
type: concept
area: me697
areas: [me697, pde, mechanics]
source-ref: "ME 697 book, pinns/basics/energy.ipynb"
tags: [physics-informed, pde, optimization, mechanics]
---

# Energy functional

Variational alternative to the residual loss: instead of penalizing $\mathcal L u - f$, minimize an energy whose minimizer solves the PDE.

> [!definition] Dirichlet energy (source: pinns/basics/energy.ipynb)
> For $-\nabla\cdot(k\nabla u)=f$ with $u=0$ on the boundary:

$$
E[u] = \int_\Omega \Big[\tfrac{k}{2}\,|\nabla u|^2 - f\,u\Big]\,dx.
$$

> [!theorem] Minimizer solves the PDE
> The first variation in direction $v$ is

$$
\delta E[u;v] = \int_\Omega \big[k\,\nabla u\cdot\nabla v - f\,v\big]\,dx.
$$

> Integrating by parts, $\delta E=0$ for all $v$ gives $-\nabla\cdot(k\nabla u)=f$. Working in $W^{1,2}$ the minimizer is unique (source: energy.ipynb).

## Use in a PINN
Evaluate $E$ by quadrature on the network output, with the boundary condition imposed by construction (hard constraint). Only first derivatives are needed, versus second for the residual loss.

> [!failure] Accuracy
> The book found the energy loss less accurate than the residual loss on its example (source: energy.ipynb).

**Wiki note**: the energy notebook contains a `kx`/`ky` slip in `tE_term1`; see [[PINN]]. The energy form is the quadratic case of a [[Physics-informed prior]] energy.

**Covered in**: ASML book pinns/basics (ME 697 5.1)
**Sources**: `text_books/advanced-scientific-machine-learning/book/pinns/basics/energy.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[PINN]] · [[Physics-informed prior]] · [[Non-dimensionalization]] · [[Information field theory]]
