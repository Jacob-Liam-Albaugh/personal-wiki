---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 3; Bazaraa, Jarvis, Sherali 2010, ch. 3-5"
tags: [optimization]
---

# Simplex method

> [!algorithm] An iteration of the simplex method (source: MIT (ch 1-5).pdf, pp. 90-91)
> 1. Start with basis columns $\mathbf A_{B(1)},\dots,\mathbf A_{B(m)}$ and a [[Basic feasible solution]] $\mathbf x$.
> 2. Compute reduced costs $r_j=c_j-\mathbf c_B'\mathbf B^{-1}\mathbf A_j$. If all are $\ge0$, stop: optimal. Else pick $j$ with $r_j<0$.
> 3. Compute $\mathbf u=\mathbf B^{-1}\mathbf A_j$. If no component is positive, the cost is $-\infty$.
> 4. Otherwise
> $$\theta^*=\min_{\{i\mid u_i>0\}}\frac{x_{B(i)}}{u_i}.$$
> 5. Let $\ell$ attain the minimum. Replace $\mathbf A_{B(\ell)}$ by $\mathbf A_j$.

**Intuition**: walk along edges of the [[Polyhedron]] from corner to adjacent corner, each time to a cheaper one, until no edge improves the cost. BJS write the reduced cost as $z_j-c_j$ with the opposite sign convention (enter when $z_j-c_j>0$ in a minimization, and the reduced cost is $c_j-z_j$), and BT write $r_j$ (the book uses a bar over $c_j$; this wiki writes $r_j$ and the vector $\mathbf r$). BJS write the current right-hand side $\hat b_i$ and the column $\mathbf y_j=\mathbf B^{-1}\mathbf a_j$.

The problem is a standard-form LP $\min\mathbf c'\mathbf x$, $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\ge0$ with $\mathbf A$ of full row rank; the method moves from one BFS to an adjacent better one until none exists. BJS first argue geometrically that an optimal extreme point suffices (§3.1, pp. 91-94) and that enumerating all $\binom nm$ basic solutions is not an option ([[Basic feasible solution]]).

## Feasible directions and reduced costs

A direction $\mathbf d$ is feasible at $\mathbf x\in P$ if $\mathbf x+\theta\mathbf d\in P$ for some $\theta>0$ (BT Def. 3.1, §3.1, pp. 83-84). At a BFS with basis matrix $\mathbf B=[\mathbf A_{B(1)}\cdots\mathbf A_{B(m)}]$, $\mathbf x_B=\mathbf B^{-1}\mathbf b$. Raise one nonbasic $x_j$ to $\theta$ and keep the others nonbasic at zero: $d_j=1$, and $\mathbf A\mathbf d=0$ forces
$$\mathbf d_B=-\mathbf B^{-1}\mathbf A_j .\qquad(3.1)$$
This is the $j$th basic direction. If $\mathbf x$ is nondegenerate it is feasible; if degenerate it may immediately violate $x_{B(i)}\ge0$ (p. 84). The cost changes at rate $\mathbf c'\mathbf d=c_j-\mathbf c_B'\mathbf B^{-1}\mathbf A_j$.

> [!definition] Reduced cost (p. 84, Def. 3.2)
> $$r_j=c_j-\mathbf c_B'\mathbf B^{-1}\mathbf A_j$$
> The reduced cost of every basic variable is zero (p. 86).

BJS reach the same quantity by rewriting the problem in the nonbasic variables (§3.3, pp. 103-105). Given a BFS with objective $z_0$, let $J$ be the nonbasic index set: the objective value is $z_0=\mathbf c_B\mathbf B^{-1}\mathbf b$, the basic variables satisfy $\mathbf x_B=\mathbf B^{-1}\mathbf b-\sum_{j\in J}\mathbf y_jx_j$, and (displays garbled in the text layer, so only the structure is recorded)
$$z=z_0-\sum_{j\in J}(z_j-c_j)x_j,\qquad z_j=\mathbf c_B\mathbf B^{-1}\mathbf a_j\ \ \text{[text layer]}$$
The problem can be rewritten in the $p=n-m$ nonbasic variables alone, with $\mathbf x_B$ acting as slack variables. The coefficients $c_j-z_j$ are the **reduced cost coefficients**, since they live in this reduced space (p. 104).

> [!theorem] Optimality conditions (p. 86, Thm 3.1)
> For a BFS $\mathbf x$ with basis $\mathbf B$ and reduced costs $\mathbf r$: (a) if $\mathbf r\ge0$ then $\mathbf x$ is optimal; (b) if $\mathbf x$ is optimal and nondegenerate then $\mathbf r\ge0$.

Proof of (a): for any feasible $\mathbf y$, with $\mathbf d=\mathbf y-\mathbf x$ one has $\mathbf c'\mathbf d=\sum_{i\in N}r_id_i\ge0$ because $d_i\ge0$ on nonbasic indices (p. 86). In the degenerate case an optimal BFS can have negative reduced costs (BJS Thm 4.1 shows a basis with the right signs still exists, [[Simplex initialization and anticycling]]).

