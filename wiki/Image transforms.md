---
type: method
area: dsp
source-ref: "ECE 438 Topic IP.5, pp. 1-24; lectures L32-L33"
tags: [signals]
---

# Image transforms

**Summary**: Unitary 1D and 2D transforms as basis expansions $f=A^{*T}t$, with the DFT, DCT, DST, Walsh-Hadamard and Haar transforms compared by basis images and energy compaction. All are invertible and carry the same information and energy as the image; they differ in how that energy is spread over the coefficients.

> [!definition] Inner product
> For complex vectors $\langle u,v\rangle=u^Tv^*$, with conjugate symmetry, linearity and positivity (zero only for $v=0$). For functions
> $$\langle f,g\rangle=\int_a^bf(x)\,g^*(x)\,dx$$
>
> (source: Topic IP.5 image transforms and wavelets Apr 14, 2025.pdf, pp. 1-2)

> [!definition] 1D transform pair
> Forward kernel $r$ and inverse kernel $s$, independent of $f$ and $T$:
> $$T(u)=\sum_{m=0}^{N-1}f(m)\,r(m,u),\qquad f(m)=\sum_{u=0}^{N-1}T(u)\,s(m,u)$$
> The $s(m,u)$ are the basis vectors and $f(m)=T(0)s(m,0)+\dots+T(N-1)s(m,N-1)$. If they are orthonormal, $T(u)=\langle s(m,u),f(m)\rangle$.
>
> (source: IP.5, pp. 3-4)

> [!theorem] Matrix form
> $$t=Af,\qquad A=[s_0\ s_1\ \dots\ s_{N-1}]^T$$
> For orthonormal $s$, $A$ is unitary: $A^{*T}A=AA^{*T}=I$, so $A^{*T}=A^{-1}$ and $f=A^{*T}t$.
>
> (source: IP.5, pp. 5-6)

> [!definition] 2D transform
> $$T(u,v)=\sum_{m=0}^{N-1}\sum_{n=0}^{N-1}f(m,n)\,r(m,n,u,v)$$
> with inverse kernel $s(m,n,u,v)$. The kernel is separable if $r=r_1(m,u)r_2(n,v)$ and symmetric if also $r_1=r_2$. Then a 2D transform is two 1D transforms: premultiply by $A$ (columns), then postmultiply by $A^T$ (rows):
> $$T=AFA^T,\qquad F=A^{*T}\,T\,A^*$$
> In words: apply $A$ to the columns, transpose, apply $A$ again, transpose back, $(A(AF)^T)^T=AFA^T$. Basis images are $s_us_v^T$ and $F=\sum_u\sum_vT(u,v)s_us_v^T$ for real separable bases. This separability mirrors the 2D [[Fourier transform]] and [[Spatial filtering]].
>
> (source: IP.5, pp. 6-9; L33 Apr 14, 2025.pdf, p. 1)

> [!example] N = 2 real orthonormal transform
> $s_0=\tfrac1{\sqrt2}(1,1)^T$, $s_1=\tfrac1{\sqrt2}(1,-1)^T$, $A=\tfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$. For $F=\begin{pmatrix}20&63\\21&128\end{pmatrix}$:
> $$T=AFA^T=\begin{pmatrix}116&-75\\-33&32\end{pmatrix}$$
> and $F=A^TTA$ recovers the image, as a weighted sum of four basis images with weights $116/2,-75/2,-33/2,32/2$. At $N=2$ the DFT, Hartley, cosine, sine, Walsh-Hadamard, slant and Haar transforms all reduce to this one.
>
> (source: IP.5, pp. 8-10)

## DFT
$$s(m,u)=\tfrac1{\sqrt N}e^{j2\pi mu/N},\qquad T(u)=\tfrac1{\sqrt N}\sum_{m=0}^{N-1}f(m)e^{-j2\pi mu/N}$$
(an earlier form used $r=e^{-j2\pi ux/N}$ and $s=\tfrac1Ne^{j2\pi ux/N}$, p. 4). This is the orthonormal-scaled [[DFT]].
- Overcomplete: twice as many coefficients as input values, since real and imaginary parts are both needed, with duplicates; for $N=8$, $s_5=s_3^*$, $s_6=s_2^*$, $s_7=s_1^*$.
- Weak energy compaction: it analyses the periodic extension, whose abrupt discontinuities produce high frequencies and many large coefficients (the [[Spectral leakage]] mechanism).
- Coefficients are floating point.
- Basis images (8x8): DC at $u=v=0$, highest frequency at $u=v=4$.

## DCT
$$s(m,u)=\alpha(u)\cos\frac{(2m+1)u\pi}{2N},\qquad\alpha(0)=\tfrac1{\sqrt N},\ \alpha(u)=\sqrt{2/N}\ (u\ge1)$$
- Real, orthogonal, not symmetric; complete ($N$ coefficients, not $2N$); twice the frequency resolution of the DFT. Basis images: DC at $u=v=0$, highest frequency at $u=v=7$ for $N=8$.
- Implies $2N$-point periodicity with even symmetry, which removes the boundary discontinuity (Fig. 6.11) and gives a large compaction gain. Used in JPEG, MPEG, H.264.
- The DCT of an $N$-point $f$ is the DFT of the $2N$-point symmetric extension $g(m)=f(m)$ for $0\le m<N$ and $g(m)=f(2N-m-1)$ for $N\le m<2N$.

## DST
$$s(m,u)=\sqrt{\tfrac2{N+1}}\sin\frac{(m+1)(u+1)\pi}{N+1}$$
Real, orthogonal, symmetric; no DC component. It equals a DFT of a $2(N+1)$-point periodic odd-symmetric signal (zero average) and does not reduce boundary discontinuities. It is an optional transform in H.265 (HEVC).

## Walsh-Hadamard
Basis functions take only the values $\pm1$. With $H_2=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$,
$$H_{2N}=\begin{pmatrix}H_N&H_N\\H_N&-H_N\end{pmatrix}$$
(Hadamard ordering), $A_W=\tfrac1{\sqrt N}H_N$ and $A_W^{-1}=A_W^T$. Sequency is the number of sign changes along a row; Fig. 6.16 shows the sequency-ordered $N=8$ version, entries all $\pm0.35$, highest frequency last.

## Haar
A wavelet transform shown as a block transform (Fig. 6.18). Basis images start very spread out and become increasingly localised. Rows of $A_H$ for $N=8$ include the DC row $0.35$, the row $(0.35,\dots,-0.35)$, rows with $\pm0.50$ and rows with $\pm0.71$. It has local frequency selectivity and is the bridge to the [[Wavelet transform]].

(source: IP.5, pp. 10-20; L33, p. 1; L34 Apr 18, 2025.pdf, p. 1)

Compaction is what [[Image compression]] exploits (DCT in JPEG). Wiki note: unitarity is the same orthonormal-basis idea behind the [[Karhunen-Loève expansion]] and [[Principal component analysis]]; the slides do not make this link.

**Covered in**: ECE 438 IP.5, L32, L33 (Digital Signal Processing/Topic IP.5 image transforms and wavelets Apr 14, 2025.pdf)
**Sources**: `Digital Signal Processing/Topic IP.5 image transforms and wavelets Apr 14, 2025.pdf`, `Digital Signal Processing/front page/L32 Apr 11, 2025.pdf`, `Digital Signal Processing/front page/L33 Apr 14, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DFT]] · [[FFT]] · [[Fourier transform]] · [[Wavelet transform]] · [[Spectral leakage]] · [[Spatial filtering]] · [[Image compression]] · [[Digital image]] · [[Karhunen-Loève expansion]] · [[Principal component analysis]]
