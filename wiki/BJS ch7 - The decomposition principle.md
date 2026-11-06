---
type: paper
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 7 (printed pp. 339-392)"
tags: [optimization]
authors: ["[[Mokhtar S. Bazaraa]]", "[[John J. Jarvis]]", "[[Hanif D. Sherali]]"]
year: 2010
venue: "Wiley, Linear Programming and Network Flows, 4th ed. (textbook)"
file: "Linear Optimization/BJS full book.pdf"
---

# BJS ch7 - The decomposition principle

**Summary**: Dantzig-Wolfe decomposition for linear programs whose constraints split into complicating constraints $\mathbf A\mathbf x=\mathbf b$ and a structured polyhedron $X$. The problem is rewritten over the extreme points of $X$ as a master problem and solved by the revised simplex method, with a subproblem over $X$ pricing the columns. The chapter also covers an unbounded $X$, block diagonal structure, and the equivalence with Benders and Lagrangian relaxation. See [[Dantzig-Wolfe decomposition]], [[BT ch6 - Large scale optimization]].

**Authors**: Mokhtar S. Bazaraa, John J. Jarvis, Hanif D. Sherali · **Year**: 2010 · **File**: `Linear Optimization/BJS full book.pdf` (printed pp. 339-392). Cites use printed pages; pdf = printed + 16.

## Motivation (p. 339)
Corporate and logistics models can have thousands of rows and a seemingly unlimited number of columns. The Dantzig-Wolfe, Benders and Lagrangian relaxation techniques, "all equivalent for linear programming problems", are called the decomposition principle. The constraints are partitioned into general (complicating) constraints and constraints with special structure, where special structure helps efficiency but is not needed (p. 339, text).

## The decomposition algorithm (§7.1, p. 340-347)
Problem (p. 340, image seen): $\min\mathbf c\mathbf x$ s.t. $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\in X$, where $X$ is a polyhedral set, $\mathbf A$ is $m\times n$. Assume $X$ nonempty and bounded (relaxed in §7.4). By the representation theorem (Theorem 2.1, [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]]) with extreme points $\mathbf x_1,\dots,\mathbf x_t$:
$$\mathbf x=\sum_{j=1}^t\lambda_j\mathbf x_j,\quad\sum_{j=1}^t\lambda_j=1,\quad\lambda_j\ge0$$
Substitution gives the **master problem** in $\lambda_1,\dots,\lambda_t$ (eq. 7.1-7.3, p. 340):
$$\min\ \sum_{j=1}^t(\mathbf c\mathbf x_j)\lambda_j$$
$$\sum_{j=1}^t(\mathbf A\mathbf x_j)\lambda_j=\mathbf b,\qquad\sum_{j=1}^t\lambda_j=1,\qquad\lambda_j\ge0$$
Since $t$ is usually huge, the extreme points are not enumerated. Apply the revised simplex method to the master problem ([[BJS ch5 - Special simplex implementations and optimality conditions]]). With a basic feasible solution $(\boldsymbol\lambda_B,\boldsymbol\lambda_N)$ and $(m+1)\times(m+1)$ basis inverse $\mathbf B^{-1}$, the dual variables for (7.1) and (7.2) are $(\mathbf w,\alpha)=\hat{\mathbf c}_B\mathbf B^{-1}$ with $\hat c_j=\mathbf c\mathbf x_j$ (p. 340-341, images seen). The master array holds $\mathbf B^{-1}$, $(\mathbf w,\alpha)$, the right-hand side $\hat{\mathbf c}_B\hat{\mathbf b}$ and $\hat{\mathbf b}=\mathbf B^{-1}\binom{\mathbf b}{1}$ (p. 341).

