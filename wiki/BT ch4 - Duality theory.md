---
type: paper
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 4 (printed pp. 139-200)"
tags: [optimization]
authors: ["[[Dimitris Bertsimas]]", "[[John N. Tsitsiklis]]"]
year: 1997
venue: "Athena Scientific (textbook)"
file: "Linear Optimization/MIT (ch 1-5).pdf"
---

# BT ch4 - Duality theory

**Summary**: Builds the dual of a linear program from a lower-bound (relaxation) argument, proves weak and strong [[LP duality]], complementary slackness and the dual simplex method, then uses Farkas' lemma, separating hyperplanes and cones to give a geometric proof of duality and the resolution theorem for [[Polyhedron|polyhedra]].

## Motivation: duality as a bound (§4.1, p. 141-142)
Primal in standard form: minimize $\mathbf c'\mathbf x$ subject to $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\ge\mathbf 0$. Relax the equality with a price vector $\mathbf p$ and define
$$g(\mathbf p)=\min_{\mathbf x\ge\mathbf0}\big[\mathbf c'\mathbf x+\mathbf p'(\mathbf b-\mathbf A\mathbf x)\big]$$
Because the optimal $\mathbf x^*$ is feasible, $g(\mathbf p)\le\mathbf c'\mathbf x^*$ for every $\mathbf p$. Searching for the best bound means maximizing $g$. Rewriting,
$$g(\mathbf p)=\mathbf p'\mathbf b+\min_{\mathbf x\ge\mathbf0}(\mathbf c'-\mathbf p'\mathbf A)\mathbf x$$
The inner minimum is $0$ if $\mathbf c'-\mathbf p'\mathbf A\ge\mathbf0'$ and $-\infty$ otherwise, so only those $\mathbf p$ matter and the dual is: maximize $\mathbf p'\mathbf b$ subject to $\mathbf p'\mathbf A\le\mathbf c'$ (p. 141).

## The dual problem (§4.2, p. 142-146)
Rows are $\mathbf a_i'$, columns $\mathbf A_j$. For a minimization primal the dual is a maximization, one dual variable per primal constraint and one dual constraint per primal variable (Table 4.1, p. 143):

| Primal (min) | Dual (max) |
|---|---|
| constraint $\mathbf a_i'\mathbf x\ge b_i$ | variable $p_i\ge0$ |
| constraint $\mathbf a_i'\mathbf x\le b_i$ | variable $p_i\le0$ |
| constraint $\mathbf a_i'\mathbf x=b_i$ | variable $p_i$ free |
| variable $x_j\ge0$ | constraint $\mathbf p'\mathbf A_j\le c_j$ |
| variable $x_j\le0$ | constraint $\mathbf p'\mathbf A_j\ge c_j$ |
| variable $x_j$ free | constraint $\mathbf p'\mathbf A_j=c_j$ |

Two common pairs (p. 143):
$$\min\ \mathbf c'\mathbf x:\ \mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf0\quad\longleftrightarrow\quad\max\ \mathbf p'\mathbf b:\ \mathbf p'\mathbf A\le\mathbf c'$$
$$\min\ \mathbf c'\mathbf x:\ \mathbf A\mathbf x\ge\mathbf b\quad\longleftrightarrow\quad\max\ \mathbf p'\mathbf b:\ \mathbf p'\mathbf A=\mathbf c',\ \mathbf p\ge\mathbf0$$

> [!theorem] Theorem 4.1 (p. 144)
> The dual of the dual is the primal (after turning the dual into a minimization).

> [!theorem] Theorem 4.2 (p. 146)
> Transformations of an LP (free variable to difference of nonnegatives, inequality to equality with slack, dropping a redundant equality row) do not change the dual: the duals are equivalent (both infeasible or same optimal cost).

## Weak and strong duality (§4.3, p. 146-152)
> [!theorem] Theorem 4.3, weak duality (p. 146)
> If $\mathbf x$ is primal feasible and $\mathbf p$ is dual feasible then
> $$\mathbf p'\mathbf b\le\mathbf c'\mathbf x$$

Corollary 4.2 (p. 148): if both are feasible and $\mathbf p'\mathbf b=\mathbf c'\mathbf x$, both are optimal. A feasible dual implies the primal cannot be unbounded below, and vice versa (Cor. 4.1, p. 147).

> [!theorem] Theorem 4.4, strong duality (p. 148)
> If an LP has an optimal solution, so does its dual, and the optimal costs are equal.

