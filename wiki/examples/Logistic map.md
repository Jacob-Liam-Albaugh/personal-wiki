---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [mechanics]
data-origin: [analytic]
tasks: [dynamical simulation]
uses: 1
---

# Logistic map

**Summary**: 1 use in ASML (ME 697). Data: analytic. Tasks: dynamical simulation.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/homework/01_homework.ipynb`.
**Last updated**: 2026-11-18

---

## Logistic map bifurcation

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/homework/01_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: dynamical system simulation
- **Technique**: vmap/scan
- **Data origin**: analytic
- **Forward model**: x_{n+1}=r x_n(1-x_n), r in linspace(0,4,1000), x0 in linspace(0,1,100), n=10000 steps (array 1000x100x10000), vectorised in JAX.
- **Ground truth**: none
- **What makes it hard**: Chaos for r>~3.57
- **Libraries**: jax
- **Notes**: Problem 4. Problems 1-3 (factorial, Fibonacci, foldl/scan) are syntax drills, skipped.

## Related pages
- [[Examples catalogue]]
