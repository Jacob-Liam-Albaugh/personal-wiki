---
type: theorem
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 4; Bazaraa, Jarvis, Sherali 2010, ch. 6"
tags: [optimization]
---

# LP duality

> [!theorem] Strong duality (source: MIT (ch 1-5).pdf, p. 148, Thm 4.4)
> If a linear program has an optimal solution, so does its dual, and the optimal costs are equal.

**Intuition**: every price vector $\mathbf p$ gives a lower bound on the primal cost; the dual searches for the best bound, and for LPs the best bound is tight (BT §4.1). BJS call the original problem the primal and its associated problem the dual; "primal" was suggested by Dantzig's father, a mathematician, to avoid the phrase "the original problem of which this is the dual" (BJS p. 259, image seen).

## Duality as a bound

Primal in standard form: minimize $\mathbf c'\mathbf x$ subject to $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\ge\mathbf 0$. Relax the equality with a price vector $\mathbf p$ and define (BT §4.1, pp. 141-142)
$$g(\mathbf p)=\min_{\mathbf x\ge\mathbf0}\big[\mathbf c'\mathbf x+\mathbf p'(\mathbf b-\mathbf A\mathbf x)\big]$$
Because the optimal $\mathbf x^*$ is feasible, $g(\mathbf p)\le\mathbf c'\mathbf x^*$ for every $\mathbf p$. Searching for the best bound means maximizing $g$. Rewriting,
$$g(\mathbf p)=\mathbf p'\mathbf b+\min_{\mathbf x\ge\mathbf0}(\mathbf c'-\mathbf p'\mathbf A)\mathbf x$$
The inner minimum is $0$ if $\mathbf c'-\mathbf p'\mathbf A\ge\mathbf0'$ and $-\infty$ otherwise, so only those $\mathbf p$ matter and the dual is: maximize $\mathbf p'\mathbf b$ subject to $\mathbf p'\mathbf A\le\mathbf c'$ (p. 141).

## The dual problem

Rows are $\mathbf a_i'$, columns $\mathbf A_j$ (BT §4.2, pp. 142-146). For a minimization primal the dual is a maximization, one dual variable per primal constraint and one dual constraint per primal variable (Table 4.1, p. 143):

| Primal (min) | Dual (max) |
|---|---|
| constraint $\mathbf a_i'\mathbf x\ge b_i$ | variable $p_i\ge0$ |
| constraint $\mathbf a_i'\mathbf x\le b_i$ | variable $p_i\le0$ |
| constraint $\mathbf a_i'\mathbf x=b_i$ | variable $p_i$ free |
| variable $x_j\ge0$ | constraint $\mathbf p'\mathbf A_j\le c_j$ |
| variable $x_j\le0$ | constraint $\mathbf p'\mathbf A_j\ge c_j$ |
| variable $x_j$ free | constraint $\mathbf p'\mathbf A_j=c_j$ |

Two common pairs (BT p. 143; BJS write $\mathbf w$ for $\mathbf p$, p. 260):
$$\min\ \mathbf c'\mathbf x:\ \mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf0\quad\longleftrightarrow\quad\max\ \mathbf p'\mathbf b:\ \mathbf p'\mathbf A\le\mathbf c'$$
$$\min\ \mathbf c'\mathbf x:\ \mathbf A\mathbf x\ge\mathbf b\quad\longleftrightarrow\quad\max\ \mathbf p'\mathbf b:\ \mathbf p'\mathbf A=\mathbf c',\ \mathbf p\ge\mathbf0$$

BJS (§6.1, pp. 259-264, images seen at pp. 259-260) give two equivalent forms.

