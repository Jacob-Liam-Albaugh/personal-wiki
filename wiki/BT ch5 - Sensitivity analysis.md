---
type: paper
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 5 (printed pp. 201-229)"
tags: [optimization]
authors: ["[[Dimitris Bertsimas]]", "[[John N. Tsitsiklis]]"]
year: 1997
venue: "Athena Scientific (textbook)"
file: "Linear Optimization/MIT (ch 1-5).pdf"
---

# BT ch5 - Sensitivity analysis

**Summary**: How the optimal cost and optimal basis of a standard-form [[Linear programming|linear program]] respond to changes in $\mathbf A$, $\mathbf b$, $\mathbf c$, to added rows or columns, and globally as functions of $\mathbf b$ and $\mathbf c$. Standing assumption: standard form, rows of $\mathbf A$ linearly independent (p. 201-202).

## Local sensitivity (§5.1, p. 202-211)
Start from an optimal basis $\mathbf B$. It satisfies two conditions (p. 202-203):
- feasibility: $\mathbf B^{-1}\mathbf b\ge\mathbf0$
- optimality: $\mathbf c'-\mathbf c_B'\mathbf B^{-1}\mathbf A\ge\mathbf0'$

After a data change, recheck both. If the basis stays feasible and optimal it is still optimal. If only one fails, restart from the current basis with the matching simplex variant: primal simplex if optimality fails, dual simplex if feasibility fails ([[Dual simplex method]], [[BT ch4 - Duality theory]]). This is usually far faster than solving from scratch.

| Change | Check | If violated |
|---|---|---|
| New variable $x_{n+1}$ with column $\mathbf A_{n+1}$ (p. 203) | reduced cost $c_{n+1}-\mathbf c_B'\mathbf B^{-1}\mathbf A_{n+1}\ge0$ | add a column, run primal simplex |
| New inequality $\mathbf a_{m+1}'\mathbf x\ge b_{m+1}$ violated by $\mathbf x^*$ (p. 205) | new basis is $\mathbf B$ plus the new slack; reduced costs stay $\ge0$ | dual simplex |
| New equality constraint (p. 206-207) | $(\mathbf p^*,0)$ need not be a dual BFS | big-M auxiliary problem, primal simplex |
| Change $b_i\to b_i+\delta$ (p. 207-208) | $\mathbf B^{-1}(\mathbf b+\delta\mathbf e_i)\ge\mathbf0$ | dual simplex |
| Change in cost $c_j$ (p. 208-209) | nonbasic $j$: only $r_j+\delta\ge0$; basic $j$: all reduced costs change | primal simplex |
| Change in nonbasic column (p. 209) | only that reduced cost | primal simplex |
| Change in basic column (p. 210) | both conditions affected; range is again an interval (Exercise 5.3) | |

For a changed right-hand side the optimal cost on the allowed range is (p. 208)
$$\mathbf c_B'\mathbf B^{-1}(\mathbf b+\delta\mathbf e_i)=\mathbf p'\mathbf b+\delta p_i$$
with $\mathbf p'=\mathbf c_B'\mathbf B^{-1}$, so $p_i$ is the rate of change (see marginal cost in [[BT ch4 - Duality theory]]).

Worked numbers (Examples 5.1-5.4, p. 203-209), for a problem with optimal $\mathbf x=(2,2,0,0)$ and optimal cost $-12$ in the printed tableau:
- Adding $\delta$ to $b_1$: basic variables become $x_1=2-3\delta$, $x_2=2+5\delta$, feasible for $-2/5\le\delta\le2/3$; cost rate $=\mathbf c_B'\mathbf B^{-1}\mathbf e_1=10$ (p. 208).
- Cost ranges keeping the basis optimal: $\delta_3\ge-2$, $\delta_4\ge-7$ for nonbasic costs; $-2/3\le\delta_1\le7/2$ for the basic cost $c_1$ (p. 209).

Perturbing a basic column $\mathbf A_j\to\mathbf A_j+\delta\mathbf e_i$ with nondegenerate unique optima gives (Exercise 5.2, p. 210)
$$\mathbf c'\mathbf x^*(\delta)=\mathbf c'\mathbf x^*-\delta x_j^*p_i+o(\delta^2)$$
read as "free" extra nutrient $\delta x_j^*$ worth $p_i$ per unit in the diet problem.

