---
type: lecture
area: dsp
source-ref: "Digital Signal Processing/Topic IP.5 image transforms and wavelets Apr 14, 2025.pdf (ECE 438 handwritten slides, Gonzalez ch. 6, 4th ed.)"
course: ece438
lecture: IP.5
tags: [signals]
---

# ECE438 IP.5 - Image transforms and wavelets

**Summary**: Unitary 1-D and 2-D transforms as basis expansions $f = A^{*T}t$, with the DFT, DCT, DST, Walsh-Hadamard and Haar transforms compared by basis images and energy compaction.

**File**: `Digital Signal Processing/Topic IP.5 image transforms and wavelets Apr 14, 2025.pdf`

---

## Topics
- Inner products and inner-product spaces (complex vectors, continuous functions) (source: Topic IP.5 image transforms and wavelets Apr 14, 2025.pdf, p. 1-2).
- 1-D transform pair, kernels, and the inverse as a linear expansion in basis vectors (p. 3-4).
- Matrix form $t = Af$; unitary $A$ (p. 5-6).
- 2-D separable, symmetric transforms $T = AFA^T$ (p. 7-10).
- Basis images; DFT attributes; DCT, DST, Walsh-Hadamard, Haar (p. 11-24).

## Key results

> [!definition] Inner product
> For complex vectors $\langle u,v\rangle = u^T v^*$ (p. 2).
> Properties: conjugate symmetry, linearity, and positivity (zero only for $v=0$).
> For functions:
> $$\langle f,g\rangle = \int_a^b f(x)\,g^*(x)\,dx$$

> [!definition] 1-D transform pair
> Forward, with forward kernel $r$:
> $$T(u) = \sum_{m=0}^{N-1} f(m)\,r(m,u)$$
> Inverse, with inverse kernel $s$:
> $$f(m) = \sum_{u=0}^{N-1} T(u)\,s(m,u)$$
> The kernels do not depend on $f$ or $T$; they fix the nature and usefulness of the pair. The $s(m,u)$ are the basis vectors (p. 3).

The inverse is a linear expansion: $f(m) = T(0)s(m,0) + \dots + T(N-1)s(m,N-1)$. It is most useful when the $s(m,u)$ are orthonormal, since then $T(u) = \langle s(m,u), f(m)\rangle$ (p. 4).
All such transforms are invertible and carry the same information and energy as the signal. They differ in how that energy is spread over the coefficients (p. 1).

> [!theorem] Matrix form
> Stack $f$, $t$ and the columns $s_u$.
> $$t = A f,\quad A = [s_0\ s_1\ \dots\ s_{N-1}]^T$$
> $A$ does not depend on $t$ or $f$. If the $s$ are orthonormal, $A$ is unitary:
> $$A^{*T}A = AA^{*T} = I$$
> so $A^{*T}=A^{-1}$ and
> $$f = A^{*T}\,t$$
> (p. 5-6).

> [!definition] 2-D transform
> $$T(u,v) = \sum_{m=0}^{N-1}\sum_{n=0}^{N-1} f(m,n)\,r(m,n,u,v)$$
> The inverse uses $s(m,n,u,v)$.
> The kernel is separable if $r = r_1(m,u)\,r_2(n,v)$, and symmetric if also $r_1 = r_2$ (p. 6).

For separable symmetric kernels, premultiply $F$ by $A$ (transform the columns), then postmultiply by $A^T$ (transform the rows): a 2-D transform is two 1-D transforms (p. 7).
$$T = A F A^T$$
$$F = A^{*T}\,T\,A^{*}$$
Basis images are $s_u s_v^T$, and $F=\sum_u\sum_v T(u,v)\,s_u s_v^T$ for real separable bases (p. 8-9).

## Examples

> [!example] N = 2 real orthonormal transform (p. 8-9)
> $s_0 = \tfrac{1}{\sqrt2}(1,1)^T$, $s_1=\tfrac{1}{\sqrt2}(1,-1)^T$, so
> $$A = \tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$$
> With $F=\begin{pmatrix}20&63\\21&128\end{pmatrix}$ the slide computes
> $$T = AFA^T = \begin{pmatrix}116&-75\\-33&32\end{pmatrix}$$
> and $F = A^TTA$ recovers the image (the slide says to do the math). $F$ is then a weighted sum of four basis images with weights $116/2$, $-75/2$, $-33/2$, $32/2$.
> Many named transforms reduce to this one at $N=2$: DFT, Hartley, cosine, sine, Walsh-Hadamard, slant, Haar (p. 10).

