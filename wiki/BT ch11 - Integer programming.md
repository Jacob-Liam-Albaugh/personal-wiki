---
type: paper
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 11 (printed pp. 479-531)"
tags: [optimization]
authors: ["[[Dimitris Bertsimas]]", "[[John N. Tsitsiklis]]"]
year: 1997
venue: "Athena Scientific (textbook)"
file: "Linear Optimization/MIT (ch 1-5).pdf"
---

# BT ch11 - Integer programming

**Summary**: Algorithms for integer programs and the theory behind them. Exact methods (cutting planes, branch and bound, dynamic programming), a Lagrangean duality that yields bounds, approximation algorithms with guarantees, local search heuristics (2OPT, simulated annealing), and an introduction to NP-completeness. Formulations are in [[BT ch10 - Integer programming formulations]]; see [[Integer programming]].

## Overview (p. 480)
No efficient general algorithm is known. The book groups methods into three categories:
- **Exact**: guaranteed optimal but possibly exponential (cutting planes, branch and bound, branch and cut, dynamic programming).
- **Approximation**: polynomial time with a proven bound on suboptimality.
- **Heuristic**: no guarantee on quality (local search, simulated annealing).

## Cutting plane methods (§11.1, p. 480-484)
Integer program $\min\mathbf c'\mathbf x$ s.t. $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\ge\mathbf0$ integer, with LP relaxation (11.2). Generic algorithm (p. 481):
1. Solve the LP relaxation, optimum $\mathbf x^*$.
2. If $\mathbf x^*$ is integer, stop.
3. Else add a linear inequality that every integer solution satisfies but $\mathbf x^*$ violates, and repeat.

This is the cutting plane scheme of [[BT ch6 - Large scale optimization]].

**Gomory cuts** (p. 482, image seen). Take an optimal basis $\mathbf B$ and a tableau row with fractional right side $\bar a_{i0}$, $N$ the nonbasic indices:
$$x_i+\sum_{j\in N}\bar a_{ij}x_j=\bar a_{i0}$$
Because $x_j\ge0$, replacing coefficients by their floors weakens the left side:
$$x_i+\sum_{j\in N}\lfloor\bar a_{ij}\rfloor x_j\le x_i+\sum_{j\in N}\bar a_{ij}x_j=\bar a_{i0}$$
For integer $\mathbf x$ the left side is an integer, so
$$x_i+\sum_{j\in N}\lfloor\bar a_{ij}\rfloor x_j\le\lfloor\bar a_{i0}\rfloor$$
It cuts off $\mathbf x^*$, since there $x_i^*=\bar a_{i0}$, $x_j^*=0$ on $N$ and $\lfloor\bar a_{i0}\rfloor<\bar a_{i0}$. Adding such cuts and re-solving by the dual simplex method ([[Dual simplex method]]) with anticycling rules gives a finitely terminating algorithm (Gomory, 1958), but in practice it has not been successful (p. 482).

Example 11.2 (p. 482-484): minimize $x_1-2x_2$ s.t. $-4x_1+6x_2\le9$, $x_1+x_2\le4$. The LP optimum is $(1.5,2.5)$; cuts $x_2\le2$, then $-3x_1+5x_2\le7$, give the integer optimum $(1,2)$ in three LP solves.

Deeper problem-specific cuts help, e.g. the weighted independent set problem (Example 11.3, p. 484) with clique inequalities.

## Branch and bound (§11.2, p. 485-490)
Partition the feasible set $F$ into subsets $F_1,\dots,F_k$, solve each subproblem, keep the best, recursing into a tree of subproblems (Figure 11.2). Ingredients (p. 485-486):
- A lower bound $b(F_i)$ on each subproblem, commonly the LP relaxation cost.
- An upper bound $U$, the cost of the best feasible solution found so far.
- **Pruning**: if $b(F_i)\ge U$, discard $F_i$.

At a node, solve the LP relaxation. If infeasible, prune. If the solution is integer, update $U$. If not, pick a fractional $x_i^*$ and create two subproblems with $x_i\le\lfloor x_i^*\rfloor$ and $x_i\ge\lceil x_i^*\rceil$ (p. 487). Each child adds one constraint, so the dual simplex method warm-starts from the parent's optimum.

