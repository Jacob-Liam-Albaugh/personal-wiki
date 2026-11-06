---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 9 §9.4-9.5; Bazaraa, Jarvis, Sherali 2010, §8.6"
tags: [optimization]
---

# Path-following interior point methods

**Intuition**: replace the nonnegativity constraints by a logarithmic barrier, solve the barrier problem approximately with Newton's method ([[Newton's method]]), and let the barrier weight $\mu$ fall; the minimizers trace the central path to an LP optimum. Path following is the method of choice in large implementations and commercial codes (BT p. 394-395, 431). Setting: the standard-form primal and dual of [[Interior point method]].

## Primal path following
**Barrier problem** (BT §9.4, p. 419-420). For $\mu>0$ the barrier function and problem are
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

## Primal-dual path following
(BT §9.5, p. 431-437) Instead of Newton on the barrier problem, apply Newton's method for root finding, $\mathbf F(\mathbf z^k)+\mathbf J(\mathbf z^k)\mathbf d=\mathbf0$ (9.27), directly to the system (9.26) with $\mathbf z=(\mathbf x,\mathbf p,\mathbf s)$:
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


## BJS version: primal-dual path following

BJS (§8.6, p. 433-434, text layer only, images not seen) apply one Newton step to the perturbed KKT system, neglecting a second-order product term $d_{v_j}d_{x_j}$ in system (8.41c) so that the direction is the unique solution of a linear system. A unit step gives the new iterate (8.42). With the step parameter chosen as $\beta=1-\delta/\sqrt n$ with $\delta=0.35$ (eq. 8.43, formula garbled, **[unverified]**), the new iterate stays near the central path and the optimality gap shrinks geometrically as $\beta^k$ (eq. 8.44), so after $k>4L\ln2/[-\ln\beta]$ iterations the gap is below $2^{-2L}$ and an optimal rounding is possible. The barrier parameter is reduced by $\mu_{k+1}=\mu_k/n$ for $n\le5000$ and $\mu_k/\sqrt n$ otherwise (eq. 8.45, **[unverified]**). BT's counterpart is the step-length rule above; both give $O(\sqrt n\log(1/\epsilon))$ iterations in theory.

**Predictor-corrector** (BJS p. 434): first take a predictor step in the direction of the system with $\mu_{k+1}=0$ and the second-order term neglected, then a corrector. It is described as one of the most computationally effective interior point variants.

## Key facts
- The central path system $\mathbf A\mathbf x=\mathbf b$, $\mathbf A'\mathbf p+\mathbf s=\mathbf c$, $\mathbf X\mathbf S\mathbf e=\mu\mathbf e$ is the [[KKT conditions]] of the barrier problems; at $\mu=0$ the last equation is complementary slackness ([[LP duality]]).
- Both variants take $O(\sqrt n\log(\epsilon_0/\epsilon))$ iterations at $O(n^3)$ work each (polynomial, see [[Complexity of linear programming]]); the observed average is $O(\log n\log(\epsilon_0/\epsilon))$ iterations.
- The self-dual homogeneous formulation (Thm 9.8) needs no feasibility assumption and decides optimality, unboundedness or infeasibility.
- Interior point codes return a point in the relative interior of the optimal face, so a crossover to a basis is needed for reoptimization ([[LP in practice]]).

**Covered in**: Bertsimas-Tsitsiklis ch. 9 §9.4-9.5 (pp. 419-437); Bazaraa-Jarvis-Sherali ch. 8 §8.6 (pp. 433-434)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 9; printed pp. 419-437, pdf 425 viewed as image, the rest read from the text layer); `text_books/Linear Optimization/BJS full book.pdf` (ch. 8, printed pp. 433-434, text layer).
**Last updated**: 2026-11-06

---

## Related pages
- [[Interior point method]] · [[Affine scaling method]] · [[Newton's method]] · [[KKT conditions]] · [[LP duality]] · [[Linear programming]] · [[Complexity of linear programming]] · [[LP in practice]] · [[Convex function]]
