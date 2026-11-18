---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [physics-informed, pde]
data-origin: [analytic]
tasks: [physics-informed]
uses: 1
---

# Parametric Poisson

**Summary**: 1 use in ASML (ME 697). Data: analytic. Tasks: physics-informed.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/pinns/parametric/parametric_example.ipynb`.
**Last updated**: 2026-11-18

---

## Parametric Poisson on unit square (branch-trunk PINN)

`text_books/advanced-scientific-machine-learning/book/pinns/parametric/parametric_example.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: PINN forward solve (parametric)
- **Technique**: DeepONet-style u(x,y;xi)=sum b_i(xi) t_i(x,y), 10 branches and 10 trunks, residual loss
- **Data**: No data; random xi ~ U[0,1] and collocation points.
- **Data origin**: analytic
- **Forward model**: -Lap(u)=f on [0,1]^2 with f=2 pi^2 xi sin(pi x) sin(pi y), zero Dirichlet; exact u=xi sin(pi x) sin(pi y).
- **Unknown dimension**: network weights; 1 parameter xi
- **Ground truth**: Exact analytic solution
- **Libraries**: jax, equinox, optax
- **Notes**: 1000 iterations; loss 5.7e-2 -> 2.1e-2, i.e. under-trained.

## Related pages
- [[Examples catalogue]]
- [[PINN]] · [[Parametric PINN]] · [[DeepONet]] · [[Poisson and Laplace equations]]
