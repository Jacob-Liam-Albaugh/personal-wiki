---
type: lecture
area: dsp
source-ref: "Topic DSP.6, pp. 1-16"
course: ece438
lecture: DSP.6
tags: [signals]
---

# ECE438 DSP.6 - z-transforms

**Summary**: The [[Z-transform]]: definition, region of convergence (ROC), poles and zeros, and the ROC rules that decide causality and BIBO stability of a DT [[LTI system]]. Ends with common properties, a table of pairs and an inverse-transform example.

**File**: `Digital Signal Processing/Topic DSP.6 z-transforms March 7, 2025.pdf`

---

## Topics
- **Motivation (p. 1)**: understand system stability, design linear filters, and handle $h[n]$ with no DTFT (absolute summability needed; e.g. $h[n]=e^nu[n]$ has no FT). The z-transform is to the [[Laplace transform]] what the [[DTFT]] is to the continuous-time FT.
- **Definition (p. 2)**: $z=re^{j\omega}$ is any complex number, not only on the unit circle:
$$X(z)=\sum_{n=-\infty}^{\infty}x[n]\,z^{-n}$$
- **ROC (p. 3)**: the set of $z$ for which the transform converges. Identifying it is a critical part of stating the transform, because different sequences can have the same $H(z)$ with different ROC.
- **Rational transfer functions (p. 6)**: for a linear constant-coefficient difference equation
$$y[n]=\sum_{i=0}^{M}b_ix[n-i]-\sum_{k=1}^{N}a_ky[n-k]$$
$$H(z)=\frac{\sum_ib_iz^{-i}}{1+\sum_ka_kz^{-k}}$$
If all $a_k=0$ the filter is FIR, otherwise IIR (p. 7). Factoring gives zeros $z_k$ (where $H=0$) and poles $p_k$ (where $|H|\to\infty$), possibly also at $z=\infty$ (p. 7).

## Key results
> [!theorem] DTFT as a slice (p. 2)
> $$H(e^{j\omega})=H(z)\big|_{z=e^{j\omega}}$$
> valid when the unit circle is inside the ROC.

> [!example] Same function, different ROC (pp. 3-5)
> $x[n]=a^nu[n]$ (causal): $X(z)=\frac{1}{1-az^{-1}}=\frac{z}{z-a}$, ROC $|z|>|a|$ (outside a circle).
> $x[n]=-a^nu[-n-1]$ (anti-causal): same $X(z)$, ROC $|z|<|a|$ (inside).
> Two-sided $x[n]=a^nu[n]+b^nu[-n-1]$: converges for $|z|>|a|$ and $|z|<|b|$. If $a>b$ there is no ROC; if $a<b$ the ROC is the ring $|a|<|z|<|b|$, the intersection of the two pieces. Then
> $$X(z)=\frac{1}{1-az^{-1}}-\frac{1}{1-bz^{-1}}$$
> Any causal signal has ROC outside a circle; any anti-causal signal has ROC inside a circle.

> [!theorem] ROC properties (pp. 8-10)
> 1. The ROC is a disc or ring centred at the origin, $r_1<|z|<r_2$ (either may be $0$ or $\infty$).
> 2. The ROC contains no poles.
> 3. The DTFT exists only if the ROC contains the unit circle.
> 4. A finite-duration signal has the entire $z$-plane as ROC, except possibly $z=0$ (and $\infty$).
> 5. A right-sided signal has ROC $|z|>p_{max}$, outermost pole.
> 6. A left-sided signal has ROC $|z|<p_{min}$, innermost nonzero pole.
> 7. If $X(z)$ is rational and the signal right-sided, the ROC is outside the outermost pole.
> 8. A DT LTI system is causal iff the ROC is the exterior of a circle (including $\infty$). Proof: causal means $h[n]=0$ for $n<0$, so right-sided; use property 5.
> 9. A DT LTI system is BIBO stable iff the ROC of $H(z)$ includes the unit circle. Proof: stability means $h[n]$ absolutely summable, which happens if the DTFT exists; use property 3.
> 10. A causal DT LTI system is stable iff its poles are inside the unit circle (apply 8 and 9). The sheet sketches three cases: causal and stable, causal and unstable, non-causal and stable.

