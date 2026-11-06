---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, §7.3; Bazaraa, Jarvis, Sherali 2010, §9.3-9.11"
tags: [optimization]
---

# Network simplex method

> [!algorithm] Network simplex (source: BJS full book.pdf, pp. 466-475; MIT (ch 1-5).pdf, pp. 280-291)
> The [[Simplex method]] on a minimal cost [[Network flow problem]], carried out on a graph. A basis is a spanning tree of arcs, so every linear solve is a tree traversal.
> 1. Take a feasible tree solution.
> 2. Compute node prices from the tree, then reduced costs $c_{ij}-(p_i-p_j)$ of the nonbasic arcs.
> 3. If none is negative (BJS sign convention: no $z_{ij}-c_{ij}>0$), stop. Else the violating arc closes a unique cycle with the tree.
> 4. Push flow around the cycle until a tree arc blocks it, and pivot that arc out.

**Intuition**: the node-arc incidence matrix has a column $\mathbf e_p-\mathbf e_q$ per arc, so a set of arcs is linearly independent exactly when it has no cycle. That makes bases trees, basis matrices triangular with entries $0,\pm1$, and optimal flows integer. BJS report network simplex 200-300 times faster than a standard simplex that exploits only sparsity (BJS p. 453).

## Basis structure
- **Rank**: for a connected graph with $m$ nodes the incidence matrix has rank $m-1$, because the rows sum to zero, so one row is dropped or an artificial root arc is attached to one node (BT Cor. 7.1, p. 282; BJS §9.3, p. 459-465).
- **Tree solutions** (BT Def. 7.1, p. 280): a flow built from a forest of arcs, all other arcs at zero flow. $m-1$ arcs forming a tree give independent columns (BT Thm 7.3, p. 281).
- **Theorem** (BT Thm 7.4, p. 283; BJS Thm 9.1, p. 463): a flow is a [[Basic feasible solution]] iff it is a tree solution; $\mathbf B$ is a basis matrix iff it is the incidence matrix of a rooted spanning tree. With several components or root arcs the basis is a spanning forest, which BJS §9.7 transforms back to one tree with one root arc.
- Triangularity gives integrality and total unimodularity: with integer supplies (and capacities) the optimal basic flow is integer (BT Thm 7.5, Cor. 7.2, p. 289-290; BJS p. 463).

## Computing the iteration
- **Primal values**: solve $\mathbf B\mathbf x_B=\mathbf b$ from the leaves of the tree inward to the root (BJS Fig. 9.10).
- **Dual prices**: solve $\mathbf w\mathbf B=\mathbf c_B$ by setting the root price to $0$ and moving outward along basic arcs with
$$w_i-w_j=c_{ij}$$
  (BT eq. 7.10 writes the same with $p_i$). For the five-node basis of BJS Fig. 9.9 with right-hand side $(2,-4,0,3,0)$ and $w_5=0$ one gets $w_4=w_3=3$, $w_2=-1$, $w_1=2$ (p. 469).
- **Reduced cost** of a nonbasic arc $(i,j)$: $c_{ij}-(p_i-p_j)$ in BT, or $z_{ij}-c_{ij}=\mathbf w\mathbf a_{ij}-c_{ij}$ in BJS, entering when positive.
- **Entering column** (BJS §9.4, p. 465-466): for nonbasic arc $(p,q)$, $\mathbf a_{pq}=\mathbf e_p-\mathbf e_q$ and $\mathbf y_{pq}=\mathbf B^{-1}\mathbf a_{pq}$ is a unit flow along the **basis equivalent chain** from $p$ to $q$ in the tree, with $+1$ on arcs traversed forward and $-1$ on arcs traversed backward. The artificial root arc never appears in another column, so its cost can be set to $0$.

## Capacitated version
Partition the nonbasic arcs into $D$ (flow $0$) and $U$ (flow $u_{ij}$). A flow is optimal when reduced costs are $\ge0$ on $D$ and $\le0$ on $U$. A violating arc closes a cycle with the tree; choose its orientation, push $\theta^*$ (BT eq. 7.11) around it and pivot (BT p. 291). BJS §9.8 reaches the same rule through the bounded-variable simplex (pp. 478-481).

## Implementation and degeneracy (BJS)
- §9.7 builds an initial basic feasible solution with an artificial root arc (Example 9.2, p. 478); Example 9.1 (p. 475) runs the algorithm.
- §9.9 shows the simplex tableau of a network (p. 481); §9.10 gives the list structures (predecessor, thread and depth indices) with which a program "sees" the tree (pp. 482-488).
- §9.11 treats degeneracy, cycling and stalling, with leaving-arc rules to avoid cycling (pp. 488-494).
- Worst case is exponential on some transportation problems, though polynomial variants exist; BJS rank network simplex and the [[Out-of-kilter algorithm]] as "by far the most effective in practice" (p. 453).
- Generalized networks with gains and losses are §9.12 (pp. 494-512, headings only).

## Special structure
On the bipartite incidence matrix of the [[Transportation problem]] the same rules read $z_{ij}-c_{ij}=u_i-v_j-c_{ij}$; for the [[Assignment problem]] every basis has degeneracy of order $m-1$. Column generation in the pricing step of network simplex is the same idea as in [[Column generation]].

**Covered in**: Bertsimas-Tsitsiklis ch. 7 §7.3 (pp. 280-291); Bazaraa-Jarvis-Sherali ch. 9 §9.3-9.11 (pp. 459-494)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 7); `text_books/Linear Optimization/BJS full book.pdf` (ch. 9).
**Last updated**: 2026-11-06

---

## Related pages
- [[Network flow problem]] · [[Simplex method]] · [[Basic feasible solution]] · [[LP duality]] · [[Linear programming]]
- [[Transportation problem]] · [[Assignment problem]] · [[Out-of-kilter algorithm]]
