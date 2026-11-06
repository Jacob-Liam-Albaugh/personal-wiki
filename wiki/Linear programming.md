---
type: definition
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 1; Bazaraa, Jarvis, Sherali 2010, ch. 1"
tags: [optimization]
---

# Linear programming

> [!definition] Linear program, standard form (source: MIT (ch 1-5).pdf, p. 4, eq. 1.3)
> $$\min\ \mathbf c'\mathbf x\quad\text{s.t.}\quad \mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf 0 .$$

**Intuition**: minimize a linear cost over a [[Polyhedron]]. Reading of the constraint: $\sum_i\mathbf A_ix_i=\mathbf b$ builds the target $\mathbf b$ from nonnegative amounts of the column "resources" $\mathbf A_i$ at unit cost $c_i$ (source: Bertsimas-Tsitsiklis, p. 4).

## Forms of an LP

A linear program minimizes (or maximizes) a linear objective subject to linear constraints. Bazaraa et al. write it as (source: Bazaraa-Jarvis-Sherali, p. 2)
$$\sum_{j=1}^na_{ij}x_j\ge b_i,\ \ i=1,\dots,m$$
$$x_1,\dots,x_n\ge0$$
with objective $\min c_1x_1+\dots+c_nx_n$. The $x_j$ are decision variables, the $a_{ij}$ technological coefficients forming the constraint matrix $\mathbf A$, $\mathbf b$ the right-hand-side vector, and $x_j\ge0$ the nonnegativity constraints. A point satisfying all constraints is a feasible solution; the set of all of them is the feasible region (feasible set). Example 1.1 (BJS p. 2): minimize $2x_1+5x_2$ s.t. $x_1+x_2\ge6$, $-x_1-2x_2\ge-18$, $x_1,x_2\ge0$.

> [!definition] General form (source: MIT (ch 1-5).pdf, p. 3, eq. 1.1)
> Minimize $\mathbf c'\mathbf x$ subject to
> $$\mathbf a_i'\mathbf x\ge b_i,\quad i\in M_1$$
> $$\mathbf a_i'\mathbf x\le b_i,\quad i\in M_2$$
> $$\mathbf a_i'\mathbf x= b_i,\quad i\in M_3$$
> $$x_j\ge 0\ (j\in N_1),\qquad x_j\le 0\
> (j\in N_2)$$

A variable in neither $N_1$ nor $N_2$ is free. If for every real $K$ some feasible $\mathbf x$ has cost below $K$, the cost is $-\infty$ (unbounded). Maximizing $\mathbf c'\mathbf x$ is minimizing $-\mathbf c'\mathbf x$ (BT p. 3):
$$\max\sum c_jx_j=-\min\sum(-c_j)x_j$$

An equality is two inequalities, and $\mathbf a_i'\mathbf x\le b_i$ is $(-\mathbf a_i)'\mathbf x\ge -b_i$. So every LP can be written (eq. 1.2, BT p. 4) as
$$\min\ \mathbf c'\mathbf x\quad\text{s.t.}\quad \mathbf A\mathbf x\ge\mathbf b .$$

> [!definition] Standard form (source: p. 4, eq. 1.3)
> $$\min\ \mathbf c'\mathbf x\quad\text{s.t.}\quad \mathbf A\mathbf x=\mathbf b,\ \ \mathbf x\ge\mathbf 0 .$$
> Reading: $\sum_i \mathbf A_i x_i=\mathbf b$ synthesizes the target $\mathbf b$ from nonnegative amounts of the $n$ column "resources" $\mathbf A_i$, at unit cost $c_i$.

Both books use standard form (all restrictions equalities, all variables nonnegative) for the [[Simplex method]] and interior point methods ([[Interior point method]]); BT use $\mathbf A\mathbf x\ge\mathbf b$ for the theory and assume full row rank of the $m\times n$ matrix early. The canonical form of BJS (minimization with all constraints $\ge$ and nonnegative variables, or maximization with all $\le$) is the convenient form for duality ([[LP duality]]) (BJS p. 5).

**Reduction to standard form** (BT pp. 5-6; BJS pp. 4-5):
- Free variable: replace $x_j$ by $x_j^+-x_j^-$ with $x_j^\pm\ge0$ (BT). For $k$ free variables one shared $x''$ suffices, $x_j=x_j'-x''$ (BJS). Alternatively eliminate the variable by substitution, though that is seldom used numerically.
- Inequality: $\sum_j a_{ij}x_j\le b_i$ becomes $\sum_j a_{ij}x_j+s_i=b_i$, $s_i\ge0$ (slack); a $\ge$ gets $-s_i$ (surplus).
- A lower bound $x_j\ge\ell_j$ is handled by $x_j'=x_j-\ell_j$; an upper bound $x_j\le u_j$ by $x_j'=u_j-x_j$ (BJS).

Equivalent means a feasible point of one maps to a feasible point of the other with the same cost, so optimal costs agree.

## Modelling assumptions

