---
type: method
area: ift
areas: [ift, gp, bayesian]
source-ref: "Enßlin IT & IFT, chs. 6, 8, 9, pp. 83-114 (PDF pages)"
tags: [ift, bayesian, inverse-problems, signals, gp]
---

# Wiener filter

**Summary**: the posterior mean of a Gaussian signal measured linearly with Gaussian noise, $m=DR^\dagger N^{-1}d$. It is also the best linear estimator for any signal and data with known second moments, and in the statistically homogeneous case it is a diagonal filter in Fourier space that weights each mode by signal-to-noise.

Page numbers are PDF pages of the lecture notes (printed page = PDF page minus 6); section and equation numbers are the book's.

---

## Definition

> [!definition] Wiener filter (source: Ensslin - Information Theory & Information Field Theory.pdf, §5.1, p. 81; §6.1, p. 84)
> For $d=Rs+n$ with $P(s)=\mathcal G(s,S)$, $P(n)=\mathcal G(n,N)$:
> $$F_W=\big(S^{-1}+R^\dagger N^{-1}R\big)^{-1}R^\dagger N^{-1},\qquad m=F_Wd,\qquad D=\big(S^{-1}+R^\dagger N^{-1}R\big)^{-1}.$$
> $P(s|d)=\mathcal G(s-m,D)$. See [[Information Hamiltonian]] for the derivation.

The notes call $F_W$ the generalized Wiener filter and $D$ the information propagator; $j=R^\dagger N^{-1}d$ is the information source, so $m=Dj$.

## Optimal linear filter (§6.1, pp. 83-86)

> [!theorem] The Wiener filter is the optimal linear filter (source: §6.1, pp. 83-85)
> Take zero-mean signal $s$ and data $d$ (shift the means to zero first) with covariances $\langle ss^\dagger\rangle$, $\langle ds^\dagger\rangle$, $\langle dd^\dagger\rangle$. Among linear estimates $m=F_Ld$, the one minimizing the expected squared error $E^2=\langle(s-m)^\dagger(s-m)\rangle$ is
> $$F_L=\langle sd^\dagger\rangle\langle dd^\dagger\rangle^{-1}\quad(\text{cross-correlation times inverse autocorrelation}).$$
> For $d=Rs+n$ this equals $F_W$:
> $$F_L=S R^\dagger\big(R S R^\dagger+N\big)^{-1}=\big(S^{-1}+R^\dagger N^{-1}R\big)^{-1}R^\dagger N^{-1}=F_W.$$

> [!proof] Sketch (source: §6.1, pp. 83-85)
> Expanding the error
> $$E^2=\mathrm{Tr}\big[\langle ss^\dagger\rangle-F_L\langle ds^\dagger\rangle-\langle sd^\dagger\rangle F_L^\dagger+F_L\langle dd^\dagger\rangle F_L^\dagger\big]$$
> and setting $\partial E^2/\partial F_L^\dagger=0$, with $F_L$ and $F_L^\dagger$ treated as independent, gives $F_L$. For the equality with $F_W$, Proof A multiplies out both sides; Proof B uses the push-through identity $(AB+\mathbb 1_S)^{-1}A=A(BA+\mathbb 1_D)^{-1}$ with $A=R^\dagger$.

The first form is a data-space operation (it inverts $\langle dd^\dagger\rangle=RSR^\dagger+N$); the second is a signal-space operation (it inverts $D^{-1}$). Which is cheaper depends on whether data or signal has fewer degrees of freedom.

**Linear response and noise without Gaussianity** (§6.1, pp. 85-87). For any joint distribution of zero-mean $s,d$ one can define

$$R=\langle ds^\dagger\rangle\langle ss^\dagger\rangle^{-1},\qquad N=\langle dd^\dagger\rangle-\langle ds^\dagger\rangle\langle ss^\dagger\rangle^{-1}\langle sd^\dagger\rangle,\qquad n:=d-Rs.$$

