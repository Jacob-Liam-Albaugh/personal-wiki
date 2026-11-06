---
type: paper
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 5 (printed pp. 201-258)"
tags: [optimization]
authors: ["[[Mokhtar S. Bazaraa]]", "[[John J. Jarvis]]", "[[Hanif D. Sherali]]"]
year: 2010
venue: "Wiley, Linear Programming and Network Flows, 4th ed. (textbook)"
file: "Linear Optimization/BJS full book.pdf"
---

# BJS ch5 - Special simplex implementations and optimality conditions

**Summary**: Implementations of the simplex method that keep only the basis inverse (revised simplex), a variant that handles lower and upper bounds without enlarging the basis, a constructive proof of Farkas' lemma from the simplex method, and the Karush-Kuhn-Tucker conditions for linear programs, shown to be necessary and sufficient. See [[Simplex method]], [[Farkas lemma]], [[KKT conditions]].

**Authors**: Mokhtar S. Bazaraa, John J. Jarvis, Hanif D. Sherali · **Year**: 2010 · **File**: `Linear Optimization/BJS full book.pdf` (printed pp. 201-258). Cites use printed pages; pdf = printed + 16.

## The revised simplex method (§5.1, p. 201-221)
It performs the same steps as the simplex method but keeps only a smaller array, saving storage (p. 201, text). Steps for a minimization problem with basis $\mathbf B$ and inverse $\mathbf B^{-1}$ (p. 201, text layer, garbled math):
1. Basic solution $\mathbf x_B=\mathbf B^{-1}\mathbf b=\hat{\mathbf b}$, $\mathbf x_N=\mathbf0$, objective $\mathbf c_B\mathbf B^{-1}\mathbf b$.
2. Compute the **simplex multipliers** $\mathbf w=\mathbf c_B\mathbf B^{-1}$, then $z_j-c_j=\mathbf w\mathbf a_j-c_j$ for nonbasic $j$. Take the maximum $z_k-c_k$; if it is $\le0$, stop, the point is optimal.
3. Compute $\mathbf y_k=\mathbf B^{-1}\mathbf a_k$. If $\mathbf y_k\le\mathbf0$, stop, the optimum is unbounded. Else the leaving row $r$ is given by the minimum ratio of $\hat b_i/y_{ik}$ over $y_{ik}>0$, the basis is updated and one returns to step 1.

In the array, the basis inverse is stored beside the right-hand side and updated by a pivot on the column $\mathbf y_k$ appended to the right (Example 5.1, p. 203-205, text). With the identity as initial basis, $\mathbf w=\mathbf0$ at the start (p. 204, text). The chapter introduction also promises numerically stable forms of the method (p. 201), not read in detail. Partial pricing (p. 220, text): rather than pricing all nonbasic variables, keep a list $L$ of basic variables plus nonbasic ones with $z_j-c_j$ within a given percentage of the largest, and iterate within $L$, rebuilding $L$ when the best value falls below another percentage or after $N$ consecutive degenerate iterations. It is advantageous for large problems, while total pricing is convenient up to around 1000 variables.

## Bounded variables (§5.2, p. 222-233)
For $\mathbf A\mathbf x=\mathbf b$, $\boldsymbol\ell\le\mathbf x\le\mathbf u$ (p. 222, text): partition $\mathbf x$ into basic variables $\mathbf x_B$ and nonbasic variables $\mathbf x_{N_1}$ at lower bounds and $\mathbf x_{N_2}$ at upper bounds. Then $\mathbf x_{N_1}=\boldsymbol\ell_{N_1}$, $\mathbf x_{N_2}=\mathbf u_{N_2}$ and $\mathbf x_B=\mathbf B^{-1}\mathbf b-\mathbf B^{-1}\mathbf N_1\boldsymbol\ell_{N_1}-\mathbf B^{-1}\mathbf N_2\mathbf u_{N_2}$. If $\boldsymbol\ell_B\le\mathbf x_B\le\mathbf u_B$ it is a basic feasible solution, and nondegenerate when the inequalities are strict. The basis stays $m\times m$ regardless of the bounds. Two partitions are adjacent if they differ in one nonbasic variable. Example 5.5 (p. 222-224, text) finds all basic feasible partitions of a small region.

Optimality test (Example 5.6, p. 233-234, image seen at p. 234): at an optimum, $z_j-c_j\ge0$ for nonbasic variables at their upper bounds and $z_j-c_j\le0$ for those at lower bounds. In the iteration shown the step size is a minimum over three candidates, $\Delta_1=\min\{2/3,2,4\}=2/3$, with $x_1$ entering and $x_4$ leaving (p. 234, image seen); the full rule for bounded variables was not read. In Example 5.6 the final tableau has $z_j-c_j$ of the right signs, giving $(x_1,\dots,x_5)=(2/3,6,8/3,0,0)$ with objective $-28$ (p. 234, image seen).

## Farkas' lemma via the simplex method (§5.3, p. 234-237)
> [!theorem] Lemma 5.1, Farkas' Lemma (p. 234, image seen)
> One and only one of the following two systems has a solution:
> $$\text{System 1: }\ \mathbf A\mathbf x\ge\mathbf0,\ \ \mathbf c\mathbf x<0$$
> $$\text{System 2: }\ \mathbf w\mathbf A=\mathbf c,\ \ \mathbf w\ge\mathbf0$$
> where $\mathbf A$ is $m\times n$ and $\mathbf c$ is an $n$-vector.

