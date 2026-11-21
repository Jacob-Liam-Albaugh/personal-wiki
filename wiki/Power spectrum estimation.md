---
type: method
area: ift
areas: [ift, bayesian, math]
source-ref: "Enßlin, IT & IFT, §16.1-16.2, pp. 173-175"
tags: [ift, bayesian, inverse-problems]
---

# Power spectrum estimation

**Summary**: when the signal prior covariance $S$ is itself unknown, parametrise the power spectrum by $a$, marginalise the signal out of the joint Hamiltonian, and minimise over $a$. With one free parameter per Fourier mode the maximum-likelihood answer is the periodogram minus noise, which can go negative and overfits.

Page numbers `p.` are PDF pages of `Ensslin - Information Theory & Information Field Theory.pdf` (printed page = PDF page minus 6).

## Model (§16.1, pp. 173-174)
Parameters $a\mapsto P_s$, for instance a stochastic differential equation $\sum_k a_k\partial_t^ks=\xi$ with unit Gaussian $\xi$, giving $P_s=P_\xi(\omega)/\|\sum_ka_k(-i\omega)^k\|^2$ (see [[Stochastic differential equation]]). Measurement $d=R s+n$ with Gaussian noise, flat prior on $a$. The posterior over parameters is

$$P(a|d)=\int\mathcal Ds\,P(a,s|d),\qquad P(a,s|d)\propto P(d|s)\,P(s|a)\,P(a).$$

Completing the square in $s$ (with $D^{-1}=S^{-1}+R^\dagger N^{-1}R$, $j=R^\dagger N^{-1}d$, $m=Dj$ as in [[Free theory (IFT)]]) and integrating the Gaussian over $s$:

$$H(d,a)=H_0+\tfrac12\ln\big|D^{-1}S\big|-\tfrac12\,j^\dagger Dj,\qquad H_0=\tfrac12\ln|2\pi N|+\tfrac12d^\dagger N^{-1}d.$$

Wiki note: the book's printed line merges the log-determinants and drops a plus sign; the form above is my reconstruction of its result **[unverified]** and agrees with the derivative the book then takes. This is the same marginalisation that gives the [[Critical filter]] Hamiltonian.

For a diagonal (Fourier) setting define the signal-to-noise ratio per mode $P_Q=P_SP_R/P_N$ (with $P_R$ meaning $|R|^2$ in the translation-invariant case), so $D^{-1}S=1+P_Q$.

## Maximum likelihood (§16.2, pp. 174-175)
Treating each mode's $P_Q(\omega)$ as a free parameter, $\partial H(d,a)/\partial P_Q=0$ gives

$$\frac12\Big(\frac1{1+P_Q}-\frac{P_d}{P_N}\frac1{(1+P_Q)^2}\Big)=0\ \Rightarrow\ 1+P_Q=\frac{P_d}{P_N},\qquad P_S=\frac{P_d-P_N}{P_R}.$$

(source: Ensslin - Information Theory & Information Field Theory.pdf, §16.2, p. 175)

Problems listed by the book:
- $P_d-P_N$ can be negative, which is not a valid power spectrum.
- It overfits the noise.

Remedies listed: informative priors on $P_S$ with fewer parameters than modes (for example the [[Correlated field model]]), use the posterior mean rather than a plug-in, or work out $P(s|d)=\int\mathcal Da\,P(d,s,a)/P(d)$ with the parameters marginalised. Wiki note: the last is the Gibbs-free-energy route of [[Gibbs free energy]] and [[Critical filter]].

**Covered in**: Enßlin IT & IFT ch. 16 (pp. 173-175)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Jeffreys prior]]
- [[Correlated field model]] · [[Critical filter]] · [[Wiener-Khinchin theorem|Power spectrum]] · [[Wiener filter]]
- [[Free theory (IFT)]] · [[Information field theory]] · [[Wiener-Khinchin theorem]]
