---
type: paper
area: physics-informed
areas: [physics-informed, ml]
source-ref: "Otto, Oishi, Amaral, Brunton, Kutz, SSRN 4820054 preprint, Thms. 1-3, Prop. 1"
tags: [physics-informed, ml, mechanics, pde]
authors: ["[[Samuel E. Otto]]", "[[Cassio M. Oishi]]", "[[Fabio Amaral]]", "[[Steven L. Brunton]]", "[[J. Nathan Kutz]]"]
year: 2024
venue: "SSRN preprint 4820054, not peer reviewed"
file: "Physics Informed Architectures/Brunton, Otto, Kutz - ML in Viscoelastic Fluids via Kernel Embeding.pdf"
---

# Machine learning in viscoelastic fluids via energy-based kernel embedding (Otto 2024)

**Summary**: Builds, for a given viscoelastic stress model, a hyperparameter-free positive-definite kernel on flowfield snapshots whose RKHS squared norm equals the total mechanical energy. Kernel PCA with this kernel reconstructs the flow's energy far better than ordinary [[Principal component analysis]] on naively scaled state vectors.

**Authors**: Samuel E. Otto, Cassio M. Oishi, Fabio Amaral, Steven L. Brunton, J. Nathan Kutz · **Year**: 2024 **[unverified]**: the PDF carries no date; the year is inferred from the SSRN id · **File**: `Physics Informed Architectures/Brunton, Otto, Kutz - ML in Viscoelastic Fluids via Kernel Embeding.pdf`

---

## Problem

Learning and modal analysis (POD/PCA) depend on the inner product on state space. For Newtonian flow the natural choice is the kinetic-energy inner product. For viscoelastic flow, the state is $q=(u,c)$: velocity $u$ and conformation tensor $c$ (symmetric positive semidefinite). Mixed units and scales make the choice of metric ambiguous, and ad-hoc kernels carry hyperparameters (source: Otto.pdf, §1, pp. 2-3).

## Model and energy

Momentum and conformation equations (eqs. 2.1-2.4), with stress $\tau=-(1-\beta)\,s(c)$ and the general stress model
$$s(c)=-h_0(c)\,\mathrm{Wi}\,\big[h_1(c)\,c-h_2(c)\,I\big]+\kappa\,(c-I)^2$$
(eq. 2.6; Table 1 lists Oldroyd-B, Giesekus, FENE-CR, FENE-P, linear and nonlinear PTT). Total mechanical energy (eq. 2.7) is a kinetic term plus an elastic term weighted by
$$\theta=\frac{1-\beta}{\mathrm{Re}\,\mathrm{Wi}}.$$
Here $\beta$ is the viscosity ratio, Re the Reynolds number, Wi the Weissenberg number (p. 5).

## Method

An RKHS $\mathcal H$ on the finite-energy state space $\mathcal F$ is *energy-compatible* if
$$E(q)=\|\Phi(q)\|_{\mathcal H}^2=k(q,q)$$
(eq. 3.11). The induced metric needs only the kernel:
$$d_E(q_1,q_2)=\sqrt{k(q_1,q_1)-2k(q_1,q_2)+k(q_2,q_2)}.$$

> [!theorem] Theorem 1 (energy kernel, eqs. 3.14-3.16)
> Suppose $h(c)=-\mathrm{Wi}\,\mathrm{tr}[s(c)]+\text{const}=\sum_{i,p}c_{i,p}\,\mathrm{tr}\big(f_i(c)^{2p}\big)$ with $c_{i,p}\ge0$. Then
> $$\tilde k(c_1,c_2)=\sum_{i,p}c_{i,p}\,\mathrm{tr}\big[(f_i(c_1)f_i(c_2))^p\big]$$
> converges and
> $$k(q_1,q_2)=\tfrac12\int_\Omega\big[u_1\cdot u_2+\theta\,\tilde k(c_1,c_2)\big]\,dx$$
> is positive definite with $E(q)=k(q,q)$. The feature map is injective under mild extra conditions (a coefficient with $p\ge1$, $f_i$ injective, $p$ odd or $f_i\ge0$).
>
> (source: Otto.pdf, Thm. 1, pp. 6-7; proof in App. A)

