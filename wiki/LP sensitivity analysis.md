---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 5; Bazaraa, Jarvis, Sherali 2010, ch. 6 §6.7-6.8"
tags: [optimization]
---

# LP sensitivity analysis

**Intuition**: after solving an LP, ask how the optimal basis and cost respond to changes in $\mathbf A$, $\mathbf b$, $\mathbf c$, to an added row or column, or to a parameter swept along a line. Locally this is a recheck of two basis conditions; globally the optimal cost is a convex function of $\mathbf b$ and a concave function of $\mathbf c$ (BT ch. 5; BJS §6.7-6.8). Standing assumption: standard form, rows of $\mathbf A$ linearly independent (BT p. 201-202).

## Local sensitivity

Start from an optimal basis $\mathbf B$. It satisfies two conditions (BT p. 202-203):
- feasibility: $\mathbf B^{-1}\mathbf b\ge\mathbf0$
- optimality: $\mathbf c'-\mathbf c_B'\mathbf B^{-1}\mathbf A\ge\mathbf0'$

After a data change, recheck both. If the basis stays feasible and optimal it is still optimal. If only one fails, restart from the current basis with the matching simplex variant: primal simplex if optimality fails, [[Dual simplex method]] if feasibility fails. This is usually far faster than solving from scratch. BJS (§6.7, p. 295-312) do the same by updating the final tableau, reading the dual optimum off the basis as $\mathbf w^*=\mathbf c_B\mathbf B^{-1}$ (BJS Examples 6.10-6.16, headings only; sections not read in detail). Notation differs: $\mathbf p$ in BT, $\mathbf w$ in BJS, and reduced costs have opposite sign ($r_j$ versus $z_j-c_j$, see [[Simplex method]]).

| Change | Check | If violated |
|---|---|---|
| New variable $x_{n+1}$ with column $\mathbf A_{n+1}$ (p. 203) | reduced cost $c_{n+1}-\mathbf c_B'\mathbf B^{-1}\mathbf A_{n+1}\ge0$ | add a column, run primal simplex |
| New inequality $\mathbf a_{m+1}'\mathbf x\ge b_{m+1}$ violated by $\mathbf x^*$ (p. 205) | new basis is $\mathbf B$ plus the new slack; reduced costs stay $\ge0$ | dual simplex |
| New equality constraint (p. 206-207) | $(\mathbf p^*,0)$ need not be a dual BFS | big-M auxiliary problem, primal simplex |
| Change $b_i\to b_i+\delta$ (p. 207-208) | $\mathbf B^{-1}(\mathbf b+\delta\mathbf e_i)\ge\mathbf0$ | dual simplex |
| Change in cost $c_j$ (p. 208-209) | nonbasic $j$: only $r_j+\delta\ge0$; basic $j$: all reduced costs change | primal simplex |
| Change in nonbasic column (p. 209) | only that reduced cost | primal simplex |
| Change in basic column (p. 210) | both conditions affected; range is again an interval (BT Exercise 5.3) | |

The condensed rows for the new equality constraint and nonbasic column are paraphrased from the text layer **[unverified]** against page images.

For a changed right-hand side the optimal cost on the allowed range is (BT p. 208)
$$\mathbf c_B'\mathbf B^{-1}(\mathbf b+\delta\mathbf e_i)=\mathbf p'\mathbf b+\delta p_i$$
with $\mathbf p'=\mathbf c_B'\mathbf B^{-1}$, so $p_i$ is the rate of change (marginal cost in [[LP duality]]). BJS write the same as $\partial z/\partial b_i=w_i$ and caution that degeneracy can spoil this as a realizable rate (BJS p. 175, 270-277).

Worked numbers (BT Examples 5.1-5.4, p. 203-209), for a problem with optimal $\mathbf x=(2,2,0,0)$ and optimal cost $-12$ in the printed tableau:
- Adding $\delta$ to $b_1$: basic variables become $x_1=2-3\delta$, $x_2=2+5\delta$, feasible for $-2/5\le\delta\le2/3$; cost rate $=\mathbf c_B'\mathbf B^{-1}\mathbf e_1=10$ (p. 208).
- Cost ranges keeping the basis optimal: $\delta_3\ge-2$, $\delta_4\ge-7$ for nonbasic costs; $-2/3\le\delta_1\le7/2$ for the basic cost $c_1$ (p. 209).

Perturbing a basic column $\mathbf A_j\to\mathbf A_j+\delta\mathbf e_i$ with nondegenerate unique optima gives (BT Exercise 5.2, p. 210)
$$\mathbf c'\mathbf x^*(\delta)=\mathbf c'\mathbf x^*-\delta x_j^*p_i+o(\delta^2)$$
read as "free" extra nutrient $\delta x_j^*$ worth $p_i$ per unit in the diet problem.

Production planning revisited (BT p. 210-211): the DEC problem of [[LP modelling]] is re-solved in four variants (Table 5.1) and dual prices with validity ranges are reported (Table 5.2), as typical LP software does ([[LP in practice]]).

