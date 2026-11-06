---
type: method
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, §12.4-12.6"
tags: [optimization]
---

# Multicommodity flow

> [!definition] Minimal cost multicommodity flow (source: BJS full book.pdf, p. 641)
> Commodities $i=1,\dots,t$, arc capacity $\mathbf u$ shared by all, individual bounds $\mathbf u_i$:
> $$\min\ \sum_{i=1}^t\mathbf c_i\mathbf x_i\quad\text{s.t. }\sum_{i=1}^t\mathbf x_i\le\mathbf u,\ \ \mathbf A\mathbf x_i=\mathbf b_i,\ \ \mathbf 0\le\mathbf x_i\le\mathbf u_i$$

**Intuition**: a [[Network flow problem]] whose units are of different types, each with its own supplies and demands. A single-commodity model cannot tell them apart (BJS p. 607). Integer flows are not guaranteed although it is still an LP: in BJS Fig. 12.9 (pp. 639-640) three commodities on a triangle with unit capacities each have a single path, so sending one unit of any commodity blocks the others (total flow $1$) whereas half a unit of each gives total flow $3/2$.

## Key facts
- The node-arc formulation has the block diagonal structure of [[Dantzig-Wolfe decomposition]] (BJS §7.5), the shared capacity rows being the coupling constraints, so decomposition applies; subproblems are single-commodity network flow problems (BJS Figs. 12.14-12.15, p. 649). The constraint matrix is large even for moderate sizes (p. 641).
- **Basis characterization** (BJS §12.5, pp. 649-654): with an artificial column per commodity the matrix has coupling rows plus one $\mathbf A$ block per commodity (p. 649).

> [!theorem] Theorem 12.3 (BJS p. 652)
> A transformed basis matrix for the multicommodity minimal cost flow problem corresponds to a rooted spanning tree for each commodity plus a set of cycles and slack arcs.

This allows the simplex method to be applied directly (BJS Exercise 12.61, p. 652), with an example in Figs. 12.16-12.18 (pp. 652-654).

## Synthesis of multiterminal flow networks (BJS §12.6, pp. 654-662)
A design problem rather than an analysis problem. Given potential arcs $\mathcal A'$ with cost $c_{ij}$ per unit capacity and requirements $r_{ij}\ge0$ between node pairs, choose capacities $u_{ij}\ge0$ minimizing $\sum c_{ij}u_{ij}$ so that the maximum flow ([[Maximum flow problem]]) between each pair is at least $r_{ij}$ (p. 655). The first reduction replaces the $m(m-1)/2$ requirement constraints by those on the **dominant requirement tree** $T_r$, the maximum weight spanning tree of the complete graph with weights $r_{ij}$ (pp. 655-656). Build it greedily: sort $r_{ij}$ in decreasing order, take each arc unless it forms a cycle with those chosen, stop after $m-1$ arcs. In BJS's five-node example with $r_{45}=12$, $r_{34}=8$, $r_{24}=7$, $r_{13}=5$ the selected arcs are $(4,5),(3,4),(2,4),(1,3)$. The rest of the section was not read.

**Covered in**: Bazaraa-Jarvis-Sherali ch. 12 §12.4-12.6 (pp. 639-662)
**Sources**: `text_books/Linear Optimization/BJS full book.pdf` (ch. 12; math from a garbled text layer, reconstructed and not checked against an image).
**Last updated**: 2026-11-06

---

## Related pages
- [[Network flow problem]] · [[Dantzig-Wolfe decomposition]] · [[Maximum flow problem]] · [[Shortest path problem]]
- [[Linear programming]] · [[Simplex method]]
