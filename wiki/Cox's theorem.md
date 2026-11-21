---
type: theorem
area: bayesian
areas: [bayesian, ift]
source-ref: "Enßlin, IT & IFT, ch. 1, §1.3-1.5 (sketch after Cox 1946, Jaynes, Caticha)"
tags: [bayesian, ift]
---

# Cox's theorem

> [!theorem] Consistent plausibility is probability
> Degrees of plausibility $\pi(A\mid B)$ that are real numbers, agree with common sense and are self-consistent can be re-scaled to $\omega\in[0,1]$ such that
> $$\omega(AB\mid C)=\omega(A\mid BC)\,\omega(B\mid C)$$
> $$\omega(\bar A\mid B)=\big(1-\omega(A\mid B)^m\big)^{1/m}$$
> The exponent $m$ only labels equivalent systems. The choice $m=1$ gives probabilities $P$ with the product rule and the sum rule $P(A\mid B)+P(\bar A\mid B)=1$.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §1.3.2-1.4, eqs. 3-9, pp. 15-17; p. is the PDF page)

The book gives a sketch only. It points to Cox, Jaynes and Caticha, and to a more rigorous proof elsewhere (ref. 24 in its bibliography). This page follows the sketch.

**Intuition**: if you want a number for "how plausible is A given B" that never contradicts itself, there is essentially one way to do arithmetic with it, and that is probability theory. Probability is logic extended to uncertainty, not a separate invention.

## Ingredients of the sketch
- **Desiderata** (§1.3.1, pp. 14-15): (I) plausibilities are real numbers, larger means more plausible; (II) qualitative agreement with common sense, Aristotelian logic included; (III) consistency: different routes to a conclusion agree, equivalent knowledge gives equal plausibility, all available information is used.
- **Product rule from associativity**: $AB\mid C$ can be decomposed two ways, so $\pi(AB\mid C)=f(\pi(B\mid C),\pi(A\mid BC))=f(\pi(A\mid C),\pi(B\mid AC))$ (eq. 1). Decomposing $ABC\mid D$ gives $f(f(x,y),z)=f(x,f(y,z))$ (eq. 2). Cox showed this lets one transform to $\omega$ with $\omega(f(x,y))=\omega(x)\,\omega(y)$ (eq. 3).
- **True and false** (§1.3.3, pp. 15-16): certainty forces $\omega=1$; impossibility forces $\omega=0$ (or $\infty$, the same system with $\omega'=1/\omega$). Convention: $\omega\in[0,1]$.
- **Negation** (§1.3.4, p. 16): a decreasing $S$ with $S(0)=1$, $S(1)=0$ and consistency must be $S_m(x)=(1-x^m)^{1/m}$ (eq. 6). Each $m$ is a legitimate plausibility system.
- **Boolean algebra** (§1.2, pp. 13-14): "and", "or", "not" with idempotency, commutativity, associativity, distributivity and duality (De Morgan) underlie the argument.

## Consequences (§1.5, pp. 18-19)
- Marginalization, the generalized sum rule $P(A+B)=P(A)+P(B)-P(AB)$ (eq. 12) and Bayes' theorem (eq. 13) follow; see [[Bayesian inference]].
- The strong, weak and weaker syllogisms of Aristotelian logic are special cases: if $A\Rightarrow B$ then $P(B\mid AI)=1$ and $P(A\mid\bar B I)=0$, and learning $B$ can only raise $P(A)$ (§1.5.1).
- Laplace's principle of insufficient reason (eq. 14): knowledge that is symmetric under permuting $n$ exclusive and exhaustive options gives $P(A_i\mid I)=1/n$.
- Other foundations the book lists: relative frequencies, Kolmogorov set theory, de Finetti bets (§1.4.1). Chapter 2 adds calibration: a known frequency $f$ should be the probability, $P(A\mid B,F=f)=f$ (§2.1.1, p. 34).

## Where it appears
- [[Bayesian inference]]: the rules above applied to signal and data.
- [[Maximum entropy principle]] and [[Achieved information gain]]: both treat probabilities as the language of knowledge states.

Wiki note: Cox's regularity assumptions (differentiability of $f$, richness of the set of propositions) are debated in the literature, which is why the book defers to a more rigorous proof **[unverified]**.

**Covered in**: Enßlin IT & IFT ch. 1 (pp. 13-19)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Bayesian inference]] · [[Bayesian decision theory]] · [[Maximum entropy principle]]
- [[Information field theory]]