**Canonical form**:
$$\text{P: }\min\ \mathbf c\mathbf x\ \ \text{s.t.}\ \mathbf A\mathbf x\ge\mathbf b,\ \mathbf x\ge\mathbf0$$
$$\text{D: }\max\ \mathbf w\mathbf b\ \ \text{s.t.}\ \mathbf w\mathbf A\le\mathbf c,\ \mathbf w\ge\mathbf0$$
**Standard form**:
$$\text{P: }\min\ \mathbf c\mathbf x\ \ \text{s.t.}\ \mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf0$$
$$\text{D: }\max\ \mathbf w\mathbf b\ \ \text{s.t.}\ \mathbf w\mathbf A\le\mathbf c,\ \mathbf w\ \text{unrestricted}$$
There is exactly one dual variable per primal constraint and one dual constraint per primal variable. BJS Example 6.1 (p. 260): P minimizes $6x_1+8x_2$ s.t. $3x_1+x_2\ge4$, $5x_1+2x_2\ge7$, and D maximizes $4w_1+7w_2$ s.t. $3w_1+5w_2\le6$, $w_1+2w_2\le8$, all variables nonnegative. Any LP can be dualized directly by mixed rules (Lemma 6.1, Example 6.3, pp. 262-264, headings only).

> [!theorem] Theorem 4.1 (p. 144)
> The dual of the dual is the primal (after turning the dual into a minimization).

> [!theorem] Theorem 4.2 (p. 146)
> Transformations of an LP (free variable to difference of nonnegatives, inequality to equality with slack, dropping a redundant equality row) do not change the dual: the duals are equivalent (both infeasible or same optimal cost).

## Weak and strong duality

> [!theorem] Theorem 4.3, weak duality (p. 146)
> If $\mathbf x$ is primal feasible and $\mathbf p$ is dual feasible then
> $$\mathbf p'\mathbf b\le\mathbf c'\mathbf x$$

Corollary 4.2 (BT p. 148): if both are feasible and $\mathbf p'\mathbf b=\mathbf c'\mathbf x$, both are optimal. A feasible dual implies the primal cannot be unbounded below, and vice versa (Cor. 4.1, p. 147). BJS state weak duality as Lemma 6.2, with Corollaries 6.1-6.2 on bounds and unboundedness (unboundedness of one problem implies infeasibility of the other, p. 265) and Lemma 6.3 on the dual of the homogeneous form (p. 267). With $\mathrm{HD}$: max $\mathbf w\mathbf b$ s.t. $\mathbf w\mathbf A\le\mathbf0$, $\mathbf w\ge\mathbf0$ (note $\mathbf w=\mathbf0$ is feasible):

> [!theorem] Corollary 6.3 (p. 267, image seen)
> The primal problem is infeasible iff the homogeneous form of the dual problem is unbounded (and vice versa).

> [!theorem] Theorem 4.4, strong duality (p. 148)
> If an LP has an optimal solution, so does its dual, and the optimal costs are equal.

Proof idea for standard form with full-row-rank $\mathbf A$ (BT p. 148): run the simplex method with an anticycling rule ([[Simplex initialization and anticycling]]) to an optimal basis $\mathbf B$. Optimality gives $\mathbf c'-\mathbf c_B'\mathbf B^{-1}\mathbf A\ge\mathbf0'$. Set $\mathbf p'=\mathbf c_B'\mathbf B^{-1}$. Then $\mathbf p'\mathbf A\le\mathbf c'$ (dual feasible) and
$$\mathbf p'\mathbf b=\mathbf c_B'\mathbf B^{-1}\mathbf b=\mathbf c'\mathbf x$$
so $\mathbf p$ is optimal by Cor. 4.2. The general case reduces to this one by Theorem 4.2. In BJS terms, at an optimal primal tableau the simplex multipliers $\mathbf w^*=\mathbf c_B\mathbf B^{-1}$ are an optimal dual solution, since $z_j-c_j\le0$ says $\mathbf w^*\mathbf a_j\le c_j$ and $z^*=\mathbf w^*\mathbf b$ (pp. 267, 279, Lemma 6.4).

