---
type: paper
area: symmetry
areas: [symmetry, ml]
source-ref: "Ling, Kurzawski, Templeton, J. Fluid Mech. 807:155-166, 2016"
tags: [ml, symmetry, pde]
authors: ["[[Julia Ling]]", "[[Andrew Kurzawski]]", "[[Jeremy Templeton]]"]
year: 2016
venue: "J. Fluid Mech. 807, 155-166; doi 10.1017/jfm.2016.615"
file: "Symmetries/Ling - Reynolds Turbulence Modelling DNN with Embedded Invariance.pdf"
---

# Tensor basis NN turbulence (Ling 2016)

**Summary**: A tensor basis neural network (TBNN) predicts the RANS Reynolds-stress anisotropy tensor with Galilean and rotational invariance built into the architecture. It beats linear and quadratic eddy-viscosity models on two held-out flows and a plain MLP on the duct.

**Authors**: Julia Ling, Andrew Kurzawski, Jeremy Templeton · **Year**: 2016 · **File**: `Symmetries/Ling - Reynolds Turbulence Modelling DNN with Embedded Invariance.pdf`

---

## Problem

RANS closure needs the Reynolds-stress anisotropy

$$b_{ij}=\frac{\overline{u'_iu'_j}}{2k}-\frac{\delta_{ij}}{3}$$

as a function of the mean strain rate $S$ and rotation rate $R$, non-dimensionalised by $k$ and $\epsilon$. Eddy-viscosity models are linear or quadratic in $S$. Realizability is enforced by post-processing, not by the network (source: §2, eq. 2.1).

## Invariance by construction

Pope's (1975) integrity basis writes $b$ as a sum of ten tensors times scalar functions of five invariants (source: eq. 2.2):

$$b=\sum_{n=1}^{10} g^{(n)}(\lambda_1,\dots,\lambda_5)\,T^{(n)}$$

with $T^{(1)}=S$, $T^{(2)}=SR-RS$, and eight more in eq. 2.3. The invariants (source: eq. 2.4):

$$\lambda_1=\mathrm{Tr}(S^2),\quad \lambda_2=\mathrm{Tr}(R^2)$$

$$\lambda_3=\mathrm{Tr}(S^3),\quad \lambda_4=\mathrm{Tr}(R^2S)$$

$$\lambda_5=\mathrm{Tr}(R^2S^2)$$

Any $b$ of this form is rotation invariant, so the network only learns the scalar coefficients $g^{(n)}$.

## Architecture

- Invariant input layer: $\lambda_1,\dots,\lambda_5$, feeding hidden layers.
- The last hidden layer has 10 nodes, giving $g^{(n)}$.
- A tensor input layer holds the ten $T^{(n)}$. The two are merged by elementwise product and summed to give $b$.
- Hyperparameters were set by Bayesian optimisation with Spearmint (a [[Gaussian process]] method):
  - TBNN: 8 hidden layers of 30 nodes, learning rate $2.5\times10^{-7}$.
  - Baseline MLP: 10 layers of 10 nodes, learning rate $2.5\times10^{-6}$, 9 inputs from $S$ and $R$.
- Leaky ReLU activations; ensemble of 20 networks, about 200 CPU hours each.

## Data

Nine flows with RANS $k$-$\epsilon$ inputs and DNS/LES labels.

- Train (6): duct at $Re_b=3500$; channel at $Re_\tau=590$; perpendicular jet in crossflow; inclined jet in crossflow; square cylinder; converging-diverging channel.
- Validation: wall-mounted cube.
- Test: duct at $Re_b=2000$ and wavy wall at $Re=6850$.

## Results

RMSE of $b$ (source: Table 1; MLP row alignment is my reading from the text):

| Flow | LEVM | QEVM | TBNN | MLP |
|---|---|---|---|---|
| Duct | 0.25 | 0.20 | 0.14 | 0.31 |
| Wavy wall | 0.18 | 0.11 | 0.08 | 0.09 |

- TBNN RMSE is 44% and 30% below LEVM and QEVM on the duct, and 56% and 27% below on the wavy wall.
- Leave-one-out over the six training flows: TBNN beat LEVM in all 6, with 30% average RMSE reduction.
- A posteriori: injecting TBNN stresses into SIERRA Fuego (residuals below $10^{-7}$ for momentum and continuity, $10^{-4}$ for turbulence quantities) predicts duct corner vortices, slightly overpredicted, and wavy-wall separation, smaller than DNS. Using the DNS $b$ gives the upper limit.
- Quadratic model coefficients quoted: $C_1=-0.1$, $C_2=0.1$, $C_3=0.26$.

## Caveats

A broader training set is needed, and the TBNN is not queried every solver iteration.

## Wiki note

This is hard-wired [[Equivariance]] via an invariant function basis rather than a symmetric layer type, an alternative to the group-convolution route of [[Group equivariant CNN]] and [[e3nn]].


%% refs:start %%
**Cited by in this wiki**: [[Operator learning review (Kovachki 2024)]], [[PINNs (Raissi 2019)]], [[SINDy delay autoencoders (Bakarji 2022)]]
%% refs:end %%

**Sources**: Ling et al. PDF (§2-5, Table 1).
**Last updated**: 2026-11-06

---

## Related pages
- [[Equivariance]]
- [[Gaussian process]]
- [[Group equivariant CNN]]
- [[e3nn]]
- [[Rotation augmentation for CNNs (Quiroga 2018)]]
