---
type: paper
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 7 (printed pp. 265-358)"
tags: [optimization]
authors: ["[[Dimitris Bertsimas]]", "[[John N. Tsitsiklis]]"]
year: 1997
venue: "Athena Scientific (textbook)"
file: "Linear Optimization/MIT (ch 1-5).pdf"
---

# BT ch7 - Network flows

**Summary**: Formulates the minimum cost network flow problem as an [[Linear programming|LP]] with a node-arc incidence matrix, specializes the [[Simplex method]] to spanning trees (network simplex), then gives combinatorial algorithms for special cases: negative cost cycles, maximum flow (Ford-Fulkerson, max-flow min-cut), dual ascent, assignment (auction), shortest paths and minimum spanning trees. See [[Network flow problem]].

## Formulation (§7.2, p. 272-278)
A network is a directed graph $G=(\mathcal N,\mathcal A)$ with supply $b_i$ at node $i$ (source if $b_i>0$, sink if $b_i<0$), arc capacities $u_{ij}$ and unit costs $c_{ij}$ (p. 272). Flow conservation and capacity (eqs. 7.1-7.2, p. 272):
$$b_i+\sum_{j\in I(i)}f_{ji}=\sum_{j\in O(i)}f_{ij}\quad\forall i\in\mathcal N$$
$$0\le f_{ij}\le u_{ij}\quad\forall(i,j)\in\mathcal A$$
Summing the first over all nodes forces $\sum_ib_i=0$. Minimize $\sum c_{ij}f_{ij}$. In matrix form $\mathbf A\mathbf f=\mathbf b$ with $\mathbf A$ the node-arc incidence matrix. With $u_{ij}=\infty$ the problem is uncapacitated and in standard form (p. 273).

Special cases (p. 273-276): shortest path, maximum flow, transportation problem ($m$ suppliers, $n$ consumers, total supply equals total demand), assignment, and others. Redundancy: one flow-conservation row can be dropped, since the rows sum to zero (p. 277-278).

**Circulations** (p. 278): any $\mathbf f$ with $\mathbf A\mathbf f=\mathbf0$ is a circulation. A cycle $C$ with forward arcs $F$ and backward arcs $B$ gives a simple circulation $\mathbf h^C$ ($+1$ on $F$, $-1$ on $B$, $0$ elsewhere), with $\mathbf A\mathbf h^C=\mathbf0$ (eq. 7.3). Its cost is
$$\mathbf c'\mathbf h^C=\sum_{(i,j)\in F}c_{ij}-\sum_{(i,j)\in B}c_{ij}$$
Pushing $\theta$ units around $C$ changes the cost by $\theta$ times this.

## Graph theory background (§7.1, p. 265-271)
Directed and undirected graphs, paths, cycles, trees. Theorems 7.1-7.2 (p. 270-271) state basic tree facts, including that a connected graph with $n$ nodes contains a spanning tree and that any acyclic arc set extends to one.

## Network simplex (§7.3, p. 280-291)
- A flow is a **tree solution** if it can be built from a forest of arcs with other arcs at zero flow (Def. 7.1, p. 280).
- Theorem 7.3 and Corollary 7.1 (p. 281-282): $n-1$ arcs forming a tree give linearly independent columns, and for a connected graph $\mathbf A$ has rank $n-1$.
- Theorem 7.4 (p. 283): a flow vector is a basic solution if and only if it is a tree solution. Basic variables = tree arcs.
- Because the basis matrix is a tree, basic flows and dual prices $p_i$ are computed by back-substitution from the root (eq. 7.10).
- Reduced cost of arc $(i,j)$ is $c_{ij}-(p_i-p_j)$.
- Capacitated version (p. 291): partition non-tree arcs into $D$ (flow $0$) and $U$ (flow $u_{ij}$). Optimal when reduced costs are $\ge0$ on $D$ and $\le0$ on $U$. Otherwise a violating arc closes a unique cycle with the tree; choose orientation, push $\theta^*$ (eq. 7.11) around it, and pivot.
- Integrality: Theorem 7.5 and Corollary 7.2 (p. 289-290): if supplies and capacities are integers, there is an integer optimal flow (for uncapacitated, standard form).

