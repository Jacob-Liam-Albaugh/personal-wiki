---
type: concept
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 10-11"
tags: [optimization]
---

# Integer programming

> [!definition] Mixed integer program (source: MIT (ch 1-5).pdf, p. 452)
> A discrete optimization problem seeks $\mathbf x^*$ in a discrete set $F$ optimizing $c(\mathbf x)$. The mixed integer programming problem is
> $$\min\ \mathbf c'\mathbf x+\mathbf d'\mathbf y$$
> $$\mathbf A\mathbf x+\mathbf B\mathbf y=\mathbf b,\quad\mathbf x,\mathbf y\ge\mathbf0,\quad\mathbf x\ \text{integer}$$
> If all variables are integer it is a pure integer program, and a zero-one program if restricted to $\{0,1\}$.

**Intuition**: a [[Linear programming]] problem with integrality constraints. The LP relaxation, obtained by dropping integrality, gives a lower bound that the exact methods improve on. No efficient general algorithm is known; BT group methods as **exact** (guaranteed optimal, possibly exponential: cutting planes, branch and bound, branch and cut, dynamic programming), **approximation** (polynomial time with a proven bound on suboptimality) and **heuristic** (no guarantee) (BT p. 480).

## Modeling techniques (BT §10.1, pp. 452-461)
- **Zero-one knapsack** (Ex. 10.1): maximize $\sum c_jx_j$ s.t. $\sum w_jx_j\le K$, $x_j\in\{0,1\}$. The unbounded version appears as the pricing problem of the cutting stock problem ([[Column generation]]).
- **Forcing constraints**: "A only if B" is $x_A\le x_B$. In facility location (Ex. 10.2) $x_{ij}\le y_j$ says client $i$ is served at $j$ only if a facility is open there. Relations between variables: $\sum x_j\le1$ means at most one, $\sum x_j=1$ exactly one.
- **Disjunctive constraints**: to require at least one of $\mathbf a'\mathbf x\ge b$ and $\mathbf c'\mathbf x\ge d$ (nonnegative coefficients, $\mathbf x\ge\mathbf0$) add a binary $y$:
$$\mathbf a'\mathbf x\ge yb,\quad\mathbf c'\mathbf x\ge(1-y)d,\quad y\in\{0,1\}$$
- **Arbitrary piecewise linear cost** (pp. 455-456). For breakpoints $a_1<\dots<a_k$ write $x=\sum\lambda_ia_i$ with $\lambda\ge0$, $\sum\lambda_i=1$. The representation is unique if at most two consecutive $\lambda_i$ are nonzero, enforced by binaries $y_i$, $i=1,\dots,k-1$ with $\lambda_i\le y_{i-1}+y_i$. Convex piecewise linear costs need no binaries ([[Linear programming]]).
- **Set covering, packing, partitioning** (Ex. 10.3, pp. 456-457). With the $m\times n$ incidence matrix $\mathbf A$ of subsets $M_j$ and $x_j=1$ if $M_j$ is chosen, a family is a cover, packing or partition iff $\mathbf A\mathbf x\ge\mathbf e$, $\mathbf A\mathbf x\le\mathbf e$, $\mathbf A\mathbf x=\mathbf e$. They cover assignment, crew scheduling and vehicle routing.
- **Sequencing with setup times** (pp. 457-459): a flexible machine with tool magazine capacity $B$; binaries $x_{ir}$ (job $i$ in position $r$), $y_{jr}$ (tool $j$ loaded) and $z_{jr}\ge|y_{jr}-y_{j,r-1}|$ linearized by two inequalities.
- **NSF fellowship allocation** (pp. 459-461): a selection problem with fairness targets by gender, discipline and grade level; "minimize the worst rank" becomes $\min z$ with $z\ge r_ix_i$ (epigraph device).

## Strong formulations (BT §10.2, pp. 461-465)
For an LP a good formulation has few variables and constraints; for integer programs the formulation decides how well solution methods work.

> [!definition] Definition 10.1 (p. 462)
> The LP relaxation of a mixed integer program is the same problem with integrality on $\mathbf x$ dropped; for zero-one variables, $x_j\in[0,1]$.

