---
type: definition
area: dsp
source-ref: "ECE 438 Topic DSP.3.A-3.D; exam 1 review"
tags: [signals]
---

# DFT

**Summary**: The discrete Fourier transform maps $N$ samples to $N$ frequency coefficients. It is a change of basis to complex sinusoids, a matrix multiplication, and samples of the [[DTFT]] of the same data. [[FFT]] computes it fast.

## Definition
> [!definition] DFT pair
> With $W_N=e^{-j2\pi/N}$ and $k,n=0,\dots,N-1$:
> $$X(k)=\sum_{n=0}^{N-1}x(n)\,W_N^{kn}$$
> $$x(n)=\frac1N\sum_{k=0}^{N-1}X(k)\,W_N^{-kn}$$
>
> (source: Topic DSP.3.A, p. 2; DSP.3.B, pp. 5-8)

The DTFS coefficients of ECE 301 are the same up to a $1/N$ factor, but the DFT is applied to any signal (DSP.3.A, p. 2).

## Why it works
> [!theorem] Orthogonality
> The vectors $s_k[n]=e^{j2\pi kn/N}$ satisfy $\langle s_k,s_l\rangle=N\delta_{kl}$. So $X(k)=\langle x,s_k\rangle$ are projection coefficients, and the DFT is a change of coordinates from the sample basis to the sinusoid basis. (source: Topic DSP.3.A, pp. 10-12)

Keeping only $m<N$ coefficients gives the best least-squares approximation, the idea behind transform coding (DSP.3.B, p. 4).

## Matrix form
> [!theorem] DFT matrix
> $$\mathbf X=\mathbf W_N\mathbf x,\qquad \mathbf x=\tfrac1N\mathbf W_N^{*}\mathbf X$$
> $\mathbf W_N$ is symmetric, $[\mathbf W_N]_{kn}=W_N^{kn}$, and $\mathbf W_N\mathbf W_N^*=N\mathbf I$. Orthogonal columns but not unitary without a $1/\sqrt N$ scale.
>
> (source: Topic DSP.3.B, pp. 7-8)

> [!example] Exam 1 review: 4-point DFT as a matrix
> $\mathbf W_4$ has rows $(1,1,1,1)$, $(1,-j,-1,j)$, $(1,-1,1,-1)$, $(1,j,-1,-j)$. For $\mathbf x=(0,1,2,3)^T$:
> $$\mathbf X=(6,\ -2+2j,\ -2,\ -2-2j)^T$$
> The inverse $\mathbf x=\frac14\mathbf W_4^*\mathbf X$ returns $(0,1,2,3)^T$; row 1 gives $\frac14(6-2+2j-2-2-2j)=0$ and row 2 gives $\frac14\cdot4=1$. The matrix is fixed for a given $N$.
>
> (source: exam_1_review_transcribed.pdf, pp. 3-5)

Wiki note: Topic DSP.3.B, p. 9, lists the third coefficient of this same example as $2$; the exam review and direct computation ($0-1+2-3$) give $-2$. The review itself notes its answer differs slightly from the notes.

## Relation to the DTFT
Truncate to $N$ samples and sample $\omega_k=2\pi k/N$: that is the DFT of the truncated signal (DSP.3.C, p. 3). A sinusoid not at a bin frequency spreads over every bin, see [[Spectral leakage]]. Zero padding samples the same DTFT more densely and does not remove leakage.

Product of DFTs is circular convolution; zero pad to $N\ge L+K-1$ for linear (DSP.3.D, pp. 3-6), see [[Convolution]].

## Linear-algebra background
Complex arithmetic: $|z|=\sqrt{zz^*}$, polar form $z=|z|e^{j\theta}$ (easier for powers), Euler $e^{j\theta}=\cos\theta+j\sin\theta$ with $|e^{j\theta}|=1$, and
$$\cos\theta=\frac{e^{j\theta}+e^{-j\theta}}2,\quad\sin\theta=\frac{e^{j\theta}-e^{-j\theta}}{2j}$$
Because $e^{z+2\pi nj}=e^z$, DT exponentials whose frequencies differ by a multiple of $2\pi$ are identical (source: Topic DSP.3.A, p. 5).

Hermitian inner product $\langle u,v\rangle=\sum_nu_nv_n^*$, with $\langle cu,v\rangle=c\langle u,v\rangle$, $\langle u,cv\rangle=c^*\langle u,v\rangle$, $\langle u,v\rangle=\langle v,u\rangle^*$. Norm $\|v\|=\sqrt{\langle v,v\rangle}$ (real, $\ge0$, zero iff $v=0$). Orthogonal vectors have $\langle u,v\rangle=0$, and then $\|u\|^2+\|v\|^2=\|u+v\|^2$ (source: Topic DSP.3.A, pp. 7-8).

> [!theorem] Orthogonal projection
> The projection of $s$ onto $g$ is $s_g=cg$ with $(s-s_g)\perp g$, so
> $$c=\frac{\langle s,g\rangle}{\langle g,g\rangle},\qquad s_g=\frac{\langle s,g\rangle}{\langle g,g\rangle}\,g$$
> For an orthogonal set $\{g_k\}_{k=1}^N$ in $\mathbb C^N$, $s=\sum_k\frac{\langle s,g_k\rangle}{\langle g_k,g_k\rangle}g_k$. A set of linearly independent vectors that span a space is a basis; many bases span the same space.
>
> (source: Topic DSP.3.A, pp. 8-10)

