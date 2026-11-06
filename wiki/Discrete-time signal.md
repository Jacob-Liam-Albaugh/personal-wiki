---
type: definition
area: dsp
source-ref: "ECE 438 Topic DSP.1; ECE 301 review topics 2.1-2.3; exam 1 review"
tags: [signals]
---

# Discrete-time signal

**Summary**: A function defined on the integers, $x[n]$ with $n\in\mathbb Z$. It is the object that every other DSP page operates on: [[LTI system]] inputs, [[DFT]] and [[DTFT]] arguments, samples from a [[Sampling theorem]] chain.

## Definition and representations
> [!definition] DT signal
> A map $x:\mathbb Z\to\mathbb R$ (or $\mathbb C$). It must be defined for every integer $n$. A digital signal also has integer values, $\mathbb Z\to\mathbb Z$.
>
> (source: Topic DSP.1 DT signals Jan 14, 2025.pdf, pp. 2-3)

Four representations: formula, stem plot, table, column vector in $\mathbb R^N$ (source: Topic DSP.1, pp. 3-5). Special signals: unit impulse $\delta[n]$, unit step $u[n]$, sinusoid $\sin(\omega n+\phi)$.

## Energy and power
> [!definition] Energy and power
> $$\mathcal E=\sum_{n=-\infty}^{\infty}|x[n]|^2$$
> $$P=\lim_{N\to\infty}\frac1{2N+1}\sum_{n=-N}^{N}|x[n]|^2$$
> Energy signals have $\mathcal E<\infty$ (so $P=0$); power signals have $0<P<\infty$.
>
> (source: Topic 2.1 power and energy Jul 17, 2022.pdf; Topic DSP.1, p. 7)

## Periodicity
> [!theorem] Periodic DT sinusoid
> $x[n]=x[n+N]$ for all $n$, some integer $N>0$. A DT sinusoid $\cos(\omega_0 n)$ is periodic iff
> $$\frac{\omega_0}{2\pi}\ \text{is rational}$$
> equivalently $\omega_0N=2\pi k$ for integers $N,k$. The fundamental period is the smallest such $N$.
>
> (source: exam_1_review_transcribed.pdf, p. 2; Topic 2.3 period of a signal Note Jul 23, 2022.pdf)

> [!example] Periodic and aperiodic cosines
> $\cos(\tfrac\pi4 n)$: $\omega_0=\pi/4$, so $N=8k$, smallest $N=8$, periodic.
> $\cos(n)$: $\omega_0=1$, $N=2\pi k$ with $2\pi$ irrational, so aperiodic.
> A periodic signal has infinite duration, and a finite-duration signal cannot be periodic (Topic DSP.1).
>
> (source: exam_1_review_transcribed.pdf, p. 2)

Frequencies $\omega$ and $\omega+2\pi$ give the same DT exponential, and the fastest oscillation is $\omega=\pm\pi$, $\cos(\pi n)=(-1)^n$ (source: Topic DSP.1). This is the root of [[Aliasing]] in DT.

### Further energy and power facts
Energy is a total (joules, kWh) and power is energy per unit time (watts); the signal itself may be in amps, so both are "energy-like" quantities. They are always real, since $|x|^2=xx^*=x_{Re}^2+x_{Im}^2$ (source: Topic 2.1, pp. 1-3).

Over a window, in CT and DT:
$$E=\int_{t_0}^{t_1}|x(t)|^2dt,\quad P=\frac{E}{t_1-t_0}$$
$$E=\sum_{n=n_1}^{n_2}|x[n]|^2,\quad P=\frac{E}{n_2-n_1+1}$$
Totals use the symmetric limits $T\to\infty$ or $N\to\infty$: $E_\infty=\lim_{T\to\infty}\int_{-T}^{T}|x(t)|^2dt$ and $P_\infty=\lim_{T\to\infty}\frac1{2T}\int_{-T}^{T}|x(t)|^2dt$ in CT, $E_\infty=\lim_{N\to\infty}\sum_{n=-N}^{N}|x[n]|^2$ and $P_\infty=\lim_{N\to\infty}\frac1{2N+1}\sum_{n=-N}^{N}|x[n]|^2$ in DT. Instantaneous power is $|x(t)|^2$ or $|x[n]|^2$. A finite-energy CT signal is square-integrable and a finite-energy DT signal is square-summable (source: Topic 2.1, pp. 1-4). In norm notation $\mathcal E(x)=\|x\|_2^2$, and the magnitude (bound) is the infinity norm $\max_n|x[n]|$ (source: Topic DSP.1, DSP.1.3).

