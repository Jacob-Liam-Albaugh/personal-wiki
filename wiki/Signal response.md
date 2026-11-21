---
type: concept
area: ift
areas: [ift, bayesian, signals]
source-ref: "Enßlin IT & IFT, §6.3, pp. 88-93 (PDF pages)"
tags: [ift, inverse-problems, signals]
---

# Signal response

**Summary**: the response $R$ maps a signal (usually a field) into data space, $d=Rs+n$. It encodes the measuring instrument. Examples: repeated measurement, deconvolution, photography, tomography and interferometry.

Page numbers are PDF pages of the lecture notes (printed page = PDF page minus 6).

---

## Definition

> [!definition] Response (source: Ensslin - Information Theory & Information Field Theory.pdf, §6.3, p. 88)
> Generic response $R(s):=\langle d\rangle_{d|s}$, the expected data given the signal. Linear response $R(s)=Rs$ with
> $$R=\langle ds^\dagger\rangle\langle ss^\dagger\rangle^{-1}.$$

The signal lives in signal space, the data in data space, and $R$ translates between them. The noise is whatever the response does not explain, $n=d-Rs$ (see [[Wiener filter]]). [[Information Hamiltonian]] shows how $R$ enters the posterior through $R^\dagger N^{-1}R$ and $R^\dagger N^{-1}d$.

## Examples from the notes (§6.3)

- **Repeated measurement** (§6.3.1, pp. 88-89): one number $s\in\mathbb R$ measured $n$ times has $R$ equal to a column of ones, $s\mapsto(s,\dots,s)$.
- **Minimalist deconvolution** (§6.3.2, p. 89): three pixels, $S=\mathbb 1_3$, $N=\mathbb 1_2$, data $d_1=s_1+s_2+n_1$, $d_2=s_2+s_3+n_2$. Then
$$D^{-1}=\begin{pmatrix}2&1&0\\1&3&1\\0&1&2\end{pmatrix},\quad D=\frac18\begin{pmatrix}5&-2&1\\-2&4&-2\\1&-2&5\end{pmatrix},\quad m=\frac18\begin{pmatrix}3d_1-d_2\\2(d_1+d_2)\\-d_1+3d_2\end{pmatrix}.$$
- **Photography** (§6.3.3, pp. 90): $R_i:C(\mathbb R^2)\to\mathbb R$, $d_i=\int d^2x\,R_i(x)s(x)+n_i$, with $R_i$ the point spread function of detector $i$.
- **Tomography** (§6.3.4, p. 91): rays $x_i(t)=a_i+tb_i$ give $d_i=\int_0^{t_{\max,i}}dt\,s(x_i(t))+n_i$, so $R_{ix}=\int dt\,\delta(x-x_i(t))$.
- **Interferometry** (§6.3.5, pp. 91-93): the visibility $V_{ij}$ of two apertures is a Fourier component of the sky brightness, $V_{ij}\propto\int d\hat n\,s_{\hat n}e^{i\hat n\cdot k_{ij}}$ with $k_{ij}=(x_i-x_j)/\lambda$, so $R$ is a sparse sampling of the Fourier transform.
- **Convolution** (§8.3.6, p. 105): translation-invariant $R^x{}_y=b(x-y)$ is diagonal in Fourier space; see [[Wiener filter]] and [[Convolution]].
- **Masking** (§8.3.7, p. 107): a transparency operator $T$ cuts out blocked regions.
- **Non-linear / Poisson** ([[Lognormal Poisson model]]): the expected counts $\lambda=\int R\,\varrho$ are linear in the density $\varrho=\rho_0e^s$, but non-linear in $s$.

## Where it appears
- The same $R$ plays the role of the forward operator in [[Bayesian inverse problems]].
- [[Wiener filter]] section "Filter and response symmetry": filter and response are the same formula with $d$ and $s$ swapped.

**Covered in**: Enßlin IT & IFT ch. 6 (pp. 83-93)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Wiener filter]] · [[Information Hamiltonian]] · [[Lognormal Poisson model]] · [[Information field theory]] · [[Bayesian inverse problems]] · [[Convolution]]
