---
type: paper
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 11 (printed pp. 567-606)"
tags: [optimization]
authors: ["[[Mokhtar S. Bazaraa]]", "[[John J. Jarvis]]", "[[Hanif D. Sherali]]"]
year: 2010
venue: "Wiley, Linear Programming and Network Flows, 4th ed. (textbook)"
file: "Linear Optimization/BJS full book.pdf"
---

# BJS ch11 - The out-of-kilter algorithm

**Summary**: A primal-dual method for minimal cost network flow that starts dual feasible and drives every arc "into kilter", that is, toward complementary slackness. The chapter derives the circulatory formulation, its dual and the optimality conditions (Theorem 11.1), then gives the primal phase (flow change on a cycle), the dual phase (change of node potentials), a labeling implementation and a finiteness argument, and closes with relaxation algorithms. See [[Network flow problem]], [[LP duality]], [[BJS ch9 - Minimal cost network flows]].

**Authors**: Mokhtar S. Bazaraa, John J. Jarvis, Hanif D. Sherali · **Year**: 2010 · **File**: `Linear Optimization/BJS full book.pdf` (printed pp. 567-606). Cites use printed pages; pdf = printed + 16.

## Overview (p. 567)
It is another method for minimal cost network flow, similar to the primal-dual algorithm in starting from dual feasibility, but unlike a strict primal-dual method it does not always maintain complementary slackness; attaining it is the principal thrust (p. 567, image seen). State-of-the-art primal simplex codes run two to three times faster than traditional out-of-kilter codes, while primal-dual methods built on its ingredients run two to four times faster than the best primal simplex code, with larger speedups on large problems (p. 567, image seen).

## Circulatory formulation (§11.1, p. 567-569)
The form used is (11.1), p. 567 (image seen):
$$\min\ \sum_{i=1}^m\sum_{j=1}^mc_{ij}x_{ij}$$
$$\sum_{j=1}^mx_{ij}-\sum_{k=1}^mx_{ki}=0,\quad i=1,\dots,m$$
$$\ell_{ij}\le x_{ij}\le u_{ij}$$
over existing arcs. A flow satisfying the equalities is a **conserving flow**, and one that also meets the bounds is a **feasible flow**. Data are integers with $-\infty<\ell_{ij}<u_{ij}<\infty$ (p. 568, text). With zero right-hand sides, flow circulates along circuits, hence "circulatory network flow problem". The formulation is equivalent to that of [[BJS ch9 - Minimal cost network flows]]: a general right-hand side $\mathbf b$ can be handled by replacing each $|b_i|$ by a bounded variable, or by shifting to $\mathbf x=\mathbf y-\bar{\mathbf y}$ from any flow-conserving $\bar{\mathbf y}$ (p. 568, text, Exercises 11.1-11.3).

## The dual and optimality conditions (p. 569-570)
Attach $w_i$ to the conservation equation of node $i$, $h_{ij}$ to $x_{ij}\le u_{ij}$ and $v_{ij}$ to $x_{ij}\ge\ell_{ij}$. The dual (p. 569, image seen):
$$\max\ \sum_{i,j}\ell_{ij}v_{ij}-\sum_{i,j}u_{ij}h_{ij}$$
$$w_i-w_j+v_{ij}-h_{ij}=c_{ij}$$
$$h_{ij},v_{ij}\ge0,\qquad w_i\ \text{unrestricted}$$
For any integer $\mathbf w$ the dual is feasible with
$$v_{ij}=\max\{0,\ c_{ij}-w_i+w_j\}$$
$$h_{ij}=\max\{0,\ -(c_{ij}-w_i+w_j)\}$$
and these values are optimal for fixed $\mathbf w$ (p. 569, image seen). Complementary slackness (p. 569, image seen):
$$(x_{ij}-\ell_{ij})\,v_{ij}=0$$
$$(u_{ij}-x_{ij})\,h_{ij}=0$$
Define $z_{ij}-c_{ij}\equiv w_i-w_j-c_{ij}$. Then $v_{ij}=\max\{0,-(z_{ij}-c_{ij})\}$ and $h_{ij}=\max\{0,z_{ij}-c_{ij}\}$, and no basis is implied by this notation (p. 569-570, image seen).

