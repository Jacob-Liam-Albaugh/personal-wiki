---
type: definition
area: ift
areas: [ift, bayesian]
source-ref: "Enßlin IT & IFT, ch. 5, pp. 79-82 (PDF pages)"
tags: [ift, bayesian, inverse-problems]
---

# Information Hamiltonian

**Summary**: the negative log of the joint probability of data and signal, $\mathcal H(d,s)=-\ln P(d,s)$. Bayes' theorem becomes $P(s|d)=e^{-\mathcal H(d,s)}/\mathcal Z(d)$, with the evidence as a [[Partition function]]. For a linear measurement with Gaussian noise and a Gaussian prior it is quadratic, and completing the square gives the [[Wiener filter]].

Page numbers below are PDF pages of the lecture notes (printed page = PDF page minus 6).

---

## Definition

> [!definition] Information Hamiltonian, partition sum (source: Ensslin - Information Theory & Information Field Theory.pdf, §5, eqs. 283-289, p. 79)
> $$P(s|d,I)=\frac{P(d,s|I)}{\int ds\,P(d,s|I)}=\frac{e^{-\mathcal H(d,s|I)}}{\mathcal Z(d)}$$
> $$\mathcal H(d,s|I)\equiv-\ln P(d,s|I)\ \ (\text{"surprise" or information}),\qquad \mathcal Z(d|I)\equiv P(d|I)=\int ds\,e^{-\mathcal H(d,s|I)}$$

The book calls the Hamiltonian "surprise or information" and the partition sum "evidence". It also writes $\hat=$ for equality up to terms that do not depend on the signal, the logarithmic version of $\propto$ (p. 80). This page writes $\hat=$ the same way.

Because $P(d,s)=P(d|s)P(s)$, the Hamiltonian splits as $\mathcal H(d,s)=\mathcal H(d|s)+\mathcal H(s)$, a likelihood term plus a prior term (p. 79).

## Linear measurement, Gaussian signal and noise (§5.1)

Setup (p. 79): prior $P(s)=\mathcal G(s,S)$ with known covariance $S$; data $d=Rs+n$ with known response $R$; noise $P(n|s)=\mathcal G(n,N)$ with known $N$. Then $P(d|s)=\mathcal G(d-Rs,N)$ and

> [!theorem] Quadratic Hamiltonian and Gaussian posterior (source: Ensslin - Information Theory & Information Field Theory.pdf, §5.1, pp. 80-81)
> $$\mathcal H(d,s)=\tfrac12\big[s^\dagger D^{-1}s-s^\dagger j-j^\dagger s\big]+\mathcal H_0$$
> $$D^{-1}=S^{-1}+R^\dagger N^{-1}R\quad(\text{information propagator}),\qquad j=R^\dagger N^{-1}d\quad(\text{information source})$$
> $$\mathcal H_0=\tfrac12\big(d^\dagger N^{-1}d+\ln|2\pi N|+\ln|2\pi S|\big)$$
> Completing the square with $m=Dj$ gives $\mathcal H\,\hat=\,\tfrac12(s-m)^\dagger D^{-1}(s-m)$, so
> $$P(s|d)=\mathcal G(s-m,D),\qquad m=Dj=\big(S^{-1}+R^\dagger N^{-1}R\big)^{-1}R^\dagger N^{-1}d.$$

The trick for the completion is to insert $\mathbb 1=DD^{-1}$ and $\mathbb 1=D^{-1}D$ (p. 80). The evidence is $\mathcal Z(d)=e^{-\mathcal H_0'}\sqrt{|2\pi D|}$ with $\mathcal H_0'$ the constant left after completing the square (p. 81). The mean $m$ is the best guess; the uncertainty is $s_x=m_x\pm\sqrt{D_{xx}}$, and the off-diagonal entries of $D$ say how correlated the errors at two locations are (p. 81). The operator $F_W=DR^\dagger N^{-1}$ is the (generalized) [[Wiener filter]].

**Notation difference**: Enßlin writes $S$ and $N$ for covariances and $D$ for the posterior covariance. [[Information field theory]] (Alberts and Bilionis) uses $S$ for a precision (inverse covariance) and writes the posterior precision as $\tilde S=S+R^\dagger N^{-1}R$. Here $D^{-1}$ plays the role of $\tilde S$ there.

## Non-linear response (p. 81-82)

> [!failure] Non-Gaussian posterior
> For $R(s)=s+\alpha s^2$ the Hamiltonian is
> $$\mathcal H(d,s)=\tfrac12 s^\dagger S^{-1}s+\tfrac12(d-s-\alpha s^2)^\dagger N^{-1}(d-s-\alpha s^2),$$
> which is fourth order in $s$, so the posterior is not Gaussian (source: §5.1, p. 82). Higher-order terms become the "interaction Hamiltonian" of the later chapters; see [[Lognormal Poisson model]] for a worked case.

## Where it appears
- [[Wiener filter]]: the posterior mean above, its optimality among linear filters, and its Fourier-space form.
- [[Lognormal Poisson model]]: a Poisson likelihood gives $\mathcal H(d|s)\hat=\kappa^\dagger e^s-d^\dagger s$, split into free and interaction parts.
- [[Signal response]]: the operator $R$ in $d=Rs+n$.
- [[Partition function]] and [[Energy functional]]: the same objects in statistical-mechanics language.
- Later chapters of the book treat the free and interacting theory, Feynman diagrams and Gibbs free energy: [[Free theory (IFT)]], [[Interacting information field theory]], [[Interacting information field theory|Feynman diagrams]] (not yet pages).

**Covered in**: Enßlin IT & IFT ch. 5 (pp. 79-82)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Wiener filter]] · [[Signal response]] · [[Lognormal Poisson model]]
- [[Information field theory]] · [[Partition function]] · [[Energy functional]] · [[Gaussian process]] · [[Bayesian inverse problems]]
