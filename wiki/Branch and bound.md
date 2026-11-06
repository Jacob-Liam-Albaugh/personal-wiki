---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, §11.2-11.3"
tags: [optimization]
---

# Branch and bound

> [!algorithm] LP-based branch and bound (source: MIT (ch 1-5).pdf, pp. 485-487)
> Partition the feasible set $F$ into $F_1,\dots,F_k$, solve each subproblem, keep the best, recursing into a tree. With a lower bound $b(F_i)$ (commonly the LP relaxation cost) and upper bound $U$ (best feasible cost so far), prune $F_i$ if $b(F_i)\ge U$. At a node solve the LP relaxation: if infeasible, prune; if the solution is integer, update $U$; otherwise pick a fractional $x_i^*$ and create two children with $x_i\le\lfloor x_i^*\rfloor$ and $x_i\ge\lceil x_i^*\rceil$.

**Intuition**: an exact method for [[Integer programming]] whose success depends on tight lower bounds (see strong formulations and [[Lagrangian relaxation]]). Each child adds one constraint, so the [[Dual simplex method]] warm-starts from the parent's optimum. Worst case is exponential (BT Exercise 11.4).

## Key facts
- Example 11.4 (p. 487-488), the problem of the cutting-plane example (minimize $x_1-2x_2$ s.t. $-4x_1+6x_2\le9$, $x_1+x_2\le4$): the tree closes after four subproblems $F_1$ to $F_4$ with $U=-3$ and optimum $(1,2)$.
- Example 11.5 (p. 488-489): directed TSP with assignment problem relaxations ([[Assignment problem]]) and branching by prohibiting an arc of a subtour.
- **Branch and cut** (pp. 489-490) adds cutting planes at nodes ([[Cutting-plane methods]]); with deep cuts a lot of enumeration is avoided (Example 11.6, cut $-x_1+x_2\le1$).
- Related exact method, **dynamic programming** (BT §11.3, pp. 490-493): see [[Integer programming]].

**Covered in**: Bertsimas-Tsitsiklis ch. 11 §11.2 (pp. 485-490)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 11).
**Last updated**: 2026-11-06

---

## Related pages
- [[Integer programming]] · [[Cutting-plane methods]] · [[Lagrangian relaxation]] · [[Dual simplex method]] · [[Assignment problem]] · [[Linear programming]]