> [!theorem] Theorem 11.1 (p. 570, image seen)
> Let $\mathbf x$ be any conserving flow and $\mathbf w$ any integer vector. Then $\mathbf x$ and $\mathbf w$ are primal and dual optimal for (11.1) iff, for all $(i,j)$,
> $$z_{ij}-c_{ij}<0\ \Rightarrow\ x_{ij}=\ell_{ij}$$
> $$z_{ij}-c_{ij}>0\ \Rightarrow\ x_{ij}=u_{ij}$$
> $$z_{ij}-c_{ij}=0\ \Rightarrow\ \ell_{ij}\le x_{ij}\le u_{ij}$$

The algorithm searches over $\mathbf w$ and conserving $\mathbf x$ until these three conditions hold. An arc satisfying them is **in kilter**, otherwise **out of kilter**. In Figure 11.1 (p. 570, image seen), with $\mathbf w=\mathbf 0$ and $\mathbf x=\mathbf 0$, arc $(1,2)$ has $z_{12}-c_{12}=-2$ and $x_{12}=0=\ell_{12}$ so it is in kilter, while arc $(2,3)$ has $z_{23}-c_{23}=3$ and $x_{23}=0<u_{23}$ so it is out of kilter. The **primal phase** changes flows to bring arcs into kilter and the **dual phase** changes the $w_i$.

## Kilter states and numbers (p. 571-573, text)
An arc's state is read from a table (Figure 11.2) crossing the sign of $z_{ij}-c_{ij}$ with the position of $x_{ij}$ relative to $\ell_{ij}$ and $u_{ij}$. Changing the flow moves an arc up or down a column of the table, changing $\mathbf w$ moves it along a row. The **kilter number** $K_{ij}$ is the minimal change of flow on the arc needed to bring it into kilter (Figure 11.3, p. 572-573), nonnegative and zero iff the arc is in kilter. Finite convergence follows if no kilter number ever increases and, at finite intervals, some kilter number drops by an integer (p. 573, text).

## Strategy (§11.2, p. 573-586)
Generic steps (p. 573-574, text):
1. Start with a conserving flow ($x_{ij}=0$) and dual $\mathbf w$ ($w_i=0$), with $v_{ij},h_{ij}$ as above; find states and kilter numbers.
2. If an arc is out of kilter, do a **primal phase**: construct a new conserving flow that improves the kilter number of the selected arc and worsens none.
3. If that is impossible, build a new dual solution that worsens no kilter number, and return to step 2.
4. Iterating ends in an optimal solution or a proof that no feasible solution exists.

**Primal phase** (p. 574-575, text). Figure 11.4 lists, for each state, the permitted direction and amount of flow change. Since $\mathbf A\Delta\mathbf x=\mathbf0$ and each column of the incidence matrix has one $+1$ and one $-1$, flow must change along a cycle (not necessarily directed). The book builds an auxiliary network $G'$ containing the arcs whose flow may be changed, in the permitted direction, and looks for a cycle through the selected out-of-kilter arc.

**Dual phase** (p. 586-587, text layer, formulas garbled). Let $X$ be the set of nodes reachable in $G'$ from the labeled start node $q$, and $\bar X$ its complement. Define
$$S_1=\{(i,j):i\in X,\ j\in\bar X,\ z_{ij}-c_{ij}<0,\ x_{ij}<u_{ij}\}$$
$$S_2=\{(i,j):i\in\bar X,\ j\in X,\ z_{ij}-c_{ij}>0,\ x_{ij}>\ell_{ij}\}$$
and $\delta=\min$ of $|z_{ij}-c_{ij}|$ over $S_1\cup S_2$, with the book's exact index sets taken from the text (**[unverified]**, the set definitions and signs were read from the garbled text layer). If $\delta=\infty$, stop: no feasible solution exists. Otherwise $w_i$ is increased by $\delta$ on $X$ and the $z-c$ values on arcs crossing between $X$ and $\bar X$ change by $\pm\delta$ accordingly. The finiteness argument: after the change, the new $S_1\subseteq S_1$ and $S_2\subseteq S_2$ with at least one strict inclusion (at least one arc drops), so the sets shrink a finite number of times (p. 586, text).

