---
type: method
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 11"
tags: [optimization]
---

# Out-of-kilter algorithm

> [!definition] Circulatory formulation (source: BJS full book.pdf, p. 567, eq. 11.1)
> $$\min\ \sum_{i=1}^m\sum_{j=1}^mc_{ij}x_{ij}$$
> $$\sum_{j=1}^mx_{ij}-\sum_{k=1}^mx_{ki}=0,\quad i=1,\dots,m,\qquad\ell_{ij}\le x_{ij}\le u_{ij}$$
> A flow meeting the equalities is **conserving**; one that also meets the bounds is **feasible**. Data are integers with $-\infty<\ell_{ij}<u_{ij}<\infty$ (p. 568).

**Intuition**: a primal-dual method for the minimal cost [[Network flow problem]] that starts dual feasible and drives every arc "into kilter", i.e. toward complementary slackness; unlike a strict primal-dual method it does not always maintain complementary slackness, attaining it is the point (p. 567). It is equivalent to the general-supply form: a right-hand side $\mathbf b$ is handled by replacing each $|b_i|$ with a bounded variable, or by shifting $\mathbf x=\mathbf y-\bar{\mathbf y}$ from a flow-conserving $\bar{\mathbf y}$ (p. 568, Exercises 11.1-11.3). BT's min cost flow with return arcs is the same circulation device ([[Network flow problem]]; [[Maximum flow problem]]). BJS report primal simplex codes two to three times faster than traditional out-of-kilter codes, while primal-dual codes built on its ingredients run two to four times faster than the best primal simplex code (p. 567).

## Dual and optimality conditions (BJS pp. 569-570)
Attach $w_i$ to conservation at node $i$, $h_{ij}$ to $x_{ij}\le u_{ij}$, $v_{ij}$ to $x_{ij}\ge\ell_{ij}$:
$$\max\ \sum_{i,j}\ell_{ij}v_{ij}-\sum_{i,j}u_{ij}h_{ij}\quad\text{s.t. }w_i-w_j+v_{ij}-h_{ij}=c_{ij},\ h_{ij},v_{ij}\ge0$$
For any integer $\mathbf w$ the dual is feasible with
$$v_{ij}=\max\{0,\ c_{ij}-w_i+w_j\},\qquad h_{ij}=\max\{0,\ -(c_{ij}-w_i+w_j)\}$$
optimal for fixed $\mathbf w$. Complementary slackness:
$$(x_{ij}-\ell_{ij})v_{ij}=0,\qquad(u_{ij}-x_{ij})h_{ij}=0$$
With $z_{ij}-c_{ij}\equiv w_i-w_j-c_{ij}$ (no basis implied), $v_{ij}=\max\{0,-(z_{ij}-c_{ij})\}$ and $h_{ij}=\max\{0,z_{ij}-c_{ij}\}$.

> [!theorem] Theorem 11.1 (BJS p. 570)
> A conserving flow $\mathbf x$ and integer $\mathbf w$ are primal and dual optimal iff for all $(i,j)$
> $$z_{ij}-c_{ij}<0\Rightarrow x_{ij}=\ell_{ij},\qquad z_{ij}-c_{ij}>0\Rightarrow x_{ij}=u_{ij},\qquad z_{ij}-c_{ij}=0\Rightarrow\ell_{ij}\le x_{ij}\le u_{ij}$$

These are the complementary slackness conditions of [[LP duality]] for the bounded-variable network LP ([[KKT conditions]]). An arc satisfying them is **in kilter**, otherwise **out of kilter**. In BJS Fig. 11.1 with $\mathbf w=\mathbf 0$, $\mathbf x=\mathbf 0$, arc $(1,2)$ has $z_{12}-c_{12}=-2$ and $x_{12}=0=\ell_{12}$ (in kilter) while arc $(2,3)$ has $z_{23}-c_{23}=3$ and $x_{23}=0<u_{23}$ (out of kilter).

## Kilter states and numbers (pp. 571-573)
An arc's state comes from a table (Fig. 11.2) crossing the sign of $z_{ij}-c_{ij}$ with the position of $x_{ij}$ against $\ell_{ij},u_{ij}$; changing the flow moves an arc along a column of the table, changing $\mathbf w$ along a row. The **kilter number** $K_{ij}$ is the minimal flow change on the arc that brings it into kilter (Fig. 11.3), nonnegative and zero iff in kilter. Finite convergence follows if no kilter number ever increases and, at finite intervals, some kilter number drops by an integer.