Theorem 2: under the same conditions $(\mathcal F,d_E)$ is a complete metric space (p. 7). Worked examples:
- **Oldroyd-B** ($h=\mathrm{tr}\,c$, $f_0=\sqrt{x}$): $\tilde k=\mathrm{tr}(\sqrt{c_1}\sqrt{c_2})$ (eq. 3.19). The feature map is explicit, $\Psi(q)=\tfrac1{\sqrt2}\,(u,\sqrt\theta\,\mathrm{vec}\sqrt c)$ (eq. 3.20).
- **Giesekus**: adds $\alpha\,\mathrm{tr}[(c_1-I)(c_2-I)]$ (eq. 3.22).
- **FENE-CR, FENE-P, PTT**: kernels from series expansions of $h(c)$, valid only for constrained parameters (for example $0\le\varepsilon\le d^{-1}$ for nonlinear PTT, eq. 3.33) (pp. 7-9).

States at different $\theta$ are compared with a product kernel $\check k((q_1,\theta_1),(q_2,\theta_2))$ using $\sqrt{\theta_1\theta_2}$ (eq. 3.34, p. 9).

## Preimage and KPCA

Theorem 3 and Corollary 1 (pp. 10-11): the fields $y=(u,\sqrt c)$ (and other $(u,f_i(c)^{\otimes p})$) are recovered from $\Phi(q)$ by a bounded linear operator $R$. Hence they can be reconstructed linearly from truncated kernel principal components. Proposition 1 (eqs. 4.45-4.46) bounds the average reconstruction error by a constant times $\sum_{j>r}\sigma_j^2$, the tail of the covariance-operator spectrum.

KPCA uses the kernel matrix with the empirical [[Kernel integral operator]] eigenproblem (eqs. 4.42-4.44). Algorithm (§5.1, eqs. 5.50-5.54): center $K$, eigendecompose, take $Z_r=\sqrt{\Lambda_r}V_r^\top$, then fit an affine reconstruction $\hat y=r_0+Rz_r$ by least squares. Ordinary PCA is KPCA with the $L^2$ inner-product kernel.

Three error metrics (eqs. 5.55-5.57): $E_F$ (Frobenius), $E_E$ (error in total energy, which can vanish for different fields), $E_{\mathcal H}$ (squared RKHS distance over total energy, the principled one).

## Results

Lid-driven cavity on a $80\times80$ grid with lid velocity $16x^2(1-x)^2\sin(\pi t)$ (eq. 5.47), $\Delta t=10^{-5}$, log-conformation stabilization (pp. 11-12).
- **Oldroyd-B** (Figs. 3-5): ordinary PCA wins in $E_F$ as expected, but when $\theta\ne1$ the Oldroyd-B kernel gives lower $E_{\mathcal H}$ and $E_E$. With 2 modes, KPCA tracks total energy over time; PCA fails, most for small $\theta$. At $\theta=1$ the two methods are nearly identical.
- **Nonlinear models** (Figs. 6-10; FENE-P $L^2=5$, nonlinear PTT $\varepsilon=0.5$, Giesekus $\alpha=1$): the matching kernel helps most for few modes; at intermediate mode counts the Oldroyd-B kernel is sometimes slightly better. The benefit grows with the nonlinearity parameters ($1/L^2$, $\varepsilon$) and vanishes in the Oldroyd-B limit (Fig. 9, p. 17).

## Limitations and caveats

The authors note the choice is only partially resolved: other energy-compatible kernels may exist (p. 3). Giesekus experiments at large $\alpha$ were not run due to numerical difficulty (p. 18). Only one benchmark flow is tested. Wiki note: the paper is an unreviewed preprint, and the lid-driven cavity is a benchmark rather than an application.

## Connections

- Physics enters through the metric, not a loss term: a different route in [[Physics-informed machine learning]] than [[PINN]] residual losses.
- Generalizes energy-inner-product POD ([[Principal component analysis]], [[Proper orthogonal decomposition]]) via [[Kernel methods]] and [[RKHS]].
- Viscoelastic constitutive models also appear in [[Kelvin-Voigt viscoelasticity]] and [[Markovian homogenized viscoelasticity (Bhattacharya 2023)]]; compare [[Markovian constitutive model]].
- Compare [[Navier-Stokes equations]] (the Newtonian limit).

%% refs:start %%
**Cites in this wiki**: [[SINDy autoencoders (Champion 2019)]]
%% refs:end %%

**Sources**: `Physics Informed Architectures/Brunton, Otto, Kutz - ML in Viscoelastic Fluids via Kernel Embeding.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Kernel methods]] · [[RKHS]] · [[Kernel integral operator]] · [[Principal component analysis]] · [[Proper orthogonal decomposition]]
- [[Physics-informed machine learning]] · [[Navier-Stokes equations]] · [[Kelvin-Voigt viscoelasticity]] · [[Markovian constitutive model]]
