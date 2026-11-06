---
type: concept
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 7; Bazaraa, Jarvis, Sherali 2010, ch. 9-12"
tags: [optimization]
---

# Network flow problem

> [!definition] Minimal cost network flow (source: BJS full book.pdf, p. 454, eq. 9.1)
> $$\min\ \sum_{i,j}c_{ij}x_{ij}$$
> $$\sum_{j}x_{ij}-\sum_{k}x_{ki}=b_i,\quad i=1,\dots,m$$
> $$x_{ij}\ge0\ \ (\text{and }x_{ij}\le u_{ij}\text{ if capacitated})$$

**Intuition**: ship a commodity over a directed graph at least cost. Node $i$ has supply $b_i>0$ (source), demand $b_i<0$ (sink) or $b_i=0$ (transshipment), with $\sum b_i=0$. BT write the same problem with flows $f_{ij}$, capacities $u_{ij}$ and the constraint $\mathbf A\mathbf f=\mathbf b$ (BT ch7, eqs. 7.1-7.2).

## Key facts
- The constraint matrix is the node-arc incidence matrix; its rank is $m-1$ for a connected graph, so one row is redundant (BT p. 277-278; BJS ch9, §9.3).
- A basis is a rooted spanning tree (BJS Thm 9.1, p. 463). Basis matrices are triangular with entries $0,\pm1$, so primal values and duals ($w_i-w_j=c_{ij}$ on basic arcs) come from tree traversals (BJS ch9, §9.5). BT specialize the [[Simplex method]] to spanning trees in the same way (BT ch7).
- A nonbasic arc closes a unique cycle with the tree; the column representation is a unit flow along the basis equivalent chain (BJS p. 466).
- Special cases: transportation, assignment ([[BJS ch10 - Transportation and assignment problems]]), shortest path, maximum flow, multicommodity flow ([[BJS ch12 - Maximal flow shortest path multicommodity flow and network synthesis]]), negative-cost cycle cancelling (BT ch7).
- Circulation form with bounds $\ell_{ij}\le x_{ij}\le u_{ij}$ and the out-of-kilter algorithm, whose optimality test is complementary slackness ([[BJS ch11 - The out-of-kilter algorithm]]; see [[LP duality]]).
- Generalized networks with gains and losses are covered in BJS §9.12.

## Where it appears
- [[BT ch7 - Network flows]]: formulation, circulations, network simplex, combinatorial algorithms.
- [[BJS ch9 - Minimal cost network flows]]: network simplex.
- [[BJS ch10 - Transportation and assignment problems]]: bipartite special cases.
- [[BJS ch11 - The out-of-kilter algorithm]]: primal-dual circulation method.
- [[BJS ch12 - Maximal flow shortest path multicommodity flow and network synthesis]]: path and cut problems.

**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 7); `text_books/Linear Optimization/BJS full book.pdf` (ch. 9-12).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Simplex method]] · [[Basic feasible solution]] · [[LP duality]] · [[Integer programming]]