Geometric sums used throughout (source: Topic DSP.1, p. 7):
$$\sum_{k=0}^{\infty}r^k=\frac1{1-r},\ |r|<1$$
$$\sum_{k=0}^{n}r^k=\frac{1-r^{n+1}}{1-r},\ r\ne1$$

> [!example] Complex exponential on $(-1/2,1)$
> $x(t)=\cos t+j\sin t$ has $|x|^2=1$, so $E=\int_{-1/2}^{1}dt=3/2$ and $P=(3/2)/(3/2)=1$ (source: Topic 2.1, p. 5).

Three categories: finite total energy forces $P_\infty=0$; nonzero $P_\infty$ forces infinite energy. So the possible cases are $(E_\infty,P_\infty)=(\infty,\infty)$, $(\infty,\text{finite})$, (finite, $0$); finite energy with infinite power cannot occur. Periodic signals have infinite energy and finite power (source: Topic 2.1, p. 5). Energy of a DT signal reappears as Parseval's relation for the [[DTFT]] and [[DFT]].

### Representations
A signal can be given as a formula (defined for all $n$, e.g. $f[n]=n/3$ for $n>0$, else $0$), a labelled stem plot, a table, or a column vector in $\mathbb R^N$ when it has $N$ nonzero points or is $N$-periodic. $x[n]=n^2u[n]$ is a function; "$n^2$ when $n>0$" is not; $x[n,m]=n+m$ is 2-D. The course is almost entirely DT, 1-D and 2-D (source: Topic DSP.1, DSP.1.1-DSP.1.2, pp. 2-5). A Fourier transform can be seen as a rotation in $N$-dimensional signal space that preserves distance and angle (source: Topic DSP.1, p. 5); see [[DFT]].

## Periodicity of CT and DT signals
$x(t)$ has period $T>0$ if $x(t-T)=x(t)$ for all $t$; $x[n]$ has period $N\in\mathbb Z_{>0}$ if $x[n-N]=x[n]$. The fundamental period is the smallest one. $\sin 2t$ has period $\pi$, so $2\pi$ is also a period, but $T_0=\pi$ (source: Topic 2.3, p. 2).

> [!theorem] CT complex exponential
> For $x(t)=e^{jat}$ need $e^{jaT}=1$, so
> $$T=\left|\frac{2\pi k}{a}\right|,\ k\ne0$$
> $$T_0=\left|\frac{2\pi}{a}\right|,\quad \omega_0=\frac{2\pi}{T_0}$$
> $\omega_0$ is the fundamental frequency (source: Topic 2.3, p. 3).

> [!example] $x[n]=\sin(3\pi n/4)$
> Need $\omega_1N=2\pi k$ with $\omega_1=3\pi/4$, so $N=8k/3$. The smallest integer reached is $N=8$ (check: $\cos6\pi=1$, $\sin6\pi=0$) (source: Topic 2.3, pp. 3-5).

> [!example] $x[n]=\sin(5n)$ is aperiodic
> The CT signal $\sin5t$ has $T=2\pi/5$, and the DT period would be $\mathrm{LCM}(1,2\pi/5)$, which does not exist (source: Topic 2.3, p. 6).

> [!example] Period of a sampled cosine
> $\cos(\tfrac{4\pi}5t)$ has $T_0=2.5$, so the samples $\cos(\tfrac{4\pi}5n)$ have $N_0=\mathrm{LCM}(2.5,1)=5$. $\cos t$ has period $2\pi$ but $\cos n$ is aperiodic, since $\mathrm{LCM}(1,2\pi)$ does not exist (source: Topic DSP.1, p. 9).

Examples of the other kind: $(-1)^n$ has $N_0=2$; $(-2)^n$ is not periodic because its magnitude grows (source: Topic DSP.1, DSP.1.3).

