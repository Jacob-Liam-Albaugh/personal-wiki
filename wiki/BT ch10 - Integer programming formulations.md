---
type: paper
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 10 (printed pp. 451-478)"
tags: [optimization]
authors: ["[[Dimitris Bertsimas]]", "[[John N. Tsitsiklis]]"]
year: 1997
venue: "Athena Scientific (textbook)"
file: "Linear Optimization/MIT (ch 1-5).pdf"
---

# BT ch10 - Integer programming formulations

**Summary**: How to model discrete decisions as integer programs, and how to judge a formulation by how closely its LP relaxation approximates the convex hull of the integer feasible points. The chapter shows that a stronger formulation can need exponentially many constraints, yet still be optimizable through separation ([[BT ch8 - Complexity of LP and the ellipsoid method]]). Algorithms for solving the resulting problems follow in [[BT ch11 - Integer programming]]. See also [[Integer programming]].

## Integer programs (§10.1, p. 452)
A discrete optimization problem seeks $\mathbf x^*$ in a discrete set $F$ that optimizes $c(\mathbf x)$. The mixed integer programming problem is (p. 452):
$$\min\ \mathbf c'\mathbf x+\mathbf d'\mathbf y$$
$$\mathbf A\mathbf x+\mathbf B\mathbf y=\mathbf b,\quad\mathbf x,\mathbf y\ge\mathbf0,\quad\mathbf x\ \text{integer}$$
If all variables are integer it is a (pure) integer program, and if they are restricted to $\{0,1\}$ a zero-one program. It is a [[Linear programming]] problem with integrality constraints added.

## Modeling techniques (§10.1, p. 452-459)
- **Zero-one knapsack** (Ex. 10.1, p. 453): maximize $\sum c_jx_j$ subject to $\sum w_jx_j\le K$, $x_j\in\{0,1\}$. The unbounded version appeared in [[BT ch6 - Large scale optimization]].
- **Forcing constraints** (p. 453): "A only if B" is $x_A\le x_B$. In facility location (Ex. 10.2) $x_{ij}\le y_j$ says client $i$ is served at $j$ only if a facility is opened there.
- **Relations between variables** (p. 454): $\sum x_j\le1$ means at most one, and $\sum x_j=1$ exactly one.
- **Disjunctive constraints** (p. 454): to require at least one of $\mathbf a'\mathbf x\ge b$ and $\mathbf c'\mathbf x\ge d$ (nonnegative coefficients, $\mathbf x\ge\mathbf0$), add a binary $y$:
$$\mathbf a'\mathbf x\ge yb,\quad\mathbf c'\mathbf x\ge(1-y)d,\quad y\in\{0,1\}$$
- **Arbitrary piecewise linear cost** (p. 455-456). For breakpoints $a_1<\dots<a_k$ write $x=\sum\lambda_ia_i$ with $\lambda\ge0$, $\sum\lambda_i=1$. The representation is unique if at most two consecutive $\lambda_i$ are nonzero, enforced by binaries $y_i$, $i=1,\dots,k-1$ with $\lambda_i\le y_{i-1}+y_i$. Convex piecewise linear costs need no binaries (see [[BT ch1 - Introduction]]).
- **Set covering, packing, partitioning** (Ex. 10.3, p. 456-457). With the $m\times n$ incidence matrix $\mathbf A$ of subsets $M_j$ and $x_j=1$ if $M_j$ is chosen, a family is a cover, packing or partition iff
$$\mathbf A\mathbf x\ge\mathbf e,\quad\mathbf A\mathbf x\le\mathbf e,\quad\mathbf A\mathbf x=\mathbf e$$
These cover assignment, crew scheduling and vehicle routing.
- **Sequencing with setup times** (p. 457-459): a flexible machine with a tool magazine of capacity $B$; binaries $x_{ir}$ (job $i$ in position $r$), $y_{jr}$ (tool $j$ loaded) and $z_{jr}\ge|y_{jr}-y_{j,r-1}|$ linearized by two inequalities.
- **NSF fellowship allocation** (p. 459-461): a selection problem with fairness targets by gender, discipline and grade level; the "minimize the worst rank" objective becomes $\min z$ with $z\ge r_ix_i$ via the epigraph device.

## Strong formulations (§10.2, p. 461-465)
For an LP a good formulation has few variables and constraints. For integer programs the formulation itself decides how well solution methods work.

> [!definition] Definition 10.1 (p. 462)
> The linear programming relaxation of a mixed integer program is the same problem with the integrality requirement on $\mathbf x$ dropped. For zero-one variables, $x_j\in[0,1]$.

Facility location has two formulations with the same integer solutions (Examples 10.2 and 10.4, pp. 453, 462). The original (10.1) has $x_{ij}\le y_j$; the aggregate (10.2) has $\sum_ix_{ij}\le my_j$, which uses $m+n$ constraints against $m+mn$. Their relaxations satisfy $P_{FL}\subset P_{AFL}$, the inclusion possibly strict (Exercise 10.11), so (p. 463)
$$z_{AFL}\le z_{FL}\le z_{IP}$$
Many methods for integer minimization rely on lower bounds like $z_{FL}$ ([[BT ch11 - Integer programming]]), and the sharper the bound the better. In Figure 10.3 the LP optimum over $P_{FL}$ is already integer, while over $P_{AFL}$ it is fractional (p. 464).

