---
type: method
area: ift
areas: [ift, bayesian]
source-ref: "Enßlin, IT & IFT, §11.3-11.7, eqs. 317-318, pp. 130-138"
tags: [ift, bayesian, inverse-problems]
---

# Interacting information field theory

**Summary**: When the information Hamiltonian has terms beyond quadratic, the partition function is expanded around the free theory and every term of the expansion is drawn as a Feynman diagram. The posterior mean is the sum of all diagrams with one external leg: tree diagrams alone give the MAP estimate, loop diagrams add uncertainty corrections.

Page numbers `p.` are PDF pages of `Ensslin - Information Theory & Information Field Theory.pdf` (printed page = PDF page minus 6).

> [!definition] Interacting Hamiltonian (§11.3, p. 130)
> $$H(d,s)=\underbrace{\tfrac12 s^\dagger D^{-1}s-j^\dagger s+H_0}_{H_{\mathcal G}}
> +\underbrace{\sum_n\tfrac1{n!}\Lambda^{(n)}_{x_1\ldots x_n}s_{x_1}\cdots s_{x_n}}_{H_{\rm int}}.$$
> The expansion needs $H_{\rm int}$ small. For that the book shifts the field, $s=t+\phi$, with $t$ for example $\arg\min_s H(d,s)$, giving new $H_0'$, $j'=j-D^{-1}t$ and couplings $\Lambda'^{(m)}=\sum_n\frac1{n!}\Lambda^{(m+n)}t^n$ (§11.3, p. 131; the book leaves the proof as an exercise).
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §11.3, pp. 130-131)

## Perturbation series
For a local quartic term $\Lambda^{(4)}=\lambda\,\delta\delta\delta$ one has $H_{\rm int}=\frac\lambda{4!}\int dx\,s_x^4$ and

$$Z=\exp\!\Big(-H_{\rm int}\big[\tfrac{\delta}{\delta j}\big]\Big)\,Z_{\mathcal G}(j),\qquad Z_{\mathcal G}(j)=Z_{\mathcal G}(0)\,e^{\frac12 j^\dagger Dj}.$$

The book states the first identity holds in general, not only for this example. To first order in $\lambda$:

$$Z(j)=Z_{\mathcal G}(j)\Big(1-\lambda\!\int\!dx\Big[\tfrac18 D_{xx}^2+\tfrac14 D_{xx}(Dj)_x^2+\tfrac1{4!}(Dj)_x^4\Big]\Big).$$

(source: Ensslin - Information Theory & Information Field Theory.pdf, §11.4, pp. 131-133)

> [!failure] Zero radius of convergence (§11.4, Fig. 18, p. 132)
> For $\lambda<0$ the Hamiltonian $\tfrac12 s^2+\tfrac{\lambda}{4!}s^4$ is unbounded below and the partition function diverges. The series is therefore only asymptotic.

## Feynman rules (§11.5, p. 133)
- the propagator $D_{xy}$ is a line joining $x$ and $y$;
- a source $j_y$ is a dot at the end of a line;
- $-\lambda$ is a vertex with four legs, and $-\Lambda^{(n)}$ a vertex with $n$ legs;
- internal positions are integrated over;
- the prefactor is one over the symmetry factor (a loop contributes $1/2$).

The Feynman diagrams of eq. 317 are drawings in the book (a figure-eight, a "bow-tie with two sources" and a four-legged star). In words: $Z(j)=Z_{\mathcal G}(j)\,[1+\text{vacuum bubbles}+\ldots]$, i.e. the sum of all (possibly disconnected) diagrams, with the empty diagram counted as 1.

Examples, in the book's notation (§11.5, p. 134), with $\widehat D=\mathrm{diag}(D)$:

$$-\tfrac\lambda{4!}(Dj)^4,\quad -\tfrac\lambda4 (Dj)^2\widehat D,\quad -\tfrac\lambda8\widehat D^2.$$