Production planning revisited (p. 210-211): the DEC problem of [[BT ch1 - Introduction]] is re-solved in four variants (Table 5.1) and dual prices with validity ranges are reported (Table 5.2), as typical LP software does.

## Global dependence on the right-hand side (§5.2, p. 212-215)
Let $F(\mathbf b)$ be the optimal cost of min $\mathbf c'\mathbf x$ s.t. $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\ge\mathbf0$, on the set $S$ of $\mathbf b$ with a feasible solution. Near a nondegenerate optimal BFS, $F(\mathbf b)=\mathbf p'\mathbf b$ is linear with gradient $\mathbf p$ (p. 213).

> [!theorem] Theorem 5.1 (p. 213)
> $F$ is a convex function of $\mathbf b$ on $S$.

Proof (p. 213): take optimal $\mathbf x^1,\mathbf x^2$ for $\mathbf b^1,\mathbf b^2$; then $\lambda\mathbf x^1+(1-\lambda)\mathbf x^2$ is feasible for $\lambda\mathbf b^1+(1-\lambda)\mathbf b^2$, giving
$$F(\lambda\mathbf b^1+(1-\lambda)\mathbf b^2)\le\lambda F(\mathbf b^1)+(1-\lambda)F(\mathbf b^2)$$
A second proof via the dual shows $F(\mathbf b)=\max_i(\mathbf p^i)'\mathbf b$ over the dual extreme points, so $F$ is piecewise linear and convex (p. 213-214). At breakpoints every optimal primal BFS is degenerate (p. 215). See [[Convex function]].

## The set of all dual optimal solutions (§5.3, p. 215-216)
> [!definition] Subgradient (Def. 5.1, p. 215)
> $\mathbf p$ is a subgradient of a convex $F$ at $\mathbf b^*$ if
> $$F(\mathbf b^*)+\mathbf p'(\mathbf b-\mathbf b^*)\le F(\mathbf b)\quad\forall\,\mathbf b\in S$$

> [!theorem] Theorem 5.2 (p. 216)
> If the primal is feasible with finite optimal cost, $\mathbf p$ is dual optimal if and only if it is a subgradient of $F$ at $\mathbf b^*$.

At breakpoints there are several subgradients, so dual optimal solutions act as generalized gradients and the marginal-cost reading survives there.

## Global dependence on the cost vector (§5.4, p. 216-217)
Let $T$ be the set of $\mathbf c$ with finite optimal cost (dual feasible) and $G(\mathbf c)$ the optimal cost. Since an optimum sits at a basic feasible solution $\mathbf x^1,\dots,\mathbf x^N$ (independent of $\mathbf c$),
$$G(\mathbf c)=\min_{i=1,\dots,N}\mathbf c'\mathbf x^i$$
a minimum of linear functions, hence piecewise linear and concave.

> [!theorem] Theorem 5.3 (p. 217)
> (a) $T$ is convex. (b) $G$ is concave on $T$. (c) If $\mathbf x^*$ is the unique primal optimum for some $\mathbf c$, then $G$ is linear near $\mathbf c$ with gradient $\mathbf x^*$.

## Parametric programming (§5.5, p. 217-219)
Fix $\mathbf A,\mathbf b,\mathbf c,\mathbf d$ and solve for a scalar $\theta$:
$$\min\ (\mathbf c+\theta\mathbf d)'\mathbf x\quad\text{s.t.}\ \mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf0$$
The optimal cost $g(\theta)=\min_i(\mathbf c+\theta\mathbf d)'\mathbf x^i$ is piecewise linear concave (p. 217). The simplex method is adapted to sweep $\theta$: keep the current basis while its reduced costs stay nonnegative, then pivot at the breakpoint (Example 5.5, p. 218-219). Anticycling rules for this variant are in Murty (notes, p. 229).

## Notes
- Wiki note: the table of changes above condenses §5.1; exact ranges for each case are the cited inequalities and examples. The condensed rows for the new equality constraint and nonbasic column are paraphrased from the text layer **[unverified]** against page images.

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf 217-245, printed pp. 201-229).
**Last updated**: 2026-11-06

---

## Related pages
- [[LP duality]] · [[Dual simplex method]] · [[Simplex method]] · [[Linear programming]]
- [[BT ch4 - Duality theory]] · [[BT ch3 - The simplex method]] · [[BT ch6 - Large scale optimization]] · [[BJS ch6 - Duality and sensitivity analysis]]
- [[Convex function]]
