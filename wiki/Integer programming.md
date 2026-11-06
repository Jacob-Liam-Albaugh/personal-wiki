---
type: concept
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 10-11"
tags: [optimization]
---

# Integer programming

> [!definition] Mixed integer program (source: MIT (ch 1-5).pdf, p. 452)
> $$\min\ \mathbf c'\mathbf x+\mathbf d'\mathbf y$$
> $$\mathbf A\mathbf x+\mathbf B\mathbf y=\mathbf b,\quad\mathbf x,\mathbf y\ge\mathbf0,\quad\mathbf x\ \text{integer}$$
> If all variables are integer it is a pure integer program, and a zero-one program if restricted to $\{0,1\}$.

**Intuition**: a [[Linear programming]] problem with integrality constraints. The LP relaxation, obtained by dropping integrality, gives a lower bound that the exact methods improve on.

## Key facts
- Modeling devices: knapsack, forcing constraints $x_A\le x_B$, disjunctions with a binary $y$ ($\mathbf a'\mathbf x\ge yb$, $\mathbf c'\mathbf x\ge(1-y)d$), piecewise linear costs, set covering, packing and partitioning ($\mathbf A\mathbf x\ge\mathbf e$, $\le$, $=$) (BT §10.1, pp. 452-461).
- A formulation is judged by how closely its LP relaxation approximates the convex hull of the integer feasible points; a stronger formulation may need exponentially many constraints, which separation can handle (BT §10.2, p. 461-465).
- No efficient general algorithm is known. BT group methods as exact, approximation and heuristic (BT p. 480).
- Cutting planes: solve the relaxation, add a valid inequality cutting off the fractional optimum, repeat; Gomory cuts come from tableau rows by rounding down coefficients (BT p. 481-482), re-solving with the [[Dual simplex method]].
- Branch and bound: bound with the LP relaxation, prune when the lower bound is at least the best known cost, branch on a fractional variable into $x_i\le\lfloor x_i^*\rfloor$ and $x_i\ge\lceil x_i^*\rceil$ (BT p. 485-487). Branch and cut adds cuts at nodes.
- Dynamic programming for knapsack (BT p. 490-493).
- Lagrangean dual: $Z(\mathbf p)=\min_{\mathbf x\in X}(\mathbf c'\mathbf x+\mathbf p'(\mathbf b-\mathbf A\mathbf x))\le Z_{IP}$ for $\mathbf p\ge\mathbf0$; maximizing over $\mathbf p$ gives a bound, but unlike [[LP duality]] there is no strong duality in general; $Z$ is concave and piecewise linear, optimized by subgradients (BT p. 494-507).
- Approximation algorithms, local search, simulated annealing and NP-completeness complete BT ch11 (§11.5-11.8).
- Network flow and assignment problems are the special cases treated in the LP chapters ([[Network flow problem]]).

## Where it appears
- [[BT ch10 - Integer programming formulations]]: modeling and strong formulations.
- [[BT ch11 - Integer programming]]: algorithms and theory.
- [[BT ch6 - Large scale optimization]]: column generation and cutting plane tools reused here.

**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 10-11).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[LP duality]] · [[Dual simplex method]] · [[Network flow problem]] · [[Polyhedron]] · [[Convex function]]
