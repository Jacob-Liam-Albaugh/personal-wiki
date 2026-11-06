---
type: paper
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 9 (printed pp. 393-450)"
tags: [optimization]
authors: ["[[Dimitris Bertsimas]]", "[[John N. Tsitsiklis]]"]
year: 1997
venue: "Athena Scientific (textbook)"
file: "Linear Optimization/MIT (ch 1-5).pdf"
---

# BT ch9 - Interior point methods

**Summary**: Algorithms that solve a [[Linear programming|linear program]] by moving through the interior of the feasible set instead of along its vertices as the [[Simplex method]] does. Three families: affine scaling (approximate the polyhedron from inside by an ellipsoid), potential reduction (a potential function trades objective decrease against staying off the boundary), and path following (follow the central path of a logarithmic barrier). Path following is the method of choice in large implementations (p. 394-395). See [[Interior point method]].

## Overview (p. 393-395)
- In practice these methods are competitive with the simplex method and often beat it on large sparse problems (p. 393).
- Affine scaling: the approximating ellipsoid lies inside the polyhedron, whereas in the ellipsoid method of [[BT ch8 - Complexity of LP and the ellipsoid method]] it contains it.
- Potential reduction: progress is measured by a nonlinear potential, not by the cost.
- Path following: solve a log-barrier problem approximately with Newton's method (see [[Newton's method]]) and let the barrier weight fall; the optimum traces a path to the LP optimum.

Setting for §9.1: the standard form problem and its dual
$$\min\ \mathbf c'\mathbf x\ \ \text{s.t. }\mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf0$$
$$\max\ \mathbf p'\mathbf b\ \ \text{s.t. }\mathbf p'\mathbf A\le\mathbf c'$$
with $\mathbf A$ of size $m\times n$ (p. 395). The interior of the feasible set $P$ is $\{\mathbf x\in P\mid\mathbf x>\mathbf0\}$.

## Affine scaling (§9.1, p. 395-403)
**Ellipsoid inside the positive orthant** (Lemma 9.1, p. 396). For $\beta\in(0,1)$, $\mathbf y>\mathbf0$ and
$$S=\Big\{\mathbf x\ \Big|\ \sum_i\frac{(x_i-y_i)^2}{y_i^2}\le\beta^2\Big\}$$
every $\mathbf x\in S$ has $\mathbf x>\mathbf0$. With $\mathbf Y=\mathrm{diag}(y_1,\dots,y_n)$ this is $\|\mathbf Y^{-1}(\mathbf x-\mathbf y)\|\le\beta$. Intersecting with $\mathbf A\mathbf x=\mathbf b$ gives an ellipsoid $S_0$ inside the feasible set (Figure 9.2, p. 397).

**Step problem** (9.1)-(9.2, p. 397). With $\mathbf d=\mathbf x-\mathbf y$ and $\mathbf A\mathbf y=\mathbf b$:
$$\min\ \mathbf c'\mathbf d\ \ \text{s.t. }\mathbf A\mathbf d=\mathbf0,\ \ \|\mathbf Y^{-1}\mathbf d\|\le\beta$$

> [!theorem] Lemma 9.2 (p. 397)
> Assume the rows of $\mathbf A$ are independent, $\mathbf c$ is not a combination of the rows of $\mathbf A$, and $\mathbf y>\mathbf0$. The optimal direction is
> $$\mathbf d^*=-\beta\frac{\mathbf Y^2(\mathbf c-\mathbf A'\mathbf p)}{\|\mathbf Y(\mathbf c-\mathbf A'\mathbf p)\|}$$
> with $\mathbf p=(\mathbf A\mathbf Y^2\mathbf A')^{-1}\mathbf A\mathbf Y^2\mathbf c$. Then $\mathbf x=\mathbf y+\mathbf d^*\in P$ and $\mathbf c'\mathbf x=\mathbf c'\mathbf y-\beta\|\mathbf Y(\mathbf c-\mathbf A'\mathbf p)\|<\mathbf c'\mathbf y$.

