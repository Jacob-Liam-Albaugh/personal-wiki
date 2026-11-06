---
type: paper
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 3 (printed pp. 91-150)"
tags: [optimization]
authors: ["[[Mokhtar S. Bazaraa]]", "[[John J. Jarvis]]", "[[Hanif D. Sherali]]"]
year: 2010
venue: "Wiley, Linear Programming and Network Flows, 4th ed. (textbook)"
file: "text_books/Linear Optimization/BJS full book.pdf"
---

# BJS ch3 - The simplex method

**Summary**: Develops the simplex method for the standard form $\min\mathbf c\mathbf x$ s.t. $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\ge\mathbf0$: extreme points and basic feasible solutions, the optimality test based on reduced costs, the entering and leaving rules, termination by optimality or unboundedness, finite convergence without degeneracy, and the tableau implementation. See [[Simplex method]], [[Basic feasible solution]], [[Linear programming]].

**Authors**: Mokhtar S. Bazaraa, John J. Jarvis, Hanif D. Sherali · **Year**: 2010 · **File**: `text_books/Linear Optimization/BJS full book.pdf` (printed pp. 91-150). Cites use printed pages; pdf = printed + 16.

Notation: the book writes the current right-hand side with a bar; this page writes it $\hat b_i$ and the column $\mathbf y_j=\mathbf B^{-1}\mathbf a_j$. The book's coefficients are $z_j-c_j$ (reduced cost is $c_j-z_j$).

## Extreme points and optimality (§3.1-3.2, p. 91-102)
Optimality of an extreme point is argued geometrically first (§3.1, p. 91-94). Basic feasible solutions are then defined algebraically (§3.2, p. 94-102): with $\mathbf A$ of rank $m$, a basis $\mathbf B$ is $m$ linearly independent columns, $\mathbf x_B=\mathbf B^{-1}\mathbf b$, $\mathbf x_N=\mathbf0$. These are the vertices of the feasible region, see [[Polyhedron]] and [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]].

> [!theorem] Theorems 3.1-3.4, summary of results (p. 102, image seen)
> - **3.1**: the extreme points correspond to the basic feasible solutions, and both are nonempty if the feasible region is nonempty.
> - **3.2**: if the region is nonempty, a finite optimum exists iff $\mathbf c\mathbf d_j\ge0$ for every extreme direction $\mathbf d_j$; otherwise the optimal value is unbounded.
> - **3.3**: if an optimum exists, an optimal extreme point (optimal basic feasible solution) exists.
> - **3.4**: every extreme point has a corresponding basis (not necessarily unique), and every basis has a unique corresponding extreme point. An extreme point with more than one basis is degenerate, and this happens iff $\mathbf A\mathbf x=\mathbf b$ does not itself force the degenerate basic variables to be zero.

Enumerating all basic feasible solutions is bounded by $\binom nm$ but is rejected: that count is large, it does not detect unboundedness, and an empty region is found only after trying all column subsets (p. 102). The simplex method moves between extreme points without enumerating them.

## Key to the simplex method (§3.3, p. 103-105)
Given a basic feasible solution with objective $z_0$, partition into basic and nonbasic variables, $J$ the nonbasic index set. From the text layer (p. 103-104, the displays were garbled so only the structure is recorded): the objective value is $z_0=\mathbf c_B\mathbf B^{-1}\mathbf b$, the basic variables satisfy $\mathbf x_B=\mathbf B^{-1}\mathbf b-\sum_{j\in J}\mathbf y_jx_j$, and
$$z=z_0-\sum_{j\in J}(z_j-c_j)x_j,\qquad z_j=\mathbf c_B\mathbf B^{-1}\mathbf a_j\ \ \text{[text layer]}$$
The problem can be rewritten in the $p=n-m$ nonbasic variables alone, with $\mathbf x_B$ acting as slack variables. The coefficients $c_j-z_j$ are the **reduced cost coefficients**, since they live in this reduced space (p. 104).

## Geometric motivation and algebra (§3.4-3.5, p. 105-113)
Moving from an extreme point to an adjacent one raises one nonbasic variable $x_k$ from zero while the basic variables adjust along an edge (§3.4, Figures 3.6-3.8). In Figure 3.8 raising $x_4$ by one unit lowers $x_1$ and $x_2$ by $1/3$ each, the move continuing until the nonnegativity of $x_1$ blocks (p. 114, image seen). §3.5 (p. 108-113) gives the algebra: the entering variable is chosen among nonbasic ones and the step size is set by the minimum ratio below.

## Termination (§3.6, p. 114-121)
> [!definition] Entering and leaving rules (p. 114, image seen)
> Entering: $x_k$ may enter if $z_k-c_k>0$. Leaving: $x_{B_r}$ may leave, where
> $$\frac{\hat b_r}{y_{rk}}=\min_{1\le i\le m}\Big\{\frac{\hat b_i}{y_{ik}}:\ y_{ik}>0\Big\}$$

