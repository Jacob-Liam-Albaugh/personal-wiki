---
type: paper
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 6 (printed pp. 231-263)"
tags: [optimization]
authors: ["[[Dimitris Bertsimas]]", "[[John N. Tsitsiklis]]"]
year: 1997
venue: "Athena Scientific (textbook)"
file: "Linear Optimization/MIT (ch 1-5).pdf"
---

# BT ch6 - Large scale optimization

**Summary**: Methods for LPs with very many columns or rows: delayed column generation (with the cutting stock problem), its dual view as cutting planes, Dantzig-Wolfe decomposition for block-structured problems, and Benders decomposition for two-stage stochastic programs (p. 232).

## Delayed column generation (§6.1, p. 232-234)
Standard form problem with so many columns that $\mathbf A$ cannot be stored. The revised simplex method ([[BT ch3 - The simplex method]]) only needs the basic columns and the entering column, so generate columns on demand. The missing piece is finding a variable with negative reduced cost without listing all of them, by solving (eq. 6.1)
$$\min_i\ r_i$$
over all $i$, which is often easy by problem structure. If the minimum is $\ge0$ the current solution is optimal; otherwise the minimizing column enters (p. 233).

Variants differ in which columns are kept in the restricted problem (p. 234): (a) only the basic columns plus the entering one; (b) every column that ever became basic; (c) a moderate set, dropping old ones. All are special cases of revised simplex, so they terminate without degeneracy, and the lexicographic rule prevents cycling with it.

## Cutting stock problem (§6.2, p. 234-236)
Large rolls of width $W$ are cut into $b_i$ rolls of width $w_i$ ($w_i<W$, integers). A pattern $j$ is a column $\mathbf A_j$ of nonnegative integers $a_{ij}$ with $\sum_iw_ia_{ij}\le W$ (p. 234). The LP over all patterns has an exponential number of columns. Pricing a new pattern with dual prices $p_i$ is the integer knapsack problem (eq. 6.5, p. 236):
$$\max\ \sum_ip_ia_i\quad\text{s.t.}\ \sum_iw_ia_i\le W,\ a_i\ge0\ \text{integer}$$
A dynamic programming recursion solves it in $O(mW)$ time. With $F(v)=0$ for $v<w_{\min}$, for larger $v$
$$F(v)=\max_i\{F(v-w_i)+p_i\}$$
(eq. 6.6, p. 236; the OCR of the displayed recursion is garbled, so the form is taken from the surrounding text). Dynamic programming reappears in [[BT ch11 - Integer programming]].

## Cutting plane methods (§6.3, p. 236-239)
Column generation seen from the dual: maximize $\mathbf p'\mathbf b$ s.t. $\mathbf p'\mathbf A_i\le c_i$ for a huge number of $i$ (eq. 6.7). Solve a relaxed dual using only a subset $I$ of the constraints (eq. 6.8), giving $\mathbf p^*$ (p. 237).
- If $\mathbf p^*$ is feasible for all constraints it is optimal, because the relaxed problem has fewer constraints.
- Else find a violated constraint and add it. Finding it is the separation problem, e.g. by minimizing $c_i-(\mathbf p^*)'\mathbf A_i$ over $i$ (eq. 6.9); a negative minimum gives a violated constraint (p. 237).

Constraints that become inactive may be dropped (Figure 6.1, p. 238-239). The computation is just revised simplex on the primal, so this is the same algorithm as column generation. Integer programming applications are in [[BT ch11 - Integer programming]].

## Dantzig-Wolfe decomposition (§6.4, p. 239-252)
Problem (eq. 6.10, p. 239): minimize $\mathbf c_1'\mathbf x_1+\mathbf c_2'\mathbf x_2$ subject to the coupling constraint $\mathbf D_1\mathbf x_1+\mathbf D_2\mathbf x_2=\mathbf b_0$ and the block constraints $\mathbf F_i\mathbf x_i=\mathbf b_i$, $\mathbf x_i\ge\mathbf0$. There are $m_0$ coupling rows and $m_i$ rows per block.

**Reformulation** (p. 240). Let $P_i=\{\mathbf x_i\ge\mathbf0\mid\mathbf F_i\mathbf x_i=\mathbf b_i\}$ with extreme points $\mathbf x_i^j$ and a complete set of extreme rays $\mathbf w_i^k$. By the resolution theorem ([[BT ch4 - Duality theory]], Thm 4.15) every $\mathbf x_i$ is
$$\mathbf x_i=\sum_j\lambda_i^j\mathbf x_i^j+\sum_k\theta_i^k\mathbf w_i^k$$
with $\lambda,\theta\ge0$ and $\sum_j\lambda_i^j=1$ for each $i$. Substituting gives the master problem (eqs. 6.11-6.13) with only $m_0+2$ equality constraints but a possibly astronomical number of variables. The column of $\lambda_1^j$ is $(\mathbf D_1\mathbf x_1^j,\,1,\,0)$ and that of $\theta_1^k$ is $(\mathbf D_1\mathbf w_1^k,\,0,\,0)$ (p. 241).

