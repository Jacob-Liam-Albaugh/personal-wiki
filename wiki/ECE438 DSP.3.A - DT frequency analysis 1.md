---
type: lecture
area: dsp
source-ref: "Topic DSP.3.A, pp. 1-14"
course: ece438
lecture: DSP.3.A
tags: [signals]
---

# ECE438 DSP.3.A - DT frequency analysis 1

**Summary**: Introduces the [[DFT]] as a change of basis. Reviews complex arithmetic and inner products, derives orthogonal projection, shows the complex sinusoids $e^{j2\pi kn/N}$ are orthogonal, and reads the DFT pair off as projection coefficients and reconstruction.

**File**: `Digital Signal Processing/Topic DSP.3.A DT frequency analysis Part 1 Jan 31, 2025.pdf`

---

## Topics
- **DFT and DTFS (p. 2)**: the book's DFT and inverse, for $k,n=0,\dots,N-1$.
  $$X(k)=\sum_{n=0}^{N-1}x(n)\,e^{-j2\pi nk/N}$$
  $$x(n)=\frac1N\sum_{k=0}^{N-1}X(k)\,e^{j2\pi nk/N}$$
  The ECE 301 Fourier series coefficients (DTFS) $a_k=\frac1N\sum_n x[n]e^{-j2\pi nk/N}$ are the same up to a factor of $1/N$, but are used only for $N$-periodic signals; the DFT is applied to any DT signal. Mathematicians often use the symmetric version with $1/\sqrt N$ in both directions.
- **Why the DFT (p. 3)**: a fast algorithm exists (see [[ECE438 DSP.3.E - FFT]]); it is a matrix operation, one example of a linear transformation; keeping a subset of the basis vectors approximates a signal, the idea behind image compression.
- **Complex exponentials are eigenfunctions of LTI systems (p. 4)**: feeding $e^{j\omega n}$ into an [[LTI system]] with impulse response $h[n]$:
  $$y[n]=\sum_k h[k]e^{j\omega(n-k)}=e^{j\omega n}\sum_k h[k]e^{-j\omega k}=e^{j\omega n}H(e^{j\omega})$$
  The output is the same exponential scaled by a complex number; being complex, it may add a phase shift.
- **Complex arithmetic review (p. 5)**: $z^*$, real and imaginary parts, $|z|=\sqrt{zz^*}$, polar form $z=|z|e^{j\theta}$ (easier for powers). Euler: $e^{j\theta}=\cos\theta+j\sin\theta$, $|e^{j\theta}|=1$.
  $$\cos\theta=\frac{e^{j\theta}+e^{-j\theta}}2,\quad \sin\theta=\frac{e^{j\theta}-e^{-j\theta}}{2j}$$
  Because $e^{z+2\pi nj}=e^z$, DT exponentials whose frequencies differ by a multiple of $2\pi$ are identical.
- **Linear algebra review (pp. 7-8)**: Hermitian inner product $\langle u,v\rangle=\sum_n u_nv_n^*$, with $\langle cu,v\rangle=c\langle u,v\rangle$, $\langle u,cv\rangle=c^*\langle u,v\rangle$, $\langle u,v\rangle=\langle v,u\rangle^*$. Norm $\|v\|=\sqrt{\langle v,v\rangle}$ (always real, $\ge0$, zero iff $v=0$). Orthogonal vectors have $\langle u,v\rangle=0$; then $\|u\|^2+\|v\|^2=\|u+v\|^2$ (Pythagoras).

## Key results
> [!theorem] Orthogonal projection
> The projection of $s$ onto $g$ is $s_g=cg$ with $(s-s_g)\perp g$, which gives
> $$c=\frac{\langle s,g\rangle}{\langle g,g\rangle},\qquad s_g=\frac{\langle s,g\rangle}{\langle g,g\rangle}\,g$$
> (source: p. 8)

If $\{g_k\}_{k=1}^N$ is an orthogonal set in $\mathbb C^N$, then $s=\sum_k \frac{\langle s,g_k\rangle}{\langle g_k,g_k\rangle}g_k$ (proof omitted, p. 10). A set of linearly independent vectors that span a space is a basis; many bases span the same space.

> [!theorem] Orthogonality of the DFT basis
> With $s_k[n]=e^{j2\pi kn/N}$, $n=0..N-1$:
> $$\langle s_k,s_l\rangle=\sum_{n=0}^{N-1}e^{j2\pi(k-l)n/N}=\begin{cases}N&k=l\\0&k\ne l\end{cases}$$
> For $k\ne l$ it is a finite geometric sum $\frac{1-r^N}{1-r}$ with $r=e^{j2\pi(k-l)/N}$; the numerator is zero and the denominator is not. (source: pp. 10-11)

> [!theorem] DFT as change of basis
> Define $X(k)=\langle x,s_k\rangle=\sum_n x(n)e^{-j2\pi nk/N}$. Since $\langle s_k,s_k\rangle=N$,
> $$x=\sum_k\frac{X(k)}{N}s_k\;\Rightarrow\; x(n)=\frac1N\sum_kX(k)e^{j2\pi nk/N}$$
> Interpretation: a change of coordinates from the natural (time-sample) basis to the sinusoidal (spectral) basis. The signal itself has not changed. (source: p. 12)

## Examples
> [!example] Projections in $\mathbb R^2$ (p. 9)
> $s=(3,2)^T$ onto $g=(1,0)^T$ gives $s_g=(3,0)^T$, the usual coordinate. $s=(3,2)^T$ onto $g=(-2,3)^T$ gives $\frac{6-6}{4+9}g=0$: they are orthogonal, so the projection is zero.

## Connections
- The finite-length sinusoid basis continues in [[ECE438 DSP.3.B - DT frequency analysis 2]] (matrix form, DTFT link) and [[ECE438 DSP.3.C - More on DFT]].
- Eigenfunction property is why [[LTI system]] analysis uses frequency; see [[DTFT]].

**Sources**: `Digital Signal Processing/Topic DSP.3.A DT frequency analysis Part 1 Jan 31, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DFT]] · [[DTFT]] · [[Fourier transform]] · [[FFT]] · [[LTI system]] · [[ECE438 DSP.1 - DT signals]] · [[ECE438 DSP.2 - DT systems]]