> [!definition] Optimal basis (p. 87, Def. 3.3)
> $\mathbf B$ is optimal if (a) $\mathbf B^{-1}\mathbf b\ge0$ and (b) $\mathbf r'=\mathbf c'-\mathbf c_B'\mathbf B^{-1}\mathbf A\ge\mathbf 0'$.

## The iteration

Let $\mathbf u=-\mathbf d_B=\mathbf B^{-1}\mathbf A_j$ (BT §3.2, pp. 87-91). The box above is BT's iteration; the new BFS has $y_j=\theta^*$ and $y_{B(i)}=x_{B(i)}-\theta^*u_i$ for $i\ne\ell$.

> [!theorem] Basis change is valid (p. 89, Thm 3.2)
> (a) $\mathbf A_{B(i)}$, $i\ne\ell$, and $\mathbf A_j$ are linearly independent, so $\overline{\mathbf B}$ is a basis matrix. (b) $\mathbf y=\mathbf x+\theta^*\mathbf d$ is a BFS for the basis $\overline{\mathbf B}$.

> [!theorem] Termination, nondegenerate case (p. 91, Thm 3.3)
> If the feasible set is nonempty and every BFS is nondegenerate, the method stops after finitely many iterations, with either (a) an optimal basis and BFS, or (b) $\mathbf d$ with $\mathbf A\mathbf d=0$, $\mathbf d\ge0$, $\mathbf c'\mathbf d<0$ (cost $-\infty$).

Finiteness: each step lowers the cost strictly and there are finitely many BFS.

BJS phrase the same rules in their notation (§3.4-3.6, pp. 105-121). Moving from an extreme point to an adjacent one raises one nonbasic variable $x_k$ from zero while the basic variables adjust along an edge (Figures 3.6-3.8). In Figure 3.8 raising $x_4$ by one unit lowers $x_1$ and $x_2$ by $1/3$ each, the move continuing until the nonnegativity of $x_1$ blocks (p. 114, image seen).

> [!definition] Entering and leaving rules (p. 114, image seen)
> Entering: $x_k$ may enter if $z_k-c_k>0$. Leaving: $x_{B_r}$ may leave, where
> $$\frac{\hat b_r}{y_{rk}}=\min_{1\le i\le m}\Big\{\frac{\hat b_i}{y_{ik}}:\ y_{ik}>0\Big\}$$

If every nonbasic $x_j$ has $z_j-c_j\le0$, the point is optimal. For any feasible $\mathbf x$ with value $z$ and the current value $z^*=\mathbf c_B\mathbf B^{-1}\mathbf b$ (p. 114, eq. 3.13, image seen):
$$z^*-z=\sum_{j\in J}(z_j-c_j)x_j\le0$$
so $z\ge z^*$ and $\mathbf x^*$ is optimal. If $z_k-c_k>0$ and $\mathbf y_k\le\mathbf0$, no ratio exists, $x_k$ can grow without bound, and the optimal value is unbounded (the direction is an extreme direction of the region, pp. 114-121, read from text). Zero entries $z_j-c_j=0$ at an optimum signal alternative optima (not detailed).

