---
type: method
area: ift
areas: [ift, bayesian, vi]
source-ref: "Enßlin, IT & IFT, ch. 12 (§12.1, eqs. 319-334, pp. 133-137); Enßlin & Weig 2010 (cited by the book)"
tags: [ift, bayesian, vi, mechanics]
---

# Gibbs free energy (thermodynamical inference)

**Summary**: Thermodynamical inference treats the posterior as a Boltzmann distribution and estimates its mean and covariance by minimising a Gibbs free energy, obtained from the Helmholtz free energy by a Legendre transform. With a Gaussian ansatz this equals minimising the KL divergence from the Gaussian to the true posterior.

Page numbers `p.` are PDF pages of `Ensslin - Information Theory & Information Field Theory.pdf` (printed page = PDF page minus 6).

## Set-up (§12.1, pp. 133-134)
> [!definition] Tempered posterior with source
> $$P(s|d,T,J)=\frac{e^{-\beta\,(H(d,s)+J^\dagger s)}}{Z(d,\beta,J)},\qquad \beta=1/T.$$
> $T=\beta=1$ is ordinary inference. $T\to0$ concentrates on the MAP, $T\to\infty$ flattens the posterior.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §12.1, eq. 319, p. 133)

The Boltzmann entropy relative to a reference $q(s)$ (eq. 320) satisfies

$$T\,\Delta S_B=U+J^\dagger m-F\qquad\text{(eq. 322)}$$

with internal energy $U=\langle H\rangle$, mean field $m=\langle s\rangle=\partial F/\partial J$, and Helmholtz free energy $F=-\tfrac1\beta\ln Z$.

**Goal**: find $m=\langle s\rangle$ and $D=\langle ss^\dagger\rangle_c$. Since only $m$ and $D$ are reported, maximum entropy says the posterior should be Gaussian, so the book adopts the ansatz $\widetilde P(s|m,D)=\mathcal G(s-m,D)$ (eq. 323-324), for which

$$\widetilde U=\langle H\rangle_{\mathcal G(s-m,D)},\qquad \widetilde S_B(D)=\tfrac12\mathrm{Tr}\,(1+\ln 2\pi D)\quad\text{(eq. 327)}.$$

## Legendre transform and Gibbs free energy
Removing the dependence on $J$ by a Legendre transform of $F$ (eqs. 329-331):

> [!definition] Gibbs free energy (eqs. 331-332, p. 135)
> $$G=F-\big(\partial F/\partial J\big)^\dagger J=U-T S_B,$$
> $$\widetilde G(d,\beta,m,D)=\widetilde U(d,\beta,m,D)-T\,\widetilde S_B(D).$$

> [!theorem] Minimum of $G$ (eqs. 333-334, p. 135)
> $\delta G/\delta m=0$ gives $m=\langle s\rangle_{s|d}$ at $T=1$. The inverse curvature gives the uncertainty,
> $$\Big(\frac{\delta^2G}{\delta m\,\delta m^\dagger}\Big)^{-1}\Big|_{m=\langle s\rangle}=-\frac{\delta^2F}{\delta J\,\delta J^\dagger}\Big|_{J=0}=\beta D.$$

> [!proof] Sketch
> $\delta G/\delta m=-J(m)$ because the term $(\delta J/\delta m)^\dagger\,\partial F/\partial J$ cancels $-(\delta J/\delta m)^\dagger m$. Setting $J=0$ gives $m=\partial F/\partial J|_{J=0}$. For the curvature: $\delta J/\delta m=-(\delta^2F/\delta J^2)^{-1}$ and $\delta^2\ln Z/\delta J^2=\beta^2D$.
> (source: ibid., p. 135)

## Lognormal Poisson model (§12.1.1, pp. 136-137)
With $H=\tfrac12s^\dagger S^{-1}s-d^\dagger s+\kappa^\dagger e^s$ and the Gaussian ansatz,
$$\widetilde U=\tfrac12m^\dagger S^{-1}m+\tfrac12\mathrm{Tr}(DS^{-1})-d^\dagger m+\kappa^\dagger e^{m+\frac12\widehat D}.$$
Minimising $\widetilde G$ gives

$$m=S\big(d-\kappa\,e^{m+\frac12\widehat D}\big),\qquad D=T\Big(S^{-1}+\widehat{\kappa e^{m+\frac12\widehat D}}\Big)^{-1}.$$

This is the "loop-normalised" classical solution of [[Interacting information field theory]]: the loop-corrected MAP is the minimum of the Gibbs energy in a Gaussian posterior approximation. (source: ibid., p. 137)

## Relation to KL divergence (§12.1.2, p. 137)
> [!theorem] Gibbs free energy equals relative entropy up to a constant
> With $D_{\rm KL}[\widetilde P,P]=\int\widetilde P\ln(\widetilde P/P)$,
> $$\widetilde G(m,D)=D_{\rm KL}\big[\mathcal G(s-m,D)\,\|\,P(s|d)\big]-\ln P(d)\quad\text{at }T=1.$$
> Minimising $\widetilde G$ is therefore minimising the KL distance, i.e. the amount of information $\widetilde P$ "invents" beyond $P$.

The book says the Gibbs free energy "describes, up to a constant, the mutual information"; the displayed formula is a relative entropy (KL divergence), and this page follows the formula.

Wiki note: $\widetilde G(m,D)$ is then exactly the negative [[ELBO]] of a Gaussian variational family, $-\ln P(d)$ being the dropped constant. This is why thermodynamical inference, [[Metric Gaussian variational inference]] and [[Variational inference]] with Gaussian guides are the same idea (the MGVI loss in book §17.1.3 has the same form). Not stated in this form in the book.

## Notation and trust parameter
- The book's $\beta=1/T$ multiplies the **whole** information Hamiltonian $H(d,s)+J^\dagger s$ (prior and likelihood together). In the wiki's [[MAP uniqueness in IFT (Alberts 2025)]] the "model trust" $\beta$ multiplies only the prior energy, $H=\ell+\beta U$. They are different tempering parameters; the book never uses $\beta$ as a prior-trust weight. For the wiki's $\beta$ see [[Information field theory]].
- After eq. 324 the book drops the reference measure $q(s)$ (or sets $q=1$) and writes $S_B$ for $\Delta S_B$.

## Where it appears
- [[Critical filter]]: the same Gibbs free energy applied to the filter with unknown power spectrum.
- [[Metric Gaussian variational inference]] / [[Geometric variational inference]]: practical large-scale versions.
- Operator calculus for the Gaussian averages: [[Operator calculus for free theory]] (book §12.2).

**Covered in**: Enßlin IT & IFT ch. 12 (pp. 133-137)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Free energy]] · [[Partition function]] · [[KL divergence]] · [[ELBO]] · [[Statistical entropy]]
- [[Information field theory]] · [[Free theory (IFT)]] · [[Maximum entropy principle]]