Using an LP model presumes (BJS pp. 3-4): proportionality (contribution to cost and constraints is linear in the activity level, no economies of scale or setup costs), additivity (no interaction between activities), divisibility (fractional levels allowed) and deterministic coefficients. Dantzig's reply to Hotelling's objection that the world is nonlinear (via von Neumann) is that LP is a model on postulated axioms and applies exactly when the situation fits them (p. 4). Models are collected in [[LP modelling]]; integrality is added in [[Integer programming]].

History (BJS p. 1): the problem was conceived by Dantzig around 1947 while advising the US Air Force on planning; Kantorovich had formulated and solved such a problem in 1939, but his work was unknown until 1959; the term "linear programming" was coined by Koopmans in 1948; the simplex method was published in 1949.

## Geometric solution

Level sets $\mathbf c'\mathbf x=z$ are lines (planes) orthogonal to $\mathbf c$. For two variables, draw the feasible region as an intersection of half-planes and slide a line of constant objective value in the improving direction (direction $-\mathbf c$ for minimization) until it last touches the region (BT §1.4, pp. 21-25; BJS §1.3, pp. 18-22). BT Example 1.6: minimize $-x_1-x_2$ s.t. $x_1+2x_2\le3$, $2x_1+x_2\le3$, $\mathbf x\ge0$; optimum $(1,1)$ with cost $-2$, a corner (p. 21). Four outcomes (BT Example 1.8, pp. 23-24; BJS Figures 1.1-1.8, pp. 20-22):
- a unique optimal solution at an extreme point,
- alternative optima (a whole edge; the optimal set may be bounded or unbounded),
- unbounded optimal cost $-\infty$ with no optimal solution,
- an empty feasible region (inconsistent constraints, BJS Figure 1.8).

BT note that "feasible, finite cost, but no optimum" (e.g. $\min 1/x$, $x>0$) never happens for an LP (p. 24). An optimum, if it exists and the region has an extreme point, is attained at an extreme point of the region, made precise in [[Polyhedron]] and [[Basic feasible solution]]; this motivates the simplex method.

## Requirement space

For the standard form with columns $\mathbf a_1,\dots,\mathbf a_n$ (BJS §1.4, p. 23, Figure 1.9):
$$\sum_{j=1}^n\mathbf a_jx_j=\mathbf b,\quad x_j\ge0$$
The set $\{\sum\mathbf a_jx_j:x_j\ge0\}$ is the cone generated by the columns. The problem is feasible iff $\mathbf b$ lies in this cone, hence the name "requirement space" ($\mathbf b$ reflects requirements to be satisfied). Among all representations, choose the one minimizing $\sum c_jx_j$. BJS Example 1.5 (p. 27): minimizing $-2x_1-3x_2$ subject to $x_1+2x_2\ge2$ and nonnegativity is unbounded, seen in the requirement space because points in the cone with arbitrarily small $z$ exist (Figure 1.13). The same cone picture drives the proof of [[Farkas lemma]].

## Key facts
- The general form has $\ge$, $\le$ and $=$ rows and sign-restricted or free variables. Every LP converts to standard form by splitting free variables and adding slack or surplus variables. Maximizing $\mathbf c'\mathbf x$ is minimizing $-\mathbf c'\mathbf x$.
- Cost can be unbounded ($-\infty$); the feasible set can be empty.
- A feasible set with an extreme point and a finite optimum has an optimal extreme point, so it suffices to search [[Basic feasible solution]]s (BT Thm 2.7-2.8).
- Every LP has a partner problem; see [[LP duality]] (weak and strong duality, complementary slackness).
- Piecewise linear convex costs, absolute values and minimax objectives are LPs after adding variables ([[LP modelling]]).
- Algorithms: [[Simplex method]] and [[Dual simplex method]] (vertex walks, exponential worst case), [[Ellipsoid method]] (polynomial, impractical), [[Interior point method]] (polynomial and competitive); the theory is in [[Complexity of linear programming]]. Solvers and practice: [[LP in practice]]. Structured LPs: [[Dantzig-Wolfe decomposition]], [[Network flow problem]]. Adding integrality gives [[Integer programming]].
- The $\ell_1$ trick of [[LP modelling]] is the LP form of absolute-value penalties such as [[LASSO]].

## Duality
- Basu derives LP strong duality from the valid-inequality theorem (Farkas) and treats the LP dual as a case of conic duality (source: Basu 2018, Thm 2.85, p. 35; ch. 4 pp. 80-84; see [[Lagrangian duality]]).

**Covered in**: Bertsimas-Tsitsiklis ch. 1 (pp. 1-33 as printed, forms and reductions pp. 3-6, graphical solution pp. 21-25); Bazaraa-Jarvis-Sherali ch. 1 (pp. 1-28)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 1-2, 8-9, 12); `text_books/Linear Optimization/BJS full book.pdf` (ch. 1).
**Last updated**: 2026-11-06

---

## Related pages
- [[Polyhedron]] · [[Basic feasible solution]] · [[Simplex method]] · [[LP duality]] · [[LP modelling]] · [[Complexity of linear programming]] · [[LP in practice]] · [[Integer programming]] · [[Convex set]] · [[Convex function]] · [[KKT conditions]] · [[Network flow problem]] · [[Lagrangian duality]]