Facility location has two formulations with the same integer solutions (Examples 10.2 and 10.4). The original has $x_{ij}\le y_j$; the aggregate has $\sum_ix_{ij}\le my_j$, with $m+n$ constraints against $m+mn$. Their relaxations satisfy $P_{FL}\subset P_{AFL}$, possibly strictly (Exercise 10.11), so
$$z_{AFL}\le z_{FL}\le z_{IP}$$
Many methods rely on lower bounds like $z_{FL}$ and the sharper the better. In BT Fig. 10.3 the LP optimum over $P_{FL}$ is already integer while over $P_{AFL}$ it is fractional (p. 464).

> [!theorem] Principle (p. 465)
> The quality of a formulation with feasible set $F$ is judged by how close the feasible set of its LP relaxation is to the convex hull of $F$. Formulation $A$ is at least as strong as $B$ if $P_A\subset P_B$.

The ideal has $P=\mathrm{CH}(F)$; then the LP optimum is attained at an extreme point in $F$ ([[Polyhedron]], [[Convex set]]).

## Exponentially many constraints (BT §10.3, pp. 465-472)
**Minimum spanning tree** (pp. 465-469). With $x_e=1$ if edge $e$ is in the tree, $\delta(S)$ the edges leaving $S$ and $E(S)$ the edges inside:
- Cutset: $\sum_{e\in\delta(S)}x_e\ge1$ for all $\emptyset\ne S\subsetneq\mathcal N$, with $\sum_ex_e=n-1$. Relaxation $P_{cut}$.
- Subtour elimination: $\sum_{e\in E(S)}x_e\le|S|-1$, same $S$, with $\sum_ex_e=n-1$. Relaxation $P_{sub}$.

> [!theorem] Theorem 10.1 (p. 467)
> (a) $P_{sub}\subset P_{cut}$, possibly strictly. (b) $P_{cut}$ can have fractional extreme points.

For (a), $\sum_{\delta(S)}x_e=(n-1)-\sum_{E(S)}x_e-\sum_{E(\mathcal N\setminus S)}x_e\ge(n-1)-(|S|-1)-(n-|S|-1)=1$. In BT Fig. 10.6 an optimum over $P_{cut}$ is fractional with cost $3/2$ while the best tree costs $2$. In fact $P_{sub}=\mathrm{CH}(T)$ for the set $T$ of spanning trees, a strong formulation despite exponentially many constraints: separation over $P_{sub}$ reduces to minimum cut, so by the ellipsoid method ([[Ellipsoid method]]; BT Thm 8.5) one can optimize over it in polynomial time (p. 469). The greedy Prim algorithm solves the problem directly ([[Shortest path problem]]).

**Traveling salesman** (pp. 469-470). Cutset formulation
$$\min\ \sum_ec_ex_e\quad\text{s.t. }\sum_{e\in\delta(\{i\})}x_e=2\ \forall i,\quad\sum_{e\in\delta(S)}x_e\ge2\ \forall S\ne\emptyset,\mathcal N,\quad x_e\in\{0,1\}$$
A subtour elimination version replaces the second family by $\sum_{e\in E(S)}x_e\le|S|-1$. The two relaxations are equally strong (Exercise 10.12), neither equals the convex hull, and the hull is not known (p. 472).

**Perfect matching** (pp. 470-472). Degree constraints $\sum_{e\in\delta(\{i\})}x_e=1$ give a relaxation $P_{degree}$ that is not $\mathrm{CH}(M)$ (Fig. 10.7: optimal matching cost $L+2$ against $3$ over $P_{degree}$). Adding odd-set constraints
$$\sum_{e\in\delta(S)}x_e\ge1,\quad S\subset\mathcal N,\ |S|\text{ odd}$$
with $0\le x_e\le1$ gives $P_{matching}=\mathrm{CH}(M)$ (Edmonds, 1971). The convex hull is known for spanning trees and matchings, both polynomially solvable, and unknown for the TSP, for which no polynomial algorithm is known; this suggests that finding the strongest formulation is linked to complexity (p. 472). The cut inequalities are those of network cuts ([[Maximum flow problem]]). The bipartite special case is the [[Assignment problem]], whose LP is already integral.

