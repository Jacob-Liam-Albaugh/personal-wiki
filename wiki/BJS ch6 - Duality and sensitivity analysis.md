---
type: paper
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 6 (printed pp. 259-338)"
tags: [optimization]
authors: ["[[Mokhtar S. Bazaraa]]", "[[John J. Jarvis]]", "[[Hanif D. Sherali]]"]
year: 2010
venue: "Wiley, Linear Programming and Network Flows, 4th ed. (textbook)"
file: "text_books/Linear Optimization/BJS full book.pdf"
---

# BJS ch6 - Duality and sensitivity analysis

**Summary**: Defines the dual of a linear program in canonical and standard form, proves the fundamental theorem of duality and complementary slackness, and uses the dual to build the dual simplex method and the primal-dual method. The chapter ends with sensitivity analysis (changes in costs, right-hand sides, columns) and parametric analysis. See [[LP duality]], [[Dual simplex method]], [[KKT conditions]].

**Authors**: Mokhtar S. Bazaraa, John J. Jarvis, Hanif D. Sherali · **Year**: 2010 · **File**: `text_books/Linear Optimization/BJS full book.pdf` (printed pp. 259-338). Cites use printed pages; pdf = printed + 16.

## Formulation of the dual (§6.1, p. 259-264)
The chapter opens by calling the original problem the primal and its associated problem the dual. "Primal" was suggested by Dantzig's father, who was a mathematician, to avoid the phrase "the original problem of which this is the dual", and the dual of the dual is the primal (p. 259, image seen). Two equivalent forms.

**Canonical form** (p. 259-260, images seen):
$$\text{P: }\min\ \mathbf c\mathbf x\ \ \text{s.t.}\ \mathbf A\mathbf x\ge\mathbf b,\ \mathbf x\ge\mathbf0$$
$$\text{D: }\max\ \mathbf w\mathbf b\ \ \text{s.t.}\ \mathbf w\mathbf A\le\mathbf c,\ \mathbf w\ge\mathbf0$$
**Standard form** (p. 260):
$$\text{P: }\min\ \mathbf c\mathbf x\ \ \text{s.t.}\ \mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf0$$
$$\text{D: }\max\ \mathbf w\mathbf b\ \ \text{s.t.}\ \mathbf w\mathbf A\le\mathbf c,\ \mathbf w\ \text{unrestricted}$$
There is exactly one dual variable per primal constraint and one dual constraint per primal variable. Example 6.1 (p. 260): P minimizes $6x_1+8x_2$ s.t. $3x_1+x_2\ge4$, $5x_1+2x_2\ge7$, and D maximizes $4w_1+7w_2$ s.t. $3w_1+5w_2\le6$, $w_1+2w_2\le8$, all variables nonnegative. Any LP can be dualized directly by mixed rules (Lemma 6.1, Example 6.3, p. 262-264, headings only).

## Primal-dual relationships (§6.2, p. 264-270)
Results in this order: Lemma 6.2 is weak duality (the book refers to "the weak duality property of Lemma 6.2", p. 267, image seen), Corollaries 6.1-6.2 on bounds and unboundedness (unboundedness of one problem implies infeasibility of the other, p. 265, text), Lemma 6.3 on the dual of the homogeneous form (p. 267). With $\mathrm{HD}$: max $\mathbf w\mathbf b$ s.t. $\mathbf w\mathbf A\le\mathbf0$, $\mathbf w\ge\mathbf0$ (note $\mathbf w=\mathbf0$ is feasible):

> [!theorem] Corollary 6.3 (p. 267, image seen)
> The primal problem is infeasible iff the homogeneous form of the dual problem is unbounded (and vice versa).

> [!theorem] Theorem 6.1, Fundamental Theorem of Duality (p. 267, image seen)
> Exactly one of the following holds: (1) both problems have optimal solutions $\mathbf x^*,\mathbf w^*$ with $\mathbf c\mathbf x^*=\mathbf w^*\mathbf b$; (2) one problem has an unbounded optimal value and the other is infeasible; (3) both are infeasible.

Duality is not completely symmetric (p. 268, image seen). Using "P(D)" for primal (dual):

| if | then |
|---|---|
| P optimal | D optimal (iff) |
| P(D) unbounded | D(P) infeasible |
| P(D) infeasible | D(P) unbounded or infeasible |
| P(D) infeasible | D(P) unbounded in homogeneous form (iff) |

**Supervisor's principle**: feasible $\mathbf x,\mathbf w$ are both optimal iff $\mathbf c\mathbf x=\mathbf w\mathbf b$. With the KKT conditions of [[BJS ch5 - Special simplex implementations and optimality conditions]], an equivalent check is complementary slackness.

> [!theorem] Theorem 6.2, Complementary Slackness (p. 268, image seen)
> Let $\mathbf x^*,\mathbf w^*$ be feasible for the canonical primal and dual. They are optimal iff
> $$(c_j-\mathbf w^*\mathbf a_j)x_j^*=0,\quad j=1,\dots,n$$
> $$w_i^*(\mathbf a^i\mathbf x^*-b_i)=0,\quad i=1,\dots,m$$

