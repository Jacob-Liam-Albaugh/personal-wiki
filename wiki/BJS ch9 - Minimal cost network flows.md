---
type: paper
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 9 (printed pp. 453-512)"
tags: [optimization]
authors: ["[[Mokhtar S. Bazaraa]]", "[[John J. Jarvis]]", "[[Hanif D. Sherali]]"]
year: 2010
venue: "Wiley, Linear Programming and Network Flows, 4th ed. (textbook)"
file: "Linear Optimization/BJS full book.pdf"
---

# BJS ch9 - Minimal cost network flows

**Summary**: The minimal cost network flow problem and the network simplex algorithm, which performs the simplex operations directly on a graph. A basis is a rooted spanning tree, the basis matrix is triangular with entries $0,\pm1$, so primal and dual solves are tree traversals and optimal flows are integer. See [[Network flow problem]], [[Simplex method]], [[BT ch7 - Network flows]].

**Authors**: Mokhtar S. Bazaraa, John J. Jarvis, Hanif D. Sherali · **Year**: 2010 · **File**: `Linear Optimization/BJS full book.pdf` (printed pp. 453-512). Cites use printed pages; pdf = printed + 16.

## Overview (p. 453)
The network simplex algorithm solves problems 200-300 times faster than a standard simplex that ignores structure other than sparsity (p. 453, text). It has worst-case exponential behavior on some transportation problems, though polynomial variants exist, and the methods of this chapter and [[BJS ch11 - The out-of-kilter algorithm]] are "by far the most effective in practice".

## The minimal cost network flow problem (§9.1, p. 453-454)
A directed network has $m$ nodes and $n$ arcs (p. 454, image seen). Each node $i$ has a number $b_i$: supply if $b_i>0$ (a source), demand if $b_i<0$ (a sink), and a transshipment node if $b_i=0$. Each arc $(i,j)$ carries flow $x_{ij}\ge0$ at unit cost $c_{ij}$. Supply equals demand, $\sum b_i=0$, else a dummy demand node with zero-cost arcs is added. The problem is (9.1), p. 454:
$$\min\ \sum_{i=1}^m\sum_{j=1}^mc_{ij}x_{ij}$$
$$\sum_{j=1}^mx_{ij}-\sum_{k=1}^mx_{ki}=b_i,\quad i=1,\dots,m$$
$$x_{ij}\ge0$$
The constraints are the flow conservation (nodal balance, Kirchhoff) equations: net flow out of node $i$ equals $b_i$. Without upper bounds the problem is uncapacitated, with upper bounds on arcs capacitated (§9.8). Applications include logistics, communication networks, supply chains, oil pipelines and tanker scheduling (p. 454).

## Graph terminology and the constraint matrix (§9.2-9.3, p. 455-465)
Graph definitions, chains, cycles, trees and spanning trees (p. 455-459, Figures 9.2-9.3, headings only) are followed by properties of the node-arc incidence matrix $\mathbf A$ (§9.3, p. 459-465). Its rank is $m-1$ for a connected graph, so one dependent row is removed or an artificial **root arc** is added to a node. The text (p. 462-463) argues that the columns of a basis cannot contain a cycle, because a cycle gives a linearly dependent set of columns (Figure 9.6, p. 462, figure not viewed), so the basis graph with $m$ nodes and $m-1$ arcs plus the root is a tree.

> [!theorem] Theorem 9.1 (p. 463, text)
> For a minimum-cost network flow problem on a connected digraph $G$ with one root arc, $\mathbf B$ is a basis matrix iff it is the node-arc incidence matrix of a rooted spanning tree of $G$.

With several components or several root arcs, a basis is a rooted spanning forest, but the problem can be transformed (§9.7) to a connected digraph with one root arc (p. 463, text). Each basis is lower triangular with $\pm1$ on the diagonal after permutation, entries being $0,\pm1$. The text lists the consequences for solving $\mathbf B\mathbf x_B=\mathbf b$ and $\mathbf w\mathbf B=\mathbf c_B$ (triangularity, integrality, total unimodularity, p. 463, only the first feature read). The section is titled "Triangularity, Integrality, and Total Unimodularity" (p. 463); only the triangularity part was read.