## Exact methods (BT §11.1-11.3, pp. 480-493)
**Cutting planes** (pp. 480-484). Solve the LP relaxation; if $\mathbf x^*$ is integer stop, else add a linear inequality satisfied by all integer solutions but violated by $\mathbf x^*$, and repeat (generic scheme of [[Cutting-plane methods]]; the LP-side dual view is in [[Column generation]]). **Gomory cuts**: take an optimal basis and a tableau row with fractional right side $\bar a_{i0}$, $N$ the nonbasic indices:
$$x_i+\sum_{j\in N}\bar a_{ij}x_j=\bar a_{i0}$$
Since $x_j\ge0$, replacing coefficients by floors weakens the left side, and for integer $\mathbf x$ the left side is an integer, so
$$x_i+\sum_{j\in N}\lfloor\bar a_{ij}\rfloor x_j\le\lfloor\bar a_{i0}\rfloor$$
It cuts off $\mathbf x^*$ since $x_i^*=\bar a_{i0}$, $x_j^*=0$ on $N$ and $\lfloor\bar a_{i0}\rfloor<\bar a_{i0}$. Adding such cuts and re-solving by the [[Dual simplex method]] with anticycling rules terminates finitely (Gomory, 1958) but has not been successful in practice (p. 482). Example 11.2 (pp. 482-484): minimize $x_1-2x_2$ s.t. $-4x_1+6x_2\le9$, $x_1+x_2\le4$; the LP optimum is $(1.5,2.5)$ and cuts $x_2\le2$, then $-3x_1+5x_2\le7$, give the integer optimum $(1,2)$ in three LP solves. Problem-specific cuts help, e.g. clique inequalities for weighted independent set (Example 11.3, p. 484).

**Branch and bound / branch and cut**: see [[Branch and bound]].

**Dynamic programming** (§11.3, pp. 490-493). Guidelines: (1) view the solution as a sequence of decisions in stages, cost the sum of decision costs; (2) define the state as a summary of all relevant past decisions (the crucial step; Example 11.7 does it for the TSP); (3) determine state transitions and costs; (4) write a recursion for the optimal cost from origin to destination state. For the **zero-one knapsack** let $W_i(u)$ be the least weight needed to accumulate value $u$ using the first $i$ items:
$$W_{i+1}(u)=\min\{W_i(u),\ W_i(u-c_{i+1})+w_{i+1}\}$$
(eq. 11.4, read from text). This is the Bellman equation of a shortest path problem in a graph of states $(i,u)$ ([[Shortest path problem]]). With $c_{\max}=\max_jc_j$ only $u\le nc_{\max}$ matters.

> [!theorem] Theorem 11.1 (p. 493)
> The zero-one knapsack problem can be solved in time $O(n^2c_{\max})$.

Pseudopolynomial, since it depends on the size of the numbers; the scaling idea below builds on it.

## Lagrangean duality (BT §11.4, pp. 494-507)
Relaxing hard constraints gives the bound $Z_{LP}\le Z_D\le Z_{IP}$, optimized by subgradients; with no strong duality in general. Full treatment, including the Held-Karp TSP bound, on [[Lagrangian relaxation]] (see also [[Lagrangian duality]], [[Subgradient method]]).