At least one factor in each product vanishes, for example $x_j^*>0\Rightarrow\mathbf w^*\mathbf a_j=c_j$. The proof (p. 268) expands $\mathbf w^*(\mathbf A\mathbf x^*-\mathbf b)+(\mathbf c-\mathbf w^*\mathbf A)\mathbf x^*=\mathbf c\mathbf x^*-\mathbf w^*\mathbf b$ (image seen). Example 6.5 follows. At an optimal primal tableau, the simplex multipliers $\mathbf w^*=\mathbf c_B\mathbf B^{-1}$ are an optimal dual solution, since $z_j-c_j\le0$ says $\mathbf w^*\mathbf a_j\le c_j$ and $z^*=\mathbf w^*\mathbf b$ (p. 267 and Lemma 6.4, p. 279, image seen and text).

## Economic interpretation (§6.3, p. 270-277)
The dual variables are marginal values of the resources (shadow prices): $\partial z/\partial b_i=w_i$ (the book cautions in ch4, p. 175, that degeneracy can spoil this as a realizable rate). Example 6.6 (p. 276-277, headings only). The section was not read in detail.

## The dual simplex method (§6.4, p. 277-285)
Motivation (p. 279, text): when no feasible starting basis is available without artificials, a basis that is dual feasible ($z_j-c_j\le0$ for all $j$, minimization) may be easy to find. The dual simplex method keeps dual feasibility and works toward primal feasibility. If $\hat b_r<0$, pick row $r$ as pivot row. If $y_{rj}\ge0$ for all $j$ in that row the primal is infeasible (stated in the text around p. 279-280, not seen as an image). Otherwise the pivot column $k$ comes from the minimum ratio test (eq. 6.7, p. 280, text):
$$\frac{z_k-c_k}{y_{rk}}=\min_j\Big\{\frac{z_j-c_j}{y_{rj}}:\ y_{rj}<0\Big\}$$
The new row-0 entries are $(z_j-c_j)'=(z_j-c_j)-\frac{y_{rj}}{y_{rk}}(z_k-c_k)$ and are shown to remain $\le0$ in both cases $y_{rj}\ge0$ and $y_{rj}<0$ (p. 280, text). The dual objective changes by $-(z_k-c_k)\hat b_r/y_{rk}\ge0$ per iteration, strictly increasing without dual degeneracy, so no basis repeats (p. 285, text). Dual degeneracy needs a cycling rule, obtained by applying the ordinary rules of [[BJS ch4 - Starting solution and convergence]] to the dual (p. 285, text). Example 6.7 (p. 281-284).

**Complementary bases** (p. 283-284, images seen). For a primal basis $\mathbf B$ the matrix pairing it is the dual basis
$$\begin{pmatrix}\mathbf B'&\mathbf0\\\mathbf N'&\mathbf I_{n-m}\end{pmatrix}$$
of rank $n$. The dual slack vector is $\mathbf w_s'=\mathbf c'-\mathbf A'\mathbf w'$, which equals $(\mathbf 0,\ \mathbf c_N-\mathbf c_B\mathbf B^{-1}\mathbf N)$ at $\mathbf w=\mathbf c_B\mathbf B^{-1}$ (eq. 6.11). The primal basis is feasible iff $\mathbf B^{-1}\mathbf b\ge\mathbf0$ and the dual basis is feasible iff $\mathbf c_N-\mathbf c_B\mathbf B^{-1}\mathbf N\ge\mathbf0$. Complementary slackness holds for the pair, since $(\mathbf w\mathbf A-\mathbf c)\mathbf x=\mathbf w_s\mathbf x=0$. In every dual simplex iteration the primal basis is not necessarily feasible and the dual basis is feasible, and at termination all KKT conditions hold.

## Primal-dual method (§6.5, p. 285-293)
Maintains dual feasibility and builds primal feasibility through a restricted primal problem solved with artificial variables (Example 6.8, p. 289-293, headings and text only, not read). §6.6 (p. 293-295) finds an initial dual feasible solution (Example 6.9).

## Sensitivity and parametric analysis (§6.7-6.8, p. 295-336)
Sensitivity analysis studies changes in the cost vector, right-hand side and constraint matrix by updating the final tableau (Examples 6.10-6.16, p. 296-312, headings only). Parametric analysis (§6.8, p. 312-336, Examples 6.17-6.18) varies the cost or right-hand side along a parameter, with piecewise linear convex optimal-value functions (the convex functions of [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]]). These sections were not read. Compare [[BT ch5 - Sensitivity analysis]].

## Notes
- Wiki note: BT treat the same pair of problems and the fundamental theorem in [[BT ch4 - Duality theory]]; the notation differs ($\mathbf p$ there, $\mathbf w$ here).
- Wiki note: here the dual optimum is read off the optimal basis as $\mathbf w^*=\mathbf c_B\mathbf B^{-1}$ ([[Simplex method]]).

**Sources**: `text_books/Linear Optimization/BJS full book.pdf` (pdf 275-354, printed pp. 259-338). Pages viewed as images: pdf 275 (printed 259), 276 (260), 283 (267), 284 (268), 299 (283), 300 (284). Dual simplex details (printed 279-285) and the sections on the economic interpretation, primal-dual method, sensitivity and parametric analysis were read only as headings or text layer and are not transcribed beyond what is cited.
**Last updated**: 2026-11-06

---

## Related pages
- [[LP duality]] · [[Dual simplex method]] · [[KKT conditions]] · [[Farkas lemma]] · [[Simplex method]]
- [[BJS ch5 - Special simplex implementations and optimality conditions]] · [[BJS ch7 - The decomposition principle]] · [[BT ch4 - Duality theory]] · [[BT ch5 - Sensitivity analysis]]