## Representing a nonbasic column (§9.4, p. 465-466)
For a nonbasic arc $(p,q)$ the column is $\mathbf a_{pq}=\mathbf e_p-\mathbf e_q$ and $\mathbf y_{pq}$ solves $\mathbf B\mathbf y_{pq}=\mathbf a_{pq}$ (p. 466, text and p. 469, image seen). This is a flow of one unit along the **basis equivalent chain** from $p$ to $q$ in the tree. The coefficients of $\mathbf y_{pq}$ are $+1$ on tree arcs traversed forward and $-1$ on those traversed backward. The artificial arc never appears in another column, so its cost can be set to $0$ (p. 466).

## Network simplex method (§9.5, p. 466-475)
The steps are the usual ones, specialized to the tree (p. 466-469). Assume a starting feasible basis and one root arc.
- **Primal values.** Solve $\mathbf B\mathbf x_B=\mathbf b$ by working inward from the leaves of the basis tree toward the root (Figure 9.10).
- **Dual variables.** Solve $\mathbf w\mathbf B=\mathbf c_B$ (p. 469, image seen). Set the root node's dual to zero and move outward along basic arcs using
$$w_i-w_j=c_{ij}$$
For the five-node basis of Figure 9.9 (p. 469, image seen) the triangular system $\mathbf w\mathbf B=\mathbf c_B$ has right-hand side $(2,-4,0,3,0)$, and starting from $w_5=0$ one gets $w_4=3$, $w_3=3$, $w_2=-1$, $w_1=2$.
- **Reduced costs.** For a nonbasic arc, $z_{ij}-c_{ij}=\mathbf w\mathbf a_{ij}-c_{ij}$ (p. 469, image seen); enter an arc with $z_{ij}-c_{ij}>0$.
- **Leaving arc.** The remaining steps (entering arc, blocking arc, pivot) are described in the text on p. 470-475 and were not read in detail; with a tree basis the entering arc closes a unique cycle.

## Example, initial solution, bounds (§9.6-9.8, p. 475-481)
Example 9.1 (p. 475) runs the algorithm. §9.7 finds an initial basic feasible solution with an artificial root arc (Example 9.2, p. 478). §9.8 adds lower and upper bounds, using the bounded-variable simplex of [[BJS ch5 - Special simplex implementations and optimality conditions]] (p. 478-481). Headings only for these.

## Tableau, list structures, degeneracy, generalized networks (§9.9-9.12, p. 481-512)
§9.9 shows the simplex tableau associated with a network (p. 481). §9.10 gives list structures (predecessor, thread and depth indices, p. 482-488) by which the computer "sees" the tree. §9.11 treats degeneracy, cycling and stalling (p. 488-494), with rules on the choice of the leaving arc to avoid cycling (not read). §9.12 covers generalized network problems with gains and losses (p. 494-512, headings only). Exercises and notes follow.

## Notes
- Wiki note: [[BT ch7 - Network flows]] covers the same network flow problem and its simplex specialization.
- Wiki note: the transportation and assignment problems are special cases ([[BJS ch10 - Transportation and assignment problems]]), and maximal flow and shortest path are in [[BJS ch12 - Maximal flow shortest path multicommodity flow and network synthesis]].

**Sources**: `Linear Optimization/BJS full book.pdf` (pdf 469-528, printed pp. 453-512). Pages viewed as images: pdf 470 (printed 454) and 485 (469). Everything else read from the text layer, which garbles math, and from headings.
**Last updated**: 2026-11-06

---

## Related pages
- [[Network flow problem]] · [[Simplex method]] · [[Linear programming]] · [[Basic feasible solution]]
- [[BJS ch5 - Special simplex implementations and optimality conditions]] · [[BJS ch10 - Transportation and assignment problems]] · [[BJS ch11 - The out-of-kilter algorithm]] · [[BT ch7 - Network flows]]
