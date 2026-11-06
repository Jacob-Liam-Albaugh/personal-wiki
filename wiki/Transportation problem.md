---
type: method
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, §10.1-10.6, 10.10; Bertsimas, Tsitsiklis 1997, §7.2"
tags: [optimization]
---

# Transportation problem

> [!definition] Transportation problem (source: BJS full book.pdf, pp. 513-516)
> $m$ origins with supplies $s_i$, $n$ destinations with demands $d_j$, shipping cost $c_{ij}$ and flow $x_{ij}$, total supply equal to total demand. With $\mathbf x=(x_{11},\dots,x_{1n},x_{21},\dots,x_{mn})$ and $\mathbf b=(s_1,\dots,s_m,-d_1,\dots,-d_n)$,
> $$\min\ \mathbf c\mathbf x\quad\text{s.t. }\mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf0$$
> where the column of $x_{ij}$ is $\mathbf a_{ij}=\mathbf e_i-\mathbf e_{m+j}\in\mathbb R^{m+n}$. The demand constraints are multiplied by $-1$ to agree with the [[Network flow problem]] form.

**Intuition**: a [[Network flow problem]] on a bipartite graph. $\mathbf A$ is the $(m+n)\times mn$ node-arc incidence matrix: its top $m$ rows have a row of ones over the $n$ columns of each origin, and its bottom $n$ rows hold $-\mathbf I$ repeated $m$ times. BJS's example has $s=(30,20)$, $d=(15,10,25)$, $c_{11}=4$, $c_{12}=7$, $c_{13}=5$, $c_{21}=2$, $c_{22}=4$, $c_{23}=3$ (p. 516). BT list it among the special cases of the min cost flow model ($m$ suppliers, $n$ consumers, total supply equals total demand; BT p. 273-276).

## Key facts
- **Feasibility**: with $d=\sum_is_i=\sum_jd_j$ the point $x_{ij}=s_id_j/d$ is feasible, and every feasible $x_{ij}$ obeys $0\le x_{ij}\le\min\{s_i,d_j\}$, so the feasible set is bounded and an optimum exists (p. 516).
- **Rank** is $m+n-1$ since the rows sum to zero; an artificial root-arc column $\mathbf e_{m+n}$ with variable $x_a$ gives $\bar{\mathbf A}=(\mathbf A,\mathbf e_{m+n})$ (p. 517).
- **Total unimodularity**: every square submatrix of $\mathbf A$ has determinant $-1,0,+1$, so bases and inverses have entries in $\{-1,0,1\}$, and by Cramer's rule so does $\mathbf y_{ij}=\mathbf B^{-1}\mathbf a_{ij}$ (p. 517). Integer data give integer optimal flows.
- **Representation on the tableau** (pp. 517-522): for a nonbasic cell $(i,j)$ the representation alternates $+1,-1$ along the unique chain of basic cells joining row $i$ to column $j$; with $(i,j)$ that chain forms a cycle. The artificial variable never enters it and stays at zero.
- Any finite-valued capacitated or uncapacitated min cost flow problem transforms into an uncapacitated transportation problem (BJS Exercise 9.27), and any transportation problem into an [[Assignment problem]] by unit-supply and unit-demand copies, though BJS call that computationally inadvisable (p. 513).

## Simplex method on the tableau (BJS §10.4, pp. 522-532)
This is the [[Network simplex method]] carried out on the tableau, the customary presentation for transportation problems.

> [!algorithm] Northwest corner rule (pp. 522-524)
> Keep residual supplies $s_i'$ and demands $d_j'$. At cell $(k,l)$ set $x_{kl}=\min\{s_k',d_l'\}$, subtract it from both, and move right if the row supply is positive, otherwise down. If $s_k'=d_l'$ the next basic variable is at level zero (degenerate) and either direction is allowed.

It yields exactly $m+n-1$ basic variables forming a connected, cycle-free spanning graph, hence a [[Basic feasible solution]]. Vogel's approximation method is an alternative (BJS Exercise 10.25, p. 524).

**Pricing** (pp. 524-526). For a nonbasic cell
$$z_{ij}-c_{ij}=\mathbf c_B\mathbf B^{-1}\mathbf a_{ij}-c_{ij}=\mathbf c_B\mathbf y_{ij}-c_{ij}$$
- *Cycle method*: add and subtract the costs of the basic cells on the cycle through $(i,j)$. In the example $z_{21}-c_{21}=4-5+3-2=0$ and $z_{22}-c_{22}=7-5+3-4=1$, so $x_{22}$ is a candidate (p. 525).
- *Dual variable method* (preferred): with $\mathbf w=(u_1,\dots,u_m,v_1,\dots,v_n)$,
$$z_{ij}-c_{ij}=u_i-v_j-c_{ij}$$
  where $\mathbf w\mathbf B=\mathbf c_B$ with artificial cost $c_a=0$ gives $v_n=0$ and $u_p-v_q=c_{pq}$ on each basic cell. The system is triangular, so back-substitute from $v_n=0$, using only basic cells.
- Optimal iff $z_{ij}-c_{ij}\le0$ on every nonbasic cell. This is the general rule $w_i-w_j-c_{ij}$ of the network simplex with the transportation incidence matrix.

**Pivot** (pp. 527-531): the entering cell closes a cycle with basic cells; shift flow around it until a basic cell hits zero, which leaves. Examples 10.1-10.2 (pp. 528-533) work this through; one example's dual variables, read from a garbled text layer, are $u=(14,20,18,13)$, $v=(4,2,8,4,\dots)$, $v_6=0$ **[unverified]**. §10.5 treats degeneracy (pp. 528-534). §10.6 builds the explicit simplex tableau from the $\mathbf y_{ij}$ and $z_{ij}-c_{ij}$ (p. 535, Fig. 10.19).

## Transshipment problem (BJS §10.10, pp. 551-552)
Intermediate points that neither supply nor demand goods may transship. It is a network flow problem solved directly by network simplex, or converted to a transportation problem by tracing shortest paths between each origin-destination pair (BJS Exercise 9.27; see [[Shortest path problem]]) or by adding buffer stocks (Exercise 10.51).

**Covered in**: Bazaraa-Jarvis-Sherali ch. 10 §10.1-10.6, 10.10 (pp. 513-535, 551-552); Bertsimas-Tsitsiklis ch. 7 §7.2 (pp. 273-276)
**Sources**: `text_books/Linear Optimization/BJS full book.pdf` (ch. 10); `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 7).
**Last updated**: 2026-11-06

---

## Related pages
- [[Network flow problem]] · [[Network simplex method]] · [[Assignment problem]] · [[Shortest path problem]]
- [[Simplex method]] · [[Basic feasible solution]] · [[Linear programming]]