If every nonbasic $x_j$ has $z_j-c_j\le0$, the point is optimal. For any feasible $\mathbf x$ with value $z$ and the current value $z^*=\mathbf c_B\mathbf B^{-1}\mathbf b$ (p. 114, eq. 3.13, image seen):
$$z^*-z=\sum_{j\in J}(z_j-c_j)x_j\le0$$
so $z\ge z^*$ and $\mathbf x^*$ is optimal. If $z_k-c_k>0$ and $\mathbf y_k\le\mathbf0$, no ratio exists, $x_k$ can grow without bound, and the optimal value is unbounded (the direction is an extreme direction of the region, p. 114-121, read from text). Zero entries $z_j-c_j=0$ at an optimum signal alternative optima (read from text, not detailed).

## The algorithm (§3.7, p. 121-125)
Per the summary on p. 121-122 (read from text and the page seen at p. 122): at each iteration solve $\mathbf B\mathbf x_B=\mathbf b$, $\mathbf w\mathbf B=\mathbf c_B$ and $\mathbf B\mathbf y_k=\mathbf a_k$ (p. 125). Compute $z_j-c_j=\mathbf w\mathbf a_j-c_j$ for nonbasic $j$, take $k$ with $z_k-c_k>0$ (the book's usual rule is the largest, **[unverified]**), stop if $\mathbf y_k\le\mathbf0$, else apply the minimum ratio test and update the basis. For a **maximization** problem, either multiply the costs by $-1$ or pick the minimum $z_j-c_j$ and stop when $z_k-c_k\ge0$ (p. 122, image seen).

### Finite convergence without degeneracy (p. 122, image seen)
At each iteration one of three things happens: stop with an optimum ($z_k-c_k\le0$), stop with unboundedness ($z_k-c_k>0$, $\mathbf y_k\le\mathbf0$), or move to a new basic feasible solution. If $\hat b_r>0$, then $x_k=\hat b_r/y_{rk}>0$ and the objective changes by $x_k(z_k-c_k)>0$, so it strictly decreases and no basis repeats.

> [!theorem] Theorem 3.5, Finite Convergence (p. 122)
> In the absence of degeneracy (and assuming feasibility), the simplex method stops in a finite number of iterations, either with an optimal basic feasible solution or with the conclusion that the optimal value is unbounded.

With degeneracy cycling is possible, the subject of [[BJS ch4 - Starting solution and convergence]].

**Example 3.8** (p. 122-125, image seen for the statement): minimize $-x_1-3x_2$ subject to $2x_1+3x_2\le6$, $-x_1+x_2\le1$, $x_1,x_2\ge0$, with slacks $x_3,x_4$. Read from text (p. 125, final iteration): the basis $\{x_1,x_2\}$ is reached, with $\mathbf w=(-4/5,-3/5)$ and $z_4-c_4=-3/5\le0$, giving
$$(x_1,x_2,x_3,x_4)=(3/5,\,8/5,\,0,\,0),\quad z=-27/5$$
Figure 3.11 shows the simplex path. The text layer was used for these values, they were not checked against an image.

## Tableau format (§3.8, p. 125-135)
The simplex method in tableau form solves $\mathbf B\mathbf x_B=\mathbf b$, $\mathbf w\mathbf B=\mathbf c_B$, $\mathbf B\mathbf y_k=\mathbf a_k$ by pivoting (p. 125, read from text); other ways of solving and updating these systems give other algorithms inside the same framework, such as [[BJS ch5 - Special simplex implementations and optimality conditions]] (revised simplex). The tableau rows are the representation of $z$ and $\mathbf x_B$ in terms of the nonbasic variables. Details of the tableau layout, the pivot operation, and the exercises were not read (headings only).

## Block pivoting (§3.9, p. 135)
A heading appears at pdf 150 (printed 134); the section was not read.

## Notes
- Wiki note: BT develop the same algorithm in [[BT ch3 - The simplex method]], with reduced cost written $c_j-\mathbf c_B'\mathbf B^{-1}\mathbf A_j$ and the entering rule "reduced cost negative", which is the same condition as $z_j-c_j>0$ here. BT's Theorems 3.1-3.3 play the roles of 3.1-3.4 above.
- Wiki note: the optimality certificate $\mathbf w=\mathbf c_B\mathbf B^{-1}$ is a dual solution, developed in [[BJS ch6 - Duality and sensitivity analysis]] and [[LP duality]].

**Sources**: `text_books/Linear Optimization/BJS full book.pdf` (pdf 107-166, printed pp. 91-150). Pages viewed as images: pdf 118 (printed 102), 130 (printed 114), 138 (printed 122). Everything else read from the text layer, whose math is garbled, so those parts are described and not transcribed.
**Last updated**: 2026-11-06

---

## Related pages
- [[Simplex method]] · [[Basic feasible solution]] · [[Linear programming]] · [[LP duality]] · [[Polyhedron]]
- [[BT ch3 - The simplex method]] · [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]] · [[BJS ch4 - Starting solution and convergence]] · [[BJS ch5 - Special simplex implementations and optimality conditions]]