Proof (p. 398): $\mathbf A\mathbf Y^2\mathbf A'$ is invertible, $\mathbf d^*$ is feasible, and optimality follows from the Schwarz inequality. If $\mathbf d^*\ge\mathbf0$ the problem is unbounded with cost $-\infty$.

**Dual estimates** (p. 398-399). Applying the formula for $\mathbf p$ at a nondegenerate basic feasible solution $\mathbf y$ gives $\mathbf p=(\mathbf B')^{-1}\mathbf c_B$, the dual basic solution of [[BT ch4 - Duality theory]]. The vector $\mathbf r=\mathbf c-\mathbf A'\mathbf p$ is then the reduced cost vector of [[BT ch3 - The simplex method]]. So $\mathbf p$ is called the dual estimate for any $\mathbf y$. If $\mathbf r\ge\mathbf0$, $\mathbf p$ is dual feasible and the duality gap is
$$\mathbf r'\mathbf y=\mathbf c'\mathbf y-\mathbf p'\mathbf b$$

> [!theorem] Lemma 9.3 (p. 399)
> If $\mathbf y,\mathbf p$ are primal and dual feasible with $\mathbf c'\mathbf y-\mathbf b'\mathbf p\le\epsilon$, then $\mathbf c'\mathbf y^*\le\mathbf c'\mathbf y\le\mathbf c'\mathbf y^*+\epsilon$ and $\mathbf b'\mathbf p^*-\epsilon\le\mathbf b'\mathbf p\le\mathbf b'\mathbf p^*$.

**Affine scaling algorithm** (box, p. 400). Inputs: $\mathbf A,\mathbf b,\mathbf c$, a start $\mathbf x^0>\mathbf0$ feasible, tolerance $\epsilon$, and $\beta\in(0,1)$. Iterate:
1. $\mathbf X_k=\mathrm{diag}(x_1^k,\dots,x_n^k)$, $\mathbf p^k=(\mathbf A\mathbf X_k^2\mathbf A')^{-1}\mathbf A\mathbf X_k^2\mathbf c$, $\mathbf r^k=\mathbf c-\mathbf A'\mathbf p^k$.
2. If $\mathbf r^k\ge\mathbf0$ and $\mathbf e'\mathbf X_k\mathbf r^k<\epsilon$, stop: $\mathbf x^k$ and $\mathbf p^k$ are $\epsilon$-optimal.
3. If $-\mathbf X_k^2\mathbf r^k\ge\mathbf0$, stop: the cost is $-\infty$.
4. Update:
$$\mathbf x^{k+1}=\mathbf x^k-\beta\frac{\mathbf X_k^2\mathbf r^k}{\|\mathbf X_k\mathbf r^k\|}$$

**Step-size variants** (p. 400-401). The rule above is the short-step method. Long-step variants keep the direction $-\mathbf X_k^2\mathbf r^k$ but divide by $\|\mathbf X_k\mathbf r^k\|_\infty$ (Eq. 9.4) or by $\gamma(\mathbf X_k\mathbf r^k)=\max\{u_i\mid u_i>0\}$ (Eq. 9.5), with $\gamma(\mathbf u)\le\|\mathbf u\|_\infty\le\|\mathbf u\|$. Eq. 9.5 reduces cost most and is most popular.

**Convergence** (p. 401-403). Assumption 9.1: rows of $\mathbf A$ independent, $\mathbf c$ not in their span, an optimal solution exists, a positive feasible solution exists. Assumption 9.2: primal basic feasible solutions nondegenerate and nonbasic reduced costs nonzero.

> [!theorem] Theorem 9.1 (p. 402)
> For the long-step method with $\epsilon=0$: (a) for steps (9.4) or (9.5), under Assumptions 9.1-9.2 and $0<\beta<1$, $\mathbf x^k$ and $\mathbf p^k$ converge to the optimal primal and dual solutions; (b) for step (9.5), under Assumption 9.1 alone and $0<\beta<2/3$, they converge to some optimal solutions.

For $\beta>2/3$ there is an example (Exercise 9.4) where the dual sequence fails to converge; the corresponding primal threshold is not known (p. 403).

**Starting point** (p. 403). Add an artificial variable $x_{n+1}$ with column $\mathbf b-\mathbf A\mathbf e$ and cost $M$, a large number. Then $(\mathbf x,x_{n+1})=(\mathbf e,1)$ is positive feasible. **Cost per iteration**: forming $\mathbf A\mathbf X_k^2\mathbf A'$ is $O(m^2n)$ and solving is $O(m^3)$, so $O(n^3)$ in all.

## Convergence of short-step affine scaling (§9.2, p. 404-409)
Theorem 9.2 (Bolzano-Weierstrass: every bounded sequence has a convergent subsequence), Lemma 9.4 and Theorem 9.3 (pp. 405-408) prove that the short-step iterates converge to a basic feasible solution, under the nondegeneracy assumptions. The proof shows the sequence is bounded, every limit point is a basic feasible solution (via complementary slackness in the limit), the limit is unique, and it is optimal because otherwise a negative reduced cost would drive that variable up. Once near the optimum the cost falls geometrically (Exercise 9.1, p. 409). The detailed steps were read from the text layer only. **[unverified]**

## Potential reduction (§9.3, p. 409-419)
Assumption 9.3 (p. 409): $\mathbf A$ has independent rows, and strictly feasible $\mathbf x>\mathbf0$ and $(\mathbf p,\mathbf s)$ with $\mathbf s>\mathbf0$ exist for the primal and the dual
$$\max\ \mathbf p'\mathbf b\ \ \text{s.t. }\mathbf p'\mathbf A+\mathbf s'=\mathbf c',\ \mathbf s\ge\mathbf0$$
Affine scaling pushes toward the boundary and then takes tiny steps. The cure is the potential function with $q>n$ (p. 409):
$$G(\mathbf x,\mathbf s)=q\log\mathbf s'\mathbf x-\sum_{j}\log x_j-\sum_j\log s_j$$
The first term measures the duality gap, since $\mathbf c'\mathbf x-\mathbf b'\mathbf p=\mathbf s'\mathbf x$; the others penalize closeness to the boundary of the primal and the dual.

> [!theorem] Theorem 9.4 (p. 410)
> Any algorithm that keeps primal and dual feasibility and lowers $G$ by at least $\delta>0$ per iteration reaches duality gap $(\mathbf s^K)'\mathbf x^K\le\epsilon$ after $K=\big\lceil\frac{G(\mathbf x^0,\mathbf s^0)+(q-n)\log(1/\epsilon)-n\log n}{\delta}\big\rceil$ iterations.

The proof uses $G\ge n\log n+(q-n)\log\mathbf s'\mathbf x$ (Eq. 9.7), with equality when $x_js_j=\mathbf s'\mathbf x/n$.

**Direction** (p. 411-412). Linearize $G(\mathbf x+\mathbf d,\mathbf s)$ in $\mathbf d$ subject to $\mathbf A\mathbf d=\mathbf0$ and $\|\mathbf X^{-1}\mathbf d\|\le\beta$. This is the affine scaling problem with cost vector $\nabla_xG$, whose components are $\frac{q s_i}{\mathbf s'\mathbf x}-\frac1{x_i}$. Define
$$\mathbf u^k=\Big(\mathbf I-\mathbf X_k\mathbf A'(\mathbf A\mathbf X_k^2\mathbf A')^{-1}\mathbf A\mathbf X_k\Big)\Big(\frac q{(\mathbf s^k)'\mathbf x^k}\mathbf X_k\mathbf s^k-\mathbf e\Big)$$
and $\mathbf d^k=-\beta\mathbf X_k\mathbf u^k/\|\mathbf u^k\|$. The algorithm (p. 412-413) with parameters $\beta,\gamma,q$:
- If $\|\mathbf u^k\|\ge\gamma$ (primal step): $\mathbf x^{k+1}=\mathbf x^k+\mathbf d^k$, dual unchanged.
- If $\|\mathbf u^k\|<\gamma$ (dual step): $\mathbf x$ unchanged and $\mathbf p,\mathbf s$ updated so that $\mathbf A'\mathbf p+\mathbf s=\mathbf c$ and $\mathbf s>\mathbf0$ stay true.

> [!theorem] Theorem 9.5 (p. 413)
> For $0<\beta<1$, $0<\gamma<1$: (a) a primal step lowers $G$ by at least a quantity of order $\beta\gamma-\frac{\beta^2}{2(1-\beta)}$; (b) a dual step lowers it by a bounded amount depending on $q$, $n$ and $\gamma$; (c) for $q=n+\sqrt n$, $\beta\approx0.285$, $\gamma\approx0.479$, $G$ falls by at least $\delta=0.079$ per iteration.

Only the text layer was read for the exact bounds in (a)-(b). **[unverified]**

**Initialization** (Theorem 9.6, p. 417-418): artificial variables with big-$M$ costs make a strictly feasible start; the artificial problem's optima are those of the original provided $M_1,M_2$ are large enough.

**Complexity** (p. 418). With integer data bounded by $U$, $K=O(\sqrt n\log\frac1\epsilon+n^2\log(nU))$ iterations at $O(n^3)$ work each, so $O(n^{3.5}\log\frac1\epsilon+n^5\log(nU))$ arithmetic operations: polynomial. A matching lower bound of order $\sqrt n\log(1/\epsilon)$ iterations exists (Exercise 9.6). Line searches on $G$ help in practice without improving the worst case (p. 419).

## Primal path following (§9.4, p. 419-430)
**Barrier problem** (p. 419-420). For $\mu>0$ the barrier function and problem are
$$B_\mu(\mathbf x)=\mathbf c'\mathbf x-\mu\sum_j\log x_j$$
$$\min\ B_\mu(\mathbf x)\ \ \text{s.t. }\mathbf A\mathbf x=\mathbf b$$
Its minimizers $\mathbf x(\mu)$ form the **central path** (Figure 9.4), and $\lim_{\mu\to0}\mathbf x(\mu)$ is an optimal LP solution. The minimizer as $\mu\to\infty$ is the analytic center of the feasible set, which minimizes $-\sum\log x_j$. The dual barrier problem (9.16) is $\max\ \mathbf p'\mathbf b+\mu\sum\log s_j$ on the dual feasible set.

> [!theorem] Lemma 9.5 (p. 421)
> The conditions (the Karush-Kuhn-Tucker conditions for both barrier problems)
> $$\mathbf A\mathbf x=\mathbf b,\ \ \mathbf x>\mathbf0$$
> $$\mathbf A'\mathbf p+\mathbf s=\mathbf c,\ \ \mathbf s>\mathbf0$$
> $$\mathbf X\mathbf S\mathbf e=\mu\mathbf e$$
> are sufficient (and necessary) for $\mathbf x=\mathbf x(\mu)$, $\mathbf p=\mathbf p(\mu)$, $\mathbf s=\mathbf s(\mu)$.

At $\mu=0$ the last equation is complementary slackness ([[LP duality]]). Proof: for any feasible $\mathbf x$, $B_\mu(\mathbf x)\ge\mu n+(\mathbf p^*)'\mathbf b-\mu\sum\log(\mu/s_j^*)$, with equality iff $x_j=\mu/s_j^*$. See [[KKT conditions]].

Example 9.2 (p. 422): minimize $x$ subject to $x\ge0$ has $x(\mu)=\mu$. Example 9.3 (p. 422-423): for minimize $x_2$ on the simplex $x_1+x_2+x_3=1$ the analytic center of $P$ is $(1/3,1/3,1/3)$, and the limit of the central path is $(1/2,0,1/2)$, the analytic center of the optimal face.

**Newton step on the barrier** (p. 423-424). Use the second-order Taylor model of $B_\mu(\mathbf x+\mathbf d)$:
$$\min\ (\mathbf c'-\mu\mathbf e'\mathbf X^{-1})\mathbf d+\tfrac\mu2\mathbf d'\mathbf X^{-2}\mathbf d\ \ \text{s.t. }\mathbf A\mathbf d=\mathbf0$$
Its Lagrange conditions are $\mathbf c-\mu\mathbf X^{-1}\mathbf e+\mu\mathbf X^{-2}\mathbf d-\mathbf A'\mathbf p=\mathbf0$ and $\mathbf A\mathbf d=\mathbf0$ (9.18), a linear system. The solutions are
$$\mathbf d(\mu)=\Big(\mathbf I-\mathbf X^2\mathbf A'(\mathbf A\mathbf X^2\mathbf A')^{-1}\mathbf A\Big)\Big(\mathbf X\mathbf e-\tfrac1\mu\mathbf X^2\mathbf c\Big)$$
$$\mathbf p(\mu)=(\mathbf A\mathbf X^2\mathbf A')^{-1}\mathbf A\big(\mathbf X^2\mathbf c-\mu\mathbf X\mathbf e\big)$$
After one Newton step $\mu$ is replaced by $\alpha\mu$ with $0<\alpha<1$, so the iterate stays near the moving target $\mathbf x(\mu)$ (Figure 9.6). The closeness measure is
$$\Big\|\frac1\mu\mathbf X\mathbf S\mathbf e-\mathbf e\Big\|\le\beta$$
(Eq. 9.20).

**Algorithm** (box, p. 426): start with feasible $\mathbf x^0>\mathbf0$, $\mathbf s^0>\mathbf0$, $\mathbf p^0$; stop if $(\mathbf s^k)'\mathbf x^k<\epsilon$; set $\mu^{k+1}=\alpha\mu^k$; solve
$$\mu^{k+1}\mathbf X_k^{-2}\mathbf d-\mathbf A'\mathbf p=\mu^{k+1}\mathbf X_k^{-1}\mathbf e-\mathbf c,\quad\mathbf A\mathbf d=\mathbf0$$
and set $\mathbf x^{k+1}=\mathbf x^k+\mathbf d$, $\mathbf p^{k+1}=\mathbf p$, $\mathbf s^{k+1}=\mathbf c-\mathbf A'\mathbf p$.

> [!theorem] Theorem 9.7 (p. 426-427)
> Take $\alpha=1-\frac{\sqrt\beta-\beta}{\sqrt\beta+\sqrt n}$ with $\beta<1$ and a feasible start with $\|\frac1{\mu^0}\mathbf X_0\mathbf S_0\mathbf e-\mathbf e\|\le\beta$. After
> $$K=\Big\lceil\frac{\sqrt\beta+\sqrt n}{\sqrt\beta-\beta}\log\frac{(\mathbf s^0)'\mathbf x^0(1+\beta)}{\epsilon(1-\beta)}\Big\rceil$$
> iterations the duality gap is $(\mathbf s^K)'\mathbf x^K\le\epsilon$.

The proof shows by induction that iterates stay feasible and positive with $\|\mathbf X_k^{-1}\mathbf d\|\le\sqrt\beta<1$, and that $\mu^k(1-\beta)n\le(\mathbf s^k)'\mathbf x^k\le\mu^k(1+\beta)n$ (9.23).

**Initialization and complexity** (p. 429-431). An artificial problem with $\mathbf e'\mathbf x\le n+2$ gives a start with $\beta=1/4$. The iteration count is $O(\sqrt n\log(\epsilon_0/\epsilon))$, with $O(n^3)$ work per iteration, which is polynomial in $n$, $\log U$ and $\log(1/\epsilon)$.

## Primal-dual path following (§9.5, p. 431-437)
Instead of Newton on the barrier problem, apply Newton's method for root finding, $\mathbf F(\mathbf z^k)+\mathbf J(\mathbf z^k)\mathbf d=\mathbf0$ (9.27), directly to the system (9.26) with $\mathbf z=(\mathbf x,\mathbf p,\mathbf s)$:
$$\mathbf F(\mathbf z)=\begin{pmatrix}\mathbf A\mathbf x-\mathbf b\\\mathbf A'\mathbf p+\mathbf s-\mathbf c\\\mathbf X\mathbf S\mathbf e-\mu\mathbf e\end{pmatrix}$$
At a feasible point the Newton direction solves (9.28)-(9.30):
$$\mathbf A\mathbf d_x=\mathbf0$$
$$\mathbf A'\mathbf d_p+\mathbf d_s=\mathbf0$$
$$\mathbf S_k\mathbf d_x+\mathbf X_k\mathbf d_s=\mu_k\mathbf e-\mathbf X_k\mathbf S_k\mathbf e$$
Step lengths $\beta_P,\beta_D=\min\{1,\alpha\min(-x_i/(d_x)_i)\}$ (and the same for $s$) with $0<\alpha<1$ keep positivity. The barrier parameter is set $\mu_k=\rho_k(\mathbf s^k)'\mathbf x^k/n$ with $\rho_k=1$ unless progress stalls (p. 434). A slightly different step rule gives $O(\sqrt n\log(\epsilon_0/\epsilon))$ iterations (p. 435); the observed average is $O(\log n\log(\epsilon_0/\epsilon))$ (p. 438). It is the method of choice in commercial codes (p. 431).

**Infeasible variant** (p. 435-436): start from $\mathbf x^0>\mathbf0$, $\mathbf s^0>\mathbf0$ that need not satisfy the equations; the same Newton system with right-hand sides $\mathbf A\mathbf x^k-\mathbf b$ and $\mathbf A'\mathbf p^k+\mathbf s^k-\mathbf c$.

**Self-dual method** (p. 436-437): the homogeneous self-dual problem (9.33), with extra variables $\tau,\theta,\kappa$, is always feasible and has the interior start $(\mathbf x^0,\mathbf p^0,\mathbf s^0,1,1,1)$.

> [!theorem] Theorem 9.8 (p. 437)
> Take an optimal solution of (9.33) with $\theta^*=0$ and strict complementarity. (a) The original problem has an optimal solution iff $\tau^*>0$, and then $\mathbf x^*/\tau^*$ and $(\mathbf p^*/\tau^*,\mathbf s^*/\tau^*)$ are optimal. (b) Otherwise $\kappa^*>0$ and the problem is unbounded or infeasible, as determined by the signs of $\mathbf c'\mathbf x^*$ and $-\mathbf b'\mathbf p^*$.

This needs no assumption of feasibility and can start anywhere.

## Overview (§9.6, p. 438-440)
Directions at a feasible $\mathbf x$ are linear combinations of the affine scaling and centering directions:
$$\mathbf d_{\text{affine}}=-\mathbf X^2(\mathbf I-\mathbf A'(\mathbf A\mathbf X^2\mathbf A')^{-1}\mathbf A\mathbf X^2)\mathbf c$$
$$\mathbf d_{\text{centering}}=(\mathbf I-\mathbf X^2\mathbf A'(\mathbf A\mathbf X^2\mathbf A')^{-1}\mathbf A)\mathbf X\mathbf e$$
The book states the path-following direction (p. 438) is a linear combination of these two; the exact coefficients were not read from an image. **[unverified]** Centering dominates early (large $\mu$), affine scaling late. Potential reduction behaves likewise. Since path following and potential reduction are polynomial and affine scaling has no polynomial bound, centering seems responsible for polynomiality (p. 439). Guideline: the simplex method does poorly on large, massively degenerate problems, which hardly hurt interior point methods (p. 439).

## Notes
- Wiki note: the dual estimate $\mathbf p$ and reduced costs $\mathbf r$ reuse [[BT ch4 - Duality theory]] and [[BT ch3 - The simplex method]] unchanged, which explains why affine scaling starting near a vertex follows edges (p. 394).
- Wiki note: the term "Karush-Kuhn-Tucker" appears here for the central path system (9.17).
- Sources credited (p. 448): Karmarkar's 1984 algorithm started the field; Dikin (1974) analyzed short-step affine scaling; Ye (1991) potential reduction. **[unverified]** for the exact attributions beyond those named.

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf 409-466, printed pp. 393-450). Pages viewed as images: pdf 412, 413, 416, 425, 442; the rest read from the text layer.
**Last updated**: 2026-11-06

---

## Related pages
- [[Interior point method]] · [[Linear programming]] · [[Simplex method]] · [[LP duality]] · [[KKT conditions]]
- [[Newton's method]] · [[Convex function]]
- [[BT ch3 - The simplex method]] · [[BT ch4 - Duality theory]] · [[BT ch8 - Complexity of LP and the ellipsoid method]] · [[BT ch11 - Integer programming]]
- [[BJS ch4 - Starting solution and convergence]]