Example 11.4 (p. 487-488) reuses the problem of Example 11.2: the tree closes after subproblems $F_1$ to $F_4$ with $U=-3$ and optimum $(1,2)$. Example 11.5 (p. 488-489) is the directed TSP, with assignment problem relaxations and branching by prohibiting an arc of a subtour. Success depends on tight lower bounds (see §11.4). Worst case is exponential (Exercise 11.4).

**Branch and cut** (p. 489-490) adds cutting planes at nodes: with deep cuts a lot of enumeration is avoided (Example 11.6, cut $-x_1+x_2\le1$).

## Dynamic programming (§11.3, p. 490-493)
Exact method that solves integer programs by stages. Guidelines (p. 491):
1. View the solution as a sequence of decisions in stages, total cost the sum of decision costs.
2. Define the state as a summary of all relevant past decisions.
3. Determine the possible state transitions and their costs.
4. Write a recursion for the optimal cost from origin to destination state.

The crucial step is the definition of the state. Example 11.7 (p. 490) does this for the traveling salesman problem.

**Zero-one knapsack** (p. 491-493). Let $W_i(u)$ be the least weight needed to accumulate value $u$ using only the first $i$ items. Then (eq. 11.4, p. 491-492, read from text)
$$W_{i+1}(u)=\min\{W_i(u),\ W_i(u-c_{i+1})+w_{i+1}\}$$
This is the Bellman equation of a shortest path problem in a graph of states $(i,u)$ ([[BT ch7 - Network flows]]). With $c_{\max}=\max_jc_j$ only $u\le nc_{\max}$ matters, giving $O(n^2c_{\max})$ states and time.

> [!theorem] Theorem 11.1 (p. 493)
> The zero-one knapsack problem can be solved in time $O(n^2c_{\max})$.

This is pseudopolynomial, since it depends on the size of the numbers, and the scaling idea in §11.5 builds on it.

## Integer programming duality (§11.4, p. 494-506)
Setting (11.5), image seen p. 494. The problem is
$$\min\ \mathbf c'\mathbf x$$
$$\mathbf A\mathbf x\ge\mathbf b,\quad\mathbf D\mathbf x\ge\mathbf d,\quad\mathbf x\ \text{integer}$$
Let $X=\{\mathbf x\ \text{integer}\mid\mathbf D\mathbf x\ge\mathbf d\}$, a set that is easy to optimize over (e.g. assignment). Dualize the hard constraints $\mathbf A\mathbf x\ge\mathbf b$ with multipliers $\mathbf p\ge\mathbf0$ (eq. 11.6):
$$Z(\mathbf p)=\min_{\mathbf x\in X}\ \big(\mathbf c'\mathbf x+\mathbf p'(\mathbf b-\mathbf A\mathbf x)\big)$$

> [!theorem] Lemma 11.1 (p. 494)
> If (11.5) has an optimal solution and $\mathbf p\ge\mathbf0$, then $Z(\mathbf p)\le Z_{IP}$.

Proof idea: at an optimal $\mathbf x^*$, $\mathbf b-\mathbf A\mathbf x^*\le\mathbf0$ and $\mathbf x^*\in X$. The best bound is the **Lagrangean dual** (11.7)
$$Z_D=\max_{\mathbf p\ge\mathbf0}Z(\mathbf p)$$
$Z(\mathbf p)$ is a minimum of finitely many linear functions of $\mathbf p$, so it is concave and piecewise linear (Figure 11.6, p. 495). Weak duality $Z_D\le Z_{IP}$ is Theorem 11.2; unlike [[LP duality]] there is no strong duality in general (p. 495-496, Example 11.8). The method of obtaining bounds this way is called Lagrangean relaxation.

**Strength of the bound** (p. 496-497, images seen).

> [!theorem] Theorem 11.3 (p. 496)
> If $\mathbf D\mathbf x\ge\mathbf d$ is feasible and $\mathbf D,\mathbf d$ have integer entries, then $\mathrm{CH}(X)$ is a polyhedron.

