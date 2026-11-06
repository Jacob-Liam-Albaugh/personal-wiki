---
type: paper
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 10 (printed pp. 513-566)"
tags: [optimization]
authors: ["[[Mokhtar S. Bazaraa]]", "[[John J. Jarvis]]", "[[Hanif D. Sherali]]"]
year: 2010
venue: "Wiley, Linear Programming and Network Flows, 4th ed. (textbook)"
file: "text_books/Linear Optimization/BJS full book.pdf"
---

# BJS ch10 - Transportation and assignment problems

**Summary**: The transportation problem as a network flow LP with a special incidence matrix, the simplex method carried out directly on the transportation tableau (northwest corner start, dual-variable pricing, cycle pivots), and the assignment problem solved by Kuhn's Hungarian algorithm, with brief treatments of an alternating path basis method, a successive shortest path method and the transshipment problem. See [[Network flow problem]], [[Simplex method]], [[BJS ch9 - Minimal cost network flows]].

**Authors**: Mokhtar S. Bazaraa, John J. Jarvis, Hanif D. Sherali · **Year**: 2010 · **File**: `text_books/Linear Optimization/BJS full book.pdf` (printed pp. 513-566). Cites use printed pages; pdf = printed + 16.

## Overview (p. 513)
Both problems are special cases of network flow problems. Any finite-valued minimum cost network flow problem, capacitated or not, can be transformed into an uncapacitated transportation problem (Exercise 9.27), and any transportation problem can be transformed into an assignment problem (§10.7), though the book calls that computationally inadvisable (p. 513, text). The tableau is used because it is the customary way to present the network simplex algorithm for transportation problems.

## Definition and matrix form (§10.1, p. 513-516)
There are $m$ origins with supplies $s_i$ and $n$ destinations with demands $d_j$, shipping cost $c_{ij}$ and flow $x_{ij}$, with total supply equal to total demand (p. 515-516, text and image seen). The demand constraints are multiplied by $-1$ to agree with [[BJS ch9 - Minimal cost network flows]]. With $\mathbf x=(x_{11},\dots,x_{1n},x_{21},\dots,x_{mn})$ and $\mathbf b=(s_1,\dots,s_m,-d_1,\dots,-d_n)$ the problem is
$$\min\ \mathbf c\mathbf x\quad\text{s.t. }\mathbf A\mathbf x=\mathbf b,\ \ \mathbf x\ge\mathbf0$$
where the column of $x_{ij}$ is $\mathbf a_{ij}=\mathbf e_i-\mathbf e_{m+j}$ in $\mathbb R^{m+n}$ (p. 515, text). Matrix $\mathbf A$ is the node-arc incidence matrix, of size $(m+n)\times mn$ (p. 516, image seen). Its top $m$ rows have a row of ones over the $n$ columns of each origin, and its bottom $n$ rows hold $-\mathbf I$ repeated $m$ times. The book's 2-origin, 3-destination example has $s=(30,20)$, $d=(15,10,25)$ and costs $c_{11}=4$, $c_{12}=7$, $c_{13}=5$, $c_{21}=2$, $c_{22}=4$, $c_{23}=3$ (p. 516, image seen).

**Feasibility** (p. 516, image seen). With $d=\sum_is_i=\sum_jd_j$, the point
$$x_{ij}=\frac{s_id_j}{d}$$
is feasible, and every feasible $x_{ij}$ satisfies $0\le x_{ij}\le\min\{s_i,d_j\}$. A bounded feasible LP has an optimum, so an optimal solution exists.

## Properties of the A matrix (§10.2-10.3, p. 516-522)
- **Rank** (p. 517, text). The rows sum to zero, and the rank is $m+n-1$ (as shown in Chapter 9). The book adds an artificial root-arc column $\mathbf e_{m+n}$ with variable $x_a$ and writes $\bar{\mathbf A}=(\mathbf A,\mathbf e_{m+n})$.
- **Total unimodularity** (p. 517, text). Every square submatrix of $\mathbf A$ has determinant $-1$, $0$ or $+1$, so every basis and its inverse have entries in $\{-1,0,1\}$. By Cramer's rule the updated column $\mathbf y_{ij}$, the solution of $\mathbf B\mathbf y_{ij}=\mathbf a_{ij}$, has entries in $\{-1,0,1\}$, so a nonbasic column is obtained by adding and subtracting basic columns.
- **Representation on the tableau** (p. 517-521, text). For a nonbasic cell $(i,j)$ the representation alternates $+1,-1$ along the unique chain of basic cells joining row $i$ to column $j$, and together with $(i,j)$ this forms a cycle (Figure 10.2). The representation uses only basic vectors on that chain, so the artificial variable never enters it and stays at zero (p. 522, text), which lets the method ignore it.

