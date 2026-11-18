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

# Neo-Hookean hyperelasticity PINN

**Summary**: 1 use in ASML (ME 697). Data: analytic. Tasks: physics-informed.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/homework/07_homework.ipynb`.
**Last updated**: 2026-11-18

---

## Neo-Hookean hyperelasticity PINN

`text_books/advanced-scientific-machine-learning/book/homework/07_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: PINN forward solve
- **Technique**: Energy PINN, Fourier features, MLP 3x128 tanh, Adam 1e-3, 32 collocation; delta=0.1, continuation to 0.5, then parametric delta in [0,0.5] with branch-trunk (n=10)
- **Data origin**: analytic
- **Forward model**: Unit square, energy E=int 1/2(sum F_ij^2-2)-ln detF+50 (ln detF)^2, F=I+grad u; u1(0)=0,u1(1)=delta; BCs built into ansatz.
- **Unknown dimension**: network weights
- **Ground truth**: none
- **What makes it hard**: delta=0.5 fails without continuation
- **Libraries**: jax, equinox, optax
- **Notes**: Problem 3.

## Related pages
- [[Examples catalogue]]
- [[PINN]] · [[Parametric PINN]] · [[Fourier features]] · [[Adam]]
