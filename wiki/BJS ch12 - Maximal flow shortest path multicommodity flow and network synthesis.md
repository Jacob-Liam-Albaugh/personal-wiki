---
type: paper
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 12 (printed pp. 607-680)"
tags: [optimization]
authors: ["[[Mokhtar S. Bazaraa]]", "[[John J. Jarvis]]", "[[Hanif D. Sherali]]"]
year: 2010
venue: "Wiley, Linear Programming and Network Flows, 4th ed. (textbook)"
file: "Linear Optimization/BJS full book.pdf"
---

# BJS ch12 - Maximal flow shortest path multicommodity flow and network synthesis

**Summary**: Specialized network flow problems. The maximal flow problem with its dual, cuts, the augmenting path algorithm and the max flow min cut theorem; shortest paths by a label-setting method for nonnegative costs and label-correcting methods for arbitrary costs; multicommodity flow solved by decomposition; and network synthesis of multiterminal flow networks. See [[Network flow problem]], [[LP duality]], [[BJS ch11 - The out-of-kilter algorithm]], [[BJS ch7 - The decomposition principle]].

**Authors**: Mokhtar S. Bazaraa, John J. Jarvis, Hanif D. Sherali · **Year**: 2010 · **File**: `Linear Optimization/BJS full book.pdf` (printed pp. 607-680). Cites use printed pages; pdf = printed + 16.

## Overview (p. 607)
Maximal flow and shortest path can be solved by the network simplex method of [[BJS ch9 - Minimal cost network flows]] or the out-of-kilter algorithm, but their frequency and the efficient specialized procedures justify separate treatment. Multicommodity flow distinguishes types of units, with supplies and demands per commodity. Synthesis (design) problems construct an optimal network rather than analyze a given one (p. 607, text).

## The maximal flow problem (§12.1, p. 607-624)
A network with $m$ nodes, arc capacities $u_{ij}$ (finite integers), lower bounds $\ell_{ij}=0$ and no costs. Maximize the flow $f$ from node $1$ to node $m$ (p. 608, text layer):
$$\max\ f$$
$$\sum_jx_{ij}-\sum_kx_{ki}=\begin{cases}f&i=1\\0&i\ne1,m\\-f&i=m\end{cases}$$
$$0\le x_{ij}\le u_{ij}$$
This is the node-arc formulation. In matrix form $(\mathbf e_m-\mathbf e_1)f+\mathbf A\mathbf x=\mathbf0$, so $f$ is a flow on an arc from node $m$ to node $1$, giving an out-of-kilter circulatory form (Figure 12.1, p. 609).

**Cuts** (p. 609-610, text). For a node set $X$ containing node $1$ but not node $m$, with $\bar X$ its complement, the arcs with one end in each form a cut $[X,\bar X]$, with forward arcs $(X,\bar X)$ and reverse arcs $(\bar X,X)$. Its capacity is $u[X,\bar X]=\sum_{(X,\bar X)}u_{ij}-\sum_{(\bar X,X)}\ell_{ij}$, which equals the forward capacity $u(X,\bar X)$ when $\ell_{ij}=0$. Summing the conservation equations over $X$ gives
$$\sum_{i\in X,\ j\notin X}x_{ij}-\sum_{i\notin X,\ j\in X}x_{ij}=f$$
(eq. 12.1, p. 610, text), and with $x_{ij}\le u_{ij}$, $x_{ij}\ge0$ this gives $f\le u[X,\bar X]$ (eq. 12.2).

> [!theorem] Lemma 12.1 (p. 610, text)
> The value $f$ of any feasible flow is less than or equal to the capacity of any cut separating node $m$ from node $1$.

**Dual** (p. 610-611, text). With $\mathbf w$ on the conservation equations and $h_{ij}$ on $x_{ij}\le u_{ij}$:
$$\min\ \sum_{i,j}u_{ij}h_{ij}$$
$$w_m-w_1=1$$
$$w_j-w_i+h_{ij}\ge0,\quad h_{ij}\ge0$$
For a cut take $w_i=0$ for $i\in X$ and $w_i=1$ for $i\in\bar X$, with $h_{ij}=1$ on forward arcs and $0$ otherwise. This is dual feasible with objective equal to the capacity of the cut, so Lemma 12.1 also follows from weak duality ([[LP duality]]).

**Algorithm** (p. 611-612, image seen at p. 612). Start from a feasible integer flow, say $x_{ij}=0$. Build the residual network $G'$ with all nodes of $G$ and
- an arc $(i,j)$ with permitted change $\Delta_{ij}=u_{ij}-x_{ij}$ whenever $x_{ij}<u_{ij}$,
- an arc $(j,i)$ with permitted change $\Delta_{ji}=x_{ij}$ whenever $x_{ij}>0$.