Then $n$ is linearly uncorrelated with $s$ ($\langle ns^\dagger\rangle=0$) and has covariance $N$, so $F_L=F_W$ holds by construction. This gives a Gaussian ("maximum entropy with known second moments") model that reproduces the optimal linear estimate (p. 87). See [[Signal response]].

> [!example] Noiseless cubic data (source: §6.1, pp. 86-87)
> $s\sim\mathcal G(s,\sigma^2)$, $d=s^3$. Moments $\langle ss\rangle=\sigma^2$, $\langle ds\rangle=3\sigma^4$, $\langle dd\rangle=15\sigma^6$ give $R=3\sigma^2$, $N=6\sigma^6$, $F_L=\tfrac15\sigma^{-2}$ and error $\langle(s-F_Ld)^2\rangle=\tfrac25\sigma^2$. The linear estimate is poor because the measurement is non-linear; a non-linear operation on $d$ can do better.

## Filter and response symmetry (§6.2, pp. 87-88)

In the joint Gaussian of $x=(d,s)$ with covariance $X$, the estimate and the response have the same form:

$$\langle s\rangle_{s|d}=\langle sd^\dagger\rangle\langle dd^\dagger\rangle^{-1}d,\qquad \langle d\rangle_{d|s}=Rs=\langle ds^\dagger\rangle\langle ss^\dagger\rangle^{-1}s.$$

 Swapping $d\leftrightarrow s$ turns signal estimate into data response and data estimate into signal response. For sub-vectors, $m_a=X_{ab}X_{bb}^{-1}x_b$ and the conditional covariance is (p. 88)

$$D_{aa}=\Big(X_{aa}^{-1}+X_{aa}^{-1}X_{ab}\big[X_{bb}-X_{ab}^\dagger X_{aa}^{-1}X_{ab}\big]^{-1}X_{ab}^\dagger X_{aa}^{-1}\Big)^{-1}.$$

## Statistically homogeneous case: Fourier-space filter (§8, pp. 97-102)

With $R=\mathbb 1$, $d=s+n$ and statistically homogeneous signal and noise ($S^x{}_y=C_s(x-y)$), the covariances are diagonal in Fourier space by the [[Wiener-Khinchin theorem]], $S^k{}_{k'}=(2\pi)^u\delta(k-k')P_s(k)$ and likewise $N$ with $P_n$ (§8.3, p. 99-100). Then (§8.3.3, pp. 100-101):

> [!theorem] Spectral Wiener filter (source: §8.3.3, pp. 100-101)
> $$D=(2\pi)^u\delta(k-q)\big([P_s(k)]^{-1}+[P_n(k)]^{-1}\big)^{-1},\qquad m^k=f(k)\,d^k,\qquad f(k)=\frac{1}{1+P_n(k)/P_s(k)}.$$

The filter passes modes with $P_s\gg P_n$ unchanged and down-weights modes with $P_s\ll P_n$ by the factor $P_s/P_n$.

Position space (§8.3.4, pp. 101-102): $m=f*d$, a convolution with the inverse Fourier transform of $f(k)$. Spectra of the result and of the error $\epsilon=s-m$:

$$P_m=f\,P_s=\frac{P_s^2}{P_s+P_n},\qquad P_\epsilon=P_D=f\,P_n,\qquad P_m+P_D=P_s.$$

The map therefore has less power than the signal, and the missing power is exactly the posterior uncertainty (eqs. 302-304, pp. 102-103).

> [!example] Large-scale signal, white noise (source: §8.3.5, pp. 103-105)
> $P_n=\sigma_n^2$ and $P_s=\sigma_s^2(k/k_0)^{-2}$ give $f(k)=q^2/(k^2+q^2)$ with cut-off $q=\sigma_sk_0/\sigma_n$. Closing the contour with the residue theorem gives the position-space kernel $f(x)=\tfrac q2e^{-q|x|}=\tfrac1{2\lambda}e^{-|x|/\lambda}$ with correlation length $\lambda=1/q$.