> [!theorem] Theorem 6.1, Fundamental Theorem of Duality (p. 267, image seen)
> Exactly one of the following holds: (1) both problems have optimal solutions $\mathbf x^*,\mathbf w^*$ with $\mathbf c\mathbf x^*=\mathbf w^*\mathbf b$; (2) one problem has an unbounded optimal value and the other is infeasible; (3) both are infeasible.

Duality is not completely symmetric (BJS p. 268, image seen). Using "P(D)" for primal (dual):

| if | then |
|---|---|
| P optimal | D optimal (iff) |
| P(D) unbounded | D(P) infeasible |
| P(D) infeasible | D(P) unbounded or infeasible |
| P(D) infeasible | D(P) unbounded in homogeneous form (iff) |

BT's version is the table of possible primal/dual status pairs (Table 4.2, p. 151): both finite optimal; primal unbounded with dual infeasible and vice versa; both infeasible is possible (Example 4.5, p. 151). Clark's theorem (BT Exercise 4.21): unless both are infeasible, at least one has an unbounded feasible set.

**Supervisor's principle** (BJS): feasible $\mathbf x,\mathbf w$ are both optimal iff $\mathbf c\mathbf x=\mathbf w\mathbf b$. An equivalent check is complementary slackness, which with feasibility gives the KKT conditions ([[Farkas lemma]], [[KKT conditions]]).

## Complementary slackness

