---
type: method
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, §10.7-10.9; Bertsimas, Tsitsiklis 1997, §7.7-7.8"
tags: [optimization]
---

# Assignment problem

> [!definition] Assignment problem (source: BJS full book.pdf, pp. 535-537)
> Match $m$ individuals to $m$ jobs at cost $c_{ij}$, the [[Transportation problem]] with $m=n$ and $s_i=d_j=1$:
> $$\min\ \sum_{i=1}^m\sum_{j=1}^mc_{ij}x_{ij}$$
> $$\sum_{j=1}^mx_{ij}=1,\qquad-\sum_{i=1}^mx_{ij}=-1,\qquad x_{ij}\in\{0,1\}$$

**Intuition**: minimum weighted matching on a bipartite graph. It has the transportation constraint matrix, so by total unimodularity the 0-1 restriction can be relaxed to $x_{ij}\ge0$ without losing an integer optimum (the BJS text breaks off at "Applying the total unimodularity property of", p. 536, so the integrality statement is from the matrix structure shown on the [[Transportation problem]] page). BT list it among the special cases of the [[Network flow problem]] (BT p. 273-276).

## Key facts
- Each basic feasible solution has $2m-1$ basic variables of which only $m$ are positive, so $m-1$ are degenerate at zero (BJS p. 536). About 90 percent of pivots are degenerate for $m>500$ (p. 544).
- The polytope has $m!$ extreme points, one per matching (p. 537).
- A transportation problem becomes an assignment problem by making $s_i$ unit-supply copies of origin $i$ and $d_j$ unit-demand copies of destination $j$ (p. 537).
- The relaxation with only degree constraints is not the matching polytope for general (non-bipartite) graphs; Edmonds' odd-set constraints repair that ([[Integer programming]], BT §10.3). Assignment problem relaxations also give lower bounds for the traveling salesman problem in branch and bound ([[Branch and bound]], BT Example 11.5).

## Hungarian algorithm (BJS pp. 538-544)
Primal-dual: keep dual feasibility, build primal feasibility. Subtract each row minimum, then each column minimum, giving a **reduced matrix** with nonnegative entries
$$\hat c_{ij}=c_{ij}-u_i+v_j$$
and a zero in every row and column (p. 541). Zero cells are **independent** if no two share a row or column.

> [!theorem] Theorem 10.1 (BJS p. 540)
> The maximum number of independent zero cells in a reduced assignment matrix equals the minimum number of lines needed to cover all its zeros.

Not proved there; BJS Exercise 12.17 asks to show it is a special case of the max flow min cut theorem ([[Maximum flow problem]]).

**Dual update** (p. 541). If fewer than $m$ independent zeros exist, cover the zeros with the minimum number $k<m$ of lines. Let $S_r$ be the uncovered rows, $S_c$ the uncovered columns and
$$c_0=\min_{i\in S_r,\ j\in S_c}\hat c_{ij}>0$$
Then
$$\bar u_i=\hat u_i+c_0\ (i\in S_r),\qquad\bar u_i=\hat u_i\ (i\notin S_r)$$
$$\bar v_j=\hat v_j\ (j\in S_c),\qquad\bar v_j=\hat v_j+c_0\ (j\notin S_c)$$
which means subtracting $c_0$ from each uncovered element and adding it to each twice-covered element. In BJS's $3\times3$ example $c_0=\min\{2,5,3,3\}=2$ yields reduced rows $(0,0,3)$, $(5,0,0)$, $(0,1,1)$ and the optimum $x_{12}^*=x_{23}^*=x_{31}^*=1$.

**Algorithm summary** (pp. 541-542). Initialization: row then column reduction. Main step: cover all zeros with the fewest lines; if that number is $m$ an optimal assignment exists among independent zeros; otherwise apply the dual update and repeat. Primal feasibility is attained, dual feasibility maintained and complementary slackness holds, so the [[KKT conditions]] hold and the solution is optimal. It terminates finitely: covering with $k<m$ lines raises the dual objective by $c_0(m-k)\ge1$ per iteration (p. 544).

## Other methods
- **Alternating path basis algorithm** (BJS §10.8, pp. 544-545, Fig. 10.21): a network simplex variant that exploits the order-$(m-1)$ degeneracy; not read in detail.
- **Successive shortest paths** (BJS §10.9, pp. 546-550): a polynomial-time algorithm that solves a sequence of [[Shortest path problem]] instances, said to run up to seven times faster than the alternating path basis algorithm with an efficient shortest path routine. After each augmentation the partial assignment stays complementary slack with the dual vector $\mathbf w$, so at most $m$ iterations reach optimality (p. 551).
- **Dual ascent and the auction algorithm** (BT §7.7-7.8, pp. 316-329): dual ascent keeps flows nonnegative but allows conservation to be violated while changing node prices to raise the dual cost (p. 324). The auction algorithm changes one node price at a time; a single move can lower the dual cost, but if the loss is kept small it makes progress and can be viewed as approximate dual ascent (p. 325). Detailed convergence results were not read **[unverified]**.

**Covered in**: Bazaraa-Jarvis-Sherali ch. 10 §10.7-10.9 (pp. 535-551); Bertsimas-Tsitsiklis ch. 7 §7.7-7.8 (pp. 316-329)
**Sources**: `text_books/Linear Optimization/BJS full book.pdf` (ch. 10); `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 7).
**Last updated**: 2026-11-06

---

## Related pages
- [[Transportation problem]] · [[Network flow problem]] · [[Network simplex method]] · [[Maximum flow problem]] · [[Shortest path problem]]
- [[KKT conditions]] · [[LP duality]] · [[Integer programming]]