**The algorithm in BJS terms** (§3.7, pp. 121-125; read from text and the page seen at p. 122): at each iteration solve $\mathbf B\mathbf x_B=\mathbf b$, $\mathbf w\mathbf B=\mathbf c_B$ and $\mathbf B\mathbf y_k=\mathbf a_k$ (p. 125). Compute $z_j-c_j=\mathbf w\mathbf a_j-c_j$ for nonbasic $j$, take $k$ with $z_k-c_k>0$ (the book's usual rule is the largest, **[unverified]**), stop if $\mathbf y_k\le\mathbf0$, else apply the minimum ratio test and update the basis. For a **maximization** problem, either multiply the costs by $-1$ or pick the minimum $z_j-c_j$ and stop when $z_k-c_k\ge0$ (p. 122, image seen).

**Finite convergence without degeneracy** (BJS p. 122, image seen). At each iteration one of three things happens: stop with an optimum ($z_k-c_k\le0$), stop with unboundedness ($z_k-c_k>0$, $\mathbf y_k\le\mathbf0$), or move to a new basic feasible solution. If $\hat b_r>0$, then $x_k=\hat b_r/y_{rk}>0$ and the objective changes by $x_k(z_k-c_k)>0$, so it strictly decreases and no basis repeats.

> [!theorem] Theorem 3.5, Finite Convergence (p. 122)
> In the absence of degeneracy (and assuming feasibility), the simplex method stops in a finite number of iterations, either with an optimal basic feasible solution or with the conclusion that the optimal value is unbounded.

**Example 3.8** (BJS pp. 122-125, image seen for the statement): minimize $-x_1-3x_2$ subject to $2x_1+3x_2\le6$, $-x_1+x_2\le1$, $x_1,x_2\ge0$, with slacks $x_3,x_4$. Read from text (p. 125, final iteration): the basis $\{x_1,x_2\}$ is reached, with $\mathbf w=(-4/5,-3/5)$ and $z_4-c_4=-3/5\le0$, giving
$$(x_1,x_2,x_3,x_4)=(3/5,\,8/5,\,0,\,0),\quad z=-27/5$$
Figure 3.11 shows the simplex path. The values come from the text layer and were not checked against an image.

## Pivoting rules and degenerate pivots

Entering variable: most negative $r_j$ (steepest rate), or largest decrease $\theta^*|r_j|$ (costlier per iteration, no clear win in practice). Simpler rules are often used for large problems (BT pp. 92-93). With $\theta^*=0$ the basis changes but the point does not. Cycling and the rules that prevent it, and how to find a starting BFS, are in [[Simplex initialization and anticycling]]. With degeneracy BJS's Theorem 3.5 no longer applies.

## Tableau and implementations

The tableau holds the representation of $z$ and $\mathbf x_B$ in terms of the nonbasic variables (BT §3.3, pp. 94-107). Full tableau: top row $[-\mathbf c_B'\mathbf B^{-1}\mathbf b\mid\mathbf r']$, body $[\mathbf B^{-1}\mathbf b\mid\mathbf B^{-1}\mathbf A]$ (BT p. 99); the pivot is a Gauss-Jordan step on the entry $u_\ell>0$ chosen by the ratio $x_{B(i)}/u_i$. BJS's tableau form (§3.8, pp. 125-135) solves $\mathbf B\mathbf x_B=\mathbf b$, $\mathbf w\mathbf B=\mathbf c_B$, $\mathbf B\mathbf y_k=\mathbf a_k$ by pivoting (p. 125); other ways of solving and updating these systems give other algorithms inside the same framework, namely the [[Revised simplex method]] (storage, partial pricing, bounded variables). The layout details of the tableau, the pivot operation and the exercises were not read in BJS (headings only), nor was block pivoting (§3.9, p. 135).

## Column geometry and efficiency

BT §3.6 (pp. 119-124) gives an alternative picture of the method, offered to explain why it works well in practice (p. 119). **[unverified]**: details not read. Worst-case behaviour (Hirsch conjecture, exponential examples, average case) is in [[Complexity of linear programming]]; worst case is exponential for known rules while practice is much better (BT p. 129), and whether a polynomial pivoting rule exists is open.

## Key facts
- Optimality: $\mathbf r\ge\mathbf 0$ at a BFS implies optimal; the converse holds if the BFS is nondegenerate (BT Thm 3.1, p. 86).
- Without degeneracy the method stops finitely at an optimal basis or a ray of unbounded cost (BT Thm 3.3, p. 91; BJS Thm 3.5).
- With degeneracy it can cycle (BT Example 3.6, p. 104; BJS Beale's example). Fixes: lexicographic rule (BT Thm 3.4) and Bland's smallest-index rule (BT p. 111; BJS p. 180); see [[Simplex initialization and anticycling]].
- Implementations: full tableau, revised simplex keeping $\mathbf B^{-1}$, bounded-variable simplex ([[Revised simplex method]]).
- Initialization: Phase I with artificial variables, big-M, single artificial variable.
- Worst case is exponential: BT cite $2^n-1$ iterations on a particular problem (§8.1); BJS give a construction taking $2^{n-1}$ pivots (§8.2). Empirically about $O(m)$ iterations are typical (BT p. 360). See [[Complexity of linear programming]].
- At an optimal basis, $\mathbf p'=\mathbf c_B'\mathbf B^{-1}$ (BJS: $\mathbf w=\mathbf c_B\mathbf B^{-1}$) is dual optimal; this proves strong duality ([[LP duality]]). The [[Dual simplex method]] runs the same tableau with the roles of feasibility swapped. Re-optimizing after data changes is [[LP sensitivity analysis]].
- Specializations: network simplex on spanning trees ([[Network flow problem]]), column generation and [[Dantzig-Wolfe decomposition]].

**Covered in**: Bertsimas-Tsitsiklis ch. 3 (pp. 82-129, derivation, tableau, column geometry); Bazaraa-Jarvis-Sherali ch. 3 (pp. 91-135)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 3, 8); `text_books/Linear Optimization/BJS full book.pdf` (ch. 3-5, 8-9). BJS pages viewed as images: printed 102, 114, 122; the rest of BJS ch. 3 from a text layer with garbled math.
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Basic feasible solution]] · [[Dual simplex method]] · [[LP duality]] · [[Interior point method]] · [[Ellipsoid method]] · [[Polyhedron]]
- [[Revised simplex method]] · [[Simplex initialization and anticycling]] · [[LP sensitivity analysis]] · [[Complexity of linear programming]] · [[Network flow problem]]