> [!theorem] Theorem 11.4 (p. 496)
> $Z_D$ equals the optimal cost of the LP
> $$\min\ \mathbf c'\mathbf x\quad\text{s.t.}\ \mathbf A\mathbf x\ge\mathbf b,\ \mathbf x\in\mathrm{CH}(X)$$

The proof swaps $X$ for $\mathrm{CH}(X)$ in $Z(\mathbf p)$, writes $\mathrm{CH}(X)$ via extreme points and extreme rays ([[Polyhedron]]) and applies LP duality (p. 496-497). Consequently (p. 499)
$$Z_{LP}\le Z_D\le Z_{IP}$$
Example 11.8 (p. 498-500): minimizing $3x_1-x_2$ with the first constraint relaxed gives $Z_D=-1/3$ at $p=5/3$, against $Z_{LP}=-9/5$ and $Z_{IP}=1$. Corollary 11.1 (p. 500): (a) $Z_{IP}=Z_D$ for all costs iff $\mathrm{CH}(X\cap\{\mathbf A\mathbf x\ge\mathbf b\})=\mathrm{CH}(X)\cap\{\mathbf A\mathbf x\ge\mathbf b\}$; (b) $Z_{LP}=Z_D$ for all costs if $\mathrm{CH}(X)=\{\mathbf D\mathbf x\ge\mathbf d\}$.

The **Held-Karp bound** (Example 11.10, p. 501-502) is the Lagrangean dual of the subtour-elimination TSP formulation of [[BT ch10 - Integer programming formulations]], with $Z_D=Z_{LP}$ by Corollary 11.1(b). $Z(\mathbf p)$ is computed through minimum 1-trees.

