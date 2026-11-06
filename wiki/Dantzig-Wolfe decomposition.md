---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, §6.4; Bazaraa, Jarvis, Sherali 2010, ch. 7"
tags: [optimization]
---

# Dantzig-Wolfe decomposition

> [!definition] Master problem (source: BJS full book.pdf, p. 340, eqs. 7.1-7.3)
> For $\min\mathbf c\mathbf x$ s.t. $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\in X$ ($X$ a nonempty bounded [[Polyhedron]] with extreme points $\mathbf x_1,\dots,\mathbf x_t$, $\mathbf A$ is $m\times n$), write $\mathbf x=\sum_j\lambda_j\mathbf x_j$ with $\sum_j\lambda_j=1$, $\lambda_j\ge0$ (representation theorem) and solve
> $$\min\ \sum_{j=1}^t(\mathbf c\mathbf x_j)\lambda_j$$
> $$\sum_{j=1}^t(\mathbf A\mathbf x_j)\lambda_j=\mathbf b,\quad\sum_{j=1}^t\lambda_j=1,\quad\lambda_j\ge0$$

**Intuition**: split off the complicating constraints $\mathbf A\mathbf x=\mathbf b$, keep the easy structured set $X$ inside a subproblem, and let the revised [[Simplex method]] pick extreme points of $X$ as columns on demand. Corporate and logistics models can have thousands of rows and a seemingly unlimited number of columns; the constraints are partitioned into general (complicating) constraints and constraints with special structure, where structure helps efficiency but is not required (BJS p. 339). Dantzig-Wolfe is credited to Dantzig and Wolfe (BT notes, p. 263).

## Algorithm (BJS §7.1, pp. 340-347)
Apply revised simplex to the master with basis inverse $\mathbf B^{-1}$ of size $(m+1)\times(m+1)$. The dual variables for the two constraint families are $(\mathbf w,\alpha)=\hat{\mathbf c}_B\mathbf B^{-1}$ with $\hat c_j=\mathbf c\mathbf x_j$. The master array holds $\mathbf B^{-1}$, $(\mathbf w,\alpha)$, the right-hand side $\hat{\mathbf c}_B\hat{\mathbf b}$ and $\hat{\mathbf b}=\mathbf B^{-1}\binom{\mathbf b}{1}$ (p. 341).

**Pricing** (eq. 7.4, p. 341): $\max_{1\le j\le t}\ \mathbf w\mathbf A\mathbf x_j+\alpha-\mathbf c\mathbf x_j$. It cannot be evaluated by enumeration, but since a linear function over a bounded $X$ is maximized at an extreme point it equals the **subproblem**
$$\max\ (\mathbf w\mathbf A-\mathbf c)\mathbf x+\alpha\quad\text{s.t. }\mathbf x\in X$$
Zero optimal value means the master is optimal. Otherwise the column
$$\mathbf y_k=\mathbf B^{-1}\binom{\mathbf A\mathbf x_k}{1}$$
joins the master array with entry $z_k-\hat c_k$ and a pivot is made at the minimum ratio $\hat b_r/y_{rk}=\min\{\hat b_i/y_{ik}:y_{ik}>0\}$ (p. 343).

**Remarks** (p. 343):
1. It is revised simplex with $z_k-\hat c_k$ computed by a subproblem, so with an anti-cycling rule in both master and subproblem it converges finitely.
2. Each subproblem returns an extreme point giving a new column: a [[Column generation]] method.
3. The last subproblem basis can be reused by changing its cost row.
4. The subproblem need not be solved to optimality; any $\mathbf x_k$ with $z_k-\hat c_k>0$ is a candidate.
5. For inequality master constraints, slacks must also be checked, with $z_{s_i}-c_{s_i}=w_i$.

**Example and start** (BJS §7.2-7.3, pp. 345-353): the process is run to termination; the known lower bound $-56/3$ matched the revised upper bound, and the final point is a convex combination of the generated extreme points. An initial basis comes from an artificial-variable phase as in the [[Simplex method]] (§7.3, headings only).