If $G'$ has a path $P$ from node $1$ to node $m$ (a **breakthrough**), add the minimum permitted change $\Delta$ on $P$ to the flows of the arcs of $G$ traversed in their own direction and subtract it on those traversed against it. If no path exists (a nonbreakthrough), stop. At that point let $X$ be the nodes reachable from node $1$ in $G'$. Every arc of $G$ from $X$ to $\bar X$ has $x_{ij}=u_{ij}$ and every arc from $\bar X$ to $X$ has $x_{ij}=0$, so by (12.1)
$$u[X,\bar X]=f$$
(p. 612, image seen).

> [!theorem] Theorem 12.1, Maximal Flow-Minimal Cut Theorem (p. 612, image seen)
> The value of the maximal flow in $G$ is equal to the capacity of the minimal cut in $G$.

Exercise 12.7 generalizes to $\ell_{ij}\ne0$ (p. 612). Further topics (p. 613-619, text): an example (Figures 12.1-12.2), the fact that the iterates are basic solutions when the arcs with $0<x_{ij}<u_{ij}$ contain no cycle (p. 613), and a capacity scaling variant whose phases use $\Delta=2^q,2^{q-1},\dots,1$, with $O(\log_2U)$ phases (p. 618-619). The text also mentions the preflow-push strategy of better theoretical complexity (p. 619), motivated by augmenting paths that repeatedly traverse long high-capacity chains before reaching a bottleneck.

## The shortest path problem (§12.2, p. 620-634)
**Formulation** (p. 620, text). Send one unit from node $1$ to node $m$ at minimum cost, $x_{ij}\in\{0,1\}$ marking the arcs on the path:
$$\min\ \sum_{i,j}c_{ij}x_{ij}$$
$$\sum_jx_{ij}-\sum_kx_{ki}=\begin{cases}1&i=1\\0&i\ne1,m\\-1&i=m\end{cases}$$
Because the incidence matrix is totally unimodular (chapter 9), replacing $x_{ij}\in\{0,1\}$ by $x_{ij}\ge0$ keeps an integral optimum, so it is solved as a linear program. It is a minimal cost network flow problem and so can be solved by chapter 9 or chapter 11 methods, but more efficient methods exist (p. 620, text). After the substitution $w_i'=-w_i$ the dual variables become shortest distances from node $1$ (p. 620, text, formula garbled).

**Nonnegative costs: label-setting (Dijkstra)** (p. 621-624, text). Initialize $w_1=0$ and $X=\{1\}$. Repeat $m-1$ times: among arcs $(i,j)$ with $i\in X$, $j\notin X$ take the minimum of $w_i+c_{ij}$, attained at $(p,q)$, set $w_q=w_p+c_{pq}$ and add $q$ to $X$ (the main step, eq. 12.3). The label set at insertion is the length of a shortest path to $q$, which is proved by induction (p. 621-622). Each iteration is $O(m)$ and the algorithm is $O(m^2)$ (p. 624, text). The text also notes it is an implementation of the primal simplex method on a flow problem with supply $m-1$ at node $1$ and unit demands elsewhere (p. 624, text).

**Arbitrary costs** (p. 625-634). Without negative circuits in $G$, the label-setting method fails when costs have mixed signs (Figure 12.6, p. 625: node $3$ would be labelled via the direct arc $(1,3)$ though a path through node $2$ is shorter). With a negative circuit the problem is unbounded, and finding a shortest simple path is NP-complete (p. 625, text).

> [!theorem] Theorem 12.2 (p. 626-627, text)
> If $G$ has no negative cost circuit, then the lengths $w_j'$ of shortest simple paths from node $1$ satisfy (eq. 12.4)
> $$w_j'=\min_{i:\,(i,j)\text{ exists}}\{w_i'+c_{ij}\},\quad j=2,\dots,m$$
> and conversely labels satisfying this are shortest path distances (p. 627, text; the statement of the converse was read from the text layer).

This corresponds to primal-dual feasibility and complementary slackness for the shortest path problem (p. 628, image seen). The **label-correcting algorithm** (p. 628, image seen):
- Set $w_1'=0$ and $w_i'=\infty$ for $i\ne1$, with scan eligible list $SE=\{1\}$.
- If $SE=\emptyset$ stop. The labels are the shortest path distances.
- Otherwise remove a node $p$ from $SE$ and scan its forward star. For every arc $(p,q)$ with $w_q'>w_p'+c_{pq}$, set $w_q'=w_p'+c_{pq}$, record $p$ as the predecessor of $q$ and add $q$ to $SE$.
- Repeat.

Figure 12.7 (p. 628, image seen) is a four-node example with negative costs.

