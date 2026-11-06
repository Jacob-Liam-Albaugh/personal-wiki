---
type: paper
area: operators
areas: [operators, physics-informed]
source-ref: "Bhattacharya, Liu, Stuart, Trautner 2023, Multiscale Model. Simul. 21(2), 641-679"
tags: [operators, mechanics, ml]
authors: ["[[Kaushik Bhattacharya]]", "[[Burigede Liu]]", "[[Andrew M. Stuart]]", "[[Margaret Trautner]]"]
year: 2023
venue: "SIAM Multiscale Modeling & Simulation 21(2), 641-679"
file: "papers/PSL Reading Group/26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf"
---

# Learning Markovian homogenized models in viscoelasticity (Bhattacharya 2023)

**Summary**: For 1D Kelvin-Voigt (KV) viscoelasticity with a rapidly varying periodic microstructure, the homogenized constitutive law has memory, but for piecewise-constant media that memory is exactly a finite set of exponentially decaying hidden variables (a Markovian ODE system). The authors prove this, prove a neural network (RNN) with the same structure can approximate it, and show numerically that an RNN trained on cell-problem data reproduces fine-scale FEM at far lower cost. The same architecture also learns a 1D elasto-viscoplastic law.

**Authors**: Kaushik Bhattacharya, Burigede Liu, Andrew Stuart, Margaret Trautner · **Year**: 2023 · **File**: `papers/PSL Reading Group/26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`

Discussed in the PSL reading group on 2026-10-29.

---

## Problem

Fine-scale simulation of materials with rapidly varying features (scale $\epsilon\ll1$) is expensive. Homogenization removes $\epsilon$ but, in complex settings, only defines the effective constitutive model implicitly; the goal is to learn that model explicitly from localized fine-scale (unit-cell) simulations (source: `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`, abstract, p. 1).

Setup (p. 2, eq. 1.1): displacement $u^\epsilon$ solves
$$\rho\,\partial_t^2u^\epsilon=\nabla\cdot\sigma^\epsilon+f,\qquad \sigma^\epsilon=\Psi^\dagger_\epsilon\big(\nabla u^\epsilon,\partial_t\nabla u^\epsilon,\{\nabla u^\epsilon(x,\tau)\}_{\tau\in\mathcal T},x,t\big)$$
with initial data and zero Dirichlet boundary data. The constitutive map $\Psi^\dagger_\epsilon$ is causal: stress at time $t$ depends only on strain history up to $t$.

Why Markovian: a Markovian model is interpretable and cuts cost from $\mathcal O(|\mathcal T|^2)$ (general memory) to $\mathcal O(|\mathcal T|)$ (p. 3). In KV viscoelasticity the multiscale model has no memory, but the homogenized model does (fading memory, Sanchez-Palencia, p. 5).

Earlier work: [20] learns a non-causal homogenized law for crystal plasticity; [21] learns causal plasticity laws empirically. This paper supplies theory for [21]'s method in the linear 1D setting (p. 2).

## Method

### 1D Kelvin-Voigt model and homogenization

> [!definition] 1D KV viscoelasticity (inertia-free)
> $$\sigma^\epsilon=E^\epsilon\,\partial_xu^\epsilon+\nu^\epsilon\,\partial^2_{xt}u^\epsilon,\qquad -\partial_x\big(E^\epsilon\partial_xu^\epsilon+\nu^\epsilon\partial^2_{xt}u^\epsilon\big)=f,$$
> with $E^\epsilon(x)=E(x/\epsilon)$, $\nu^\epsilon(x)=\nu(x/\epsilon)$ 1-periodic elasticity and viscosity; weak form $q_{\nu^\epsilon}(\partial_tu^\epsilon,\varphi)+q_{E^\epsilon}(u^\epsilon,\varphi)=\langle f,\varphi\rangle$ with $q_\xi(u,w)=\int\xi\,\partial_xu\,\partial_xw\,dx$.
>
> (source: `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`, eqs. 2.1-2.2, pp. 8-9; $q_\xi$ is eq. 1.4, p. 7)

> [!definition] Homogenized coefficient (harmonic average in Laplace space)
> After Laplace transform in $t$, with $\hat a(s,y)=E(y)+\nu(y)s$, two-scale expansion gives the homogenized problem $-\partial_x(\hat a_0(s)\partial_x\hat u_0)=\hat f$ with
> $$\hat a_0(s)=\big\langle\hat a(s,y)^{-1}\big\rangle^{-1}=\Big(\int_0^1\frac{dy}{s\nu(y)+E(y)}\Big)^{-1}.$$
>
> (source: same file, eqs. 2.3-2.5, p. 9)