## Approximation algorithms (BT §11.5, pp. 507-510)
An $\epsilon$-approximation algorithm runs in polynomial time and returns for every instance a feasible solution with relative error at most $\epsilon$ (Def. 11.2, p. 507).
- **Knapsack** (pp. 507-509): scale profits by dropping the $t$ least significant digits and run the exact algorithm of Theorem 11.1 on the scaled instance. Theorem 11.5: for every $\epsilon>0$ there is an $\epsilon$-approximation running in $O(n^3/\epsilon)$; a family with this property is a polynomial time approximation scheme (PTAS), here fully polynomial.
- **Metric TSP** (pp. 509-510): take a minimum spanning tree of cost $L$, walk it using each edge twice (cost $2L$) and shortcut repeated nodes via the triangle inequality. The tour costs at most $2L$ and the optimal tour at least $L$ (delete an edge from it to get a spanning tree), so this is a 1-approximation (error at most 100 percent). Exercise 11.14 improves it to $1/2$ with a matching of odd-degree nodes (Christofides' idea).

It is not known which structure allows arbitrarily good, fixed or no approximation (p. 510).

## Local search and simulated annealing (BT §11.6-11.7, pp. 511-514)
- **Local search**: start at feasible $\mathbf x$, move to a neighbor of lower cost, stop at a local optimum. For TSP, 2OPT swaps two edges (Fig. 11.13) and 3OPT three (Fig. 11.14, $O(n^3)$ neighbors); a neighbor's cost update takes $O(1)$. Larger neighborhoods have fewer local minima but cost more per step. Local search can be restarted from many starting points.
- **Simulated annealing**: pick a random neighbor $\mathbf y$ of $\mathbf x$ with probability $q_{xy}$; accept with probability $1$ if $c(\mathbf y)\le c(\mathbf x)$ and with probability $e^{-(c(\mathbf y)-c(\mathbf x))/T}$ otherwise (p. 513). The state is a Markov chain with stationary distribution (eq. 11.14)
$$\pi(\mathbf x)=\frac{e^{-c(\mathbf x)/T}}{A},\qquad A=\sum_{\mathbf z\in F}e^{-c(\mathbf z)/T}$$
  shown by detailed balance (pp. 513-514) for a symmetric irreducible neighborhood. As $T$ falls the mass concentrates on optima; in practice $T$ is lowered gradually (cooling schedule). Compare the Metropolis acceptance rule in [[Markov chain Monte Carlo]].

## Complexity theory (BT §11.8, pp. 514-522)
- **P** (polynomial time) and **NP** (YES instances have certificates checkable in polynomial time, p. 520).
- **Reduction** (Def. 11.4, p. 516): $\Pi_1$ transforms to $\Pi_2$ if a polynomial algorithm maps instances so YES maps to YES. Theorem 11.7: if $\Pi_1$ reduces to $\Pi_2$ and $\Pi_2\in P$ then $\Pi_1\in P$.
- Optimization, evaluation and recognition versions of a problem are equivalent in difficulty (p. 517).
- **NP-hard / NP-complete** (Def. 11.7, p. 519): $\Pi$ is NP-complete if it is in NP and every NP problem (via zero-one integer programming, ZOIP, in the book's definition) transforms to it. A polynomial algorithm for any NP-complete problem would give $P=NP$ (Fig. 11.15).
- Proving hardness means reducing a known hard problem to it, "mostly an art" (p. 521); the ATSP is shown hard this way. NP-hardness does not mean give up (p. 522): approximation, heuristics, special cases and exact methods for moderate sizes all remain.
- LP is in P ([[Ellipsoid method]]) whereas ZOIP is NP-hard.

## Summary and notes (BT §11.9-11.11, pp. 522-531)
Not covered: genetic algorithms, tabu search, interior point methods for integer programming. All existing algorithms need exponential time in the worst case or give approximate solutions (p. 523). Credits: Gomory (cuts), Land and Doig (branch and bound), Kirkpatrick, Gelatt and Vecchi (1983, annealing), Cook, Levin and Karp (NP-completeness) (pp. 530-531), Edmonds (matching hull, BT pp. 477-478).

**Covered in**: Bertsimas-Tsitsiklis ch. 10 (pp. 452-472) and ch. 11 (pp. 480-531)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 10-11; pdf 467-548, pdf 483, 498, 510, 512 viewed as images, rest from text layer).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[LP duality]] · [[Dual simplex method]] · [[Network flow problem]] · [[Polyhedron]] · [[Convex function]]
- [[Branch and bound]] · [[Cutting-plane methods]] · [[Lagrangian relaxation]] · [[Column generation]] · [[Assignment problem]] · [[Dantzig-Wolfe decomposition]]