## The simplex method on the tableau (§10.4, p. 522-532)
The four generic steps (starting basic feasible solution, compute $z-c$, choose the leaving column, update) are performed directly on the tableau (p. 522, text).

**Northwest corner rule** (p. 522-524, text). Keep residual supplies $s_i'$ and demands $d_j'$. Begin at cell $(1,1)$, set $x_{kl}=\min\{s_k',d_l'\}$, subtract that from both, and move right if the row supply is positive, otherwise down. If $s_k'=d_l'$ the next basic variable is at level zero (degenerate), and either direction may be taken. It produces exactly $m+n-1$ basic nonnegative variables forming a connected, spanning, cycle-free graph, because each step raises the row or column index, so the cells form a spanning tree and a basic feasible solution. Vogel's approximation method is an alternative (Exercise 10.25, p. 524).

**Pricing** (p. 524-526, image seen at p. 525). For a nonbasic cell,
$$z_{ij}-c_{ij}=\mathbf c_B\mathbf B^{-1}\mathbf a_{ij}-c_{ij}=\mathbf c_B\mathbf y_{ij}-c_{ij}$$
which is computed by the **cycle method**: add and subtract the costs of the basic cells on the cycle through $(i,j)$. In the book's example the cycle gives $z_{21}-c_{21}=4-5+3-2=0$ and $z_{22}-c_{22}=7-5+3-4=1$, so $x_{22}$ is a candidate to enter (p. 525, image seen). Optimality holds iff $z_{ij}-c_{ij}\le0$ for every nonbasic cell, and a cell with $z_{ij}-c_{ij}>0$ is a candidate.

The preferred alternative is the **dual variable** or $(u_i,v_j)$ method (p. 525-526, image seen at p. 525). Write the dual vector as
$$\mathbf w=(u_1,\dots,u_m,v_1,\dots,v_n)$$
Since $\mathbf a_{ij}$ has $+1$ in row $i$ and $-1$ in position $m+j$,
$$z_{ij}-c_{ij}=u_i-v_j-c_{ij}$$
The vector solves $\mathbf w\mathbf B=\mathbf c_B$ with the artificial cost set to $c_a=0$, which gives $v_n=0$, and for each basic cell
$$u_p-v_q=c_{pq}$$
The system is triangular, so one back-substitutes from $v_n=0$ (p. 526, text). Only basic cells are used.

**Pivot** (p. 527-531, text; the Figure 10.10 numbers on p. 529 are text-layer values). The entering cell closes a cycle with basic cells, flow is shifted around the cycle until a basic cell reaches zero, and that cell leaves. Examples 10.1 and 10.2 (p. 528-533) work this through, with one example whose dual variables read from the text layer are $u=(14,20,18,13)$ and $v=(4,2,8,4,\dots)$ with $v_6=0$ (p. 529, text, partly garbled, **[unverified]**).

## Degeneracy, tableau form (§10.5-10.6, p. 528-535)
§10.5 gives examples and notes on degeneracy (p. 528-534). §10.6 (p. 535) builds the explicit simplex tableau associated with a transportation tableau from the $\mathbf y_{ij}$ and $z_{ij}-c_{ij}$ values, as in Figure 10.19 (text only).

## The assignment problem and the Hungarian algorithm (§10.7, p. 535-544)
The special case $m=n$, $s_i=d_j=1$ matches $m$ individuals to $m$ jobs at cost $c_{ij}$ (p. 535, text). The model (p. 536, text layer):
$$\min\ \sum_{i=1}^m\sum_{j=1}^mc_{ij}x_{ij}$$
$$\sum_{j=1}^mx_{ij}=1,\qquad-\sum_{i=1}^mx_{ij}=-1$$
$$x_{ij}=0\ \text{or}\ 1$$
It has the transportation constraint matrix, an underlying bipartite graph, and is also called minimum weighted matching on a bipartite graph. The text breaks off at "Applying the total unimodularity property of" (p. 536), so the integrality conclusion there was not read. Each basic feasible solution has $2m-1$ basic variables of which only $m$ are positive, so $m-1$ are degenerate at zero (p. 536, text). The polytope has $m!$ extreme points, one per matching (p. 537, text), and any transportation problem becomes an assignment problem by making $s_i$ unit-supply copies of origin $i$ and $d_j$ unit-demand copies of destination $j$ (p. 537, text).

**Hungarian algorithm** (p. 538-543). It is primal-dual: keep dual feasibility, build primal feasibility. Subtract each row minimum, then each column minimum, to get a **reduced matrix** with nonnegative entries $\hat c_{ij}=c_{ij}-u_i+v_j$ and a zero in every row and column (p. 541, image seen and text). Zero cells are **independent** if no two share a row or column.

