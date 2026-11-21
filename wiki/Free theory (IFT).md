---
type: method
area: ift
areas: [ift, bayesian]
source-ref: "Enßlin, IT & IFT, ch. 11 (§11.1-11.2, pp. 129-130)"
tags: [ift, bayesian, inverse-problems]
---

# Free theory (IFT)

**Summary**: The free (Gaussian) theory is the case where the information Hamiltonian is quadratic in the field. The generating function is a closed Gaussian integral, the posterior mean is the Wiener filter, and all cumulants above order two vanish.

Page numbers `p.` below are PDF pages of `Ensslin - Information Theory & Information Field Theory.pdf` (printed page = PDF page minus 6).

> [!definition] Moment and cumulant generating function (§11.1, p. 129)
> With $P(d,s)=e^{-H(d,s)}$ and evidence $Z(d)=\int\mathcal Ds\,e^{-H(d,s)}$,
> $$Z(d,J)=\int\mathcal Ds\,e^{-H(d,s)+J^\dagger s}.$$
> Moments are $\langle s_{x_1}\cdots s_{x_n}\rangle=Z^{-1}\,\delta^nZ/\delta J_{x_1}\cdots\delta J_{x_n}\big|_{J=0}$.
> Cumulants are the same derivatives of $\ln Z(d,J)$.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §11.1, p. 129)

> [!theorem] Free theory (§11.2, p. 130)
> Linear response $d=Rs+n$, independent Gaussian signal and noise, $P(s,n)=\mathcal G(s,S)\,\mathcal G(n,N)$. Then
> $$H(d,s)=\tfrac12 s^\dagger D^{-1}s-j^\dagger s+H_0,$$
> $$D^{-1}=S^{-1}+R^\dagger N^{-1}R,\qquad j=R^\dagger N^{-1}d,$$
> $$\ln Z(J)=\tfrac12(J+j)^\dagger D(J+j)+\tfrac12\ln|2\pi D|-H_0.$$
> Hence $\langle s\rangle=m=Dj$, $\langle ss^\dagger\rangle_c=D$ and all cumulants of order $n\ge3$ are zero.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §11.2, p. 130)

The book notes that the source $J$ is not needed: one can differentiate with respect to $j$ directly. The scalar constant $H_0=\tfrac12\ln|2\pi S||2\pi N|+\ldots$ collects all terms free of $s$.

**Intuition**: completing the square turns the posterior into $\mathcal G(s-m,D)$. The posterior mean is the quantity $Dj$, called the Wiener filter in [[Wiener filter]].

## Notation
- The book writes $S$ for the prior **covariance** and $D$ for the posterior covariance, and the Hamiltonian $H=-\ln P(d,s)$ up to a constant ($\widehat=$ in the book). The [[Information field theory]] page writes the Gaussian density with a **precision** $S$ ($e^{-\frac12\phi^\dagger S\phi}$), so its $\tilde S$ equals the book's $D^{-1}$ and its $S$ is the book's $S^{-1}$.
- The book's field is $s$ (or $\phi$ for a shifted field), the response $R$, the noise covariance $N$.
- Wiki note: the information Hamiltonian in the book is the full $-\ln P(d,s)$; the wiki's $H[\phi|d]=\ell(d,R\phi)+\beta U[\phi]$ has a prior weight $\beta$ that the book does not use in this chapter. See [[Gibbs free energy]] for the book's $\beta$ (a temperature on the whole posterior).

## Where it appears
- Interacting theory is an expansion around this one: [[Interacting information field theory]].
- Operator-calculus derivation of Gaussian moments: [[Operator calculus for free theory]].
- Marginalisation over an unknown spectrum leaves the free theory: [[Critical filter]].
- Solving $Dj$ numerically: [[Conjugate gradient]].

**Covered in**: Enßlin IT & IFT ch. 11 (pp. 129-130)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Information field theory]] · [[Information Hamiltonian]] · [[Wiener filter]] · [[Multivariate Gaussian]]
- [[Partition function]] · [[Gaussian process]]