> [!theorem] Linked-cluster theorem (p. 134-135)
> $\ln Z(j)=\sum_i C_i+\ln Z_{\mathcal G}(0)$, the sum over all **connected** diagrams $C_i$.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §11.5, pp. 134-135)

> [!proof] Sketch (p. 135)
> A disconnected diagram with $n_i$ copies of $C_i$ contributes $\prod_i C_i^{n_i}/n_i!$ (the symmetry factor). Summing over all $n_i$ gives $\prod_i e^{C_i}$, so $Z=Z_{\mathcal G}(0)\exp\sum_iC_i$.

## Diagrammatic expectation values (§11.6, pp. 135-136)
For the $\phi^4$ example with $\lambda$ to first order:

$$\ln Z(j)=\tfrac12 j^\dagger Dj-\tfrac\lambda{4!}(Dj)^4-\tfrac\lambda4(Dj)^2\widehat D-\tfrac\lambda8\widehat D^2+\ln Z_{\mathcal G}(0).$$

$$\langle\phi\rangle=Dj-\tfrac{\lambda}{3!}D(Dj)^3-\tfrac\lambda2 D\big((Dj)\widehat D\big),$$
$$\langle\phi\phi^\dagger\rangle_c=D-\tfrac\lambda2 D\,\mathrm{diag}\big((Dj)^2\big)D-\tfrac\lambda2 D\,\mathrm{diag}(\widehat D)D.$$

(source: Ensslin - Information Theory & Information Field Theory.pdf, §11.6, pp. 135-136; the second display transcribed from the page images, powers of the diagonal operators written as in the book's text)

Derivatives with respect to $j$ are read off diagrams by cutting off end dots. With $\lambda=0$ this is the Wiener filter ([[Free theory (IFT)]]).

## Log-normal Poisson model, diagrammatically (§11.7, pp. 136-138)
With rate $\rho=\rho_0e^s$ the Hamiltonian is $H=\tfrac12s^\dagger S^{-1}s-d^\dagger s+\kappa^\dagger e^s$. Splitting $e^s$ into its quadratic and higher parts gives the free part with $D^{-1}=S^{-1}+\hat\kappa$, source $j=d-\kappa$, and vertices $\Lambda^{(n)}=\kappa\,\delta\cdots\delta$ for $n\ge3$.

The MAP condition $\delta H/\delta s=0$ gives the fixed point
$$m=D\Big(j-\kappa\sum_{n\ge2}\tfrac{m^n}{n!}\Big).$$
Iterating from $m_0=0$ builds trees: the MAP estimate is the sum of all tree diagrams with one external point (p. 137).

The posterior mean $\langle s\rangle_{s|d}$ also includes loop diagrams: tree (MAP) plus loops (uncertainty corrections). Attaching a self-loop to every vertex replaces $\kappa\to\kappa\,e^{\widehat D/2}$, so the loop-corrected equation is
$$m=S\big(d-\kappa\,e^{m+\widehat D/2}\big),\qquad D=\big(S^{-1}+\widehat{\kappa e^{m+\widehat D/2}}\big)^{-1}.$$
This still only approximates $\langle s\rangle$, since more complex diagrams (vacuum-polarisation type) are left out.

(source: Ensslin - Information Theory & Information Field Theory.pdf, §11.7.1, p. 138)

Wiki note: §12 of the book shows this loop-corrected solution is exactly the minimum of the Gibbs free energy in a Gaussian approximation, see [[Gibbs free energy]].

## Where it appears
- Gaussian base theory: [[Free theory (IFT)]].
- Moments of exponentials by operators: [[Operator calculus for free theory]].
- The correlated field model needs interacting IFT: [[Correlated field model]].
- Related to the Laplace-type approximation in [[Laplace approximation]] (the MAP is the tree-level result). Wiki note, **[unverified]** as a book claim.

**Covered in**: Enßlin IT & IFT ch. 11 (pp. 129-138)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Information field theory]] · [[Free theory (IFT)]] · [[Gibbs free energy]] · [[Lognormal Poisson model]]
- [[Partition function]] · [[Information Hamiltonian]]