The lemma is used to establish the KKT conditions. The simplex method gives a constructive proof (p. 234, image seen for the framing; the proof and Corollary 5.1, an alternative form, were read only as headings). The geometric interpretation (p. 236-237, text and figures 5.2-5.3): with $\mathbf y=-\mathbf x$, System 1 has a solution iff the cone $\{\mathbf y:\mathbf A\mathbf y\le\mathbf0\}$ meets the open half-space $\{\mathbf y:\mathbf c\mathbf y>0\}$. System 2 says $\mathbf c$ is in the cone generated by the rows of $\mathbf A$. See [[Farkas lemma]].

## Karush-Kuhn-Tucker conditions (§5.4, p. 237-245)
Consider $\min\mathbf c\mathbf x$ s.t. $\mathbf A\mathbf x\ge\mathbf b$, $\mathbf x\ge\mathbf0$ (p. 237, image seen). At a feasible $\bar{\mathbf x}$ let $I=\{i:\mathbf a^i\bar{\mathbf x}=b_i\}$ and $J=\{j:\bar x_j=0\}$ be the binding constraints (p. 237-238, images seen). No improving feasible direction $\mathbf d$ (with $\mathbf c\mathbf d<0$, $\mathbf G\mathbf d\ge\mathbf0$ for the binding rows $\mathbf G$) can exist at an optimum, so Farkas' lemma gives multipliers with $\mathbf u\mathbf G=\mathbf c$, $\mathbf u\ge\mathbf0$, that is (eq. 5.21-5.22, p. 238):
$$\sum_{i\in I}w_i\mathbf a^i+\sum_{j\in J}v_j\mathbf e_j=\mathbf c$$
$$w_i\ge0\ (i\in I),\qquad v_j\ge0\ (j\in J)$$
Geometrically the objective gradient lies in the cone generated by the gradients of the binding constraints. Conversely, if these hold at a feasible $\bar{\mathbf x}$ then for any feasible $\hat{\mathbf x}$
$$\mathbf c\hat{\mathbf x}-\mathbf c\bar{\mathbf x}=\sum_{i\in I}w_i(\mathbf a^i\hat{\mathbf x}-b_i)+\sum_{j\in J}v_j\mathbf e_j\hat{\mathbf x}\ge0$$
so $\bar{\mathbf x}$ is optimal (p. 238). The conditions are thus necessary and sufficient. In the usual form, with $\mathbf w\ge\mathbf0$, $\mathbf v\ge\mathbf0$ (eq. 5.23-5.25, p. 238-239):
$$\mathbf A\mathbf x\ge\mathbf b,\qquad\mathbf x\ge\mathbf0\qquad\text{(primal feasibility)}$$
$$\mathbf w\mathbf A+\mathbf v=\mathbf c,\qquad\mathbf w\ge\mathbf0,\ \mathbf v\ge\mathbf0\qquad\text{(dual feasibility)}$$
$$\mathbf w(\mathbf A\mathbf x-\mathbf b)=0,\qquad\mathbf v\mathbf x=\mathbf0\qquad\text{(complementary slackness)}$$
The vectors $\mathbf w,\mathbf v$ are the Lagrangian multipliers (dual variables), and dual feasibility corresponds to feasibility of the dual problem of [[BJS ch6 - Duality and sensitivity analysis]] (p. 239). Example 5.7 (p. 239, image seen): minimize $-x_1-3x_2$ s.t. $x_1-2x_2\ge-4$, $-x_1-x_2\ge-4$, $\mathbf x\ge\mathbf0$. A claimed optimum at $(0,0)$ has no binding rows from $\mathbf A$, so $\mathbf w=\mathbf0$, which with $\mathbf v\ge\mathbf0$ cannot give $\mathbf v=\mathbf c=(-1,-3)$. The point is therefore not optimal (Figure 5.4 shows the true optimum at the vertex $(4/3,8/3)$, which the figure labels). The extension to general equalities and bounds (p. 240-245) and the exercises (p. 246-258) were not read.

## Notes
- Wiki note: BT derive duality and the optimality conditions without KKT, through reduced costs and the dual simplex view in [[BT ch4 - Duality theory]]; their Farkas lemma is in the same chapter.
- Wiki note: the multipliers $\mathbf w=\mathbf c_B\mathbf B^{-1}$ of the revised simplex method are exactly the dual solution that complementary slackness above pairs with the primal basic solution.

**Sources**: `Linear Optimization/BJS full book.pdf` (pdf 217-274, printed pp. 201-258). Pages viewed as images: pdf 250 (printed 234), 253 (237), 254 (238), 255 (239). The revised simplex steps and bounded variable material come from the text layer, whose math is garbled. Example 5.6 values were read from the image of pdf 250 only for the last tableau.
**Last updated**: 2026-11-06

---

## Related pages
- [[Simplex method]] · [[Farkas lemma]] · [[KKT conditions]] · [[LP duality]] · [[Dual simplex method]]
- [[BJS ch3 - The simplex method]] · [[BJS ch4 - Starting solution and convergence]] · [[BJS ch6 - Duality and sensitivity analysis]] · [[BT ch4 - Duality theory]]
