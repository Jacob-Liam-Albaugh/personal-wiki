---
type: theorem
area: operators
source-ref: "Kovachki, Lanthaler, Stuart 2024, §5.2, pp. 21-27; Prop. 5.4"
tags: [operators, ml]
---

# Curse of parametric complexity

> [!theorem] Proposition 5.4 — DeepONet lower bound (Kovachki et al. 2024, pp. 25-26)
> Let $K=\{u\in C^k(D):\|u\|_{C^k}\le1\}\subset C(D)$ and $\alpha>2+k/d$. For every $r\in\mathbb N$ there is an $r$-times Fréchet-differentiable $\Psi^\dagger:C(D)\to\mathbb R$ and constants $c,\bar\varepsilon>0$ (depending only on $k,\alpha,r$) such that any [[DeepONet]] $\Psi$ with $\varepsilon\le\bar\varepsilon$ and
> $$\sup_{u\in K}|\Psi^\dagger(u)-\Psi(u)|\le\varepsilon$$
> has
> $$\operatorname{size}(\psi)\ge\exp\big(c\,\varepsilon^{-1/(\alpha r)}\big)$$
>
> (source: `papers/Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`, pp. 25-26; the review attributes it to its ref. [78, Ex. 2.17])

**Intuition**: for operators that are merely Lipschitz or $C^r$, standard architectures need a parameter count exponential in a power of $1/\varepsilon$. Smoothness in the usual sense is not enough. Efficient operator learning needs extra structure.

## Heuristic
Use the [[Encoder-decoder operators]] split $\mathcal E\lesssim\mathcal E_U+\mathcal E_\psi+\mathcal E_V$ with $\mathcal E_U\lesssim d_U^{-\alpha}$ and the Yarotsky network bound $\operatorname{size}(\psi)\sim d_V\,\varepsilon^{-d_U/k}$ (pp. 22-24). Then $d_U\sim\varepsilon^{-1/\alpha}$, so
$$\operatorname{size}(\psi)\gtrsim\exp\big(c\,\varepsilon^{-1/\alpha}/k\big)\quad\text{(eq. 5.7)}$$
With $\alpha=s/d$ this is $\exp(c\,\varepsilon^{-d/s}/k)$ (eq. 5.8).

## Rigorous versions
- **Nonlinear $n$-width** (pp. 24-25, simplified from the review's ref. [97]): for 1-Lipschitz functionals on a Sobolev ball $K_s$, the width decays only like $\log(n)^{-s/d}$. So any continuous encoder-decoder pair needs $n\gtrsim\exp(c\,\varepsilon^{-d/s})$ (eq. 5.9).
- **Samples**: the sample complexity has the same form, $N\gtrsim\exp(c\,\varepsilon^{-d/s})$ (p. 27).
- Remark 5.5: the exponent was not optimised, and the $r$ may be an artifact of the proof.

## Ways out
The review lists:
- holomorphic operators, which give algebraic rates;
- operator Barron spaces;
- operators with explicit formulas, or networks that emulate numerical schemes;
- hyperexpressive or "3D" networks, which cut the parameter count but need more bits of precision.

## Where it appears
- [[Operator learning review (Kovachki 2024)]]: the central negative result.

**Sources**: `papers/Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Universal approximation for operators]] · [[Operator learning]] · [[DeepONet]]