## Deconvolution (§8.3.6, pp. 105-107)

For $d=b*s+n$ the response is also diagonal in Fourier space, $R^k{}_{k'}=(2\pi)^u\delta(k-k')b(k)$. With $P_R=|b|^2$ and the fidelity $P_Q=P_sP_R/P_n$ (the diagonal of $Q=SR^\dagger N^{-1}R$):

$$P_D=\frac{P_s}{1+P_sP_R/P_n},\qquad f(k)=\frac{P_Q}{1+P_Q}\,\frac1{b(k)},\qquad P_m=\frac{P_Q}{1+P_Q}P_s.$$

High-fidelity modes ($P_Q\gg1$) are fully deconvolved ($f\to1/b$). Low-fidelity modes ($P_Q\ll1$) are suppressed by $P_Q$ instead of dividing the noise by a small $b$. The reconstruction is $m^k=\tfrac{P_Q}{1+P_Q}\big(s^k+n^k/b(k)\big)$, so it is shaped by the convolution, the noise and the deconvolution (p. 106).

## Missing data (§8.3.7, pp. 107-109)

Blocking part $\Omega$ of the signal space is modelled by a transparency operator $T$ (diagonal, 1 outside $\Omega$, 0 inside) so $R'=RT$. The source $j'$ vanishes in $\Omega$ and the propagator becomes $D'=(D^{-1}-\Delta)^{-1}$ with $\Delta=R^\dagger N^{-1}R-T^\dagger R^\dagger N^{-1}RT$. When $M=R^\dagger N^{-1}R$ is local, $\Delta=BMB$ with the blocking operator $B=\mathbb 1-T$, and

$$D'=D+D\Delta D+D\Delta D\Delta D+\dots$$

(eq. 305, p. 108). The series converges because $X=D^{1/2}\Delta D^{1/2}<1$ (§9, pp. 112-113). Uncertainty rises in and near $\Omega$, and information flows in from the unblocked area to compensate for the missing source (p. 109).

## Matrix algebra used (§9, pp. 111-113)
- A function of a Hermitian positive matrix acts on its eigenvalues: $f(A)=\sum_i a_ia_i^\dagger f(\alpha_i)$. The log-determinant identity is $\ln|A|=\mathrm{Tr}\ln A$.
- The square root gives samples: $\xi\sim\mathcal G(\xi,\mathbb 1)$, $s=S^{1/2}\xi$ has $\langle ss^\dagger\rangle=S$ (p. 112).
- The geometric series for $D'$ follows from $D'=D^{1/2}(1-X)^{-1}D^{1/2}$.

## Where it appears
- [[Gaussian process]]: with Dirac measurements the Wiener filter is GP regression; the notes' prior covariance $S$ is the GP kernel.
- [[Kalman filter]]: Gaussian filtering in time; the Markov structure of ch. 10 is what makes it recursive.
- [[Information field theory]]: the free theory is the Wiener filter; non-Gaussian priors or responses give interacting theories. The critical filter (unknown $P_s$) is a later chapter, [[Critical filter]] (not yet a page).
- [[Convolution]]: deconvolution is Wiener filtering with a diagonal Fourier response.

**Notation**: Enßlin writes $S,N,D$ for covariances; [[Information field theory]] (Alberts and Bilionis) uses $S$ for a precision. Enßlin's Fourier convention is $f^k=\int d^ux\,e^{ikx}f(x)$ with $f(x)=\int d^uk/(2\pi)^u\,e^{-ikx}f^k$ (§8.2, p. 98); see [[Fourier transform]].

**Covered in**: Enßlin IT & IFT chs. 5, 6, 8, 9 (pp. 79-113)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Information Hamiltonian]] · [[Signal response]] · [[Wiener-Khinchin theorem]] · [[Lognormal Poisson model]]
- [[Information field theory]] · [[Gaussian process]] · [[Kalman filter]] · [[Fourier transform]] · [[Convolution]] · [[Bayesian inverse problems]]