> [!theorem] Basic properties (p. 12)
> | Property | $x[n]$ | $X(z)$ | ROC |
> |---|---|---|---|
> | linearity | $ax_1+bx_2$ | $aX_1+bX_2$ | at least $R_1\cap R_2$ |
> | time shift | $x[n-n_0]$ | $z^{-n_0}X(z)$ | $R$, except maybe $z=0$ |
> | convolution | $x*h$ | $X(z)H(z)$ | at least $R_1\cap R_2$ |
> | upsampling | $x[r]$ if $n=rk$, else 0 | $X(z^k)$ | $R^{1/k}$ |
> | time reversal | $x[-n]$ | $X(z^{-1})$ | $R^{-1}$ |
> | differentiation | $nx[n]$ | $-z\,dX/dz$ | $R$ |
> Also $h^*[n]\leftrightarrow H^*(z^*)$. So a real $h[n]$ has $H(z)=H^*(z^*)$, and poles and zeros of a real system come in conjugate pairs (p. 12).
> A common-pairs table from Oppenheim and Willsky (Table 10.2) is reproduced on p. 12: $\delta[n]\to1$; $u[n]\to\frac1{1-z^{-1}}$, $|z|>1$; $\alpha^nu[n]\to\frac1{1-\alpha z^{-1}}$, $|z|>|\alpha|$; $n\alpha^nu[n]\to\frac{\alpha z^{-1}}{(1-\alpha z^{-1})^2}$; and cosine/sine and damped cosine/sine pairs.

> [!theorem] Eigenfunction (p. 16)
> $z^n$ is an eigenfunction of any DT LTI system, for any $z_0$ in the ROC. With $x[n]=z_0^n$:
> $$y[n]=\sum_kh[k]\,z_0^{n-k}=z_0^n\sum_kh[k]\,z_0^{-k}=z_0^nH(z_0)$$
> Nearly identical to the earlier observation for $e^{j\omega n}$ (see [[ECE438 DSP.2 - DT systems]]). Wiki note: the sheet's last line writes $z_0H(z)$; the algebra above gives $z_0^nH(z_0)$.

## Examples
> [!example] Inverse z-transform by partial fractions (pp. 13-15)
> Find all sequences with
> $$X(z)=\frac{1-4z^{-1}}{1-3z^{-1}+2z^{-2}}=\frac{1-4z^{-1}}{(1-2z^{-1})(1-z^{-1})}$$
> Poles at $z=2$ and $z=1$, zero at $z=4$. The cases can be set from the poles before any algebra. Partial fractions: $A+B=1$, $A+2B=4$, so $A=-2$, $B=3$:
> $$X(z)=\frac{-2}{1-2z^{-1}}+\frac{3}{1-z^{-1}}$$
> - Case 1, $|z|<1$ (two anti-causal terms): $x[n]=3(-1^n u[-n-1])-2(-2^nu[-n-1])$.
> - Case 2, $1<|z|<2$ (one causal, one anti-causal): $x[n]=3\cdot1^nu[n]-2(-2^nu[-n-1])$.
> - Case 3, $|z|>2$ (two causal terms): $x[n]=3u[n]-2\cdot2^nu[n]$.
> The DTFT exists for none of these (the unit circle is never in a valid ROC with a pole at $z=1$, or $z=2$ for the unstable cases). Wiki note: the sheet's case 1 simplification reads $(-3+2^n)u[-n-1]$; term-by-term it is $(-3+2\cdot2^n)u[-n-1]$.

## Connections
- Used in [[Digital filter]] design. For $|z|=1$, same function as [[DTFT]]. System context: [[LTI system]], [[Convolution]].
- Continuous-time analogue: [[Laplace transform]].

**Sources**: `Digital Signal Processing/Topic DSP.6 z-transforms March 7, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Z-transform]] · [[LTI system]] · [[Digital filter]] · [[DTFT]] · [[Convolution]] · [[Laplace transform]]
