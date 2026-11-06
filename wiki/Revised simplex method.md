---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 3 §3.3; Bazaraa, Jarvis, Sherali 2010, ch. 5 §5.1-5.2"
tags: [optimization]
---

# Revised simplex method

**Summary**: A form of the [[Simplex method]] that keeps only the basis inverse (or a factorization of it) instead of the full tableau, computes simplex multipliers $\mathbf w=\mathbf c_B\mathbf B^{-1}$ to price columns, and extends to variables with upper and lower bounds without enlarging the basis.

## Steps

It performs the same pivots as the tableau method but keeps only a smaller array, saving storage (BJS §5.1, pp. 201-221). Steps for a minimization problem with basis $\mathbf B$ and inverse $\mathbf B^{-1}$ (BJS p. 201, formulas described from the text layer):
1. Basic solution $\mathbf x_B=\mathbf B^{-1}\mathbf b=\hat{\mathbf b}$, $\mathbf x_N=\mathbf0$, objective $\mathbf c_B\mathbf B^{-1}\mathbf b$.
2. Compute the **simplex multipliers** $\mathbf w=\mathbf c_B\mathbf B^{-1}$, then $z_j-c_j=\mathbf w\mathbf a_j-c_j$ for nonbasic $j$ (BT: $r_j=c_j-\mathbf c_B'\mathbf B^{-1}\mathbf A_j$, so the signs are opposite). Take the maximum $z_k-c_k$; if it is $\le0$, stop, the point is optimal.
3. Compute $\mathbf y_k=\mathbf B^{-1}\mathbf a_k$. If $\mathbf y_k\le\mathbf0$, stop, the optimum is unbounded. Else the leaving row $r$ is given by the minimum ratio of $\hat b_i/y_{ik}$ over $y_{ik}>0$, the basis is updated and one returns to step 1.

In the array, the basis inverse is stored beside the right-hand side and updated by a pivot on the column $\mathbf y_k$ appended to the right (BJS Example 5.1, pp. 203-205). With the identity as initial basis, $\mathbf w=\mathbf0$ at the start (p. 204). The multipliers $\mathbf w$ are a dual solution when the basis is optimal ([[LP duality]]). BJS's chapter introduction also promises numerically stable forms of the method (p. 201), not read in detail.

## Cost per iteration

- Row operations are left multiplication by an invertible $\mathbf Q$ (BT Def. 3.4, p. 96).
- Full tableau: top row $[-\mathbf c_B'\mathbf B^{-1}\mathbf b\mid\mathbf r']$, body $[\mathbf B^{-1}\mathbf b\mid\mathbf B^{-1}\mathbf A]$ (BT p. 99).
- Revised simplex keeps only $\mathbf B^{-1}$ (updated by elementary row operations). Per iteration: memory $O(mn)$ for the full tableau vs $O(m^2)$, worst-case time $O(mn)$ for both, best case $O(mn)$ vs $O(m^2)$ (BT Table 3.1, p. 107).
- Practical codes reinvert periodically to control roundoff and store $\mathbf B^{-1}$ in product form (BT p. 107).
- Bland's rule suits revised implementations that compute reduced costs one at a time ([[Simplex initialization and anticycling]]).

## Partial pricing

Rather than pricing all nonbasic variables, keep a list $L$ of basic variables plus nonbasic ones with $z_j-c_j$ within a given percentage of the largest, and iterate within $L$, rebuilding $L$ when the best value falls below another percentage or after $N$ consecutive degenerate iterations (BJS p. 220). It is advantageous for large problems, while total pricing is convenient up to around 1000 variables.

## Bounded variables

For $\mathbf A\mathbf x=\mathbf b$, $\boldsymbol\ell\le\mathbf x\le\mathbf u$ (BJS §5.2, pp. 222-233): partition $\mathbf x$ into basic variables $\mathbf x_B$ and nonbasic variables $\mathbf x_{N_1}$ at lower bounds and $\mathbf x_{N_2}$ at upper bounds. Then $\mathbf x_{N_1}=\boldsymbol\ell_{N_1}$, $\mathbf x_{N_2}=\mathbf u_{N_2}$ and $\mathbf x_B=\mathbf B^{-1}\mathbf b-\mathbf B^{-1}\mathbf N_1\boldsymbol\ell_{N_1}-\mathbf B^{-1}\mathbf N_2\mathbf u_{N_2}$. If $\boldsymbol\ell_B\le\mathbf x_B\le\mathbf u_B$ it is a basic feasible solution, and nondegenerate when the inequalities are strict. The basis stays $m\times m$ regardless of the bounds. Two partitions are adjacent if they differ in one nonbasic variable. Example 5.5 (pp. 222-224) finds all basic feasible partitions of a small region.

Optimality test (Example 5.6, pp. 233-234, image seen at p. 234): at an optimum, $z_j-c_j\ge0$ for nonbasic variables at their upper bounds and $z_j-c_j\le0$ for those at lower bounds. In the iteration shown the step size is a minimum over three candidates, $\Delta_1=\min\{2/3,2,4\}=2/3$, with $x_1$ entering and $x_4$ leaving; the full rule for bounded variables was not read. The final tableau has $z_j-c_j$ of the right signs, giving $(x_1,\dots,x_5)=(2/3,6,8/3,0,0)$ with objective $-28$.

## Key facts
- Same pivots, less storage: the tableau is recomputed from $\mathbf B^{-1}$ and the original data.
- The multipliers $\mathbf w=\mathbf c_B\mathbf B^{-1}$ are exactly the dual solution that complementary slackness pairs with the primal basic solution.
- Other ways of solving $\mathbf B\mathbf x_B=\mathbf b$, $\mathbf w\mathbf B=\mathbf c_B$, $\mathbf B\mathbf y_k=\mathbf a_k$ give other algorithms in the same framework (BJS p. 125).

**Covered in**: Bertsimas-Tsitsiklis ch. 3 §3.3 (pp. 94-107, implementations); Bazaraa-Jarvis-Sherali ch. 5 §5.1-5.2 (pp. 201-233)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 3); `text_books/Linear Optimization/BJS full book.pdf` (ch. 5; pdf 217-250, math from the text layer, final tableau of Example 5.6 from an image).
**Last updated**: 2026-11-06

---

## Related pages
- [[Simplex method]] · [[Simplex initialization and anticycling]] · [[LP duality]] · [[Dual simplex method]] · [[Linear programming]]