## Polynomial-time shortest paths (§12.3, p. 635-639)
The **partitioned shortest path (PSP)** algorithm splits $SE$ into lists NOW and NEXT. Nodes in NOW are scanned first, newly eligible nodes go to NEXT, and when NOW is empty NEXT becomes NOW. FIFO is a special case (p. 635, text). It does at most $m-1$ iterations, each scanning every arc at most once, so it runs in $O(m|\mathcal A|)$ (p. 636, text). The polynomial bound rests on a property of the level of each node in the current shortest path tree at the start of each iteration (p. 636-637, text, only partially read). Keeping NEXT as a heap ordered by label is efficient in theory but computationally more expensive than simple FIFO (p. 637, text). Later pages (p. 637-639) cover other label-correcting implementations and extensions: time-dependent, label-constrained, approach-dependent and stochastic shortest paths (p. 639, text).

## Multicommodity flows (§12.4-12.5, p. 639-654)
Different commodities cannot be distinguished by a single-commodity model (p. 607). Figure 12.9 (p. 639-640, text) has three commodities on a triangle with unit arc capacities, each commodity having a single path. Sending one unit of any one commodity blocks the others, giving total flow $1$, whereas $1/2$ of each gives total flow $3/2$. So integer flows are not guaranteed, though the problem is still a linear program (p. 640, text).

**Minimal cost formulation** (p. 641, text layer). With commodities $i=1,\dots,t$, arc capacity $u$ shared by all commodities and individual bounds $\mathbf u_i$:
$$\min\ \sum_{i=1}^t\mathbf c_i\mathbf x_i$$
$$\sum_{i=1}^t\mathbf x_i\le\mathbf u$$
$$\mathbf A\mathbf x_i=\mathbf b_i,\quad\mathbf 0\le\mathbf x_i\le\mathbf u_i$$
This is the node-arc formulation. It has the block diagonal structure of [[BJS ch7 - The decomposition principle]] (§7.5), with the shared capacity rows as the coupling constraints, so decomposition applies (p. 641, text). The book gives a decomposition-based procedure with subproblems that are single-commodity network flow problems (Figures 12.14-12.15 show subproblem networks at an iteration, p. 649). The constraint matrix is large even for moderate-sized problems (p. 641, text).

**Basis characterization** (§12.5, p. 649-654, text). Adding an artificial column per commodity makes the constraint matrix have the block structure of coupling rows plus one $\mathbf A$ block per commodity (p. 649, text).

> [!theorem] Theorem 12.3 (p. 652, text)
> A transformed basis matrix for the multicommodity minimal cost flow problem corresponds to a rooted spanning tree for each commodity plus a set of cycles and slack arcs.

This allows direct application of the simplex method (Exercise 12.61, p. 652), with an example in Figures 12.16-12.18 (p. 652-654).

## Synthesis of multiterminal flow networks (§12.6, p. 654-)
A network design problem, as opposed to the analysis problems so far (p. 654, text). Given potential arcs $\mathcal A'$ with cost $c_{ij}$ per unit capacity and requirements $r_{ij}\ge0$ between node pairs, choose capacities $u_{ij}\ge0$ to minimize the cost $\sum c_{ij}u_{ij}$ subject to the maximum flow between each pair $i,j$ being at least $r_{ij}$ in the constructed network (p. 655, text). Two manipulations reduce the problem. The first replaces the $m(m-1)/2$ requirement constraints by only those on the **dominant requirement tree** $T_r$, the maximum weight spanning tree of the complete graph on the nodes with weight $r_{ij}$ on arc $(i,j)$ (p. 655-656, text). It is built greedily: sort the $r_{ij}$ in decreasing order, take each arc unless it forms a cycle with those already chosen, and stop after $m-1$ arcs. For the book's five-node example with $r_{45}=12$, $r_{34}=8$, $r_{24}=7$, $r_{13}=5$ the selected arcs are $(4,5),(3,4),(2,4),(1,3)$ (p. 656, text). The rest of the section (p. 656-662) and the exercises were not read.

## Notes
- Wiki note: Theorem 12.1 is LP duality for the maximal flow problem, as the dual above shows, so it is a special case of [[LP duality]]. The book states (p. 540) that Theorem 10.1 of [[BJS ch10 - Transportation and assignment problems]] is a special case of it, as Exercise 12.17 asks the reader to show.
- Wiki note: [[BT ch7 - Network flows]] covers the same network flow problem.

**Sources**: `Linear Optimization/BJS full book.pdf` (pdf 623-696, printed pp. 607-680). Pages viewed as images: pdf 628 (printed 612) and 644 (628). All other content (formulations, cuts, dual, Dijkstra, PSP, multicommodity, synthesis) read from the text layer, which garbles math, so those equations are reconstructed from the text and not checked against an image. Sections on capacity scaling, extensions and synthesis beyond the dominant tree were not read in detail.
**Last updated**: 2026-11-06

---

## Related pages
- [[Network flow problem]] · [[LP duality]] · [[Dantzig-Wolfe decomposition]] · [[Linear programming]]
- [[BJS ch9 - Minimal cost network flows]] · [[BJS ch10 - Transportation and assignment problems]] · [[BJS ch11 - The out-of-kilter algorithm]] · [[BJS ch7 - The decomposition principle]] · [[BT ch7 - Network flows]]