> [!theorem] Theorem 10.1 (p. 540, image seen)
> The maximum number of independent zero cells in a reduced assignment matrix is equal to the minimum number of lines to cover all the zeros in the matrix.

The book does not prove it here, and says in Exercise 12.17 that it is a special case of the max flow min cut theorem ([[BJS ch12 - Maximal flow shortest path multicommodity flow and network synthesis]]).

Dual update when fewer than $m$ independent zeros exist (p. 541, image seen). Cover the zeros by the minimum number $k<m$ of lines. Let $S_r$ be the set of uncovered rows and $S_c$ the set of uncovered columns, and let $c_0$ be the minimum uncovered element,
$$c_0=\min_{i\in S_r,\ j\in S_c}\{\hat c_{ij}\}>0$$
The new dual feasible solution is (hats are the old values, bars the new)
$$\bar u_i=\hat u_i+c_0\ (i\in S_r),\qquad\bar u_i=\hat u_i\ (i\notin S_r)$$
$$\bar v_j=\hat v_j\ (j\in S_c),\qquad\bar v_j=\hat v_j+c_0\ (j\notin S_c)$$
where the page writes the complements as $\overline{S_r}$ and $\overline{S_c}$.
which means subtracting $c_0$ from each uncovered element and adding it to each twice-covered element, keeping the matrix nonnegative. In the book's $3\times3$ example $c_0=\min\{2,5,3,3\}=2$ gives the reduced matrix with rows $(0,0,3)$, $(5,0,0)$, $(0,1,1)$ and the optimum $x_{12}^*=x_{23}^*=x_{31}^*=1$ (p. 541, image seen). Primal feasibility is attained, dual feasibility maintained and complementary slackness holds, so the KKT conditions hold and the solution is optimal ([[KKT conditions]]).

Summary of the method (p. 541-542, text): an initialization step (row then column reduction), then a main step that covers all zeros with the fewest lines; if that number is $m$ an optimal solution is available, otherwise subtract the minimum uncovered element from the uncovered elements, add it to the twice-covered ones, and repeat. It terminates finitely, because the dual objective rises by at least a unit per iteration. The p. 544 remark: covering with some $k<m$ lines gives a dual increase of $c_0(m-k)\ge1$ (p. 544, text).

## Alternating path basis and successive shortest paths (§10.8-10.9, p. 544-550)
§10.8 notes that every basic feasible solution of the assignment problem has degeneracy of order $m-1$, and that about 90 percent of pivots are degenerate for $m>500$ (p. 544, text), motivating an alternating path basis algorithm (p. 544-545, Figure 10.21, not read in detail). §10.9 presents a polynomial-time algorithm that solves a succession of shortest path problems, with an $m=3$ cost example (p. 546, text). It is said to run up to seven times faster than the alternating path basis algorithm when used with an efficient shortest path routine (p. 546, text). Its proof (p. 551, text layer) argues that after augmentation the new partial assignment stays complementary slack with the dual vector $\mathbf w$, so at most $m$ iterations reach optimality.

## Transshipment problem (§10.10, p. 551-552)
Intermediate points where goods are neither supplied nor required can transship goods (Figure 10.23). It is a network flow problem solvable by the network simplex method of chapter 9 or converted into a transportation problem by tracing shortest paths between each origin-destination pair (Exercise 9.27) or by adding buffer stocks (Exercise 10.51) (p. 551-552, text). Exercises and notes follow (p. 552-566).

## Notes
- Wiki note: the dual-variable pricing here, $z_{ij}-c_{ij}=u_i-v_j-c_{ij}$, is the general network simplex rule $z_{ij}-c_{ij}=w_i-w_j-c_{ij}$ of chapter 9 with the transportation incidence matrix.
- Wiki note: [[BT ch7 - Network flows]] covers the same network flow problem and its simplex specialization.

**Sources**: `text_books/Linear Optimization/BJS full book.pdf` (pdf 529-582, printed pp. 513-566). Pages viewed as images: pdf 532 (printed 516), 541 (525), 557 (541). Pdf 556 (540, Theorem 10.1) was read from the text layer. All other content read from the text layer and headings, so the equations transcribed above beyond those pages are from text where noted.
**Last updated**: 2026-11-06

---

## Related pages
- [[Network flow problem]] · [[Simplex method]] · [[Linear programming]] · [[Basic feasible solution]] · [[KKT conditions]]
- [[BJS ch9 - Minimal cost network flows]] · [[BJS ch11 - The out-of-kilter algorithm]] · [[BJS ch12 - Maximal flow shortest path multicommodity flow and network synthesis]] · [[BT ch7 - Network flows]]
