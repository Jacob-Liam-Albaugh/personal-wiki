---
type: definition
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 1; Bazaraa, Jarvis, Sherali 2010, ch. 1"
tags: [optimization]
---

# Linear programming

> [!definition] Linear program, standard form (source: MIT (ch 1-5).pdf, p. 4, eq. 1.3)
> $$\min\ \mathbf c'\mathbf x\quad\text{s.t.}\quad \mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf 0 .$$

**Intuition**: minimize a linear cost over a [[Polyhedron]]. Reading of the constraint: $\sum_i\mathbf A_ix_i=\mathbf b$ builds the target $\mathbf b$ from nonnegative amounts of the column "resources" $\mathbf A_i$ at unit cost $c_i$ (BT ch1, p. 4).

## Key facts
- The general form has $\ge$, $\le$ and $=$ rows and sign-restricted or free variables (BT eq. 1.1, p. 3). Every LP converts to standard form by splitting free variables and adding slack or surplus variables (BT ch1, pp. 5-6). Maximizing $\mathbf c'\mathbf x$ is minimizing $-\mathbf c'\mathbf x$.
- Cost can be unbounded ($-\infty$); the feasible set can be empty.
- A feasible set with an extreme point and a finite optimum has an optimal extreme point, so it suffices to search [[Basic feasible solution]]s (BT ch2, Thm 2.7-2.8).
- Every LP has a partner problem; see [[LP duality]] (weak and strong duality, complementary slackness).
- Piecewise linear convex costs, absolute values and minimax objectives are LPs after adding variables (BT ch1, §1.3).
- Algorithms: [[Simplex method]] and [[Dual simplex method]] (vertex walks, exponential worst case), [[Ellipsoid method]] (polynomial, impractical), [[Interior point method]] (polynomial and competitive). Structured LPs: [[Dantzig-Wolfe decomposition]], [[Network flow problem]]. Adding integrality gives [[Integer programming]].

## Where it appears
- [[BT ch1 - Introduction]], [[BJS ch1 - Introduction]]: forms, modeling, graphical solution.
- [[BT ch2 - Geometry of linear programming]], [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]]: geometry of the feasible set.
- [[BT ch3 - The simplex method]], [[BJS ch3 - The simplex method]], [[BJS ch4 - Starting solution and convergence]]: solving it.
- [[BT ch4 - Duality theory]], [[BJS ch6 - Duality and sensitivity analysis]], [[BT ch5 - Sensitivity analysis]]: duality and sensitivity.
- [[BT ch8 - Complexity of LP and the ellipsoid method]], [[BT ch9 - Interior point methods]], [[BJS ch8 - Complexity of the simplex algorithm and polynomial-time algorithms]]: complexity and polynomial algorithms.
- [[BT ch12 - The art in linear optimization]]: solvers in practice.

## Duality
- Basu derives LP strong duality from the valid-inequality theorem (Farkas) and treats the LP dual as a case of conic duality (source: Basu 2018, Thm 2.85, p. 35; ch. 4 pp. 80-84).

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (ch. 1-2, 8-9, 12); `Linear Optimization/BJS full book.pdf` (ch. 1).
**Last updated**: 2026-11-06

---

## Related pages
- [[Polyhedron]] · [[Basic feasible solution]] · [[Simplex method]] · [[LP duality]] · [[Integer programming]] · [[Convex set]] · [[Convex function]] · [[KKT conditions]] · [[Network flow problem]]
- [[Basu ch4 - Convex optimization]], [[Convex set]].
