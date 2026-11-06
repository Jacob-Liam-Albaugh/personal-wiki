---
type: theorem
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 4; Bazaraa, Jarvis, Sherali 2010, ch. 6"
tags: [optimization]
---

# LP duality

> [!theorem] Strong duality (source: MIT (ch 1-5).pdf, p. 148, Thm 4.4)
> If a linear program has an optimal solution, so does its dual, and the optimal costs are equal.

**Intuition**: every price vector $\mathbf p$ gives a lower bound on the primal cost; the dual searches for the best bound, and for LPs the best bound is tight (BT ch4, §4.1).

## Key facts
- Standard-form pair (BT p. 143; BJS write $\mathbf w$ for $\mathbf p$, p. 260):
$$\min\ \mathbf c'\mathbf x:\ \mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf0\quad\longleftrightarrow\quad\max\ \mathbf p'\mathbf b:\ \mathbf p'\mathbf A\le\mathbf c'$$
- One dual variable per primal constraint, one dual constraint per primal variable; the table of sign rules is Table 4.1 (BT p. 143). The dual of the dual is the primal (BT Thm 4.1; BJS p. 259).
- Weak duality: feasible $\mathbf x$, $\mathbf p$ give $\mathbf p'\mathbf b\le\mathbf c'\mathbf x$ (BT Thm 4.3, p. 146; BJS Lemma 6.2).
- Fundamental theorem: exactly one of (1) both have optimal solutions with equal cost, (2) one is unbounded and the other infeasible, (3) both infeasible (BJS Thm 6.1, p. 267; BT Table 4.2, p. 151).
- Complementary slackness: feasible $\mathbf x,\mathbf p$ are optimal iff
$$p_i(\mathbf a_i'\mathbf x-b_i)=0\quad\forall i$$
$$(c_j-\mathbf p'\mathbf A_j)x_j=0\quad\forall j$$
  (BT Thm 4.5, p. 151; BJS Thm 6.2, p. 268).
- Dual variables are shadow prices: if the basis stays optimal, the cost changes by $\mathbf p'\mathbf d$ when $\mathbf b$ moves by $\mathbf d$ (BT §4.4, p. 156). Degeneracy can spoil this as a rate (BJS ch6, §6.3).
- Proof routes: from the simplex method (BT p. 148) or from separating hyperplanes via [[Farkas lemma]] (BT §4.6-4.7).
- Complementary slackness plus feasibility are the [[KKT conditions]] of an LP.
- Algorithms built on the duality: [[Dual simplex method]], the primal-dual method (BJS ch6, §6.5), the out-of-kilter algorithm ([[BJS ch11 - The out-of-kilter algorithm]]), and primal-dual [[Interior point method]]s.
- Integer programs lack strong duality; Lagrangean duals give bounds only (see [[Integer programming]]).

## Where it appears
- [[BT ch4 - Duality theory]], [[BJS ch6 - Duality and sensitivity analysis]]: development.
- [[BT ch5 - Sensitivity analysis]]: dual feasibility conditions in sensitivity ranges.
- [[BT ch6 - Large scale optimization]]: column generation seen from the dual.
- [[BT ch9 - Interior point methods]]: central path as perturbed complementary slackness.
- [[BT ch11 - Integer programming]]: Lagrangean duality.
- [[BJS ch11 - The out-of-kilter algorithm]]: dual of the circulation problem.

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (ch. 4-6, 9, 11); `Linear Optimization/BJS full book.pdf` (ch. 6, 11).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Farkas lemma]] · [[Dual simplex method]] · [[KKT conditions]] · [[Simplex method]] · [[Convex function]]