> [!theorem] Principle (p. 465)
> The quality of a formulation of an integer program with feasible set $F$ is judged by how close the feasible set of its LP relaxation is to the convex hull of $F$. Formulation $A$ is at least as strong as $B$ if $P_A\subset P_B$.

The ideal formulation has $P=\mathrm{CH}(F)$ (Figure 10.4), then the LP optimum over $P$ is attained at an extreme point in $F$ ([[Polyhedron]], [[Convex set]]).

## Exponentially many constraints (§10.3, p. 465-472)
**Minimum spanning tree** (p. 465-469). With $x_e=1$ if edge $e$ is in the tree, $\delta(S)$ the edges leaving $S$ and $E(S)$ the edges inside $S$ (Figure 10.5, p. 467), two formulations with an exponential number of constraints are compared:
- Cutset: $\sum_{e\in\delta(S)}x_e\ge1$ for all $\emptyset\ne S\subsetneq\mathcal N$ (connectedness), with $\sum_ex_e=n-1$. Relaxation $P_{cut}$.
- Subtour elimination: $\sum_{e\in E(S)}x_e\le|S|-1$ for the same $S$, with $\sum_ex_e=n-1$. Relaxation $P_{sub}$.

> [!theorem] Theorem 10.1 (p. 467)
> (a) $P_{sub}\subset P_{cut}$, and the inclusion can be strict. (b) $P_{cut}$ can have fractional extreme points.

For (a), $\sum_{\delta(S)}x_e=(n-1)-\sum_{E(S)}x_e-\sum_{E(\mathcal N\setminus S)}x_e\ge(n-1)-(|S|-1)-(n-|S|-1)=1$. In Figure 10.6 an optimum over $P_{cut}$ is fractional with cost $3/2$ while the best tree costs $2$ (p. 468-469). In fact $P_{sub}=\mathrm{CH}(T)$ for the set $T$ of spanning trees, so it is a strong formulation although it has exponentially many constraints. Separation over $P_{sub}$ reduces to minimum cut (Example 8.2), so by Theorem 8.5 one can optimize over it in polynomial time (p. 469).

**Traveling salesman** (p. 469-470). The cutset formulation is
$$\min\ \sum_ec_ex_e$$
$$\sum_{e\in\delta(\{i\})}x_e=2\ \ \forall i$$
$$\sum_{e\in\delta(S)}x_e\ge2\ \ \forall S\ne\emptyset,\mathcal N$$
with $x_e\in\{0,1\}$. A subtour elimination version replaces the second family by $\sum_{e\in E(S)}x_e\le|S|-1$. The two relaxations are equally strong (Exercise 10.12), but neither equals the convex hull. The convex hull for the traveling salesman problem is not known (p. 472).

**Perfect matching** (p. 470-472). Degree constraints $\sum_{e\in\delta(\{i\})}x_e=1$ give a relaxation $P_{degree}$ that is not $\mathrm{CH}(M)$ (Figure 10.7: optimal matching cost $L+2$ against $3$ over $P_{degree}$). Adding the odd-set constraints
$$\sum_{e\in\delta(S)}x_e\ge1,\quad S\subset\mathcal N,\ |S|\ \text{odd}$$
with $0\le x_e\le1$ gives $P_{matching}=\mathrm{CH}(M)$ (p. 472, due to Edmonds).

**Formulations and complexity** (p. 472). The convex hull is explicitly known for spanning trees and for matchings, both polynomially solvable, and unknown for the traveling salesman problem, for which no polynomial algorithm is known. This suggests that the ability to find the strongest formulation is linked to the complexity of the problem.

## Summary (§10.4, p. 472)
Integer programming is a flexible modeling tool. Stronger formulations, even with exponentially many constraints, give better bounds; separation algorithms make them usable.

## Notes
- Wiki note: the cutset constraints are the same cut inequalities that appear in the separation example of [[BT ch8 - Complexity of LP and the ellipsoid method]] and the network cuts of [[BT ch7 - Network flows]].
- Source credits (p. 477-478): the matching convex hull result to Edmonds (1971); matching algorithms in Papadimitriou and Steiglitz (1982).

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf 467-494, printed pp. 451-478). Pages viewed as images: pdf 483; the rest read from the text layer.
**Last updated**: 2026-11-06

---

## Related pages
- [[Integer programming]] · [[Linear programming]] · [[Polyhedron]] · [[Convex set]]
- [[BT ch1 - Introduction]] · [[BT ch6 - Large scale optimization]] · [[BT ch7 - Network flows]] · [[BT ch8 - Complexity of LP and the ellipsoid method]] · [[BT ch11 - Integer programming]]