**Subgradient optimization** (p. 502-507). $Z(\mathbf p)$ is concave but not differentiable, so steepest ascent is replaced by subgradients (a vector $\mathbf s$ with $Z(\mathbf q)\le Z(\mathbf p)+\mathbf s'(\mathbf q-\mathbf p)$ for all $\mathbf q$, Lemma 11.4). The subdifferential at $\mathbf p$ is the convex hull of the gradients of the active pieces (Figure 11.11, Exercise 11.10). The algorithm (p. 505):
1. Choose $\mathbf p^1$, $t=1$.
2. Pick a subgradient $\mathbf s^t$ at $\mathbf p^t$; if $\mathbf s^t=\mathbf0$ stop.
3. Set $\mathbf p^{t+1}=\mathbf p^t+\theta_t\mathbf s^t$, $t\leftarrow t+1$.

The stepsize is typically $\theta_t=\alpha_t(\hat Z_D-Z(\mathbf p^t))/\|\mathbf s^t\|^2$ with $0<\alpha_t<1$ and $\hat Z_D$ an estimate of $Z_D$ (p. 505-506, read from text, **[unverified]** exact form). To keep $\mathbf p\ge\mathbf0$ the update is projected onto the nonnegative orthant. Convergence is not monotone (Table 11.1). Compare [[Gradient descent]].

## Approximation algorithms (§11.5, p. 507-510)
An $\epsilon$-approximation algorithm runs in polynomial time and, for every instance, returns a feasible solution whose relative error from the optimum is at most $\epsilon$ (Definition 11.2, p. 507, read from text).
- **Knapsack** (p. 507-509): scale the profits by dropping the $t$ least significant digits and run the exact algorithm of Theorem 11.1 on the scaled instance. Theorem 11.5: for every $\epsilon>0$ there is an $\epsilon$-approximation algorithm running in $O(n^3/\epsilon)$. A family with this property is a polynomial time approximation scheme (PTAS), here even fully polynomial.
- **Metric TSP with triangle inequality** (p. 509-510): find a minimum spanning tree of cost $L$, walk it using each edge twice (cost $2L$) and shortcut repeated nodes by the triangle inequality. The tour costs at most $2L$, and the optimal tour costs at least $L$ (delete an edge from it to get a spanning tree), so this is a 1-approximation (error at most 100 percent). Exercise 11.14 improves it to 1/2 with a matching of odd-degree nodes (Christofides' idea).

It is not known which problem structure allows arbitrarily good, fixed or no approximation (p. 510).

## Local search (§11.6, p. 511-512)
Start at feasible $\mathbf x$, move to a neighbor with lower cost, stop at a local optimum. For TSP, 2OPT swaps two edges (Figure 11.13) and 3OPT three (Figure 11.14, $O(n^3)$ neighbors). A neighbor's cost update takes $O(1)$ arithmetic. Trade-off (p. 512): larger neighborhoods have fewer local minima but cost more per step. Local search can be restarted from many starting points.

## Simulated annealing (§11.7, p. 512-514)
Pick a random neighbor $\mathbf y$ of $\mathbf x$ with probability $q_{xy}$. Accept it with probability 1 if $c(\mathbf y)\le c(\mathbf x)$, and with probability $e^{-(c(\mathbf y)-c(\mathbf x))/T}$ otherwise (p. 513). Temperature $T$ controls uphill moves. The state evolves as a Markov chain with stationary distribution (eq. 11.14, p. 513)
$$\pi(\mathbf x)=\frac{e^{-c(\mathbf x)/T}}{A},\qquad A=\sum_{\mathbf z\in F}e^{-c(\mathbf z)/T}$$
shown by detailed balance (p. 513-514), assuming a symmetric irreducible neighborhood. As $T$ falls the mass concentrates on optima, and in practice $T$ is lowered gradually (cooling schedule).

## Complexity theory (§11.8, p. 514-522)
- Classes: **P** (polynomial time) and **NP** (YES instances have certificates checkable in polynomial time, p. 520).
- **Reduction** (Def. 11.4, p. 516): $\Pi_1$ transforms to $\Pi_2$ if a polynomial algorithm maps instances so YES maps to YES. Theorem 11.7: if $\Pi_1$ reduces to $\Pi_2$ and $\Pi_2\in P$ then $\Pi_1\in P$.
- Optimization, evaluation and recognition versions of a problem are equivalent in difficulty (p. 517).
- **NP-hard / NP-complete** (Def. 11.7, p. 519): $\Pi$ is NP-complete if it is in NP and every NP problem (via zero-one integer programming, ZOIP, in this book's definition) transforms to it. A polynomial algorithm for any NP-complete problem would give $P=NP$ (Figure 11.15).
- Proving hardness of a problem means reducing a known hard problem to it, "mostly an art" (p. 521). The ATSP is shown hard by such a transformation (p. 521).
- NP-hardness does not mean give up (p. 522): approximation, heuristics, special cases and exact methods for moderate sizes all remain.

The linear programming problem is in P ([[BT ch8 - Complexity of LP and the ellipsoid method]]), whereas ZOIP is NP-hard.

## Summary and notes (§11.9-11.11, p. 522-531)
Other methods not covered: genetic algorithms, tabu search, interior point methods for integer programming. All existing algorithms either need exponential time in the worst case or give approximate solutions (p. 523). Notes credit Gomory (cuts), Land and Doig (branch and bound), Kirkpatrick, Gelatt and Vecchi (1983, annealing), Cook, Levin and Karp (NP-completeness) (p. 530-531).

## Notes
- Wiki note: Lagrangean relaxation and the Dantzig-Wolfe master are two views of the same convexified problem (Theorem 11.4 and [[BT ch6 - Large scale optimization]]); Theorem 11.4 is the integer analogue of strong duality only after replacing $X$ by $\mathrm{CH}(X)$.
- Wiki note: subgradient steps for a concave dual function are plain projected [[Gradient descent]] with nonsmooth steps.

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf 495-548, printed pp. 479-532). Pages viewed as images: pdf 498, 510, 512. All other equations and statements read from the text layer and marked where uncertain.
**Last updated**: 2026-11-06

---

## Related pages
- [[Integer programming]] · [[Linear programming]] · [[LP duality]] · [[Polyhedron]] · [[Dual simplex method]]
- [[BT ch6 - Large scale optimization]] · [[BT ch7 - Network flows]] · [[BT ch8 - Complexity of LP and the ellipsoid method]] · [[BT ch10 - Integer programming formulations]]
- [[Gradient descent]]
