---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, §7.5; Bazaraa, Jarvis, Sherali 2010, §12.1"
tags: [optimization]
---

# Maximum flow problem

> [!definition] Maximal flow (source: BJS full book.pdf, p. 608; MIT (ch 1-5).pdf, pp. 301-303)
> Network with $m$ nodes, finite integer capacities $u_{ij}$ and lower bounds $0$. Maximize the flow $f$ from source node $1$ to sink node $m$:
> $$\max\ f$$
> $$\sum_jx_{ij}-\sum_kx_{ki}=\begin{cases}f&i=1\\0&i\ne1,m\\-f&i=m\end{cases}\qquad0\le x_{ij}\le u_{ij}$$
> Equivalently (BT) a minimum cost flow with zero costs plus a return arc $(t,s)$ of infinite capacity and cost $-1$ (Fig. 7.20, p. 303); in matrix form $(\mathbf e_m-\mathbf e_1)f+\mathbf A\mathbf x=\mathbf0$, so $f$ rides an arc from $m$ to $1$, giving an out-of-kilter circulatory form (BJS Fig. 12.1, p. 609; [[Out-of-kilter algorithm]]).

**Intuition**: a special [[Network flow problem]] that could be solved by [[Network simplex method]], but whose frequency justifies the specialised augmenting path method. Application: preemptive scheduling (BT Example 7.4, p. 302).

## Cuts and weak duality
A cut is a node set $X$ with source in $X$, sink not in $X$; $\bar X$ is the complement. Its capacity is
$$u[X,\bar X]=\sum_{(X,\bar X)}u_{ij}-\sum_{(\bar X,X)}\ell_{ij}$$
(BT: $C(S)$, the sum of capacities of arcs leaving $S$). Summing the conservation equations over $X$ gives (BJS eq. 12.1, p. 610)
$$\sum_{i\in X,\ j\notin X}x_{ij}-\sum_{i\notin X,\ j\in X}x_{ij}=f$$
so with $x_{ij}\le u_{ij}$, $x_{ij}\ge0$:

> [!theorem] Lemma 12.1 (BJS p. 610; BT eq. 7.14, p. 310)
> The value of any feasible flow is at most the capacity of any cut separating source from sink: $f\le u[X,\bar X]$.

**Dual** (BJS pp. 610-611). With $\mathbf w$ on the conservation rows and $h_{ij}$ on $x_{ij}\le u_{ij}$:
$$\min\ \sum_{i,j}u_{ij}h_{ij}\quad\text{s.t. }w_m-w_1=1,\ \ w_j-w_i+h_{ij}\ge0,\ \ h_{ij}\ge0$$
Taking $w_i=0$ on $X$, $w_i=1$ on $\bar X$ and $h_{ij}=1$ on forward arcs is dual feasible with objective equal to the cut capacity, so Lemma 12.1 is weak duality ([[LP duality]]; BT Exercise 7.20, p. 312).

## Augmenting path algorithm (Ford-Fulkerson)
> [!algorithm] Ford-Fulkerson (BT box p. 305; BJS pp. 611-612)
> 1. Start with a feasible integer flow, e.g. $x_{ij}=0$.
> 2. Build the residual network $G'$ with arc $(i,j)$ of permitted change $\Delta_{ij}=u_{ij}-x_{ij}$ when $x_{ij}<u_{ij}$, and arc $(j,i)$ with $\Delta_{ji}=x_{ij}$ when $x_{ij}>0$. Search for an augmenting path $P$ from source to sink (labeling algorithm).
> 3. If none exists (nonbreakthrough), stop.
> 4. Else push $\delta(P)$, the minimum permitted change on $P$, adding it on arcs traversed forward and subtracting it on arcs traversed backward. If $\delta(P)=\infty$ the problem is unbounded. Repeat.

At nonbreakthrough let $X$ be the nodes reachable from the source in $G'$: every arc from $X$ to $\bar X$ is saturated, every arc from $\bar X$ to $X$ carries zero, so by eq. 12.1 $u[X,\bar X]=f$.

> [!theorem] Max-flow min-cut (BT Thm 7.10, p. 310; BJS Thm 12.1, p. 612)
> (a) If the algorithm stops because no augmenting path exists, the flow is optimal. (b) The value of the maximal flow equals the capacity of the minimal cut.

It is also a consequence of [[LP duality]]. BJS Exercise 12.7 generalizes to $\ell_{ij}\ne0$.

## Termination and complexity
- With integer or infinite capacities and an integer start, flows stay integer and the algorithm terminates when the maximum is finite (BT Thm 7.8, p. 305; Example 7.5: four augmentations give value $6$, the capacity out of $s$). Rational capacities terminate by scaling.
- The labeling algorithm is linear in $|\mathcal A|$ (BT Thm 7.9, p. 309). With capacities at most $U$ there are at most $|\mathcal A|U$ augmentations, so $O(|\mathcal A|^2U)$, linear in $U$ (BT p. 312).
- **Capacity scaling** (BJS pp. 618-619; BT Exercise 7.25): phases with $\Delta=2^q,2^{q-1},\dots,1$, $O(\log_2U)$ phases. BJS also mention preflow-push, with better theoretical complexity, motivated by augmenting paths that repeatedly traverse long high-capacity chains before reaching a bottleneck (p. 619).
- Iterates are basic solutions when the arcs with $0<x_{ij}<u_{ij}$ contain no cycle (BJS p. 613).

## Related negative cost cycle view
The same optimality idea for general costs is the cycle-cancelling method in [[Network flow problem]]: a flow is optimal iff its residual network has no negative cycle. Theorem 10.1 of the [[Assignment problem]] (independent zeros versus covering lines) is a special case of max flow min cut (BJS p. 540, Exercise 12.17).

**Covered in**: Bertsimas-Tsitsiklis ch. 7 §7.5 (pp. 301-312); Bazaraa-Jarvis-Sherali ch. 12 §12.1 (pp. 607-624)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 7); `text_books/Linear Optimization/BJS full book.pdf` (ch. 12; pdf 628 viewed as image).
**Last updated**: 2026-11-06

---

## Related pages
- [[Network flow problem]] · [[Out-of-kilter algorithm]] · [[Network simplex method]] · [[Assignment problem]]
- [[LP duality]] · [[Linear programming]] · [[Multicommodity flow]]