> [!theorem] Theorem 4.5, complementary slackness (p. 151)
> Feasible $\mathbf x$ and $\mathbf p$ are optimal if and only if
> $$p_i(\mathbf a_i'\mathbf x-b_i)=0\quad\forall i$$
> $$(c_j-\mathbf p'\mathbf A_j)x_j=0\quad\forall j$$

Meaning: a dual variable can be nonzero only on a binding primal constraint, and a primal variable can be nonzero only where its dual constraint is tight. Used to recover one optimal solution from the other.

> [!theorem] Theorem 6.2, Complementary Slackness (p. 268, image seen)
> Let $\mathbf x^*,\mathbf w^*$ be feasible for the canonical primal and dual. They are optimal iff
> $$(c_j-\mathbf w^*\mathbf a_j)x_j^*=0,\quad j=1,\dots,n$$
> $$w_i^*(\mathbf a^i\mathbf x^*-b_i)=0,\quad i=1,\dots,m$$

At least one factor in each product vanishes, for example $x_j^*>0\Rightarrow\mathbf w^*\mathbf a_j=c_j$. The proof (BJS p. 268) expands $\mathbf w^*(\mathbf A\mathbf x^*-\mathbf b)+(\mathbf c-\mathbf w^*\mathbf A)\mathbf x^*=\mathbf c\mathbf x^*-\mathbf w^*\mathbf b$ (image seen). Example 6.5 follows.

## Dual variables as marginal costs

If $\mathbf x^*$ is a nondegenerate optimal BFS with basis $\mathbf B$ and $\mathbf b$ is perturbed to $\mathbf b+\mathbf d$ with $\mathbf d$ small, the same basis stays optimal (reduced costs do not depend on $\mathbf b$). The optimal cost becomes $\mathbf p'(\mathbf b+\mathbf d)$, so $p_i$ is the marginal cost (shadow price) of the $i$th requirement (BT §4.4, pp. 155-156). The diet-problem reading: $\mathbf p$ prices nutrients, and duality says the food market and nutrient market value the ideal food identically (p. 156).

BJS (§6.3, pp. 270-277): the dual variables are marginal values of the resources: $\partial z/\partial b_i=w_i$ (but degeneracy can spoil this as a realizable rate, BJS p. 175). Example 6.6 (pp. 276-277, headings only); the section was not read in detail. How the shadow prices behave under larger changes is in [[LP sensitivity analysis]].

## General duality

Primal: minimize $\mathbf c'\mathbf x$ s.t. $\mathbf A\mathbf x\ge\mathbf b$, $\mathbf x\in P$ with $P=\{\mathbf x\mid\mathbf D\mathbf x\ge\mathbf d\}$. Dual objective (BT §4.10, eq. 4.7, p. 184):
$$g(\mathbf p)=\min_{\mathbf x\in P}\big[\mathbf c'\mathbf x+\mathbf p'(\mathbf b-\mathbf A\mathbf x)\big]$$
Dual: maximize $g(\mathbf p)$ subject to $\mathbf p\ge\mathbf0$. Theorem 4.17 (weak duality): $g(\mathbf p)\le\mathbf c'\mathbf x$ for feasible pairs. Theorem 4.18 (strong duality): if the primal has an optimal solution, so does the dual and the costs are equal (p. 184). This leaves some constraints un-priced, which is the idea behind decomposition and Lagrangean relaxation ([[Dantzig-Wolfe decomposition]], [[Integer programming]]). The general conic and nonlinear theory is in [[Lagrangian duality]].

## LP duality as conic duality

Basu proves LP strong duality without a Slater condition, from the valid-inequality theorem (Thm 2.85), inside the conic framework of [[Lagrangian duality]] (Basu Thm 4.31, p. 84). The LP dual and complementary slackness then appear as the continuous-optimisation view (Thms 4.32-4.33). The LP general duality of BT §4.10, pricing only some constraints, is spelled out on [[Lagrangian duality]].

## Key facts
- Standard-form pair (BT p. 143; BJS write $\mathbf w$ for $\mathbf p$, p. 260), above.
- One dual variable per primal constraint, one dual constraint per primal variable; the table of sign rules is Table 4.1 (BT p. 143). The dual of the dual is the primal (BT Thm 4.1; BJS p. 259).
- Weak duality: feasible $\mathbf x$, $\mathbf p$ give $\mathbf p'\mathbf b\le\mathbf c'\mathbf x$ (BT Thm 4.3, p. 146; BJS Lemma 6.2).
- Fundamental theorem: exactly one of (1) both have optimal solutions with equal cost, (2) one is unbounded and the other infeasible, (3) both infeasible (BJS Thm 6.1, p. 267; BT Table 4.2, p. 151).
- Complementary slackness (BT Thm 4.5, p. 151; BJS Thm 6.2, p. 268), above.
- Dual variables are shadow prices: if the basis stays optimal, the cost changes by $\mathbf p'\mathbf d$ when $\mathbf b$ moves by $\mathbf d$ (BT §4.4, p. 156). Degeneracy can spoil this as a rate (BJS §6.3).
- Proof routes: from the simplex method (BT p. 148) or from separating hyperplanes via [[Farkas lemma]] (BT §4.6-4.7).
- Complementary slackness plus feasibility are the [[KKT conditions]] of an LP.
- Algorithms built on the duality: [[Dual simplex method]], the primal-dual method (BJS §6.5), the out-of-kilter algorithm ([[Network flow problem]]), and primal-dual [[Interior point method]]s (central path as perturbed complementary slackness).
- Integer programs lack strong duality; Lagrangean duals give bounds only (see [[Integer programming]]).
- Duality is attributed to von Neumann (1947) and to Gale, Kuhn and Tucker (BT notes, p. 199).

**Covered in**: Bertsimas-Tsitsiklis ch. 4 §4.1-4.4 and §4.10 (pp. 141-156, 183-186); Bazaraa-Jarvis-Sherali ch. 6 §6.1-6.3 (pp. 259-277); Basu ch. 4 §4.3
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 4-6, 9, 11); `text_books/Linear Optimization/BJS full book.pdf` (ch. 6, 11; printed pp. 259-260, 267-268 seen as images); `text_books/Mathmatics/Basu - Intro to Convexity.pdf` (§4.3).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Farkas lemma]] · [[Dual simplex method]] · [[KKT conditions]] · [[Simplex method]] · [[Convex function]] · [[LP sensitivity analysis]] · [[Lagrangian duality]] · [[Network flow problem]]
