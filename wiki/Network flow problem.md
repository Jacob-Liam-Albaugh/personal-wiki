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

**Intuition**: ship a commodity over a directed graph at least cost. Node $i$ has supply $b_i>0$ (source), demand $b_i<0$ (sink) or $b_i=0$ (transshipment), with $\sum b_i=0$ (else a dummy demand node with zero-cost arcs is added, BJS p. 454). The constraints are flow conservation (nodal balance, Kirchhoff). Without upper bounds the problem is uncapacitated, with them capacitated. Applications: logistics, communication networks, supply chains, oil pipelines, tanker scheduling (BJS p. 454).

BT write the same problem on $G=(\mathcal N,\mathcal A)$ with flows $f_{ij}$, capacities $u_{ij}$ and unit costs $c_{ij}$ (BT §7.2, p. 272):
$$b_i+\sum_{j\in I(i)}f_{ji}=\sum_{j\in O(i)}f_{ij}\ \ \forall i,\qquad0\le f_{ij}\le u_{ij}$$
Summing the first over all nodes forces $\sum_ib_i=0$. In matrix form $\mathbf A\mathbf f=\mathbf b$ with $\mathbf A$ the node-arc incidence matrix; with $u_{ij}=\infty$ it is in standard form (p. 273).

## Key facts
- The constraint matrix is the node-arc incidence matrix with column $\mathbf e_p-\mathbf e_q$ per arc; its rank is $m-1$ for a connected graph, so one row is redundant since the rows sum to zero (BT pp. 277-278; BJS §9.3, pp. 459-465).
- A basis is a rooted spanning tree (BJS Thm 9.1, p. 463), so primal values and duals ($w_i-w_j=c_{ij}$ on basic arcs) come from tree traversals, and optimal flows are integer; see [[Network simplex method]].
- Special cases (BT pp. 273-276): [[Transportation problem]] and [[Assignment problem]], [[Shortest path problem]], [[Maximum flow problem]], [[Multicommodity flow]] (block structure, so [[Dantzig-Wolfe decomposition]] applies). BJS: any finite-valued min cost flow problem, capacitated or not, becomes an uncapacitated transportation problem (Exercise 9.27, p. 513).
- Circulation form with bounds $\ell_{ij}\le x_{ij}\le u_{ij}$ and the [[Out-of-kilter algorithm]], whose optimality test is complementary slackness ([[LP duality]]).
- Generalized networks with gains and losses are BJS §9.12 (pp. 494-512, headings only).

## Circulations and the negative cost cycle algorithm (BT §7.2, §7.4)
Any $\mathbf f$ with $\mathbf A\mathbf f=\mathbf0$ is a **circulation** (p. 278). A cycle $C$ with forward arcs $F$ and backward arcs $B$ gives a simple circulation $\mathbf h^C$ ($+1$ on $F$, $-1$ on $B$, $0$ elsewhere), $\mathbf A\mathbf h^C=\mathbf0$ (eq. 7.3), with cost
$$\mathbf c'\mathbf h^C=\sum_{(i,j)\in F}c_{ij}-\sum_{(i,j)\in B}c_{ij}$$
Pushing $\theta$ units around $C$ changes the cost by $\theta$ times this.

> [!algorithm] Negative cost cycle algorithm (BT pp. 291-300; Klein 1967)
> Start from a feasible flow. If the residual network has a negative cost cycle, push the largest feasible $\delta(C)$ units around it. Stop when none exists.

> [!theorem] Theorem 7.6 (BT p. 298)
> A feasible flow is optimal iff its residual network has no negative cost cycle.

Lemma 7.1 (flow decomposition, p. 298): a nonzero circulation $\mathbf f\ge\mathbf0$ decomposes into positive-flow cycles. Theorem 7.7 (p. 300): with integer capacities and an integer start the algorithm keeps flows integer and stops after finitely many iterations if the optimal cost is finite; with non-integer capacities termination is not guaranteed without special cycle rules (p. 301).

## Duality (BT §7.6, pp. 312-315)
With a dual variable $p_i$ per node, the uncapacitated dual is feasible when $p_i-p_j\le c_{ij}$ on every arc. A dual price is a sensitivity: with the same basis, raising $b_i$ by $\varepsilon$ and lowering $b_n$ by $\varepsilon$ costs $\varepsilon p_i$; shipping one more unit from $i$ to $j$ costs $p_i-p_j$ absent degeneracy (p. 314). See [[LP duality]] and [[Sensitivity analysis]].

> [!theorem] Complementary slackness (BT Thm 7.11, pp. 314-315)
> If $f_{ij}>0$ then $p_i-p_j=c_{ij}$. For capacitated problems the pair $(p_i-p_j,f_{ij})$ lies on a piecewise relation (BT Fig. 7.26).

Circuit analogy (p. 315): flow is current, $b_i$ injected current (Kirchhoff's current law), $p_i$ potential; an optimal $(\mathbf f,\mathbf p)$ is an equilibrium of a circuit whose elements follow that relation.

## Integrality and unimodularity
If supplies and capacities are integer, an integer optimal flow exists (BT Thm 7.5, Cor. 7.2, pp. 289-290). The reason is that incidence matrices are totally unimodular (every square submatrix has determinant $0,\pm1$); BJS §9.3 is titled "Triangularity, Integrality, and Total Unimodularity" but only the triangularity part was read (p. 463). This lets shortest path and assignment problems be solved as LPs.

## Methods and algorithms
- [[Network simplex method]]: tree bases, cycle pivots.
- Negative cost cycle cancelling (above), augmenting paths ([[Maximum flow problem]]), label correcting ([[Shortest path problem]]), Hungarian algorithm and auction ([[Assignment problem]]), [[Out-of-kilter algorithm]] and relaxation methods.
- BJS call network simplex and out-of-kilter "by far the most effective in practice" (BJS p. 453).
- Dual ascent (BT §7.7, p. 316-324): keep flows nonnegative but allow conservation to be violated, changing node prices to raise the dual cost.

**Covered in**: Bertsimas-Tsitsiklis ch. 7 §7.2, 7.4, 7.6 (pp. 272-278, 291-301, 312-315); Bazaraa-Jarvis-Sherali ch. 9 §9.1-9.3 (pp. 453-465)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 7); `text_books/Linear Optimization/BJS full book.pdf` (ch. 9; pdf 470, 485 viewed as images).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Simplex method]] · [[Basic feasible solution]] · [[LP duality]] · [[Integer programming]]
- [[Network simplex method]] · [[Transportation problem]] · [[Assignment problem]] · [[Maximum flow problem]] · [[Shortest path problem]] · [[Out-of-kilter algorithm]] · [[Multicommodity flow]]