## Negative cost cycle algorithm (§7.4, p. 291-300)
Start from a feasible flow. If the residual network has a negative cost cycle, push the largest feasible $\delta(C)$ units around it. Stop when none exists.

> [!theorem] Theorem 7.6 (p. 298)
> A feasible flow is optimal if and only if there is no negative cost cycle in its residual network.

Lemma 7.1 (flow decomposition, p. 298): a nonzero circulation $\mathbf f\ge\mathbf0$ decomposes into positive-flow cycles.

Theorem 7.7 (p. 300): with integer capacities and an integer starting flow the algorithm keeps integer flows and stops after finitely many iterations if the optimal cost is finite. With non-integer capacities, termination is not guaranteed unless cycles are chosen by special rules (p. 301).

## Maximum flow (§7.5, p. 301-312)
Find the largest value $v$ of flow from source $s$ to sink $t$. It is the minimum cost flow problem with zero costs plus a return arc $(t,s)$ of infinite capacity and cost $-1$ (Figure 7.20, p. 303). Application: preemptive scheduling (Example 7.4, p. 302).

**Ford-Fulkerson algorithm** (box, p. 305):
1. Start with a feasible flow.
2. Search for an augmenting path $P$ (labeling algorithm).
3. If none exists, stop.
4. If $\delta(P)<\infty$ push $\delta(P)$ units and repeat; if $\delta(P)=\infty$ stop (unbounded).

Theorem 7.8 (p. 305): with integer or infinite capacities and an integer start, flows stay integer and the algorithm terminates after finitely many steps when the maximum value is finite. Example 7.5 (p. 305): four augmentations give value $6$, equal to the capacity out of $s$. Rational capacities also terminate by scaling (p. 305). Theorem 7.9 (p. 309): the labeling algorithm runs in time linear in $|\mathcal A|$.

A cut is a set $S$ with $s\in S$, $t\notin S$ with capacity $C(S)$ (sum of capacities of arcs leaving $S$). Every flow value satisfies (eq. 7.14, p. 310)
$$v\le C(S)$$

> [!theorem] Theorem 7.10 (p. 310)
> (a) If Ford-Fulkerson stops because no augmenting path exists, the flow is optimal. (b) Max-flow min-cut: the maximum flow value equals the minimum cut capacity.

Proof of (a): take $S$ = labeled nodes at termination; arcs out of $S$ are saturated and arcs into $S$ carry zero, so the flow equals $C(S)$. The theorem also follows from LP duality (Exercise 7.20, p. 312).

Complexity (p. 312): with finite capacities bounded by $U$, at most $|\mathcal A|U$ augmentations at $O(|\mathcal A|)$ each, so $O(|\mathcal A|^2U)$. This depends linearly on $U$; capacity scaling (Exercise 7.25) gives a bound in $\log U$.

## Duality in network flows (§7.6, p. 312-315)
Dual variable $p_i$ per node. For the uncapacitated problem the dual is feasible when $p_i-p_j\le c_{ij}$ on every arc. A dual price is a sensitivity: with the same basis, raising $b_i$ by $\varepsilon$ and lowering $b_n$ by $\varepsilon$ costs $\varepsilon p_i$ (p. 314). Shipping one more unit from $i$ to $j$ costs $p_i-p_j$ in the absence of degeneracy (p. 314). Compare [[BT ch4 - Duality theory]] and [[BT ch5 - Sensitivity analysis]].

