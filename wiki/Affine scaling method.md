---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 9 §9.1-9.2; Bazaraa, Jarvis, Sherali 2010, §8.6"
tags: [optimization]
---

# Affine scaling method

**Intuition**: stand at a strictly positive feasible point $\mathbf y$, rescale so $\mathbf y$ becomes the all-ones vector, and move to the best point of an ellipsoid that lies inside the positive orthant. Unlike the ellipsoid method of [[Ellipsoid method]], whose ellipsoid contains the feasible set, the affine scaling ellipsoid lies inside it (BT p. 393-395). It is the simplest [[Interior point method]]; it starts from a strictly positive feasible point and is not known to be polynomial. Setting: the standard form pair $\min\mathbf c'\mathbf x$, $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\ge\mathbf0$ and its dual (stated in [[Interior point method]]); the interior of the feasible set $P$ is $\{\mathbf x\in P\mid\mathbf x>\mathbf0\}$.

## Ellipsoid, direction and algorithm
**Ellipsoid inside the positive orthant** (BT §9.1, Lemma 9.1, p. 396). For $\beta\in(0,1)$, $\mathbf y>\mathbf0$ and
$$S=\Big\{\mathbf x\ \Big|\ \sum_i\frac{(x_i-y_i)^2}{y_i^2}\le\beta^2\Big\}$$
every $\mathbf x\in S$ has $\mathbf x>\mathbf0$. With $\mathbf Y=\mathrm{diag}(y_1,\dots,y_n)$ this is $\|\mathbf Y^{-1}(\mathbf x-\mathbf y)\|\le\beta$. Intersecting with $\mathbf A\mathbf x=\mathbf b$ gives an ellipsoid $S_0$ inside the feasible set (Figure 9.2, p. 397).

**Step problem** (9.1)-(9.2, p. 397). With $\mathbf d=\mathbf x-\mathbf y$ and $\mathbf A\mathbf y=\mathbf b$:
$$\min\ \mathbf c'\mathbf d\ \ \text{s.t. }\mathbf A\mathbf d=\mathbf0,\ \ \|\mathbf Y^{-1}\mathbf d\|\le\beta$$

> [!theorem] Lemma 9.2 (p. 397)
> Assume the rows of $\mathbf A$ are independent, $\mathbf c$ is not a combination of the rows of $\mathbf A$, and $\mathbf y>\mathbf0$. The optimal direction is
> $$\mathbf d^*=-\beta\frac{\mathbf Y^2(\mathbf c-\mathbf A'\mathbf p)}{\|\mathbf Y(\mathbf c-\mathbf A'\mathbf p)\|}$$
> with $\mathbf p=(\mathbf A\mathbf Y^2\mathbf A')^{-1}\mathbf A\mathbf Y^2\mathbf c$. Then $\mathbf x=\mathbf y+\mathbf d^*\in P$ and $\mathbf c'\mathbf x=\mathbf c'\mathbf y-\beta\|\mathbf Y(\mathbf c-\mathbf A'\mathbf p)\|<\mathbf c'\mathbf y$.

Proof (p. 398): $\mathbf A\mathbf Y^2\mathbf A'$ is invertible, $\mathbf d^*$ is feasible, and optimality follows from the Schwarz inequality. If $\mathbf d^*\ge\mathbf0$ the problem is unbounded with cost $-\infty$.

**Dual estimates** (p. 398-399). Applying the formula for $\mathbf p$ at a nondegenerate basic feasible solution $\mathbf y$ gives $\mathbf p=(\mathbf B')^{-1}\mathbf c_B$, the dual basic solution of [[LP duality]]. The vector $\mathbf r=\mathbf c-\mathbf A'\mathbf p$ is then the reduced cost vector of [[Simplex method]]. So $\mathbf p$ is called the dual estimate for any $\mathbf y$. If $\mathbf r\ge\mathbf0$, $\mathbf p$ is dual feasible and the duality gap is
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

## Convergence of short-step affine scaling
Theorem 9.2 (Bolzano-Weierstrass: every bounded sequence has a convergent subsequence), Lemma 9.4 and Theorem 9.3 (pp. 405-408) prove that the short-step iterates converge to a basic feasible solution, under the nondegeneracy assumptions. The proof shows the sequence is bounded, every limit point is a basic feasible solution (via complementary slackness in the limit), the limit is unique, and it is optimal because otherwise a negative reduced cost would drive that variable up. Once near the optimum the cost falls geometrically (Exercise 9.1, p. 409). The detailed steps were read from the text layer only. **[unverified]**


## BJS version

BJS (§8.6, p. 428-440) apply affine scaling to the barrier problem and let $\mu\to0$, which recovers the standard affine scaling method, convergent for all step lengths $0<\alpha<1$ regardless of degeneracy (p. 434; text layer only, images not seen). This is the limiting case of the [[Path-following interior point methods]].

## Key facts
- Each iteration moves to the best point of the inscribed ellipsoid $\|\mathbf Y^{-1}\mathbf d\|\le\beta$ with dual estimate $\mathbf p$ computed for free, at $O(n^3)$ work per iteration.
- The dual estimate and reduced costs are those of the [[Simplex method]] and [[LP duality]] unchanged, which explains why affine scaling started near a vertex follows edges (BT p. 394).
- Long-step variants (Eq. 9.5) are the most popular; convergence for $\beta<2/3$ holds without nondegeneracy, while $\beta>2/3$ can fail on the dual side (BT p. 403).
- Dikin (1974) analyzed short-step affine scaling (BT p. 448).
- No polynomial bound is known; see [[Complexity of linear programming]] and the contrast in [[Interior point method]].

**Covered in**: Bertsimas-Tsitsiklis ch. 9 §9.1-9.2 (pp. 395-409); Bazaraa-Jarvis-Sherali ch. 8 §8.6 (p. 434)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 9; printed pp. 393-409, pdf 412, 413, 416 viewed as images, the rest read from the text layer); `text_books/Linear Optimization/BJS full book.pdf` (ch. 8, printed pp. 428-440, text layer).
**Last updated**: 2026-11-06

---

## Related pages
- [[Interior point method]] · [[Path-following interior point methods]] · [[Ellipsoid method]] · [[Simplex method]] · [[LP duality]] · [[Linear programming]] · [[Complexity of linear programming]]
