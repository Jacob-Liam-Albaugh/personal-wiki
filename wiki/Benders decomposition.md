---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, §6.5; Bazaraa, Jarvis, Sherali 2010, §7.6"
tags: [optimization]
---

# Benders decomposition

> [!definition] Two-stage stochastic program (source: MIT (ch 1-5).pdf, pp. 254-255)
> Choose $\mathbf x$ with $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\ge\mathbf0$. Then one of $K$ scenarios $\omega$ with probability $\alpha_\omega>0$ is revealed and a recourse $\mathbf y^\omega$ is chosen with $\mathbf B^\omega\mathbf x+\mathbf D\mathbf y^\omega=\mathbf d^\omega$, $\mathbf y^\omega\ge\mathbf0$. Minimize the expected cost
> $$\mathbf c'\mathbf x+\sum_\omega\alpha_\omega\mathbf f'\mathbf y^\omega$$

**Intuition**: the monolithic LP is huge even for moderate $K$ (BT Example 6.5, electric power capacity expansion, p. 255). Benders evaluates each second-stage cost through its dual and keeps few variables but many constraints, generated as needed. It is delayed constraint generation, essentially [[Dantzig-Wolfe decomposition]] applied to the dual (BT p. 259), hence a [[Cutting-plane methods]] scheme. BJS call Dantzig-Wolfe, Benders partitioning and Lagrangian relaxation "all equivalent for linear programming problems" (BJS p. 339, 371).

## Reformulation
The second-stage cost is evaluated through its dual, whose feasible polyhedron does not depend on $\mathbf x$. It is a maximum over extreme points $\mathbf p^i$, finite only if for each extreme ray $\mathbf w^j$ (eq. 6.19, p. 257)
$$(\mathbf w^j)'(\mathbf d^\omega-\mathbf B^\omega\mathbf x)\le0$$
The master (eq. 6.20) then has few variables and very many constraints:
$$(\mathbf p^i)'(\mathbf d^\omega-\mathbf B^\omega\mathbf x)\le z^\omega\ \ \forall i,\ \text{plus the ray constraints}$$

> [!algorithm] Benders algorithm (BT p. 259)
> 1. Solve the relaxed master (a subset of the constraints) for $(\mathbf x^*,\mathbf z^*)$.
> 2. For each $\omega$ solve $\min\mathbf f'\mathbf y^\omega$ s.t. $\mathbf D\mathbf y^\omega=\mathbf d^\omega-\mathbf B^\omega\mathbf x^*$ with the [[Dual simplex method]].
> 3. If every subproblem is feasible with cost at most $z^{\omega*}$, stop.
> 4. If some cost exceeds $z^{\omega*}$, add the constraint from the optimal dual BFS $\mathbf p^i$.
> 5. If a subproblem is infeasible, add the ray constraint $(\mathbf w^j)'(\mathbf d^\omega-\mathbf B^\omega\mathbf x)\le0$.

The practical difficulty is the number of scenarios $K$.

## The BJS view (§7.6, pp. 371-376)
Take P: $\min\mathbf c\mathbf x$ s.t. $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\in X=\{\mathbf D\mathbf x\ge\mathbf d,\ \mathbf x\ge\mathbf0\}$ with $X$ nonempty and bounded, and its dual
$$\text{D: }\max\ \mathbf w\mathbf b+\mathbf v\mathbf d\quad\text{s.t. }\mathbf w\mathbf A+\mathbf v\mathbf D\le\mathbf c,\ \mathbf v\ge\mathbf0,\ \mathbf w\text{ free}$$
Fixing $\mathbf w$ leaves an LP in $\mathbf v$, which is the basis of the Benders view (the rest of the section was not read; Example 7.3, p. 374).

**Covered in**: Bertsimas-Tsitsiklis ch. 6 §6.5 (pp. 254-263); Bazaraa-Jarvis-Sherali ch. 7 §7.6 (pp. 371-376)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 6); `text_books/Linear Optimization/BJS full book.pdf` (ch. 7).
**Last updated**: 2026-11-06

---

## Related pages
- [[Dantzig-Wolfe decomposition]] · [[Column generation]] · [[Cutting-plane methods]] · [[LP duality]] · [[Dual simplex method]] · [[Linear programming]]