**Algorithm** (p. 241-243). Run revised simplex on the master. The dual vector is $\mathbf p=(\mathbf q,r_1,r_2)$ with $\mathbf q$ for the coupling rows and $r_i$ for the convexity rows. Reduced costs (p. 241):
$$(\mathbf c_1'-\mathbf q'\mathbf D_1)\mathbf x_1^j-r_1\quad\text{for }\lambda_1^j$$
$$(\mathbf c_1'-\mathbf q'\mathbf D_1)\mathbf w_1^k\quad\text{for }\theta_1^k$$
Rather than test every one, solve the subproblem: minimize $(\mathbf c_1'-\mathbf q'\mathbf D_1)\mathbf x_1$ over $P_1$ (p. 242). Three outcomes:
- (a) cost $-\infty$: the simplex ends with an extreme ray $\mathbf w_1^k$, so $\theta_1^k$ has negative reduced cost; generate its column.
- (b) finite and below $r_1$: an extreme point $\mathbf x_1^j$, so $\lambda_1^j$ enters.
- (c) finite and at least $r_1$: all reduced costs of block 1 are nonnegative.

Block 2 is treated the same way. If both subproblems fall under (c), the master is optimal. Otherwise bring in a column and update $\mathbf B^{-1}$ and $\mathbf p$ (algorithm box, p. 243).

**Practice** (p. 252). Convergence can be slow near the end, so the method is sometimes stopped early with a suboptimal solution. It is usually no faster than revised simplex on the original problem; the benefit is storage. For $t$ blocks with $m_1$ rows each, $O((m_0+tm_1)^2)$ becomes $O((m_0+t)^2)$ for the master plus $t$ tableaux of size $O(m_1^2)$.

**Bounds** (Theorem 6.1, p. 252; Example 6.3, p. 254): from a current master solution and the subproblem optima one gets a lower bound on the optimal cost $z^*$ usable for early termination. In the example the bounds bracket $-21>z^*>-22$ and the true value is $-21.5$ (p. 254). The theorem statement itself was not read from a page image. **[unverified]**

## Stochastic programming and Benders decomposition (§6.5, p. 254-262)
Two-stage problem (p. 254-255): choose $\mathbf x$ with $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\ge\mathbf0$; then one of $K$ scenarios $\omega$ with probability $\alpha_\omega>0$ is revealed and recourse $\mathbf y^\omega$ is chosen with $\mathbf B^\omega\mathbf x+\mathbf D\mathbf y^\omega=\mathbf d^\omega$, $\mathbf y^\omega\ge\mathbf0$. Minimize the expected cost
$$\mathbf c'\mathbf x+\sum_\omega\alpha_\omega\mathbf f'\mathbf y^\omega$$
The monolithic LP is large even for moderate $K$. Example 6.5 (electric power capacity expansion, p. 255) illustrates.

The second-stage cost is evaluated through its dual, whose feasible polyhedron does not depend on $\mathbf x$. It is a maximum over extreme points $\mathbf p^i$, and finite only if $(\mathbf w^j)'(\mathbf d^\omega-\mathbf B^\omega\mathbf x)\le0$ for each extreme ray $\mathbf w^j$ (eq. 6.19, p. 257). The master then has few variables and very many constraints (eq. 6.20): $(\mathbf p^i)'(\mathbf d^\omega-\mathbf B^\omega\mathbf x)\le z^\omega$ for all $i$, plus the ray constraints.

**Benders algorithm** (p. 259):
1. Solve the relaxed master (a subset of constraints) for $(\mathbf x^*,\mathbf z^*)$.
2. For each $\omega$ solve min $\mathbf f'\mathbf y^\omega$ s.t. $\mathbf D\mathbf y^\omega=\mathbf d^\omega-\mathbf B^\omega\mathbf x^*$ with the dual simplex method ([[Dual simplex method]]).
3. If every subproblem is feasible with cost at most $z^{\omega*}$, stop.
4. If some cost exceeds $z^{\omega*}$, add the constraint from the optimal dual BFS $\mathbf p^i$.
5. If a subproblem is infeasible, add the ray constraint $(\mathbf w^j)'(\mathbf d^\omega-\mathbf B^\omega\mathbf x)\le0$.

Benders is delayed constraint generation (cutting planes), essentially Dantzig-Wolfe applied to the dual (p. 259). The practical difficulty is the number of scenarios $K$.

## Notes
- Dantzig-Wolfe is credited to Dantzig and Wolfe, stochastic programming to Dantzig in the 1950s (notes, p. 263).
- Wiki note: column generation is the same idea as the pricing step of the network simplex method in [[BT ch7 - Network flows]].

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf 247-280, printed pp. 231-263).
**Last updated**: 2026-11-06

---

## Related pages
- [[Dantzig-Wolfe decomposition]] · [[Simplex method]] · [[LP duality]] · [[Linear programming]] · [[Polyhedron]]
- [[BT ch3 - The simplex method]] · [[BT ch4 - Duality theory]] · [[BT ch5 - Sensitivity analysis]] · [[BT ch7 - Network flows]] · [[BT ch11 - Integer programming]]
- [[BJS ch7 - The decomposition principle]]