## Summary, example, labeling (§11.3-11.5, p. 586-591)
The complete algorithm has an initialization phase (integer flow and integer $\mathbf w$, compute $z_{ij}-c_{ij}$), a primal phase and a dual phase (p. 586-587, text). Example in §11.4 on the network of Figure 11.12 with arcs labelled $(\ell_{ij},u_{ij},c_{ij})$, e.g. $(0,4,-3)$ and $(2,5,-1)$ (p. 587-588, text). §11.5 (p. 589-591, text) gives a labeling procedure: each node $j$ carries a label $(+i,\Delta_j)$ or $(-i,\Delta_j)$ meaning flow on arc $(i,j)$ may be increased, or on arc $(j,i)$ decreased, by $\Delta_j$ without worsening any kilter number. It starts from the selected out-of-kilter arc, extends labels along arcs permitted by Figure 11.4 and, on breakthrough, changes flow around the cycle by the final $\Delta$.

## Primal and dual objective values (§11.6, p. 591-593)
Define the infeasibility $P_{ij}(x_{ij})=\max\{0,\ell_{ij}-x_{ij}\}+\max\{0,x_{ij}-u_{ij}\}$ and a primal penalty function $f(\mathbf x)=\mathbf c\mathbf x+M\sum P_{ij}(x_{ij})$ with $M$ large, similar to a big-M objective (eq. 11.12a, p. 591, image not seen, text). The book uses the primal and dual values to give a convergence argument that need not stay on one arc until it comes into kilter (p. 591-593, text). If the penalty term is positive at termination, the dual is unbounded and the primal is infeasible (p. 593, text). In the Section 11.4 example, $M\ge84$ is computed and $M=85$ taken, and the dual objective rises from $-15$ to $-3$ to $0$ over the two dual phases, with a primal penalty value of $4M=340$ at the start (p. 593, text, numbers as read from the text layer, **[unverified]**).

## Relaxation algorithms (§11.7, p. 593-)
A competitive class of primal-dual methods using a Lagrangian relaxation framework (p. 593-594, text). For the problem $\min\{\mathbf c\mathbf x:\mathbf A\mathbf x=\mathbf b,\ \mathbf 0\le\mathbf x\le\mathbf u\}$, the Lagrangian dual function is
$$\theta(\mathbf w)=\mathbf w\mathbf b+\min\{(\mathbf c-\mathbf w\mathbf A)\mathbf x:\ \mathbf 0\le\mathbf x\le\mathbf u\}$$
(eq. 11.15b, p. 594, text). The inner minimum sets $x_{ij}=u_{ij}$ when the arc coefficient is positive and $x_{ij}=0$ when it is negative, with freedom when it is zero. If the resulting pseudoflow satisfies $\mathbf A\mathbf x=\mathbf b$ it is optimal. Otherwise some nodes have net excess supply $e(i)>0$ and others unsatisfied demand $e(i)<0$, and the algorithm tries to dissipate the excess along incident arcs on which the relaxed problem leaves the flow free (p. 594, text; the rest of the section, p. 595-598, was not read). Exercises and notes follow (p. 598-606).

## Notes
- Wiki note: the three conditions of Theorem 11.1 are the complementary slackness conditions of [[LP duality]] for the bounded-variable network LP, in the sense of [[KKT conditions]].
- Wiki note: [[BT ch7 - Network flows]] treats the same network flow problem.

**Sources**: `Linear Optimization/BJS full book.pdf` (pdf 583-622, printed pp. 567-606). Pages viewed as images: pdf 583 (printed 567), 585 (569), 586 (570). The rest (kilter tables, primal phase, dual phase, labeling, penalty function, relaxation) read from the text layer, with garbled math, so the corresponding statements are paraphrased rather than transcribed.
**Last updated**: 2026-11-06

---

## Related pages
- [[Network flow problem]] · [[LP duality]] · [[KKT conditions]] · [[Linear programming]]
- [[BJS ch9 - Minimal cost network flows]] · [[BJS ch10 - Transportation and assignment problems]] · [[BJS ch12 - Maximal flow shortest path multicommodity flow and network synthesis]] · [[BT ch7 - Network flows]]
