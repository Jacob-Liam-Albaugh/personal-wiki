---
type: lecture
area: dsp
source-ref: "Topic DSP.1, pp. 1-10"
course: ece438
lecture: DSP.1
tags: [signals]
---

# ECE438 DSP.1 - DT signals

**Summary**: Opening lecture of ECE 438: what a [[Discrete-time signal]] is, four ways to represent one, and its basic properties (periodicity, duration, energy, magnitude). Introduces the unit impulse, unit step and DT sinusoids, and shows that a DT sinusoid need not be periodic.

**File**: `Digital Signal Processing/Topic DSP.1 DT signals Jan 14, 2025.pdf`

---

## Topics
- **Definition (DSP.1.1)**: a signal is a physical quantity varying with time, space or other independent variables. It must be defined for every value of the independent variable (p. 2).
  - $x[n]=n^2u[n]$ is a 1-D function; $x[n]=n^2$ "when $n>0$" is not a function; $x[n,m]=n+m$ is 2-D.
  - Continuous independent variable: CT signal ($t\in\mathbb R$). Discrete: DT signal ($n,m\in\mathbb Z$).
  - A DT signal maps $\mathbb Z\to\mathbb R$; a digital signal maps $\mathbb Z\to\mathbb Z$ (p. 3).
  - The course is almost entirely DT, 1-D and 2-D.
- **Four representations (DSP.1.2, pp. 3-5)**: (1) a formula, which must be defined for all $n$ (e.g. $f[n]=n/3$ for $n>0$, else $0$); (2) a labelled stem plot; (3) a table of values; (4) a column vector in $\mathbb R^N$ or $\mathbb Z^N$ when the signal has $N$ nonzero points or is $N$-periodic.
- **Properties (DSP.1.3)**:
  - Periodic with period $N\in\mathbb Z$, $N>0$, if $x[n-N]=x[n]$ for all $n$. The fundamental period $N_0$ is the smallest such $N$. Example: $(-1)^n$ has period 2; $(-2)^n$ is not periodic (magnitude grows).
  - Finite duration if $x[n]=0$ outside some interval. A periodic signal has infinite duration; a finite-duration signal cannot be periodic.
  - Energy: $\mathcal E(x)=\|x\|_2^2$.
  - Magnitude: the max over $n$ of $|x[n]|$, the infinity norm; finite magnitude means bounded.
- **Special signals (DSP.1.4)**: unit impulse $\delta[n]$ (1 at $n=0$), unit step $u[n]$ (1 for $n\ge0$), sinusoid $\sin(\omega n+\phi)$.
- **Sinusoid properties (DSP.1.5)**: fastest oscillation is at $\omega=\pm\pi$, $\cos(\pi n)=(-1)^n$; frequencies $\omega$ and $\omega+2\pi$ give identical signals; not all DT sinusoids are periodic.

## Key results
> [!theorem] Energy
> $$\mathcal E(x)=\sum_{n=-\infty}^{\infty}|x[n]|^2$$
> Energy is always real; $|x[n]|^2=x[n]x^*[n]$ for complex $x$. (source: p. 7)

> [!theorem] When is $\cos(\omega n)$ periodic
> It is periodic iff $2\pi/\omega$ is rational, i.e. $\omega=2\pi k/m$ for integers: there must be integers $k,m$ with $k\cdot 2\pi/\omega = m\cdot 1$. The fundamental period is $\mathrm{LCM}(T_0,1)$ with $T_0=2\pi/\omega$. (source: p. 9)

Geometric sums to remember (p. 7):
$$\sum_{k=0}^{\infty}r^k=\frac1{1-r},\quad |r|<1$$
$$\sum_{k=0}^{n}r^k=\frac{1-r^{n+1}}{1-r},\quad r\ne1$$

## Examples
> [!example] Period of a sampled cosine (p. 9)
> $x(t)=\cos(\tfrac{4\pi}{5}t)$ has $T_0=2\pi/(4\pi/5)=2.5$. Sampling gives $x[n]=\cos(\tfrac{4\pi}5 n)$ with $N_0=\mathrm{LCM}(2.5,1)=5$.
> $x(t)=\cos t$ has period $2\pi$, but $x[n]=\cos n$ is not periodic: $\mathrm{LCM}(1,2\pi)$ does not exist.

## Connections
- Aside in the notes (p. 5): a [[Fourier transform]] can be seen as a rotation in $N$-dimensional signal space that preserves distance and angle; see [[DFT]].
- Power, energy and period are reviewed again in [[ECE438 301R 2.1 - Power and energy]] and [[ECE438 301R 2.3 - Period of a signal]].

**Sources**: `Digital Signal Processing/Topic DSP.1 DT signals Jan 14, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Discrete-time signal]] · [[ECE438 DSP.2 - DT systems]] · [[ECE438 DSP.3.A - DT frequency analysis 1]] · [[LTI system]] · [[DTFT]] · [[Sampling theorem]]