## Several blocks and the BT formulation (BT §6.4, pp. 239-252)
Minimize $\mathbf c_1'\mathbf x_1+\mathbf c_2'\mathbf x_2$ s.t. the coupling constraint $\mathbf D_1\mathbf x_1+\mathbf D_2\mathbf x_2=\mathbf b_0$ and block constraints $\mathbf F_i\mathbf x_i=\mathbf b_i$, $\mathbf x_i\ge\mathbf0$ (eq. 6.10), with $m_0$ coupling rows and $m_i$ rows per block. Let $P_i=\{\mathbf x_i\ge\mathbf0\mid\mathbf F_i\mathbf x_i=\mathbf b_i\}$ with extreme points $\mathbf x_i^j$ and a complete set of extreme rays $\mathbf w_i^k$. By the resolution theorem ([[Polyhedron]], BT Thm 4.15)
$$\mathbf x_i=\sum_j\lambda_i^j\mathbf x_i^j+\sum_k\theta_i^k\mathbf w_i^k,\quad\lambda,\theta\ge0,\ \sum_j\lambda_i^j=1$$
Substituting gives a master (eqs. 6.11-6.13) with only $m_0+2$ equality constraints but possibly astronomically many variables. The column of $\lambda_1^j$ is $(\mathbf D_1\mathbf x_1^j,1,0)$ and that of $\theta_1^k$ is $(\mathbf D_1\mathbf w_1^k,0,0)$ (p. 241).

With dual vector $\mathbf p=(\mathbf q,r_1,r_2)$, $\mathbf q$ for coupling rows and $r_i$ for convexity rows, reduced costs are
$$(\mathbf c_1'-\mathbf q'\mathbf D_1)\mathbf x_1^j-r_1\ \ (\lambda_1^j),\qquad(\mathbf c_1'-\mathbf q'\mathbf D_1)\mathbf w_1^k\ \ (\theta_1^k)$$
Rather than test each, solve the subproblem $\min(\mathbf c_1'-\mathbf q'\mathbf D_1)\mathbf x_1$ over $P_1$ (p. 242). Three outcomes: (a) cost $-\infty$: the simplex ends with an extreme ray $\mathbf w_1^k$ and $\theta_1^k$ enters; (b) finite and below $r_1$: an extreme point $\mathbf x_1^j$ and $\lambda_1^j$ enters; (c) finite and at least $r_1$: all reduced costs of block 1 are nonnegative. Block 2 is treated the same way; if both fall under (c) the master is optimal, else bring in a column and update $\mathbf B^{-1}$ and $\mathbf p$ (p. 243).

## Unbounded X and block diagonal structure (BJS §7.4-7.5, pp. 354-371)
- **Unbounded $X$**: extreme directions $\mathbf d_j$ enter the master with nonnegative weights, using the full representation theorem (Example 7.1, p. 357); same as BT's extreme-ray columns. Headings only.
- **Block diagonal**: with a block diagonal part and linking rows, $X$ splits into independent subproblems, one per block, solved separately each iteration (Example 7.2, p. 365). Headings only. [[Multicommodity flow]] is the standard instance: shared arc capacities are the coupling rows and the subproblems are single-commodity network flows.

## Practice and bounds (BT pp. 252-254)
- Convergence can be slow near the end, so the method is sometimes stopped early with a suboptimal solution. It is usually no faster than revised simplex on the original problem; the benefit is storage. For $t$ blocks with $m_1$ rows each, $O((m_0+tm_1)^2)$ becomes $O((m_0+t)^2)$ for the master plus $t$ tableaux of size $O(m_1^2)$ (p. 252).
- Theorem 6.1 (p. 252) gives a lower bound on $z^*$ from the current master solution and the subproblem optima, usable for early termination; in Example 6.3 (p. 254) the bounds bracket $-21>z^*>-22$ and the true value is $-21.5$. The theorem statement itself was not read from a page image **[unverified]**.

## Duality and relatives
- Delayed column generation is the [[Cutting-plane methods]] scheme on the dual (BT §6.1-6.3; see [[Column generation]]).
- [[Benders decomposition]] is the dual counterpart for two-stage stochastic programs (BT §6.5); BJS note Dantzig-Wolfe, Benders and [[Lagrangian relaxation]] are "all equivalent for linear programming problems" (BJS p. 339, 371).
- The Lagrangean master and the Dantzig-Wolfe master are views of the same convexified problem ([[Lagrangian relaxation]], BT Thm 11.4).

**Covered in**: Bertsimas-Tsitsiklis ch. 6 §6.4 (pp. 239-254); Bazaraa-Jarvis-Sherali ch. 7 (pp. 339-376)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 6; pdf 247-280); `text_books/Linear Optimization/BJS full book.pdf` (ch. 7; pdf 356, 357, 359 viewed as images, rest from text layer and headings).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Simplex method]] · [[LP duality]] · [[Polyhedron]] · [[Integer programming]]
- [[Column generation]] · [[Benders decomposition]] · [[Lagrangian relaxation]] · [[Cutting-plane methods]] · [[Multicommodity flow]]