## Global dependence on the right-hand side

Let $F(\mathbf b)$ be the optimal cost of min $\mathbf c'\mathbf x$ s.t. $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\ge\mathbf0$, on the set $S$ of $\mathbf b$ with a feasible solution. Near a nondegenerate optimal BFS, $F(\mathbf b)=\mathbf p'\mathbf b$ is linear with gradient $\mathbf p$ (BT p. 213).

> [!theorem] Theorem 5.1 (p. 213)
> $F$ is a convex function of $\mathbf b$ on $S$.

Proof (p. 213): take optimal $\mathbf x^1,\mathbf x^2$ for $\mathbf b^1,\mathbf b^2$; then $\lambda\mathbf x^1+(1-\lambda)\mathbf x^2$ is feasible for $\lambda\mathbf b^1+(1-\lambda)\mathbf b^2$, giving
$$F(\lambda\mathbf b^1+(1-\lambda)\mathbf b^2)\le\lambda F(\mathbf b^1)+(1-\lambda)F(\mathbf b^2)$$
A second proof via the dual shows $F(\mathbf b)=\max_i(\mathbf p^i)'\mathbf b$ over the dual extreme points, so $F$ is piecewise linear and convex (p. 213-214). At breakpoints every optimal primal BFS is degenerate (p. 215). See [[Convex function]].

## The set of all dual optimal solutions

> [!definition] Subgradient (Def. 5.1, p. 215)
> $\mathbf p$ is a subgradient of a convex $F$ at $\mathbf b^*$ if
> $$F(\mathbf b^*)+\mathbf p'(\mathbf b-\mathbf b^*)\le F(\mathbf b)\quad\forall\,\mathbf b\in S$$

> [!theorem] Theorem 5.2 (p. 216)
> If the primal is feasible with finite optimal cost, $\mathbf p$ is dual optimal if and only if it is a subgradient of $F$ at $\mathbf b^*$.

At breakpoints there are several subgradients, so dual optimal solutions act as generalized gradients and the marginal-cost reading survives there. The subgradient as an algorithmic tool is in [[Subgradient method]].

## Global dependence on the cost vector

Let $T$ be the set of $\mathbf c$ with finite optimal cost (dual feasible) and $G(\mathbf c)$ the optimal cost. Since an optimum sits at a basic feasible solution $\mathbf x^1,\dots,\mathbf x^N$ (independent of $\mathbf c$),
$$G(\mathbf c)=\min_{i=1,\dots,N}\mathbf c'\mathbf x^i$$
a minimum of linear functions, hence piecewise linear and concave.

> [!theorem] Theorem 5.3 (p. 217)
> (a) $T$ is convex. (b) $G$ is concave on $T$. (c) If $\mathbf x^*$ is the unique primal optimum for some $\mathbf c$, then $G$ is linear near $\mathbf c$ with gradient $\mathbf x^*$.

## Parametric programming

Fix $\mathbf A,\mathbf b,\mathbf c,\mathbf d$ and solve for a scalar $\theta$ (BT §5.5, p. 217-219):
$$\min\ (\mathbf c+\theta\mathbf d)'\mathbf x\quad\text{s.t.}\ \mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf0$$
The optimal cost $g(\theta)=\min_i(\mathbf c+\theta\mathbf d)'\mathbf x^i$ is piecewise linear concave (p. 217). The simplex method is adapted to sweep $\theta$: keep the current basis while its reduced costs stay nonnegative, then pivot at the breakpoint (Example 5.5, p. 218-219). Anticycling rules for this variant are in Murty (BT notes, p. 229). BJS (§6.8, p. 312-336, Examples 6.17-6.18) vary the cost or right-hand side along a parameter, with piecewise linear convex optimal-value functions; the section was not read in detail.

## Key facts
- A basis stays optimal while $\mathbf B^{-1}\mathbf b\ge\mathbf0$ and the reduced costs are $\ge0$; each single-entry change gives an interval of $\delta$.
- $F(\mathbf b)$ is convex piecewise linear, $G(\mathbf c)$ is concave piecewise linear; dual optimal solutions are the subgradients of $F$.
- Violated feasibility is repaired by the [[Dual simplex method]], violated optimality by the primal [[Simplex method]], both warm-started from the current basis.

**Covered in**: Bertsimas-Tsitsiklis ch. 5 (pp. 201-229); Bazaraa-Jarvis-Sherali ch. 6 §6.7-6.8 (pp. 295-336)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 5, printed pp. 201-229); `text_books/Linear Optimization/BJS full book.pdf` (ch. 6, printed pp. 295-336).
**Last updated**: 2026-11-06

---

## Related pages
- [[LP duality]] · [[Dual simplex method]] · [[Simplex method]] · [[Linear programming]] · [[Convex function]] · [[Subgradient method]] · [[LP modelling]] · [[LP in practice]]
