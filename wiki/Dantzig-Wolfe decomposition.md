---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, §6.4; Bazaraa, Jarvis, Sherali 2010, ch. 7"
tags: [optimization]
---

# Dantzig-Wolfe decomposition

> [!definition] Master problem (source: BJS full book.pdf, p. 340, eqs. 7.1-7.3)
> For $\min\mathbf c\mathbf x$ s.t. $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\in X$ ($X$ a bounded [[Polyhedron]] with extreme points $\mathbf x_1,\dots,\mathbf x_t$), write $\mathbf x=\sum_j\lambda_j\mathbf x_j$ and solve
> $$\min\ \sum_{j=1}^t(\mathbf c\mathbf x_j)\lambda_j$$
> $$\sum_{j=1}^t(\mathbf A\mathbf x_j)\lambda_j=\mathbf b,\quad\sum_{j=1}^t\lambda_j=1,\quad\lambda_j\ge0$$

**Intuition**: split off the complicating constraints $\mathbf A\mathbf x=\mathbf b$, keep the easy structured set $X$ inside a subproblem, and let the revised [[Simplex method]] pick extreme points of $X$ as columns on demand.

## Key facts
- Too many extreme points to list, so price a column by solving the subproblem (BJS eq. 7.4, p. 341)
$$\max\ (\mathbf w\mathbf A-\mathbf c)\mathbf x+\alpha\quad\text{s.t. }\mathbf x\in X.$$
  Zero optimal value means the master is optimal; otherwise the extreme point found gives the entering column. This is column generation, and it is revised simplex with the reduced cost computed by a subproblem (BJS p. 343).
- BT's version has several blocks with coupling constraint $\mathbf D_1\mathbf x_1+\mathbf D_2\mathbf x_2=\mathbf b_0$ and block constraints $\mathbf F_i\mathbf x_i=\mathbf b_i$; the extreme points and rays of each block come from the resolution theorem (BT eq. 6.10, p. 239-240).
- Unbounded $X$ adds extreme-ray columns (BJS §7.4, BT p. 240).
- Dual view: delayed column generation is the cutting plane method on the dual (BT §6.1-6.3).
- Benders decomposition is the dual counterpart for two-stage stochastic programs (BT §6.5); BJS note that Dantzig-Wolfe, Benders and Lagrangian relaxation are "all equivalent for linear programming problems" (BJS p. 339).

## Where it appears
- [[BT ch6 - Large scale optimization]]: §6.1-6.4 with the cutting stock example.
- [[BJS ch7 - The decomposition principle]]: algorithm, interpretation and extensions (sections beyond §7.1 read only as headings).

**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 6); `text_books/Linear Optimization/BJS full book.pdf` (ch. 7).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Simplex method]] · [[LP duality]] · [[Polyhedron]] · [[Integer programming]]