Complementary slackness (Theorem 7.11, p. 314-315): if $f_{ij}>0$ then $p_i-p_j=c_{ij}$ (and for capacitated problems the pair $(p_i-p_j,f_{ij})$ lies on a piecewise relation, Figure 7.26). Circuit analogy (p. 315): flow = current, $b_i$ = injected current (Kirchhoff's current law), $p_i$ = potential; optimal $(\mathbf f,\mathbf p)$ is an equilibrium of a circuit whose elements follow the relation of Figure 7.26.

## Dual ascent and the assignment problem (§7.7-7.8, p. 316-329)
Dual ascent methods keep flows non-negative but allow flow conservation to be violated, changing node prices to raise the dual cost (p. 324). The **auction algorithm** (§7.8, p. 325) solves the assignment problem by changing the price of one node at a time. A single-node move can temporarily lower the dual cost; if the loss is kept small the method still makes progress, and it can be viewed as approximate dual ascent (p. 325). The detailed convergence results were not read from page images. **[unverified]**

## Shortest paths (§7.9, p. 332-343)
Graph with arc lengths $c_{ij}$, possibly negative. If a negative length cycle exists, walks can have length approaching $-\infty$; otherwise a shortest path is also a shortest walk and has at most $n-1$ arcs (p. 333). Bellman's equation: with $p_i$ = shortest length from $i$ to destination $n$,
$$p_i=\min_{j\in O(i)}\{c_{ij}+p_j\}$$
Its solution is the largest solution of the equation when there is no negative cycle (Figure 7.32, p. 337).

**Bellman-Ford** (p. 337): let $p_i(t)$ be the shortest walk length from $i$ to $n$ using at most $t$ arcs, $p_n(t)=0$, $p_i(0)=\infty$ for $i\ne n$:
$$p_i(t+1)=\min_{k\in O(i)}\{c_{ik}+p_k(t)\}$$
With no negative cycles $p_i(n-1)=p_i^*$, and $p_i(n)\ne p_i(n-1)$ for some $i$ exposes a negative cycle by tracing successors (p. 338-339).

**Label correcting methods** (p. 339): keep a label $p_j$ and a list $S$ of nodes whose labels dropped. Remove $j\in S$, and for each arc $(i,j)$ set $p_i:=\min\{p_i,c_{ij}+p_j\}$, adding $i$ to $S$ if it improved. Dijkstra's algorithm is the nonnegative-length case.

**All pairs** (p. 343): from Bellman's equation $p_i\le c_{ij}+p_j$, so re-weighting $\hat c_{ij}=c_{ij}+p_j-p_i\ge0$ preserves shortest paths (eq. 7.21). One Bellman-Ford run plus $n-1$ Dijkstra runs gives $O(n^3)$ against $O(n^4)$ for repeated Bellman-Ford.

## Minimum spanning tree (§7.10, p. 343-345)
Not a network flow problem but graph-structured. **Greedy (Prim) algorithm** (p. 344): start with a single node. While the tree has fewer than $n$ nodes, add a cheapest edge joining a tree node to a non-tree node. No cycle ever forms, and the result is a minimum spanning tree (proved via a stronger property, p. 344). It serves as a subroutine for a traveling salesman heuristic in [[BT ch11 - Integer programming]] (p. 344).

## Notes
- Wiki note: the unimodularity behind the integrality results is stated for incidence matrices; the connection to totally unimodular matrices is developed in [[BJS ch9 - Minimal cost network flows]] and [[BJS ch10 - Transportation and assignment problems]].
- Source credits: negative cost cycle algorithm to Klein (1967); Bellman-Ford to Ford (1956) and Bellman (notes, p. 357-358).

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf 281-374, printed pp. 265-358).
**Last updated**: 2026-11-06

---

## Related pages
- [[Network flow problem]] · [[Linear programming]] · [[Simplex method]] · [[LP duality]]
- [[BT ch3 - The simplex method]] · [[BT ch4 - Duality theory]] · [[BT ch5 - Sensitivity analysis]] · [[BT ch6 - Large scale optimization]] · [[BT ch11 - Integer programming]]
- [[BJS ch9 - Minimal cost network flows]] · [[BJS ch10 - Transportation and assignment problems]] · [[BJS ch11 - The out-of-kilter algorithm]] · [[BJS ch12 - Maximal flow shortest path multicommodity flow and network synthesis]]