Large-$s$ expansion $\hat a_0(s)=\nu's+E'+\hat\kappa(s)$ with $\hat\kappa(s)\to0$, where
$$\nu'=\Big(\int_0^1\frac{dy}{\nu(y)}\Big)^{-1},\qquad E'=\frac{\int_0^1E(y)\nu(y)^{-2}dy}{\big(\int_0^1\nu(y)^{-1}dy\big)^2}$$
(p. 10; derivation in Appendix B.1, p. 33). Inverting the Laplace transform gives the homogenized constitutive law with a convolution memory:

> [!definition] Homogenized KV constitutive law
> $$\sigma_0(t)=E'\partial_xu_0(t)+\nu'\partial^2_{xt}u_0(t)+\int_0^t\kappa(t-\tau)\,\partial_xu_0(\tau)\,d\tau .$$
>
> (source: same file, eqs. 2.7-2.8, p. 10)

Remark 2.1 (p. 10): the homogenized solution is proved for $\rho=0$; it also holds when inertia is $\mathcal O(1)$ in $\epsilon$, but for $\rho>0$ is only valid for a subset of initial conditions (Remark 3.11).

### Target model class (generic Markovian form)

> [!definition] Markovian homogenized constitutive model
> Seek hidden variables $\xi\in C(\mathcal T;\mathbb R^r)$ and functions $\mathcal F,\mathcal G$ with
> $$\Psi_0\big(B(t),\partial_tB(t),\{B(\tau)\}_\tau,t\big)=\mathcal F\big(B(t),\partial_tB(t),\xi(t)\big),\quad \partial_t\xi=\mathcal G(\xi,B(t)),\quad \xi(0)=0 .$$
> $\mathcal F,\mathcal G$ are parameterised as feed-forward networks acting pointwise in space and time.
>
> (source: same file, eq. 1.3, p. 4)

### Theory (1D KV)

Proof strategy (p. 4): (i) approximate the material by a piecewise-constant one, (ii) homogenize it to get a Markovian description, (iii) show an RNN can learn it from cell data.

> [!theorem] Piecewise-constant approximation (Theorem 3.4, Lemma 3.5)
> For piecewise-continuous $E,\nu$ with finitely many discontinuities (Assumptions 3.1: $f\in L^2$, $E^\pm,\nu^\pm\in(0,\infty)$), for any $\delta>0$ there are piecewise-constant $E^{PC},\nu^{PC}$ with $\|u^{PC}_\epsilon-u_\epsilon\|_{\mathcal Z}<\delta$. It rests on the Lipschitz bound
> $$\|u_1-u_2\|_{\mathcal Z}\le C\big(\|\nu_1-\nu_2\|_\infty+\|E_1-E_2\|_\infty\big),$$
> with $C$ independent of $\epsilon$. Here $\mathcal Z=L^\infty(\mathcal T;L^2(\mathcal D))$.
>
> (source: same file, Theorem 3.4 and Lemma 3.5, p. 11; proofs Appendix A.1, pp. 24-27)