Proof idea for standard form with full-row-rank $\mathbf A$ (p. 148): run the simplex method with an anticycling rule ([[BT ch3 - The simplex method]]) to an optimal basis $\mathbf B$. Optimality gives $\mathbf c'-\mathbf c_B'\mathbf B^{-1}\mathbf A\ge\mathbf0'$. Set $\mathbf p'=\mathbf c_B'\mathbf B^{-1}$. Then $\mathbf p'\mathbf A\le\mathbf c'$ (dual feasible) and
$$\mathbf p'\mathbf b=\mathbf c_B'\mathbf B^{-1}\mathbf b=\mathbf c'\mathbf x$$
so $\mathbf p$ is optimal by Cor. 4.2. The general case reduces to this one by Theorem 4.2.

Possible primal/dual status pairs (Table 4.2, p. 151): both finite optimal; primal unbounded with dual infeasible and vice versa; both infeasible is possible (Example 4.5, p. 151). Clark's theorem (Exercise 4.21): unless both are infeasible, at least one has an unbounded feasible set.

> [!theorem] Theorem 4.5, complementary slackness (p. 151)
> Feasible $\mathbf x$ and $\mathbf p$ are optimal if and only if
> $$p_i(\mathbf a_i'\mathbf x-b_i)=0\quad\forall i$$
> $$(c_j-\mathbf p'\mathbf A_j)x_j=0\quad\forall j$$

Meaning: a dual variable can be nonzero only on a binding primal constraint, and a primal variable can be nonzero only where its dual constraint is tight. Used to recover one optimal solution from the other.

## Dual variables as marginal costs (§4.4, p. 155-156)
If $\mathbf x^*$ is a nondegenerate optimal BFS with basis $\mathbf B$ and $\mathbf b$ is perturbed to $\mathbf b+\mathbf d$ with $\mathbf d$ small, the same basis stays optimal (reduced costs do not depend on $\mathbf b$). The optimal cost becomes $\mathbf p'(\mathbf b+\mathbf d)$, so $p_i$ is the marginal cost (shadow price) of the $i$th requirement (p. 156). The diet-problem reading: $\mathbf p$ prices nutrients, and duality says the food market and nutrient market value the ideal food identically (p. 156).

## Dual simplex method (§4.5, p. 156-164)
The primal simplex keeps primal feasibility and works toward dual feasibility; a dual algorithm does the reverse (p. 157). Start from a tableau with all reduced costs $r_j\ge0$ (dual feasible, so $\mathbf p'=\mathbf c_B'\mathbf B^{-1}$ satisfies $\mathbf p'\mathbf A\le\mathbf c'$) but possibly $\mathbf B^{-1}\mathbf b\not\ge\mathbf 0$ (p. 157).

1. If $\mathbf B^{-1}\mathbf b\ge\mathbf0$, stop: optimal for both.
2. Pick a row $\ell$ with $x_{B(\ell)}<0$ (pivot row, entries $v_i$).
3. If no $v_i<0$, the dual is unbounded and the primal infeasible.
4. Else the entering column $j$ minimizes the ratio (eq. 4.2, p. 158):
$$\frac{r_j}{|v_j|}=\min_{\{i:\,v_i<0\}}\frac{r_i}{|v_i|}$$
5. Pivot as usual. New reduced costs $r_i+(r_j/|v_j|)v_i\ge0$, so dual feasibility is kept.

Example 4.7 (p. 158) works one pivot. The method moves between basic feasible solutions of the dual; dual degeneracy and the relation between primal and dual bases are discussed on p. 160-164 (Examples 4.8-4.9). Revised version: Exercise 4.23.

## Farkas' lemma (§4.6, p. 165-167)
> [!theorem] Theorem 4.6, Farkas' lemma (p. 165)
> Exactly one holds: (a) there is $\mathbf x\ge\mathbf0$ with $\mathbf A\mathbf x=\mathbf b$; (b) there is $\mathbf p$ with $\mathbf p'\mathbf A\ge\mathbf0'$ and $\mathbf p'\mathbf b<0$.

A vector in (b) is a certificate of infeasibility. Proof by duality (p. 165): if (b) held with a feasible $\mathbf x$, then $\mathbf p'\mathbf b=\mathbf p'\mathbf A\mathbf x\ge0$, a contradiction. If (a) fails, the pair "maximize $\mathbf 0'\mathbf x$ s.t. $\mathbf A\mathbf x=\mathbf b,\mathbf x\ge\mathbf0$" and "minimize $\mathbf p'\mathbf b$ s.t. $\mathbf p'\mathbf A\ge\mathbf0'$" has an infeasible first member, the second is feasible ($\mathbf p=\mathbf0$), so it is unbounded and yields the certificate. Geometrically (a) says $\mathbf b$ lies in the cone generated by the columns of $\mathbf A$.

Consequences: Corollary 4.3 and Theorem 4.7 (p. 166-167) give the same alternative for inequality systems $\mathbf A\mathbf x\le\mathbf b$; Theorem 4.8 (p. 168) reads the result as absence of arbitrage in a one-period market.

## Separating hyperplanes (§4.7, p. 169-172)
Closedness of polyhedra is proved first, then Weierstrass' theorem (Thm 4.10, p. 170: a continuous function on a nonempty closed bounded set attains its extremes).

> [!theorem] Theorem 4.11, separating hyperplane (p. 170)
> If $S\subset\mathbb R^n$ is nonempty, closed and convex and $\mathbf x^*\notin S$, there is $\mathbf c$ with $\mathbf c'\mathbf x^*<\mathbf c'\mathbf x$ for all $\mathbf x\in S$.

The proof minimizes the Euclidean distance to $\mathbf x^*$ over $S$ intersected with a ball. §4.7 then uses this to re-derive Farkas' lemma and strong duality without the simplex method. See [[Convex set]].

## Cones, extreme rays, resolution theorem (§4.8-4.9, p. 174-183)
- Definition 4.1 (p. 174): $C$ is a cone if $\lambda\mathbf x\in C$ for all $\lambda\ge0$, $\mathbf x\in C$.
- Extreme rays of a pointed polyhedral cone and of the recession cone (Def. 4.2, Thm 4.12-4.14, p. 175-178). Theorem 4.13-4.14 tie optimality of a linear cost over a pointed polyhedron to extreme points and rays.
- When the simplex method ends with an unboundedness certificate (a column of $\mathbf B^{-1}\mathbf A$ with no positive entry), the $j$th basic direction is an extreme ray of the recession cone (p. 179).

> [!theorem] Theorem 4.15, resolution theorem (p. 179)
> Let $P=\{\mathbf x\mid\mathbf A\mathbf x\ge\mathbf b\}$ be nonempty with at least one extreme point, extreme points $\mathbf x^1,\dots,\mathbf x^k$ and a complete set of extreme rays $\mathbf w^1,\dots,\mathbf w^r$. Then $P=Q$ with
> $$Q=\Big\{\sum_i\lambda_i\mathbf x^i+\sum_j\theta_j\mathbf w^j\ \Big|\ \lambda_i,\theta_j\ge0,\ \sum_i\lambda_i=1\Big\}$$

Corollaries (p. 182-183): a bounded polyhedron is the convex hull of its extreme points; Theorem 4.16: a finitely generated set is a polyhedron (the converse of the resolution theorem). Example 4.10 (p. 181) decomposes an unbounded polyhedron. This representation is the basis of Dantzig-Wolfe decomposition in [[BT ch6 - Large scale optimization]].

## General duality (§4.10, p. 183-186)
Primal: minimize $\mathbf c'\mathbf x$ s.t. $\mathbf A\mathbf x\ge\mathbf b$, $\mathbf x\in P$ with $P=\{\mathbf x\mid\mathbf D\mathbf x\ge\mathbf d\}$. Dual objective (eq. 4.7, p. 184):
$$g(\mathbf p)=\min_{\mathbf x\in P}\big[\mathbf c'\mathbf x+\mathbf p'(\mathbf b-\mathbf A\mathbf x)\big]$$
Dual: maximize $g(\mathbf p)$ subject to $\mathbf p\ge\mathbf0$. Theorem 4.17 (weak duality): $g(\mathbf p)\le\mathbf c'\mathbf x$ for feasible pairs. Theorem 4.18 (strong duality): if the primal has an optimal solution, so does the dual and the costs are equal (p. 184). This leaves some constraints un-priced, which is the idea behind decomposition and Lagrangean relaxation.

## Notes
- Duality is attributed to von Neumann (1947) and to Gale, Kuhn and Tucker; Farkas' lemma to Farkas (1894) and Minkowski (1896) (notes, p. 199).
- Wiki note: sensitivity analysis of the optimal basis ([[BT ch5 - Sensitivity analysis]]) is built on the formulas here: $\mathbf p'=\mathbf c_B'\mathbf B^{-1}$ and the dual simplex method.
- Wiki note: statements of Cor. 4.3, Thm 4.7-4.8, 4.12-4.14 and 4.16 above are paraphrased from headings and the text layer, not read as page images. **[unverified]**

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf 155-216, printed pp. 139-200).
**Last updated**: 2026-11-06

---

## Related pages
- [[LP duality]] · [[Farkas lemma]] · [[Dual simplex method]] · [[Simplex method]] · [[Linear programming]] · [[Polyhedron]]
- [[BT ch3 - The simplex method]] · [[BT ch5 - Sensitivity analysis]] · [[BT ch6 - Large scale optimization]] · [[BJS ch6 - Duality and sensitivity analysis]]
- [[Convex set]] · [[ME697 1.4 - Optimization]]