Assorted facts (source: Topic 2.3, pp. 7-8):
- $x(t)=1$ is periodic with many periods but has no fundamental period.
- One counterexample suffices to disprove periodicity.
- A sum of signals with periods $T_1,T_2$ is periodic only if $\mathrm{LCM}(T_1,T_2)$ exists, e.g. $\cos3t+\sin\pi t$ is not.
- If a complex periodic $x(t)$ has period $T$, its real and imaginary parts are both periodic with period $T$.
- Periodic signals are the natural input class for Fourier series; see [[Fourier transform]] and [[DFT]].

## Time transformations
Three basic operations on a CT signal (source: Topic 2.2, pp. 1-5):
1. Shift $x(t-t_0)$: delayed and moved right for $t_0>0$, advanced and moved left for $t_0<0$.
2. Reversal $x(-t)$: mirror image about $t=0$.
3. Scaling $x(at)$, $a>0$: stretched (slower) for $0<a<1$, squashed (faster) for $a>1$.

For a signal with breakpoints $t_1,t_2$: shift gives $t_1+t_0,t_2+t_0$; reversal gives $-t_2,-t_1$; $x(3t)$ gives $t_1/3,t_2/3$. Heights are unchanged.

To get $x(at+b)$ there are four approaches (source: Topic 2.2, p. 6):
1. Substitute $at+b$ for $t$ in the formula.
2. Track where key change points of $x$ land.
3. Apply in the right order: shift by $b$ first, then scale by $a$.
4. Apply in the wrong order and adjust the shift. For $a=-1$ this is preferred: flip first, then shift by $-b$ (p. 8).

> [!example] $x(2t+2)$ and $x(1-t)$ with $x$ spanning $3$ to $6$
> $x(2t+2)$: shift gives $x(t+2)$ on $[1,4]$, scale gives $[1/2,2]$. Approach 2 agrees: $2c+2=3$, $2d+2=6$.
> $x(1-t)$: shift then reverse gives $[-5,-2]$. Approach 4: $x(-t)$ spans $[-6,-3]$, shifting by $1$ gives $[-5,-2]$.
>
> (source: Topic 2.2, pp. 7-8)

> [!example] $x(at+b)$ for $x(t)=t$ on $[0,1]$
> Substitution gives $at+b$ on $-b/a\le t\le(1-b)/a$ for $a>0$. The maximum value does not change (source: Topic 2.2, p. 8).

> [!example] $x(2t-5)$ and $x(5-2t)$
> $x(2t-5)$ is delayed by $5/2$ and squashed by 2: $2t-5=t_1$ at $t=(t_1+5)/2$. For $x(5-2t)$ the breakpoints are at $t=-(t_1-5)/2$, a reversal plus scale plus shift (source: Topic 2.2, pp. 8-9).

> [!example] $x(t_0-t)$ with $x(t)=t[u(t)-u(t-1)]$
> Substitution gives $t_0-t$ on $t_0-1<t\le t_0$, zero elsewhere. Graphically flip first, then shift by $t_0$; the height at $t=t_0-1$ is $1$ (source: Topic 2.2, pp. 9-10). This flip-and-shift is the pattern inside [[Convolution]].

In DT, scaling is not a free operation. $x[2n]$ drops samples and can alias; see [[Sampling theorem]].

**Covered in**: ECE 438 DSP.1 (Topic DSP.1 DT signals), ECE 301 review 2.1-2.3 (power and energy, time transformations, period of a signal)
**Sources**: `Digital Signal Processing/Topic DSP.1 DT signals Jan 14, 2025.pdf`, `Digital Signal Processing/301 Review/Topic 2.1 power and energy Jul 17, 2022.pdf`, `Digital Signal Processing/301 Review/Topic 2.3 period of a signal Note Jul 23, 2022.pdf`, `Digital Signal Processing/exam_1_review_transcribed.pdf`, `Digital Signal Processing/301 Review/Topic 2.2 time transformations.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[LTI system]] · [[Convolution]] · [[DFT]] · [[DTFT]] · [[Fourier transform]] · [[Z-transform]] · [[Sampling theorem]] · [[Quantization]]
