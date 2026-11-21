---
type: method
area: ift
areas: [ift, bayesian, signals]
source-ref: "Enßlin, IT & IFT, ch. 13, pp. 143-148; Enßlin & Frommert 2011, Enßlin & Weig 2010 (cited by the book)"
tags: [ift, bayesian, inverse-problems, signals]
---

# Critical filter

**Summary**: A Wiener filter for a Gaussian field whose power spectrum is unknown. The spectrum is treated as a nuisance parameter with a Jeffreys prior and marginalised out; the resulting reconstruction iterates a map estimate and a spectrum estimate. The critical filter is the thermodynamical (Gibbs free energy) version, which adds an uncertainty term that the MAP version lacks.

Page numbers `p.` are PDF pages of `Ensslin - Information Theory & Information Field Theory.pdf` (printed page = PDF page minus 6).

## Set-up (ch. 13, p. 143)
Signal $s$ is Gaussian with unknown covariance $S$, observed by $d=Rs+n$ with known noise $N$. In a basis $O$ where $S$ is diagonal (Fourier basis for statistical homogeneity, spherical harmonics for isotropy), $S=O^\dagger\widehat P_sO$. The strategy: build the theory for unknown $s,S$, marginalise $S$ to get an effective Hamiltonian for $s$, then solve it.

## Spectral band matrices (§13.1, p. 144)
Model the spectrum as $P_s(k)=\sum_if_i(k)\,p_i$ with indicator functions $f_i$ of non-overlapping bands covering $k$-space, and define $T_i=O^\dagger\widehat f_iO$. Then
$$S=\sum_ip_iT_i,\qquad S^{-1}=\sum_ip_i^{-1}T_i.$$
The inverse follows from $f_if_j=\delta_{ij}f_i$, i.e. the $T_i$ are projectors. Wiki note: the book's later formulas write $T_i^{-1}$ in places (§13.2-13.3) and $\rho_i=\mathrm{Tr}(T_iT_i^{-1})$; since $T_i$ is a projector, $T_i^{-1}$ must be read as the band-$i$ part of $S^{-1}$, which equals $T_i$ on its range, and $\rho_i=\mathrm{Tr}\,T_i$ is the number of modes in band $i$. See typos below.

## Joint PDF and effective Hamiltonian (§13.2-13.3, pp. 144-146)
$P(d,s,S)=P(d|s)\,P(s|S)\,P(S)$ with likelihood $\mathcal G(d-Rs,N)$, signal prior $\mathcal G(s,S)$ and Jeffreys prior $P(p_i)\propto p_i^{-1}$ (flat in $\ln p_i$, because the coefficients are positive of unknown magnitude). The normalisation $\tfrac12\ln|2\pi S|$ must be kept since $S$ is unknown, and $|S_p|=\prod_ip_i^{\rho_i}$.

> [!theorem] Effective Hamiltonian (§13.3, p. 146)
> Marginalising the spectrum, $P(s)=\int\mathcal DS\,P(s|S)P(S)=e^{-H_{\rm eff}(s)}$, with the substitution $x_i=t_i/p_i$, $t_i=\tfrac12 s^\dagger T_is$ and a Gamma integral, gives
> $$H(d,s)\ \widehat=\ \tfrac12 s^\dagger Ms-j^\dagger s+\sum_i\frac{\rho_i}{2}\ln\Big(\tfrac12 s^\dagger T_is\Big),$$
> $$M=R^\dagger N^{-1}R,\quad j=R^\dagger N^{-1}d,\quad \rho_i=\#\text{modes in band }i.$$
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §13.3, p. 146)

The logarithm makes the Hamiltonian **non-Gaussian**: this is an interacting theory in the sense of [[Interacting information field theory]].

## Classical (MAP) estimate (§13.4, p. 146)
Setting $\delta H_{\rm eff}/\delta s=0$ gives
$$j=\Big(M+\sum_i\frac{\rho_i}{s^\dagger T_is}T_i\Big)s=D_{p^*}^{-1}s,$$
so $s_{\rm cl}=m_{\rm MAP}=D_{p^*}j$ with $p_i^*=\tfrac1{\rho_i}s_{\rm cl}^\dagger T_is_{\rm cl}$: the spectrum is the power of the reconstructed map in each band (a fixed-point iteration between map and spectrum).

## Thermodynamical approach (§13.5, pp. 147-148)
At $T=1$ with the Gaussian ansatz $\mathcal G(s-m,D)$ the Gibbs energy needs $I_i=\langle\ln s^\dagger T_is\rangle$. Expand around $\tau_i=\mathrm{Tr}\big((mm^\dagger+\delta D)T_i\big)$:
$$I_i=\ln\tau_i+\sum_{n\ge1}\frac{(-1)^{n}}{n\,\tau_i^n}\langle(s^\dagger T_is-\tau_i)^n\rangle.$$
The first-order term is $(1-\delta)\mathrm{Tr}(DT_i)$, so choosing $\delta=1$ kills it and minimises the second-order term. Then (p. 147)
$$\widetilde G=\tfrac12\mathrm{Tr}\big((mm^\dagger+D)M\big)-j^\dagger m+\sum_i\tfrac{\rho_i}{2}\ln\mathrm{Tr}\big((mm^\dagger+D)T_i\big)-\tfrac12\mathrm{Tr}(1+\ln2\pi D),$$
and $\delta\widetilde G/\delta m=0$ gives $j=D_{p^*}^{-1}m$ with $p_i^*=\mathrm{Tr}((mm^\dagger+D)T_i)/\rho_i$.

> [!algorithm] Unified filter formula (p. 148)
> $$m=D_pj,\qquad p_i=\frac1{\rho_i}\mathrm{Tr}\big((mm^\dagger+\delta D)\,S_i^{-1}\big)$$
> $\delta=0$: MAP filter. $\delta=1$: **critical filter**.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §13.5, p. 148)

**Intuition**: the MAP spectrum is the power in the reconstruction, which underestimates the true power because the reconstruction is a smoothed map. The critical filter adds the posterior uncertainty $\mathrm{Tr}(DT_i)$ to the power of each band, so no power is lost; this is the missing piece compared with MAP, and it is why the thermodynamical approach is preferred. The plain-language reading is a Wiki note; the book states only the formula.

## Where it appears
- Gibbs energy machinery: [[Gibbs free energy]].
- Unknown spectrum within IFT: [[Power spectrum estimation]]; fully hierarchical spectrum: [[Correlated field model]].

**Covered in**: Enßlin IT & IFT ch. 13 (pp. 143-148)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Information field theory]] · [[Free theory (IFT)]] · [[Wiener filter]] · [[Wiener-Khinchin theorem|Power spectrum]]
- [[Wiener-Khinchin theorem]] · [[Jeffreys prior]]
