---
type: definition
area: bayesian
areas: [bayesian, ift]
source-ref: "Enßlin, IT & IFT, §2.9, eqs. 114-130"
tags: [bayesian, ift]
---

# Fisher information

> [!definition] Fisher information metric from the KL expansion
> For a family $P(s\mid\theta)$ expand $D_S(\theta',\theta)=D_{\mathrm{KL}}(P(\cdot\mid\theta')\,\|\,P(\cdot\mid\theta))$ around $\theta'=\theta$. The constant and linear terms vanish, leaving
> $$D_S(\theta+\varepsilon,\theta)=\tfrac12\,\varepsilon_i\,g_{ij}\,\varepsilon_j+O(\varepsilon^3)$$
> $$g_{ij}=\Big\langle\frac{\partial H}{\partial\theta_i}\frac{\partial H}{\partial\theta_j}\Big\rangle_{(s\mid\theta)}=\Big\langle\frac{\partial^2H}{\partial\theta_i\partial\theta_j}\Big\rangle_{(s\mid\theta)}\ \ge0$$
> with surprise $H(s\mid\theta)=-\ln P(s\mid\theta)$ and sum convention.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §2.9, eqs. 116-130, pp. 50-51; p. is the PDF page)

**Intuition**: it measures how fast the distribution changes when the parameter moves, in units of information. A large $g_{ij}$ means a small change in $\theta$ is easy to detect, so an experiment there is informative. The book calls it the sensitivity of expected information gain in the limit of little additional data and uses it to characterize future experiments with respect to parameters of interest.

Notation: the book writes $g^{ij}$ with upper indices in eq. 117 and $g_{ij}$ in eq. 116; this page uses $g_{ij}$ throughout (typographical, not substantive).

## Derivation notes
- The two equal forms follow from $\int ds\,P=1$: differentiating twice gives $\int ds\,\partial_i\partial_jP=0$, which cancels the extra term in eq. 122 and eq. 129.
- Positive semi-definiteness is clear from the first form, a covariance of the score $\partial H/\partial\theta$.

## Where it appears
- [[Achieved information gain]] and [[KL divergence]]: the Fisher metric is the local quadratic form of the KL.
- [[Riemannian manifold HMC]] and [[RMHMC (Girolami 2011)]]: use the expected Fisher information as the metric (Wiki note: the book does not discuss sampling).
- [[Active learning]]: experiment design by expected information gain.

**Covered in**: Enßlin IT & IFT §2.9 (pp. 50-51)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Jeffreys prior]]
- [[Bayesian decision theory]] · [[Maximum entropy principle]] · [[Information field theory]]
