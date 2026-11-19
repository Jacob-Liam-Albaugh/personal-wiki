---
type: method
area: stochastic
areas: [math]
source-ref: "Mak, Morton, Wood 1999, Thms 1-2, eqs. 7-10"
tags: [optimization, uq]
---

# Sample average approximation and optimality-gap bounds

> [!algorithm] SAA lower bound and gap confidence interval
> For $z^*=\min_{x\in X}\mathbb E f(x;\tilde\xi)$, draw $n$ i.i.d. scenarios and solve
> $$z_n^*=\min_{x\in X}\frac1n\sum_{i=1}^n f(x;\tilde\xi_i).$$
> Then $\mathbb E z_n^*\le\mathbb E z_{n+1}^*\le z^*$. For any candidate $\hat x$ the optimality gap is $\mathbb E f(\hat x;\tilde\xi)-z^*\ge0$; with $n_g$ i.i.d. batches of size $n$ sharing scenarios between the two terms,
> $$G_n=\frac1n\sum_{i=1}^n f(\hat x;\tilde\xi_i)-\min_{x\in X}\frac1n\sum_{i=1}^n f(x;\tilde\xi_i)\ \ge 0,\qquad \mathbb E G_n\ge \mathbb E f(\hat x;\tilde\xi)-z^*,$$
> and $[0,\ \bar G(n_g)+\epsilon_g]$ with $\epsilon_g=t_{n_g-1,\alpha}\,s_g(n_g)/\sqrt{n_g}$ is an approximate $(1-\alpha)$ confidence interval for the gap.
>
> (source: `Mak, Morton, Wood - Monte Carlo Bounding Techniques for Determining Solution Quality in Stochastic Programs.pdf`, Thms 1-2, eqs. 9-10)

**Intuition**: optimising over only $n$ sampled futures lets the decision "peek", so the optimum is optimistic on average and gives a statistical lower bound on the true optimum. A sample-mean estimate of the candidate's true cost is an upper bound. Their difference bounds how far the candidate is from optimal, for any candidate however it was produced.

## Basic consequences
- Upper bound: $U(n_u)=\frac1{n_u}\sum f(\hat x;\tilde\xi_i)$ is unbiased for $\mathbb E f(\hat x;\tilde\xi)\ge z^*$ and satisfies a CLT (eqs. 2-3).
- Independent streams: $[0,[U-L]_++\epsilon_\ell+\epsilon_u]$ is an approximate $(1-2\alpha)$ interval (eqs. 7-8, Boole-Bonferroni).
- Common random numbers (same scenarios in both terms) give $G_n\ge0$ and lower variance (§3.2).
- Needs no convexity of $X$ or of $\mathbb E f$; integer variables are allowed (Thm 1 remark).

## Failure modes
- The interval is valid only for large enough $n_\ell,n_u,n_g$ (CLT) and when $n$ is large enough that $z_n^*$ is a useful bound; the bound itself is only optimistic in expectation.
- Needs the approximating problem to be solvable at the chosen $n$ (SSN needed $n=1000$, 2443 CPU min).

## Where it appears
- [[Monte Carlo bounding for stochastic programs (Mak 1999)]]: introduces the bound and the CRN gap estimator.

**Sources**: `papers/Stochastic Methods/Mak, Morton, Wood - Monte Carlo Bounding Techniques for Determining Solution Quality in Stochastic Programs.pdf`.
**Last updated**: 2026-11-19

---

## Related pages
- [[Branch and bound]]
- [[Latin hypercube sampling]]
- [[SGD]]
