---
type: method
area: ift
areas: [ift, bayesian, vi]
source-ref: "Enßlin, IT & IFT, §17.3, pp. 176-178; Frank et al. 2021 (ref. [13])"
tags: [ift, vi, bayesian]
---

# Geometric variational inference

**Summary**: geoVI improves MGVI by changing coordinates so that the Fisher metric of the likelihood becomes flat, then using a Gaussian in those coordinates. For Poisson data a square-root transform does the flattening exactly.

Page numbers `p.` are PDF pages of `Ensslin - Information Theory & Information Field Theory.pdf` (printed page = PDF page minus 6).

## Poisson Fisher metric (§17.3.1, pp. 176-177)
Likelihood Hamiltonian $H(d|\xi)=\lambda(\xi)^\dagger\vec1-d^\dagger\ln\lambda(\xi)+\vec1^\dagger\ln d!$ with log-normal Poisson rate $\lambda(\xi)=R\exp(A_s\xi)$, $\xi\sim\mathcal G(\xi,1)$. Then $\partial H/\partial\xi=(\partial\lambda/\partial\xi)^\dagger(1-d/\lambda)$ and, using $\langle(\lambda-d)^2\rangle=\lambda$ for Poisson data,

$$M(\xi)=\frac{\partial\lambda}{\partial\xi}\,\widehat{\lambda^{-1}}\,\frac{\partial\lambda^\dagger}{\partial\xi}\ \ \text{(index placement as in the book)}.$$

Writing $x(\xi)$ for a transformed variable with $\partial x/\partial\xi=\widehat{\lambda^{-1/2}}\,\partial\lambda/\partial\xi$, this is a pullback of the flat metric:
$$M(\xi)=\Big(\frac{\partial x}{\partial\xi}\Big)^\dagger\frac{\partial x}{\partial\xi}.$$
In $x$-coordinates the metric is the identity, $d^2s/dx\,dx^\dagger=1$: coordinates that flatten the Fisher metric. The book gives $x(\xi)=\tfrac12\sqrt{\lambda(\xi)}$; but $\partial x/\partial\xi=\lambda^{-1/2}\partial\lambda/\partial\xi=2\,\partial\sqrt\lambda/\partial\xi$ requires $x=2\sqrt\lambda$ (see typos).

(source: Ensslin - Information Theory & Information Field Theory.pdf, §17.3.1, pp. 176-177)

## Flattening the MGVI metric (§17.3.2-17.3.3, pp. 177-178)
Can the full MGVI metric $\Theta^{-1}=1+M$ be flattened too? A transform $g$ with $(\partial g/\partial\xi)^\dagger(\partial g/\partial\xi)=1+(\partial x/\partial\xi)^\dagger(\partial x/\partial\xi)$ does not exist in general, but an approximate one does:

$$g(\xi;\bar\xi)=M^{-1/2}\Big[(\xi-\bar\xi)+\Big(\frac{\partial x}{\partial\xi}\Big|_{\bar\xi}\Big)^\dagger\big(x(\xi)-x(\bar\xi)\big)\Big],$$
with $M$ evaluated at the expansion point $\bar\xi$ (the book defines $M$ at $\bar\xi$ in $M^{-1/2}$ and then writes $\tilde g$; the exercise to prove the formula is left open).

> [!algorithm] geoVI (§17.3.3, p. 178)
> Take the variational density $Q(\xi|\bar\xi)=[g(\bullet|\bar\xi)\star\mathcal G(\bullet|1)](\xi)$, a unit Gaussian pushed through the nonlinear map $g$. Choose the expansion point $\bar\xi$ minimising $D_{\rm KL}(Q(\xi|\bar\xi)\|P(\xi|d))$. At $\xi=\bar\xi$ the book verifies $\Theta^{-1}=(1+M)\,M^{-1/2}M^{-1/2}(1+M)=1+M$, so it reproduces the MGVI metric at the expansion point.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §17.3.3, p. 178; model graph $y\to\xi\to s\to d'=Rs\to d$, Fig. 21)

**Intuition**: MGVI is a Gaussian in $\xi$ with a locally correct metric. geoVI keeps the same local metric but bends the coordinates, so non-Gaussian features of the posterior (such as a strongly skewed log-normal one) are better captured away from $\bar\xi$. Wiki note: the book gives only the derivation of the metric; how samples are drawn from $Q$ and how $\bar\xi$ is found are not covered here.

**Covered in**: Enßlin IT & IFT §17.3 (pp. 176-178)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Metric Gaussian variational inference]] · [[Variational inference]] · [[Fisher information]]
- [[Lognormal Poisson model]] · [[Information field theory]]