> [!example] Projections in $\mathbb R^2$
> $s=(3,2)^T$ onto $g=(1,0)^T$ gives $s_g=(3,0)^T$, the usual coordinate. Onto $g=(-2,3)^T$ it gives $\frac{6-6}{4+9}g=0$: they are orthogonal.
>
> (source: Topic DSP.3.A, p. 9)

The orthogonality theorem above is proved in the geometric-sum form: for $k\ne l$, $\langle s_k,s_l\rangle=\frac{1-r^N}{1-r}$ with $r=e^{j2\pi(k-l)/N}$, whose numerator is zero and denominator is not. Reading $X(k)=\langle x,s_k\rangle$ and $\langle s_k,s_k\rangle=N$ gives $x=\sum_k\frac{X(k)}Ns_k$, the inverse DFT. The signal itself has not changed; only its coordinates (source: Topic DSP.3.A, pp. 10-12).

Why use the DFT: a fast algorithm exists ([[FFT]]); it is a matrix operation; and keeping a subset of the basis vectors approximates a signal, the idea behind image compression (source: Topic DSP.3.A, p. 3). Mathematicians often use the symmetric version with $1/\sqrt N$ in both directions, which makes $\mathbf W_N/\sqrt N$ unitary. Complex exponentials are eigenfunctions of an [[LTI system]]: $e^{j\omega n}\to H(e^{j\omega})e^{j\omega n}$.

> [!theorem] Truncated projection is the best approximation
> Given an orthogonal basis $\{g_k\}$ and $x=\sum_ka_kg_k$, for $\mathcal G=\mathrm{span}\{g_1..g_m\}$ the choice $b_k=a_k=\langle x,g_k\rangle/\langle g_k,g_k\rangle$ minimizes $\|x-\hat x\|$ over $\mathcal G$. Proof: $(x-\hat x)\perp\mathcal G$, so for any other $f\in\mathcal G$,
> $$\|x-f\|^2=\|x-\hat x\|^2+\|\hat x-f\|^2\ge\|x-\hat x\|^2$$
> The $a_k$ are unique. How to choose the best basis is not addressed.
>
> (source: Topic DSP.3.B, pp. 2-4)

## Cost
One output $X(k)$ needs $N$ complex multiplications and $N-1$ additions, so all $N$ outputs need $N^2$ multiplications and $N(N-1)$ additions. This motivates the [[FFT]]; a useful identity is $W_N^{k+N/2}=-W_N^k$ (source: Topic DSP.3.B, pp. 5-8). For $N=4$: $W_4=-j$, $W_4^2=-1$, $W_4^3=j$, $W_4^4=1$.

## DFT of an off-bin sinusoid and periodicity
The DTFT $X(e^{j\omega})=\sum_nx[n]e^{-j\omega n}$ exists for absolutely or square summable $x$ and has period $2\pi$. It differs from the DFT in two ways: infinite-duration $x[n]$ and continuous frequency. To make it computable, (1) truncate $\tilde x[n]=x[n]$ for $0\le n\le N-1$ and (2) sample $\omega_k=2\pi k/N$, which gives $\tilde X(k)=\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi kn/N}$, the DFT of $\tilde x$ (source: Topic DSP.3.C, pp. 2-3).

Four-step trick for the DFT of $x[n]=e^{j\omega_xn}$, $n=0..N-1$, $\omega_x\ne2\pi k/N$ (source: Topic DSP.3.C, pp. 4-6):
1. Write $X(k)=\sum_ne^{j(\omega_x-\omega_k)n}$.
2. Sum the geometric series: $\frac{1-e^{j(\omega_x-\omega_k)N}}{1-e^{j(\omega_x-\omega_k)}}$.
3. Use $1-e^{j\theta}=e^{j\theta/2}(-2j)\sin(\theta/2)$ on top and bottom.
4. Read off $X(k)=e^{j(\omega_x-\omega_k)(N-1)/2}\sin[(\omega_x-\omega_k)N/2]/\sin[(\omega_x-\omega_k)/2]$.
The full statement and consequences are on [[Spectral leakage]].

The DTFS is only for $N$-periodic signals and its coefficients are $N$-periodic; the same holds for DFT coefficients. So the DFT implicitly assumes the input is $N$-periodic (source: Topic DSP.3.C, p. 6). The ECE 301 DTFS coefficients $a_k=\frac1N\sum_nx[n]e^{-j2\pi nk/N}$ differ from the DFT by the $1/N$ factor only.

Circular convolution, its dual product property, zero padding and overlap-add/save are on [[Convolution]].

**Covered in**: ECE 438 DSP.3.A, DSP.3.B, DSP.3.C (Topic DSP.3.A DT frequency analysis Part 1; Topic DSP.3.B Part 2; Topic DSP.3.C more on DFT)
**Sources**: `Digital Signal Processing/Topic DSP.3.A DT frequency analysis Part 1 Jan 31, 2025.pdf`, `Digital Signal Processing/Topic DSP.3.B DT frequency analysis Part 2 Jan 31, 2025.pdf`, `Digital Signal Processing/Topic DSP.3.C more on DFT Feb 2, 2025.pdf`, `Digital Signal Processing/Topic DSP.3.D Convolution with DFT Feb 9, 2025.pdf`, `Digital Signal Processing/exam_1_review_transcribed.pdf`, `Digital Signal Processing/Topic DSP.3.C Python Examples Spectral Leakage Feb 6, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[FFT]] · [[DTFT]] · [[Fourier transform]] · [[Spectral leakage]] · [[Convolution]] · [[Z-transform]] · [[Digital filter]] · [[Principal component analysis]] · [[Karhunen-Loève expansion]]