### The DFT as an orthonormal transform
$$s(m,u) = \tfrac{1}{\sqrt N}\,e^{j2\pi mu/N}$$
$$T(u) = \tfrac{1}{\sqrt N}\sum_{m=0}^{N-1} f(m)\,e^{-j2\pi mu/N}$$
(p. 10; the earlier example used $r=e^{-j2\pi ux/N}$ and $s=\tfrac1N e^{j2\pi ux/N}$, p. 4.)

Attributes of the DFT (p. 12):
- Over-complete: twice as many coefficients as input values, since real and imaginary parts are both needed, and some are duplicates. For $N=8$: $s_5=s_3^*$, $s_6=s_2^*$, $s_7=s_1^*$.
- Weak energy compaction: the DFT analyses the periodic extension, which may have abrupt discontinuities, so high frequencies and many large coefficients appear.
- Coefficients are floating point.
- Basis images: DC at $u=v=0$, highest frequency at $u=v=4$ for $N=8$ (p. 11).

### Discrete cosine transform (p. 13-15)
$$s(m,u) = \alpha(u)\cos\frac{(2m+1)u\pi}{2N}$$
$$\alpha(0)=\tfrac{1}{\sqrt N},\quad \alpha(u)=\sqrt{2/N}\ \ (u\ge1)$$
- Real, orthogonal, not symmetric; complete (only $N$ coefficients, not $2N$); twice the frequency resolution of the DFT.
- Implies $2N$-point periodicity with even symmetry, which minimises the boundary discontinuity and gives a large energy-compaction gain.
- Used in JPEG, MPEG, H.264 (AVC).
- Relation to the DFT: the DCT of an $N$-point $f(m)$ is the DFT of the $2N$-point symmetric extension
  $$g(m) = f(m)\ (0\le m<N),\quad g(m)=f(2N-m-1)\ (N\le m<2N)$$
  (p. 14; Fig. 6.11).

### Discrete sine transform (p. 16)
$$s(m,u)=\sqrt{\tfrac{2}{N+1}}\,\sin\frac{(m+1)(u+1)\pi}{N+1}$$
- Real, orthogonal, symmetric; no DC component.
- Equivalent to a DFT of a $2(N+1)$-point periodic, odd-symmetric signal, so the average is 0.
- Does not reduce boundary discontinuities.
- Appears as an optional transform in H.265 (HEVC).

### Walsh-Hadamard transform (p. 17-18)
Basis functions take only the values $\pm1$. With $H_2=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ and
$$H_{2N}=\begin{pmatrix}H_N&H_N\\H_N&-H_N\end{pmatrix}$$
(Hadamard ordering), $A_W = \tfrac{1}{\sqrt N}H_N$ and $A_W^{-1}=A_W^T$. Sequency is the number of sign changes along a row; the sequency-ordered version is Fig. 6.16.

### Haar transform (p. 19-20)
A wavelet transform, shown as a block transform (Fig. 6.18). Basis images start very spread out and become increasingly localised. Rows of $A_H$ for $N=8$ include the DC row $0.35$, the row $(0.35,\dots,-0.35)$, rows with $\pm0.50$ and rows with $\pm0.71$.

## Connections
- The DFT here is the orthonormal-scaled version of [[DFT]]; the 1-D form matches [[ECE438 DSP.3.A - DT frequency analysis 1]].
- The DCT's even extension removes the edge discontinuity that causes [[Spectral leakage]] in the DFT.
- Compaction is exploited by [[ECE438 IP.6 - Image compression]].
- The Haar basis is the bridge to [[Wavelet transform]] and [[ECE438 IP.7 - Multiresolution image processing]].
- 2-D separability mirrors [[ECE438 IP.3 - Continuous-space FT]] and [[Spatial filtering]].
- Wiki note: unitarity here is the same orthonormal-basis idea behind [[Karhunen-Loève expansion]] and [[Principal component analysis]]; the slides do not make this link.

**Sources**: Digital Signal Processing/Topic IP.5 image transforms and wavelets Apr 14, 2025.pdf
**Last updated**: 2026-11-06

---

## Related pages
[[DFT]] | [[FFT]] | [[Fourier transform]] | [[Wavelet transform]] | [[Spectral leakage]] | [[Spatial filtering]] | [[ECE438 IP.6 - Image compression]] | [[ECE438 IP.7 - Multiresolution image processing]] | [[ECE438 IP.3 - Continuous-space FT]]