## The algorithm (§11.2-11.5, pp. 573-591)
> [!algorithm] Out-of-kilter
> 1. Start with a conserving flow ($x_{ij}=0$) and dual $w_i=0$ with $v_{ij},h_{ij}$ as above; find states and kilter numbers.
> 2. **Primal phase**: for a selected out-of-kilter arc, build a new conserving flow that improves its kilter number and worsens none.
> 3. If impossible, **dual phase**: build a new $\mathbf w$ worsening no kilter number, and return to step 2.
> 4. End in an optimal solution or a proof that no feasible solution exists.

- **Primal phase** (pp. 574-575): Fig. 11.4 lists for each state the permitted direction and size of flow change. Since $\mathbf A\Delta\mathbf x=\mathbf0$ and each incidence column has one $+1$ and one $-1$, flow must change around a (not necessarily directed) cycle. The book builds an auxiliary network $G'$ of arcs whose flow may change in the permitted direction and searches for a cycle through the selected arc.
- **Dual phase** (pp. 586-587; formulas read from a garbled text layer, **[unverified]**): let $X$ be the nodes reachable in $G'$ from the labeled start node and $\bar X$ the rest. With
$$S_1=\{(i,j):i\in X,\ j\in\bar X,\ z_{ij}-c_{ij}<0,\ x_{ij}<u_{ij}\}$$
$$S_2=\{(i,j):i\in\bar X,\ j\in X,\ z_{ij}-c_{ij}>0,\ x_{ij}>\ell_{ij}\}$$
  and $\delta=\min|z_{ij}-c_{ij}|$ over $S_1\cup S_2$: if $\delta=\infty$ stop, no feasible solution exists; else raise $w_i$ by $\delta$ on $X$. The new $S_1,S_2$ are subsets of the old with at least one strict inclusion, so they shrink finitely often.
- **Labeling** (§11.5, pp. 589-591): node $j$ carries a label $(+i,\Delta_j)$ or $(-i,\Delta_j)$ meaning flow on arc $(i,j)$ may be increased, or on $(j,i)$ decreased, by $\Delta_j$ without worsening any kilter number. Labels start at the selected arc, extend along arcs permitted by Fig. 11.4, and on breakthrough the flow changes around the cycle by the final $\Delta$.
- **Example** (§11.4, pp. 587-588): the network of Fig. 11.12 with arcs labelled $(\ell_{ij},u_{ij},c_{ij})$, e.g. $(0,4,-3)$ and $(2,5,-1)$.

## Objective values and penalty (§11.6, pp. 591-593)
Define infeasibility $P_{ij}(x_{ij})=\max\{0,\ell_{ij}-x_{ij}\}+\max\{0,x_{ij}-u_{ij}\}$ and primal penalty function $f(\mathbf x)=\mathbf c\mathbf x+M\sum P_{ij}(x_{ij})$ with $M$ large, as in a big-M objective (eq. 11.12a, read from text). It supports a convergence argument that need not stay on one arc until it is in kilter; a positive penalty at termination means the dual is unbounded and the primal infeasible. In the Fig. 11.12 example $M\ge84$ is computed and $M=85$ taken; the dual objective rises $-15\to-3\to0$ over two dual phases, with starting primal penalty value $4M=340$ (text-layer numbers, **[unverified]**).

## Relaxation algorithms (§11.7, pp. 593-598)
A competitive class of primal-dual methods in a Lagrangian relaxation framework. For $\min\{\mathbf c\mathbf x:\mathbf A\mathbf x=\mathbf b,\ \mathbf 0\le\mathbf x\le\mathbf u\}$ the dual function is
$$\theta(\mathbf w)=\mathbf w\mathbf b+\min\{(\mathbf c-\mathbf w\mathbf A)\mathbf x:\ \mathbf 0\le\mathbf x\le\mathbf u\}$$
(eq. 11.15b, read from text). The inner minimum sets $x_{ij}=u_{ij}$ where the coefficient is positive and $0$ where negative (free if zero). If the resulting pseudoflow satisfies $\mathbf A\mathbf x=\mathbf b$ it is optimal; otherwise some nodes have excess supply $e(i)>0$ and others unmet demand $e(i)<0$, and the algorithm tries to dissipate excess along incident arcs the relaxed problem leaves free (pp. 594; pp. 595-598 not read). See [[Lagrangian relaxation]].

**Covered in**: Bazaraa-Jarvis-Sherali ch. 11 (pp. 567-598)
**Sources**: `text_books/Linear Optimization/BJS full book.pdf` (ch. 11; pdf 583, 585, 586 viewed as images, the rest from a text layer with garbled math, so dual phase, labeling and penalty are paraphrased).
**Last updated**: 2026-11-06

---

## Related pages
- [[Network flow problem]] · [[LP duality]] · [[KKT conditions]] · [[Linear programming]]
- [[Network simplex method]] · [[Maximum flow problem]] · [[Shortest path problem]] · [[Lagrangian relaxation]]