**Pricing** (eq. 7.4, p. 341, image seen):
$$z_k-\hat c_k=\max_{1\le j\le t}\ (z_j-\hat c_j)=\max_{1\le j\le t}\ \mathbf w\mathbf A\mathbf x_j+\alpha-\mathbf c\mathbf x_j$$
If it is $0$, the current solution is optimal. Else $\lambda_k$ may enter. It cannot be evaluated by enumerating the $\mathbf x_j$, but because $X$ is bounded a linear function is maximized at an extreme point, so the maximum equals $\max_{\mathbf x\in X}(\mathbf w\mathbf A-\mathbf c)\mathbf x+\alpha$. The **subproblem** (p. 341, image seen):
$$\max\ (\mathbf w\mathbf A-\mathbf c)\mathbf x+\alpha\quad\text{s.t. }\mathbf x\in X$$
is easy because of the structure of $X$. If its optimal value $z_k-\hat c_k$ is zero the basic solution is optimal. Otherwise the column
$$\mathbf y_k=\mathbf B^{-1}\binom{\mathbf A\mathbf x_k}{1}$$
joins the master array with the entry $z_k-\hat c_k$, and a pivot is made at the minimum ratio row $r$, $\hat b_r/y_{rk}=\min\{\hat b_i/y_{ik}:y_{ik}>0\}$ (p. 343, image seen).

**Remarks** (p. 343, image seen):
1. It is the revised simplex method with $z_k-\hat c_k$ computed by a subproblem, so with an anti-cycling rule in both master and subproblem it converges finitely.
2. Each subproblem returns an extreme point giving a new column, so the procedure is a **column generation method**.
3. The last subproblem basis can be reused by changing its cost row.
4. The subproblem need not be solved to optimality: any $\mathbf x_k$ with $z_k-\hat c_k>0$ is a candidate.
5. For inequality master constraints, the slack variables must be checked as well, with $z_{s_i}-c_{s_i}=w_i$.

## Numerical example and starting (§7.2-7.3, p. 345-353)
Example (§7.2, p. 345-353): the process is run to termination. In the iterations seen (p. 345, text) the known lower bound $-56/3$ matched the revised upper bound, so an optimum is at hand, and the final point is built as a convex combination of the generated extreme points. Getting started (§7.3, p. 353, text, headings only): an initial basis comes from an artificial-variable phase as in [[BJS ch4 - Starting solution and convergence]].

## Unbounded X (§7.4, p. 354-361)
When $X$ is unbounded, extreme directions $\mathbf d_j$ enter the master problem with nonnegative weights, using the full representation of Theorem 2.1 (Example 7.1, p. 357). Headings only; not read in detail.

## Block diagonal structure (§7.5, p. 361-371)
For constraints with a block diagonal part and linking rows, $X$ splits into independent subproblems, one per block, solved separately at each iteration (Example 7.2, p. 365). Headings only.

## Duality and other methods (§7.6, p. 371-376)
Dantzig-Wolfe is equivalent for linear programs to Benders partitioning and Lagrangian relaxation (p. 371, text). The setting is P: $\min\mathbf c\mathbf x$ s.t. $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\in X=\{\mathbf D\mathbf x\ge\mathbf d,\ \mathbf x\ge\mathbf0\}$ with $X$ nonempty and bounded, and its dual (p. 371, text):
$$\text{D: }\max\ \mathbf w\mathbf b+\mathbf v\mathbf d\ \ \text{s.t. }\mathbf w\mathbf A+\mathbf v\mathbf D\le\mathbf c,\ \ \mathbf v\ge\mathbf0$$
with $\mathbf w$ unrestricted. Fixing $\mathbf w$ leaves a linear program in $\mathbf v$, the basis of the Benders view (the remainder of the section was not read). Example 7.3 (p. 374). Exercises and notes follow (p. 376-392).

## Notes
- Wiki note: [[BT ch6 - Large scale optimization]] presents the same idea with the resolution theorem and also Benders cuts; here the decomposition is derived from the representation theorem of BJS ch2.

**Sources**: `Linear Optimization/BJS full book.pdf` (pdf 355-408, printed pp. 339-392). Pages viewed as images: pdf 356 (printed 340), 357 (341), 359 (343). Remaining sections read from headings and the text layer.
**Last updated**: 2026-11-06

---

## Related pages
- [[Dantzig-Wolfe decomposition]] · [[Linear programming]] · [[Simplex method]] · [[Polyhedron]]
- [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]] · [[BJS ch5 - Special simplex implementations and optimality conditions]] · [[BT ch6 - Large scale optimization]]
