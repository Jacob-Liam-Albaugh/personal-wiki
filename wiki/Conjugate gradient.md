---
type: method
area: ift
areas: [ift, math, bayesian]
source-ref: "Enßlin, IT & IFT, ch. 15, Algorithm 15.1, pp. 159-166"
tags: [ift, optimization, inverse-problems]
---

# Conjugate gradient

**Summary**: Iterative solver for $Ax=b$ with symmetric positive-definite $A$, available only as an operator. In IFT it applies the Wiener filter $m=Dj$ without ever inverting $D^{-1}=S^{-1}+R^\dagger N^{-1}R$.

Page numbers `p.` are PDF pages of `Ensslin - Information Theory & Information Field Theory.pdf` (printed page = PDF page minus 6).

## Why not the harmonic series (§15.1, p. 159)
$D=S^{1/2}(1+Q)^{-1}S^{1/2}=S-SMS+SMSMS-\cdots$ with $Q=S^{1/2}MS^{1/2}$ converges only if $\|Q\|<1$ and needs infinitely many iterations.

## Set-up (§15.2, pp. 159-161)
Wiener filtering minimises the information energy $H=\tfrac12s^\dagger D^{-1}s-j^\dagger s$ with gradient $g=D^{-1}s-j$. In CG notation $s\to x$, $D^{-1}\to A$, $j\to b$:
$$f(x)=\tfrac12x^\dagger Ax-b^\dagger x,\quad \nabla f=Ax-b,\quad x_\star=A^{-1}b.$$
Energy above the minimum, with the residual $r=b-Ax=-\nabla f$:
$$f(x)-f_\star=\tfrac12\|x-x_\star\|_A^2=\tfrac12\,r^\dagger A^{-1}r.$$
The normalised accuracy is $\eta=\|r\|/\|b\|$.

## Krylov subspace (§15.2.2, p. 161)
> [!definition] Krylov sequence
> $\mathcal K_k(A,b)=\mathrm{span}\{b,Ab,\ldots,A^{k-1}b\}$ and $x^{(k)}=\arg\min_{x\in\mathcal K_k}f(x)$. CG generates this sequence. Starting at $x^{(0)}=0$, $r^{(0)}=b$.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §15.2.2, p. 161)

Properties: $f(x^{(k+1)})\le f(x^{(k)})$ (but $\|r\|$ can increase); $x^{(n)}=x_\star$; $x^{(k)}=p_k(A)b$ for a polynomial of degree below $k$; a two-term recurrence $x^{(k+1)}=x^{(k)}+\alpha_kr^{(k)}+\beta_k(x^{(k)}-x^{(k-1)})$.

> [!theorem] Finite termination (§15.2.3, p. 162)
> By Cayley-Hamilton the characteristic polynomial satisfies $\chi(A)=0$, so $A^{-1}$ is a polynomial in $A$ of degree below $n$. Hence $x_\star\in\mathcal K_n(A,b)$ and CG needs at most $n$ steps in exact arithmetic.

> [!algorithm] Conjugate gradient (Algorithm 15.1, p. 163)
> $x^{(0)}=0,\ r^{(0)}=b,\ \rho_0=\|r^{(0)}\|^2,\ p^{(0)}=0$. For $k=1,2,\ldots$: stop if $\sqrt{\rho_{k-1}}\le\varepsilon\|b\|$, then
> $$p^{(k)}=r^{(k-1)}+\tfrac{\rho_{k-1}}{\rho_{k-2}}p^{(k-1)},\qquad w^{(k)}=Ap^{(k)},$$
> $$\alpha^{(k)}=\frac{\rho_{k-1}}{p^{(k)\dagger}w^{(k)}},\qquad x^{(k)}=x^{(k-1)}+\alpha^{(k)}p^{(k)},$$
> $$r^{(k)}=r^{(k-1)}-\alpha^{(k)}w^{(k)},\qquad \rho_k=\|r^{(k)}\|^2.$$
> The book checks $\alpha^{(1)}=b^\dagger b/b^\dagger Ab$.

## Convergence (§15.2.5, pp. 163-166)
In the eigenbasis of $A$ the energy is a sum, $f=\sum_i(\tfrac12\lambda_iy_i^2-b_iy_i)$, and the relative error is
$$\tau=\min_{\deg q<k,\,q(0)=1}\frac{\sum_iy_{\star i}^2\lambda_iq(\lambda_i)^2}{\sum_iy_{\star i}^2\lambda_i}.$$
The polynomial $q$ wants to be small at all eigenvalues, so **clustered eigenvalues** make CG fast. With the condition number $\kappa=\lambda_{\max}/\lambda_{\min}$,
$$\tau_k\le\Big(\frac{\sqrt\kappa-1}{\sqrt\kappa+1}\Big)^k.$$
Wiki note: $\tau$ is a relative squared $A$-norm error, for which the standard bound is $4\big(\tfrac{\sqrt\kappa-1}{\sqrt\kappa+1}\big)^{2k}$ **[unverified]**; the book's version drops the factor 4 and the square (see typos).

**Preconditioning** with $M\approx A^{-1}=TT^\dagger$: solve $T^\dagger ATy=T^\dagger b$, $x=Ty$, which has a smaller condition number.

> [!example] Wiener filter convergence (p. 165-166)
> $A=D^{-1}=S^{-1}+R^\dagger N^{-1}R$ with $T=S^{1/2}=F^\dagger\widehat{P_s^{1/2}}F$ (diagonal in Fourier space by the [[Wiener-Khinchin theorem]]). Then $T^\dagger AT=1+Q$ with $Q=S^{1/2}MS^{1/2}$ of rank at most the number $m$ of data points. The spectrum is $\{\lambda_1,\ldots,\lambda_m,1,\ldots,1\}$, so preconditioned CG converges exactly after about $m+1\ll n$ iterations.

## Where it appears
- Wiener filter application: [[Free theory (IFT)]].
- Quasi-Newton minimisation in [[Metric Gaussian variational inference]] and sample generation there.
- Early CG termination in posterior sampling gives conservative uncertainties (§17.2.1).

**Covered in**: Enßlin IT & IFT ch. 15 (pp. 159-166)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Wiener filter]] · [[Newton's method]] · [[Information field theory]]
