---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, §7.9; Bazaraa, Jarvis, Sherali 2010, §12.2-12.3"
tags: [optimization]
---

# Shortest path problem

> [!definition] Shortest path as a flow problem (source: BJS full book.pdf, p. 620)
> Send one unit from node $1$ to node $m$ at minimum cost, $x_{ij}\in\{0,1\}$ marking path arcs:
> $$\min\ \sum_{i,j}c_{ij}x_{ij}\quad\text{s.t. }\sum_jx_{ij}-\sum_kx_{ki}=\begin{cases}1&i=1\\0&i\ne1,m\\-1&i=m\end{cases}$$
> The incidence matrix is totally unimodular ([[Network simplex method]]), so replacing $x_{ij}\in\{0,1\}$ by $x_{ij}\ge0$ keeps an integral optimum and the problem can be solved as an LP. After $w_i'=-w_i$ the dual variables are shortest distances from node $1$ (formula garbled in the text layer).

**Intuition**: a special [[Network flow problem]], solvable by network simplex or the [[Out-of-kilter algorithm]], but specialised labeling methods are faster. Dijkstra's algorithm is an implementation of primal simplex on a flow problem with supply $m-1$ at node $1$ and unit demands elsewhere (BJS p. 624).

## Key facts
- Negative length cycles make walks approach $-\infty$ (unbounded). Without them a shortest path is also a shortest walk and has at most $n-1$ arcs (BT p. 333). Finding a shortest *simple* path in the presence of negative circuits is NP-complete (BJS p. 625).
- **Bellman's equation** (BT p. 333-337): with $p_i$ the shortest length from $i$ to destination $n$,
$$p_i=\min_{j\in O(i)}\{c_{ij}+p_j\}$$
  whose largest solution is the answer when no negative cycle exists (BT Fig. 7.32, p. 337). BJS's forward form from the source is (Theorem 12.2, pp. 626-627, converse read from the text layer): if $G$ has no negative circuit, the shortest simple path lengths satisfy
$$w_j'=\min_{i:(i,j)\text{ exists}}\{w_i'+c_{ij}\},\quad j=2,\dots,m$$
  and labels satisfying this are shortest distances. This is primal-dual feasibility plus complementary slackness (BJS p. 628).

## Algorithms
**Label setting (Dijkstra), nonnegative costs** (BJS pp. 621-624). Set $w_1=0$, $X=\{1\}$. Repeat $m-1$ times: among arcs $(i,j)$ with $i\in X$, $j\notin X$ take the minimum of $w_i+c_{ij}$, attained at $(p,q)$, set $w_q=w_p+c_{pq}$ and add $q$ to $X$ (eq. 12.3). The label at insertion is the shortest path length, by induction (pp. 621-622). Each iteration is $O(m)$ so the total is $O(m^2)$.

It fails for mixed-sign costs: in BJS Fig. 12.6 (p. 625) node $3$ would be labelled via the direct arc $(1,3)$ although the route through node $2$ is shorter.

**Label correcting, arbitrary costs** (BJS p. 628; BT p. 339). Set $w_1'=0$, $w_i'=\infty$ otherwise, scan eligible list $SE=\{1\}$. While $SE\ne\emptyset$: remove a node $p$ and scan its forward star; for each arc $(p,q)$ with $w_q'>w_p'+c_{pq}$, set $w_q'=w_p'+c_{pq}$, record $p$ as predecessor of $q$ and add $q$ to $SE$. BT state it backward with labels $p_j$ and a list $S$ of nodes whose label dropped: $p_i:=\min\{p_i,c_{ij}+p_j\}$. Dijkstra is the nonnegative case. BJS Fig. 12.7 is a four-node example with negative costs.

**Bellman-Ford** (BT p. 337-339). Let $p_i(t)$ be the shortest walk length from $i$ to $n$ using at most $t$ arcs, $p_n(t)=0$, $p_i(0)=\infty$ for $i\ne n$:
$$p_i(t+1)=\min_{k\in O(i)}\{c_{ik}+p_k(t)\}$$
With no negative cycle $p_i(n-1)=p_i^*$; if $p_i(n)\ne p_i(n-1)$ for some $i$ a negative cycle exists and is found by tracing successors.

**Polynomial label correcting: partitioned shortest path (PSP)** (BJS §12.3, pp. 635-639). Split $SE$ into lists NOW and NEXT: scan NOW first, send newly eligible nodes to NEXT, and when NOW empties NEXT becomes NOW; FIFO is a special case. At most $m-1$ iterations, each scanning every arc at most once, so $O(m|\mathcal A|)$ (p. 636); the bound rests on a property of node levels in the current shortest path tree (pp. 636-637, only partially read). A heap-ordered NEXT is efficient in theory but costlier than FIFO in practice. Pages 637-639 cover time-dependent, label-constrained, approach-dependent and stochastic variants.

**All pairs** (BT p. 343). From $p_i\le c_{ij}+p_j$, the re-weighting
$$\hat c_{ij}=c_{ij}+p_j-p_i\ge0$$
preserves shortest paths (eq. 7.21). One Bellman-Ford run plus $n-1$ Dijkstra runs costs $O(n^3)$ against $O(n^4)$ for repeated Bellman-Ford.

## Neighbouring problem: minimum spanning tree (BT §7.10, pp. 343-345)
Not a flow problem but graph-structured. **Prim's greedy algorithm**: start with one node; while the tree has fewer than $n$ nodes add a cheapest edge joining a tree node to a non-tree node. No cycle forms and the result is a minimum spanning tree (stronger property proved on p. 344). It is the subroutine of the traveling salesman heuristic in [[Integer programming]]. BJS's synthesis problem builds a maximum weight spanning tree greedily in the same way ([[Multicommodity flow]]).

## Uses elsewhere
Bellman's equation is the recursion behind the zero-one knapsack dynamic program ([[Integer programming]], BT §11.3) and the pricing step in [[Column generation]] for the cutting stock problem. Successive shortest paths solve the [[Assignment problem]]; shortest paths between origin-destination pairs turn a transshipment problem into a [[Transportation problem]].

**Covered in**: Bertsimas-Tsitsiklis ch. 7 §7.9-7.10 (pp. 332-345); Bazaraa-Jarvis-Sherali ch. 12 §12.2-12.3 (pp. 620-639)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 7); `text_books/Linear Optimization/BJS full book.pdf` (ch. 12; pdf 644 viewed as image).
**Last updated**: 2026-11-06

---

## Related pages
- [[Network flow problem]] · [[Maximum flow problem]] · [[Network simplex method]] · [[Out-of-kilter algorithm]]
- [[Assignment problem]] · [[Transportation problem]] · [[Integer programming]] · [[LP duality]]
