---
type: method
area: me697
areas: [me697, uq]
tags: [uq, sampling]
---

# Latin hypercube sampling

**Summary**: A stratified space-filling design: divide each axis into $N$ equal intervals and place exactly one of $N$ points in each interval along every axis. Compared with plain random sampling, it estimates moments of a model output with smaller error. Sobol sequences are the other design used in the course.

---

## Latin hypercube (06)
- A Latin square has one sample in each row and column; a Latin hypercube generalizes to $d$ dimensions.
- `scipy.stats.qmc.LatinHypercube(d)` generates the design on $[0,1]^d$; map to other distributions through the inverse CDF.
- Test case: $\dot y=-ay$, $a=0.1x_1$, $y_0=8+2x_2$, $x_i\sim\mathcal U(0,1)$, with exact mean and variance known. LHS reaches a smaller root squared error in $\mathbb V[y(t)]$ than uniform sampling at the same $N$.
- A single run is noisy; repeating about 100 times gives error bars on the error.
- Adding points to an existing LHS breaks its stratification (07).

## Sobol sequence (07)
- A deterministic low-discrepancy sequence, extendable point by point.
- Discrepancy measures how evenly points fill the space; the book compares the centered discrepancy of Sobol, LHS and random points.
- Direction numbers come from primitive polynomials over GF(2) (Joe-Kuo).
- Wiki note: balance properties hold for $2^m$ points; the code comment attributing the power-of-2 requirement to LHS is mistaken, since LHS works for any $N$.

## Uses
- Training and validation sets for a [[Surrogate model]]; multi-fidelity example data ([[ME697 2.4 - Multi-fidelity modeling]]).
- The Saltelli design behind [[Sobol indices]] in SALib.

**Sources**: `advanced-scientific-machine-learning/book/up/sensitivity_analysis/06_lhs.ipynb`, `07_sobol.ipynb`; `up/surrogates/01_basics_of_surrogate_models.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sensitivity analysis]] · [[Sobol indices]] · [[Surrogate model]] · [[Active learning]]
- [[ME697 2.1 - Sensitivity analysis]] · [[ME697 2.3 - Surrogates]] · [[ME697 2.5 - Active learning]]