> [!theorem] Existence of exact Markovian parametrization (Theorem 3.6)
> For a piecewise-constant material with $L'+1$ pieces, $\Psi^\dagger_0$ equals
> $$\Psi_0^{PC}=E_0\,\partial_xu_0+\nu_0\,\partial^2_{xt}u_0-\sum_{\ell=1}^{L_0}\xi_\ell(t),\qquad \partial_t\xi_\ell=\beta_\ell\,\partial_xu_0-\alpha_\ell\,\xi_\ell,\quad\xi_\ell(0)=0,$$
> with $\theta^*=(E',\nu',L',\alpha,\beta)$, $\alpha_\ell>0$, $\beta_\ell\in\mathbb R$. The number of hidden variables is $L'$, one fewer than the number of pieces.
>
> (source: same file, Theorem 3.6, eqs. 3.4-3.5, p. 12; proof Appendix A.2, pp. 28-29)

Proof idea (Lemma A.3): for $L'+1$ pieces $\hat a_0=P(s)/Q(s)$ with $P$ of degree $L'+1$, $Q$ of degree $L'$; polynomial division gives $E'+\nu's-C(s)/Q(s)$, and partial fractions give $\hat a_0(s)=E'+\nu's-\sum_\ell\beta_\ell/(s+\alpha_\ell)$. All roots of $Q$ are real and negative: $Q$ has positive coefficients, and a nonzero imaginary part of a root would make $\mathrm{Im}\,Q\ne0$. Inverting gives $\sigma_0=E'\partial_xu_0+\nu'\partial_t\partial_xu_0-\sum_\ell\beta_\ell\int_0^t\partial_xu_0(\tau)e^{-\alpha_\ell(t-\tau)}d\tau$ (eq. A.7).

> [!theorem] Weak convergence of $u_\epsilon$ (Theorem 3.7, Corollaries 3.8-3.9)
> Under Assumptions 3.1, $u_\epsilon\rightharpoonup u_0$ in $W^{1,2}(\mathcal T;V)$ for $\rho=0$, hence $\|u_\epsilon-u_0\|_{\mathcal Z^2}<\eta$ for $\epsilon<\epsilon_{crit}$ (uses Francfort-Suquet [11]). Combined with Theorem 3.4: for any $\eta>0$ there are $L_{crit},\epsilon_{crit}$ such that for $L\ge L_{crit}$ piecewise-constant approximations satisfy $\|u_\epsilon-u_0^{PC}\|_{\mathcal Z^2}<\eta$ for all $\epsilon<\epsilon_{crit}$.
>
> (source: same file, Theorem 3.7, Cor. 3.9, eq. 3.9, p. 13)

So any multiscale 1D KV solution is approximated by a solution of a Markovian homogenized model (contribution 2, p. 7).

### RNN approximation

The exact model is linear: $\mathcal F^{PC}(b,c,r)=E'b+\nu'c-\langle\mathbf 1,r\rangle$ and $\mathcal G^{PC}(r,b)=-Ar+\beta b$, $A=\mathrm{diag}(\alpha_\ell)$ (eq. 3.10, p. 14). Replacing them with neural networks gives
$$\Psi_0^{RNN}=\mathcal F^{RNN}(b,c,\xi),\qquad\dot\xi=\mathcal G^{RNN}(\xi,b),\ \xi(0)=0\quad(\text{eq. 3.12}).$$
The hidden state is advanced by a forward Euler step; the architecture is not a standard LSTM: $\mathcal F,\mathcal G$ act pointwise in time and are the same at each step, hence "recurrent" (p. 13).

> [!theorem] RNN approximation of the constitutive law (Theorem 3.10)
> Let $\mathsf Z_R=\{w:\sup_t|w(t)|\le R\}$. Assume there are $\rho>0$, $B<\infty$ with $\rho<\min_\ell|\alpha_\ell|$ and $\max_\ell|\beta_\ell|\le B$. Then for every $\eta>0$ there is $\Psi_0^{RNN}$ of form (3.12) with
> $$\sup_{t\in\mathcal T,\ b,c\in\mathsf Z_R}\big|\Psi_0^{PC}(b,c,\{b\};\theta^*)-\Psi_0^{RNN}(b,c,\{b\})\big|<\eta .$$
>
> (source: same file, Theorem 3.10, p. 14; proof Appendix A.3, pp. 30-32)

Proof sketch (Prop. A.5): if $\mathcal F^{RNN},\mathcal G^{RNN}$ are $\delta$-uniformly close to $\mathcal F^{PC},\mathcal G^{PC}$, the hidden-state error $e_\xi=\xi^{PC}-\xi^{RNN}$ obeys $\dot e_\xi=-Ae_\xi+q(t)$ with $\|q\|\le\delta$. Young plus Gronwall give $\|e_\xi(t)\|<\delta/\rho$, hence output error $\le\delta+\sqrt{L'}\delta/\rho$. The compact-set version follows from the universal approximation theorem for RNNs [9].

What is not proved (p. 15): closeness of the PDE solutions $u_0^{PC}$ and $u_0^{RNN}$; existence and uniqueness of $u_0^{RNN}$ stay open because monotonicity of $\Psi^{RNN}_0$ in strain rate is hard to establish for a trained model and the networks may not be differentiable. All experiments therefore use $\rho>0$ (Remark 3.11).

### Training data and losses

Data: $N$ strain trajectories $(\partial_xu_0)_n$ drawn i.i.d. from a measure $\mu$ on $C(\mathcal T;\mathbb R)$, with strain rate and stress (eq. 3.14). Stress data come from the cell problem, or from the forced boundary problem of Lemma 3.12: $\partial_y\sigma=0$, $\sigma=E\partial_yu+\nu\partial^2_{ty}u$, $u(0,t)=0$, $u(1,t)=b(t)$, $u(y,0)=0$, which gives $\{\sigma(t)\}=\Psi_0^\dagger(b,\partial_tb,\{b\},t)$ (proof Appendix B.2, p. 33: $\hat\sigma=\hat a_0\hat b$).

> [!definition] Accessible loss (relative $L^2$)
> $$L_1=\frac1N\sum_{n=1}^N\frac{\|(\sigma_0)_n-(\hat\sigma_0)_n\|_{L^2(\mathcal T)}}{\|(\sigma_0)_n\|_{L^2(\mathcal T)}}$$
>
> (source: same file, eq. 3.16, p. 16)

> [!definition] Inaccessible loss (also uses the analytic hidden-variable rate $\dot\xi$)
> $$L_2=\frac1N\sum_{n=1}^N\Big(\frac{\|(\sigma_0)_n-(\hat\sigma_0)_n\|}{\|(\sigma_0)_n\|}+\frac{\|\dot\xi_n-\hat{\dot\xi}_n\|}{\|\dot\xi_n\|}\Big)$$
>
> (source: same file, eq. 3.17, p. 16)

$L_2$ needs $\xi$, which is known only when the 2-piece cell problem is solved analytically; it is used to understand training. Relative and absolute squared $L^2$ losses gave no significant difference (Remark 3.13).

### Extension: standard linear solid (SLS)

For the Maxwell-type SLS, the stress depends on strain and strain history (no strain-rate term), and $\hat a_0(s)=\big(\int_0^1\frac{s+E_2/\nu}{(E_1+E_2)s+E_1E_2/\nu}dy\big)^{-1}$ (D.3). For $L$ pieces,
$$\Psi_0^{PC}=E'\partial_xu_0-\sum_{\ell=1}^L\xi_\ell,\quad\partial_t\xi_\ell=\beta_\ell\partial_xu_0-\alpha_\ell\xi_\ell,\quad E'=\Big(\int_0^1\frac1{E_1+E_2}dy\Big)^{-1}$$
(D.5, p. 36). It has one more hidden variable than the KV case at the same number of pieces (Appendix D.3, pp. 36-37).

## Results

Settings: 1D, $\rho>0$, 2-piece media $E_1=1,E_2=3,\nu_1=0.1,\nu_2=0.2$ unless stated (Appendix C.1, p. 34). Networks $\mathcal F^{RNN},\mathcal G^{RNN}$: three internal SELU layers of 100 nodes separated by linear layers, then a final linear layer.

**RNN variants (Table 1, p. 17)**: A = inaccessible loss only; B = A as initialization, then accessible loss; C = accessible loss only; D = continuous media, accessible loss. Training (Appendix C.1): A: $N=400$, $dt=0.004$, $T=4$, 1500 epochs, batch 50. B: $N=200$ for 1500 epochs with $L_2$, then 1000 epochs with $L_1$. C: $N=500$, 3000 epochs.

**I. Surrogate quality (Figs 2-4, pp. 17-19)**: relative error measured by $e(t)=\|u^\epsilon(t)-u^{RNN}_0(t)\|/(\|u^\epsilon(t)\|+0.01)$ (eq. 4.1). Against an FEM reference (periodic cell width 0.04, $h=0.005$, $dt=0.1h^2$) with sinusoidal forcing $b(t)=0.1\sin2\pi t$ and integrated Brownian motion forcing, the RNN macroscale model (cell resolution $h_{cell}=0.04$ to $0.05$, $dt=0.4h_{cell}^2$) matches the fine-scale solution with errors "of the same order of magnitude" as the exact analytic homogenized model, at far lower cost. The paper gives errors as curves, not a table. The initial gap between homogenized and FEM solutions is from inertial effects (Remark 2.1), and grows as $E/\nu$ varies more across the cell (Fig. 4).

**II. Choice of training data (Figs 8, p. 21-22)**: strain paths are built by splitting $\mathcal T$ into 10 pieces, a balanced random walk for strain values at the breakpoints, and PCHIP interpolation. This spreads strain and strain-rate pairs evenly instead of strongly correlated (Fig. 8).

**III. Local minimizers and linearity (Fig. 5, p. 19-20)**: A and B recover the linear dependence of $\mathcal F$ and $\mathcal G$ in their arguments in the domain of interest. C is also a good surrogate but does not match the linear dependence of $\mathcal G$ on the hidden variable rate, attributed to local minimizers. With $\nu_2=2$ instead of $0.2$, C does recover the linear $\mathcal G$, but inertial effects then invalidate the homogenization benchmark.

**Continuous media (RNN D, Fig. 6, p. 20-21)**: $E(y)=2+\tanh\frac{y-0.5}{0.2}$, $\nu(y)=0.5+0.1\tanh\frac{y-0.5}{0.2}$; RNNs with 1, 2, 5, 10 hidden variables (500 data, 3000 epochs). Similar error for all, suggesting one hidden variable suffices here and that the remaining error is mainly from homogenization, not from piecewise-constant approximation.

**IV. Discretization robustness (Fig. 7, p. 20-21)**: RNNs A, B, C with strain rate as an input are more robust to changing the time step $dt$ than counterparts trained without strain-rate dependence (a wrong model form). The authors propose testing at other $dt$ as a check of model form.

**Number of hidden variables (Fig. 9, p. 21-22)**: claim that an $N$-piece material needs at least $N-1$ hidden variables. Error plateaus after 2 hidden variables for 3 pieces and 4 for 5 pieces. For 10 pieces it plateaus at 4 and again at 9; the 9 decay rates in the analytic law are $\alpha\approx1.83,2.92,4.44,5.13,8.18,9.29,11.3,15.30,18.41$ with a large gap between 5.13 and 8.18, so four hidden variables capture the slow part of the memory.

**Elasto-viscoplasticity (Figs 10-11, pp. 22-23)**: 1D law $\sigma=E(\partial_yu-\epsilon_p)$, $\dot\epsilon_p=\dot\epsilon_{p0}\,\mathrm{sign}(\sigma)(|\sigma|^n/\sigma_h)$ (eq. 4.2). An RNN with one hidden variable and the same architecture but no strain-rate input, trained on 400 trajectories (3000 epochs, absolute error), reproduces stress and plastic transitions; mean relative $L^2$ error $\approx7\%$, with test performance comparable to train.

## Limitations

As stated by the authors (pp. 6-7, 15, 24):
- Proven only for 1D linear KV (plus a derivation for SLS); the nonlinear PDE with the RNN constitutive law lacks existence, uniqueness and error theory.
- Homogenization is valid for inertial problems only for a subset of initial conditions; extending to significant inertial effects is open.
- The trained RNN is for fixed material parameters; learning material-parameter dependence is future work.
- Global optimality is not guaranteed (local minimizers, RNN C); reservoir-computing ideas giving convex problems are suggested.
- Choice of training measure $\mu$ is empirical; theory for it is "very important" future work.
- Higher-dimensional plasticity is supported only by [21] and the 1D elasto-viscoplastic example.

Wiki note: (1) Error results are given as plots, so exact figures (beyond the 7% plasticity figure) were not recorded here. (2) The inaccessible loss is used only where the 2-piece cell problem has a closed form, so the strongest results (A, B) rely on privileged hidden-state data not available for general media.

## Connections

- Operator view: the constitutive map $\Psi_0^\dagger$ takes a strain history to a stress history, i.e. it is an operator between function spaces. Rather than a DeepONet-style branch/trunk network ([[DeepONet (Lu 2021)]]), the paper learns it as a causal, pointwise-in-time recurrent model with hidden state. Contrast with the neural-operator approaches the paper cites as mesh-invariant (introduction, p. 6).
- Cites universal approximation results for operators ([6], Chen-Chen) in the literature review (p. 6), and the RNN universal approximation theorem [9] in the proof of Theorem 3.10.
- Related to hidden-variable / internal-variable models in continuum mechanics ([[Markovian constitutive model]]) and to physics-informed surrogates ([15], [14]) that put the differential operator into the loss (p. 6).
- Uses [[Homogenization]] (two-scale expansion, harmonic averaging) and the [[Homogenization]] to derive the memory kernel.
- Companion empirical work [21] (Liu, Kovachki, Li, Azizzadenesheli, Anandkumar, Bhattacharya, Stuart; learning plasticity) is not in the wiki.
- Wiki note: the reading-group copy of this paper may duplicate a copy elsewhere in the library (the same applies to [[DeepONet (Lu 2021)]], e.g. `papers/Operators/Karniadakis, Lu, Jin - DeepONets - Deep Operator Networks.pdf`); the coordinator will confirm.


**Sources**: `papers/PSL Reading Group/26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Markovian constitutive model]]
- [[Homogenization]]
- [[Kelvin-Voigt viscoelasticity]]
- [[Recurrent constitutive model]]
- [[Operator learning]]
- [[DeepONet (Lu 2021)]]
- [[Energy-based kernels for viscoelastic flow (Otto 2024)]]
