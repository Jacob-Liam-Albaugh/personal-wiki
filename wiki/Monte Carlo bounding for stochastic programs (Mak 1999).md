---
type: paper
area: stochastic
areas: [math]
source-ref: "Mak, Morton, Wood 1999, Oper. Res. Lett. 24:47-56"
tags: [optimization, uq]
authors: ["[[Wai-Kei Mak]]", "[[David P. Morton]]", "[[R. Kevin Wood]]"]
year: 1999
venue: "Operations Research Letters 24 (1999) 47-56"
file: "[[papers/Stochastic Methods/Mak, Morton, Wood - Monte Carlo Bounding Techniques for Determining Solution Quality in Stochastic Programs.pdf]]"
---

# Monte Carlo bounding for stochastic programs (Mak 1999)

**Summary**: The optimum $z_n^*$ of a sampled approximating problem is, in expectation, a lower bound on the true optimum $z^*$ of a stochastic program, and the bound improves monotonically with $n$. Batch means turn this into confidence intervals on the optimality gap of any candidate solution; common random numbers keep the gap estimate nonnegative and cut variance by factors of 17 to 4100 on four test problems.

**Authors**: Wai-Kei Mak, David P. Morton, R. Kevin Wood · **Year**: 1999 · **File**: [[papers/Stochastic Methods/Mak, Morton, Wood - Monte Carlo Bounding Techniques for Determining Solution Quality in Stochastic Programs.pdf]]

---

## Problem

Stochastic program $z^*=\min_{x\in X}\mathbb E f(x;\tilde\xi)$ with approximating problem SP$_n$ (§1). Sampling-based solvers (external SAA, or internal cutting-plane and stochastic quasi-gradient methods) return finitely generated candidates $\hat x$ whose quality is hard to judge. Alternatives are testing KKT conditions (little use for a suboptimal statistical solution) or asymptotics of $\sqrt n(x_n^*-x^*)$ (usually non-normal under constraints). The paper bounds the **optimality gap** $\mathbb E f(\hat x;\tilde\xi)-z^*$ instead. Assumptions: $f$ has finite mean and variance, i.i.d. samples are available, SP$_n$ is solvable at the chosen $n$, and $f(x;\xi)$ is evaluable exactly (§1).

## Method

See [[Sample average approximation]].

> [!theorem] Theorem 1: lower bound (source: file, §2.2)
> $\mathbb E z_n^*=\mathbb E\min_x\frac1n\sum f(x;\tilde\xi_i)\le z^*$. Proof: $\min_x\mathbb E[\cdot]\ge\mathbb E\min_x[\cdot]$. Holds for any unbiased estimator $F$ in place of the sample mean, nonconvex $X$, integer variables. $n=1$ is the wait-and-see bound of Madansky.

> [!theorem] Theorem 2: monotonicity (source: file, §2.2)
> $\mathbb E z_{n+1}^*\ge\mathbb E z_n^*$. Proof: write the $(n+1)$-sample mean as the average of the $n+1$ leave-one-out $n$-sample means and use min-of-average $\ge$ average-of-min.

- **Upper bound**: $U(n)=\frac1n\sum f(\hat x;\tilde\xi_i)$, unbiased for $\mathbb E f(\hat x;\tilde\xi)\ge z^*$, CLT eq. 3.
- **Independent streams** (§3.1): $L(n_\ell)=\frac1{n_\ell}\sum_i z_n^{*i}$ from $n_\ell$ i.i.d. batches, CLT eq. 6, interval eq. 8: $[0,[U(n_u)-L(n_\ell)]_++\epsilon_\ell+\epsilon_u]$ at joint level $\approx1-2\alpha$.
- **Common random numbers** (§3.2): $G_n\ge0$ and $\mathbb E G_n\ge\mathbb E f(\hat x)-z^*$ (eq. 9); interval $[0,\bar G(n_g)+\epsilon_g]$ at level $1-\alpha$ (eq. 10).
- Related bounds: Lagrangian relaxation of non-anticipativity (eq. 4, Higle-Sen), weaker in expectation but separable by scenario; Benders-cut view (eq. 5).

## Results

Four two-stage stochastic LPs (Table 1): DB1 (vehicle allocation), WRPM1 (power capacity expansion), 20TERM (freight fleet), SSN (telecom network), solved by regularized decomposition. All use $n_\ell=n_g=30$ batches of size $n=25$ (SSN: 1000).

| Problem | Naive 95% gap CI (Table 2) | CRN 95% gap CI (Table 3) | Variance reduction |
|---|---|---|---|
| DB1 | [0, 328] | [0, 28] | 4100 |
| WRPM1 | [0, 1329] | [0, 243] | 460 |
| 20TERM | [0, 2616] | [0, 187] | 1300 |
| SSN | [0, 1.09] | [0, 0.77] | 17 |

CRN interval widths are 0.2%, 0.08%, 0.07% and 8% of the upper-bound estimates. Naive streams gave $U<L$ on DB1 (negative gap estimate), hence the $[\cdot]_+$ in eq. 8. Candidate $\hat x$ for naive: average of the $n_\ell$ lower-bound optimisers; for CRN: solve a separate SP with $2n$ scenarios. Warm-starting regularized decomposition from averaged earlier optima saved 25%, 100%, 330% time on DB1, WRPM1, 20TERM.

## Limitations

As stated: intervals rest on CLTs and large enough sample sizes; multi-stage extension is only sketched (recursive application of Thm 1); efficiency (other variance reduction, cut reuse, parallel solves) is open; SSN is expensive (2563 CPU min). Wiki note: a bound that is optimistic only in expectation says nothing about a single realisation, and the gap interval is one-sided, so it certifies "at most this far from optimal", never "optimal".

## Connections

- Gives the evaluation template (statistical upper bound minus statistical lower bound, with a confidence level) used when a stochastic objective is optimised by sampling; compare the ELBO as a lower bound on $\log p$ in [[ELBO]] and [[Variational inference]] (Wiki note: the direction and the randomness differ; here the lower bound is random but unbiased for a deterministic constant $\le z^*$).
- Sampling-based optimisers: [[SGD]] (internal sampling); [[Branch and bound]] for global versions (Norkin et al.); variance-reduction relatives such as [[Latin hypercube sampling]].

**Sources**: `papers/Stochastic Methods/Mak, Morton, Wood - Monte Carlo Bounding Techniques for Determining Solution Quality in Stochastic Programs.pdf`.
**Last updated**: 2026-11-19

---

## Related pages
- [[Sample average approximation]]
- [[SGD]]
- [[Branch and bound]]
- [[Latin hypercube sampling]]
- [[ELBO]]
