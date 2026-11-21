---
type: concept
area: bayesian
areas: [bayesian, ift]
source-ref: "Enßlin, IT & IFT, ch. 2, §2.1-2.5, eqs. 73-99"
tags: [bayesian, ift]
---

# Bayesian decision theory

**Summary**: Given a posterior over an unknown signal and a loss function, the optimal action minimizes the posterior expected loss. Quadratic, absolute and delta losses give the posterior mean, median and mode. The book also uses the same set-up to say what an intelligent system learns.

**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf` (citations below are section, equation and PDF page).
**Covered in**: Enßlin IT & IFT ch. 2 (pp. 33-41)
**Last updated**: 2026-11-21

---

## Set-up
Convention (§2.1.5, p. 36): data $d$ known; signal or situation $s$ unknown and of interest; noise or nuisance $n$ unknown and not of interest.

> [!definition] Expected utility and optimal action
> A loss $l(a,s)$ for action $a\in A$ if the true situation is $s$; utility $u=-l$. Given knowledge $I$ on $s$,
> $$u(a,I)=\langle u(a,s)\rangle_{(s\mid I)}=-l(a,I)$$
> $$a^\star(I)=\arg\max_a u(a,I)=\arg\min_a l(a,I)$$
> Calibration of probabilities to frequencies is what makes the expectation equal the average actually achieved.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §2.2, eqs. 73-74, p. 36)

Footnote (p. 36): $l(a,s)$ with a situation as second argument is a loss; $l(a,I)$ with knowledge as second argument is an expected loss.

## Standard losses (§2.3, pp. 38-39)

| loss $l(a,s)$ | optimal estimate under $P(s\mid d)$ |
|---|---|
| $(a-s)^2$ (eq. 77) | posterior mean $\langle s\rangle$ (eq. 82) |
| $\lvert a-s\rvert$ (eq. 83) | posterior median, $\int_{-\infty}^aP=1/2$ (eq. 91) |
| $-\delta(a-s)$ (eq. 92) | posterior mode, the MAP estimate (eq. 94) |

The delta loss penalizes every miss equally, which the book calls a "military" loss. Fig. 5 (p. 39) compares mode, median and mean. Wiki note: the MAP estimate used throughout [[Information field theory]] corresponds to this last case.

## Attention (§2.4, pp. 39-40)
Suppose in each situation $s$ the utility has a smooth peak, $u(a,s)=v(s)-\tfrac12w(s)\,(a-b(s))^2$ with best action $b(s)$ and curvature $w(s)$ (eq. 95). Then
$$a^\star=\frac{\langle b(s)\,w(s)\rangle}{\langle w(s)\rangle}=\int ds\,\mathcal A^{(w)}(s\mid I)\,b(s),\qquad \mathcal A^{(w)}=\frac{w\,P(s\mid I)}{\int ds\,w\,P}$$
The weight $\mathcal A^{(w)}$ is called attention: probable and critical (sharply peaked utility) situations get more of it. The book stresses that attention is a limited resource.

## Learning from experience (§2.5, pp. 40-42)
Nature draws situations $s\sim P(s\mid I_A)$ and data $d\sim P(d\mid s,I_A)$. A reasoning system, or data filter, $I_B:D\to I$ turns data into knowledge and then into the action $a^\star(I_B(d))$. Its quality is the expected utility
$$U_S(I_A,I_B)=\langle u(a^\star(I_B(d)),s)\rangle_{(d,s\mid I_A)}\approx\frac1N\sum_iu(a^\star(I_B(d_i)),s_i)$$
(eqs. 96-99). Optimal reasoning, training or evolution maximizes this. Alternatively the system learns the action directly from data (Pavlov-like conditioning, the book's spelling "Pawlow"); this is cheaper but cannot adapt when the loss changes (Fig. 7).

## From utility to information
When the "action" is the knowledge state sent to someone else, the utility-free criterion that satisfies the book's five axioms is the [[Achieved information gain]], which leads to the [[Maximum entropy principle]] for decoding. §2.1 also frames intelligence as probabilities plus decision theory plus information measures plus perception; the book's claim that IFT models equal generative neural networks and inference equals training is stated as motivation only (§2.1, p. 33).

## Where it appears
- [[Bayesian inference]]: supplies the posterior that the expected loss averages over.
- [[Active learning]]: value-of-information acquisition is expected utility.
- [[Fisher information]]: sensitivity of expected information gain.

---

## Related pages
- [[Cox's theorem]] · [[Achieved information gain]] · [[Maximum entropy principle]] · [[Bayesian inverse problems]]
