---
type: method
area: ift
areas: [ift, bayesian, vi]
source-ref: "Enßlin, IT & IFT, §17.1-17.2, pp. 171-176; Knollmüller & Enßlin 2019 (ref. [19])"
tags: [ift, vi, bayesian, sampling]
---

# Metric Gaussian variational inference

**Summary**: MGVI fits a Gaussian $Q(\zeta)=\mathcal G(\zeta-\theta,\Theta)$ to a posterior over a standardised latent field, with the covariance not optimised but fixed by the Fisher metric at the mean, $\Theta^{-1}(\theta)=1+M(\theta)$. Only the mean $\theta$ is optimised, and the covariance is applied implicitly through CG and sampling.

Page numbers `p.` are PDF pages of `Ensslin - Information Theory & Information Field Theory.pdf` (printed page = PDF page minus 6).

## Set-up (§17.1, pp. 171-172)
The latent field $\zeta$ (renamed $\xi$ later) has a unit Gaussian prior, $H(\zeta)\widehat=\tfrac12\zeta^\dagger\zeta$. The objective is $D_{\rm KL}(Q\|P)$ with $Q=\mathcal G(\zeta-\theta,\Theta)$. A full $\Theta$ has order $n^2/2$ free parameters (the book says $n(n-1)/2$, see typos), so $\Theta=\Theta(\theta)$ is wanted.

Fisher metric of the likelihood:
$$M(\zeta)=\Big\langle\frac{\partial H(d|\zeta)}{\partial\zeta}\frac{\partial H(d|\zeta)^\dagger}{\partial\zeta}\Big\rangle_{(d|\zeta)}\ \ge0.$$

> [!definition] MGVI covariance (p. 171-172)
> The posterior Hamiltonian Hessian equals that of the joint, since $H(d)$ does not depend on $\zeta$. Taking its expectation over data at $\zeta=\theta$ and using $\int dd\,P(d|\zeta)=1$:
> $$\Theta^{-1}(\theta)\simeq\Big\langle\frac{\partial^2H(d,\zeta)}{\partial\zeta\partial\zeta^\dagger}\Big\rangle_{(d|\zeta=\theta)}=1+M(\theta)>0.$$
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §17.1, p. 171-172)

The book notes this is positive definite because $M\ge0$.

**Why reasonable**:
- Linear Gaussian case ($d=R\zeta+n$): $M=R^\dagger N^{-1}R$, so $\Theta=(1+M)^{-1}=D$ is **exact** (p. 172).
- Nonlinear case: directions constrained by data get a linearisation-based approximation; unconstrained directions have $(1+M)^{-1}\approx1$, the correct prior covariance (§17.1.2, p. 173).
- General Gaussian noise $d=f(\zeta)+n$: $M(\theta)=R_\theta N^{-1}R_\theta^\dagger$ with $R_\theta=\partial f/\partial\zeta|_\theta$ the linearised response (p. 176; the book's order of the transposes is as printed).

> [!algorithm] MGVI loss (§17.1.3, p. 173)
> $$L(\theta)=D_{\rm KL}\big(\mathcal G(\zeta-\theta,\Theta(\theta))\,\|\,P(\zeta|d)\big)\ \widehat\approx\ \langle H(d,\zeta)\rangle_{\mathcal G(\zeta-\theta,\Theta)}\approx\frac1N\sum_{i=1}^NH(d,\zeta_i),$$
> with $\zeta_i\sim\mathcal G(\zeta-\theta,\Theta)$. The entropy term $S_B(\Theta(\theta))$ is dropped. Minimise with a quasi-Newton scheme using CG and $\Theta(\theta)$ as proxy for second derivatives; samples are redrawn at each step.

This is the Gaussian-ansatz Gibbs free energy of [[Gibbs free energy]], with the entropy term dropped, an evidence-free constant omitted, and the average replaced by samples.

## Posterior sampling from a Gaussian (§17.2, pp. 173-175)
How to draw samples from $\mathcal G(s-m,D)$ without forming $D$? Since $D=(S^{-1}+R^\dagger N^{-1}R)^{-1}$ does not depend on $d$, the reconstruction error can be transferred from synthetic data.

> [!algorithm] Antithetic posterior samples
> 1. Draw $s'\sim\mathcal G(s',S)$, $n'\sim\mathcal G(n',N)$, set $d'=Rs'+n'$.
> 2. Reconstruct $m'=DR^\dagger N^{-1}d'$ by [[Conjugate gradient]].
> 3. Missed signal $\Delta'=s'-m'$. Then
> $$z_\pm=m\pm\Delta'=m\pm(s'-m')$$
> are two (antithetic) samples of $P(s|d)$, where $m$ is the reconstruction from the real data.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §17.2, p. 173)

> [!proof] (pp. 174-175)
> $\Delta'=(1-DM)s'+DR^\dagger N^{-1}n'$ is Gaussian with $\langle\Delta'\rangle=0$ and
> $$\langle\Delta'\Delta'^\dagger\rangle=(1-DM)S(1-DM)^\dagger+DMD=D.$$
> The algebra uses $D^{-1}=S^{-1}+M$. A Gaussian with zero mean and covariance $D$ shifted by $m$ is the posterior.

**Early termination of CG** (Note 1, p. 175): directions not yet solved leave $m'$ too small there, so $\Delta'$ and $z_\pm$ are too large in those directions: a conservative uncertainty. **Note 2**: with $S=1$ the MGVI covariance is this $D$, with $M(\theta)$ in place of $R^\dagger N^{-1}R$; for the linear case this is shown exactly.

> [!question] Exercise left open in the book (p. 176)
> Compute $M(\theta)$ for Poisson data. The book works it out in §17.3, see [[Geometric variational inference]].

**Covered in**: Enßlin IT & IFT §17.1-17.2 (pp. 171-176)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Variational inference]] · [[KL divergence]] · [[ELBO]] · [[Fisher information]]
- [[Geometric variational inference]] · [[Gibbs free energy]] · [[Laplace approximation]] (a mode-based Gaussian; MGVI instead matches a Fisher-metric Gaussian by KL)
- [[Information field theory]] · [[Wiener filter]]
