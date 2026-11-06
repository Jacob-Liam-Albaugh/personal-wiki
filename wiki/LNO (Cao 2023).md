---
type: paper
area: operators
areas: [operators, math]
source-ref: "Cao, Goswami, Karniadakis 2023, arXiv:2303.10528v2, eqs. 8-18"
tags: [operators, ml, pde]
authors: ["[[Qianying Cao]]", "[[Somdatta Goswami]]", "[[George Em Karniadakis]]"]
year: 2023
venue: "arXiv:2303.10528v2 [cs.LG], preprint submitted to Elsevier, 30-31 May 2023"
file: "Operators/Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf"
---

# LNO: Laplace Neural Operator (Cao 2023)

**Summary**: The paper replaces the Fourier-domain kernel of the [[FNO]] with a kernel written in the [[Laplace transform]] domain in pole-residue form, so that one "Laplace layer" produces both a transient response (from learned system poles) and a steady-state response (from the input's Fourier modes). On three ODEs and three PDEs with train/test inputs of different form, one Laplace layer beats a four-layer FNO.

**Authors**: Qianying Cao, Somdatta Goswami, George Em Karniadakis (Dalian Univ. of Technology; Brown Univ.) · **Year**: 2023 (arXiv v2 dated 30 May 2023; the file is the preprint) · **File**: `Operators/Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf`

Wiki note: the file name lists Karniadakis first, but the PDF's author order is Cao, Goswami, Karniadakis (Karniadakis is corresponding author), so the slug uses Cao. The PDF carries no journal venue; a later journal version may exist **[unverified]**.

---

## Problem

(source: Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf, §1, pp. 1-3)

- The [[FNO]] (FNO) parameterizes the kernel integral operator in Fourier space. The authors list its bottlenecks: the Fourier transform does not exist for some signals, cannot handle unstable systems, and has no term for initial values (eq. 1), so it is poorly suited to initial-value problems, transient responses and non-periodic signals.
- The Laplace transform carries an exponential convergence factor, $s=\sigma+i\omega$, and its derivative rules include initial conditions (eqs. 3-4). The goal is a neural operator for time-dependent ODE/PDE solution maps that captures transient plus steady-state response and is more interpretable.
- Setting: $\Omega\subset\mathbb{R}^D$ bounded open, $X,Y$ separable Banach spaces, $\mathcal{G}:X\to Y$ the solution operator of a time-dependent PDE, approximated by $\mathcal{G}_\theta$ trained on i.i.d. pairs $\{f_j,u_j\}_{j=1}^N$ (p. 4).

## Method

**Architecture** (Fig. 1, §2.1, pp. 3-4). Lift $f(t)\in\mathbb{R}^{d_x}$ to $v(t)\in\mathbb{R}^{d_z}$ with a shallow network $P$; apply a Laplace layer plus a local linear map $W$; project back with a shallow network $Q$. This is the [[Neural operator]] layer form with a [[Kernel integral operator]]:

> [!definition] LNO layer and kernel integral operator
> $$u(t)=\sigma\big((\kappa(f;\phi)*v)(t)+Wv(t)\big),$$
> $$(\kappa(f;\phi)*v)(t)=\int_D \kappa_\phi\big(t,\tau,f(t),f(\tau);\phi\big)\,v(\tau)\,d\tau .$$
> Dropping the dependence on $f$ and imposing $\kappa_\phi(t,\tau)=\kappa_\phi(t-\tau)$ gives a convolution, $\int_D\kappa_\phi(t-\tau)v(\tau)\,d\tau$.
>
> (source: Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf, eqs. 5-7, p. 4)

**Laplace-domain kernel in pole-residue form** (§2.2, pp. 4-6). Taking the Laplace transform of the convolution gives a product, and the kernel is parameterized by trainable poles and residues. See [[LNO#Pole-residue method|pole residue method]].

> [!definition] Pole-residue kernel
> $$U(s)=K_\phi(s)V(s),\qquad K_\phi(s)=\sum_{n=1}^{N}\frac{\beta_n}{s-\mu_n},$$
> with trainable parameters $\theta=(\mu_1,\dots,\mu_N,\beta_1,\dots,\beta_N)$: system poles $\mu_n$ and residues $\beta_n$ (complex-valued in general).
>
> (source: Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf, eqs. 8-9, pp. 4-5)

The excitation $v(t)$ (period $T$) is expanded in a Fourier series, $v(t)=\sum_{\ell=-\infty}^{\infty}\alpha_\ell e^{i\omega_\ell t}$, with $\omega_\ell=\ell\omega_1$ (eq. 10), so $V(s)=\sum_\ell \alpha_\ell/(s-i\omega_\ell)$ (eq. 11). The product $K_\phi V$ is then re-expanded into partial fractions:

> [!theorem] Pole-residue response
> $$U(s)=\sum_{n=1}^{N}\frac{\gamma_n}{s-\mu_n}+\sum_{\ell=-\infty}^{\infty}\frac{\lambda_\ell}{s-i\omega_\ell},$$
> with residues from the residue theorem
> $$\gamma_n=\lim_{s\to\mu_n}(s-\mu_n)U(s)=\beta_n V(\mu_n),\quad V(\mu_n)=\sum_\ell\frac{\alpha_\ell}{\mu_n-i\omega_\ell},$$
> $$\lambda_\ell=\lim_{s\to i\omega_\ell}(s-i\omega_\ell)U(s)=\alpha_\ell K_\phi(i\omega_\ell),\quad K_\phi(i\omega_\ell)=\sum_n\frac{\beta_n}{i\omega_\ell-\mu_n}.$$
> Inverse transform:
> $$u_1(t)=\sum_{n=1}^{N}\gamma_n e^{\mu_n t}+\sum_{\ell=-\infty}^{\infty}\lambda_\ell e^{i\omega_\ell t}.$$
> The first sum is the transient response (system poles); the second is the steady-state response (excitation poles).
>
> (source: Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf, eqs. 12-18, pp. 5-6)

The paper presents this as a derivation via the standard pole-residue method (refs. [6,7] in the PDF), not as a separately stated theorem. In practice the series over $\ell$ is truncated; the "Mode" columns of Table A.1 are the numbers of retained poles/modes (the paper does not spell out the discretization).

**LNO vs FNO** (p. 6):
1. FNO's kernel is parameterized by $\theta=(K_\phi(i\omega_1),\dots,K_\phi(i\omega_L))$ in the frequency domain; LNO's by $(\mu_n,\beta_n)$ in the Laplace domain.
2. FNO yields the steady-state response only; LNO yields transient plus steady-state.

Training/eval details (§3, p. 6): relative $L^2$ test error, mean and std over five independent trainings. LNO and FNO in PyTorch; GRU baseline in TensorFlow (ODE cases only, since GRU suits sequences). Training and test inputs deliberately differ in form to probe generalization.

## Results

(source: same file, §3, Figs. 2-8, Tables A.1-A.2, pp. 6-16)

Setup: $N_{train}=200$ (amplitudes $A\in[0.05,10]$, step 0.05), $N_{vali}=50$, $N_{test}=130$ for all cases. ODEs are solved with MATLAB ode45. Architectures: LNO has 1 Laplace layer; FNO has 4 Fourier layers (Table A.1). GRU has 1 hidden layer, width 10 (20 for Lorenz $\rho=10$).

| Case | Operator | Train input / test input | Reported outcome |
|---|---|---|---|
| Duffing, $\ddot x+c\dot x+x+x^3=f$, $c=0$ and $0.5$ | $f\to x$ | $A\sin 5t$ / $Ae^{-0.05t}\sin 5t$; 2048 pts, $\Delta t=0.01$ | LNO beats FNO both cases, most for $c=0$; LNO beats GRU for $c=0$, GRU beats LNO for $c=0.5$ (p. 8) |
| Driven pendulum, $\ddot x+c\dot x+\sin x=f$ | $f\to x$ | same as Duffing | LNO beats FNO and GRU for $c=0$ (p. 11); FNO generalization gap much larger |
| Forced Lorenz, $\rho=5,10$, $\sigma=10,\beta=8/3$ | $f\to x$ | same | LNO more accurate, more so at $\rho=10$ where response has two patterns (p. 13) |
| Euler-Bernoulli beam $EI\,y_{xxxx}+\rho A\,y_{tt}=f$ | $f(x,t)\to y(x,t)$; 51x17 grid | $Ae^{-0.05x}(1-10^2)\sin 10t$ / $Ae^{-x}(1-10^2)\sin 10t$ | LNO errors "more than an order of magnitude smaller" than FNO (p. 13) |
| Diffusion $Dy_{xx}-y_t=f$, $D=1$ | $f\to y$; 25x80 grid | $Ae^{-0.05t}(1-\pi^2)\sin\pi x$ / $Ae^{-t}(1-\pi^2)\sin\pi x$ | LNO errors "two orders of magnitude smaller" than FNO (p. 16) |
| Reaction-diffusion $Dy_{xx}+ky^2-y_t=f$, $D=k=0.01$ | $f\to y$; 20x40 grid | two-term sources, $A\in[0.14,9.09]$ for test | LNO smaller error than FNO (nonlinear, p. 16) |

Approximate test relative $L^2$ errors read off the Fig. 3 markers (p. 8; the text gives no table, so these are eyeball values, mean over five runs, **[unverified to ~0.02]**):

| Case | LNO | FNO | GRU |
|---|---|---|---|
| Duffing $c=0$ | ~0.24 | ~0.76 | ~0.66 |
| Duffing $c=0.5$ | ~0.13 | ~0.27 | ~0.02 |
| Pendulum $c=0$ | ~0.23 | ~0.54 | ~0.38 |
| Pendulum $c=0.5$ | ~0.15 | ~0.24 | ~0.03 |
| Lorenz $\rho=5$ | ~0.01 | ~0.19 | ~0.00 |
| Lorenz $\rho=10$ | ~0.14 | ~0.46 | ~0.41 |
| Beam | ~0.01 | ~0.43 | n/a |
| Diffusion | ~0.00 | ~0.12 | n/a |
| Reaction-diffusion | ~0.11 | ~0.26 | n/a |

Wiki note: on these readings GRU is best for Lorenz $\rho=5$ as well as for both damped ODE cases, while the paper's summary only says LNO beats GRU for undamped and multi-pattern systems.

Other stated findings:
- If train and test input forms are the same, LNO and FNO accuracy are "very similar" (p. 17).
- LNO's accuracy depends on batch size, and it showed higher run-to-run std in the undamped Duffing case (p. 8).
- With zero damping a transient always exists, which is why LNO's gain is largest there (p. 8).

## Limitations

As stated by the authors (p. 17): the pole-residue formulation is exact only when the layer input $v(t)$ is the source term, because the convolution then has physical meaning. If the input is an initial condition, the convolution has no physical meaning and LNO does not do significantly better than FNO; they leave this to future work.

Wiki notes (not claimed in the paper):
- The abstract claims "exponential convergence" but no convergence-rate analysis or experiment on it appears in the text.
- The comparison gives FNO four layers vs one Laplace layer and uses different widths/modes per case (Table A.1); error bars come from five trainings only, and test inputs are a decaying variant of the training family, so "generalization" is tested on a narrow shift.
- No comparison against [[DeepONet]] despite its mention in the intro, and no discretization-invariance experiment although §2 asserts neural operators are [[Discretization invariance|discretization invariant]].
- Linear PDE gains (beam, diffusion) reflect that the test problems are linear systems whose exact solution is in pole-residue form; the nonlinear gain is much smaller.

## Connections

- Direct modification of [[FNO (Li 2021)]]: same lift / layer / project skeleton, but the Fourier multiplier $K_\phi(i\omega_\ell)$ is replaced by the rational function $\sum_n\beta_n/(i\omega_\ell-\mu_n)$ plus a transient term.
- Fits the integral-kernel view of the general [[Neural operator]] in [[Neural operator (Kovachki 2022)]] and the architecture taxonomy in [[Operator learning review (Kovachki 2024)]]. It is a member of the family [[LNO]].
- Motivated by DeepONet's universality background ([[DeepONet (Lu 2021)]], [[Universal approximation for operators]]); no approximation theory for LNO itself is given.
- Mathematical background in [[Laplace transform]] and [[LNO#Pole-residue method|pole residue method]] (structural dynamics literature, refs. [6,7]).

%% refs:start %%
**Cites in this wiki**: [[DeepONet (Lu 2021)]], [[FNO (Li 2021)]]
%% refs:end %%

**Sources**: `Operators/Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Operator learning]]
- [[Neural operator]]
- [[FNO]]
- [[LNO]]
- [[Laplace transform]]
- [[Kernel integral operator]]
- [[Discretization invariance]]
- [[DeepONet]]
- [[Universal approximation for operators]]
- [[FNO (Li 2021)]]
- [[Neural operator (Kovachki 2022)]]
- [[DeepONet (Lu 2021)]]
- [[Operator learning review (Kovachki 2024)]]
