---
type: paper
area: operators
areas: [operators, ml]
source-ref: "Lu, Jin, Pang, Zhang, Karniadakis 2021, Nat. Mach. Intell. 3, 218-229"
tags: [operators, ml]
authors: ["[[Lu Lu]]", "[[Pengzhan Jin]]", "[[Guofei Pang]]", "[[Zhongqiang Zhang]]", "[[George Em Karniadakis]]"]
year: 2021
venue: "Nature Machine Intelligence 3, 218-229"
file: "PSL Reading Group/26.10.22 - DeepONets.pdf"
---

# Learning nonlinear operators via DeepONet (Lu 2021)

**Summary**: Extends the Chen-Chen universal approximation theorem for operators to deep networks and uses it to design DeepONet, a branch net (encodes the input function sampled at sensors) plus a trunk net (encodes the output location) merged by a dot product. On 16 test problems (explicit operators, deterministic and stochastic ODEs/PDEs) it generalises far better than FNN, ResNet and Seq2Seq baselines and shows exponential-then-polynomial error decay in training-set size.

**Authors**: Lu Lu, Pengzhan Jin, Guofei Pang, Zhongqiang Zhang, George Em Karniadakis · **Year**: 2021 · **File**: `PSL Reading Group/26.10.22 - DeepONets.pdf`

Discussed in the PSL reading group on 2026-10-22.

---

## Problem

Learn an operator $G: u \mapsto G(u)$ from a function space $V$ into another function space, where $G(u)(y)\in\mathbb{R}$ is the value of the output function at a point $y$ (source: `26.10.22 - DeepONets.pdf`, p. 2). Operators can be explicit (integral, Laplace/Legendre transform, fractional derivatives) or implicit (solution operators of ODEs/PDEs/SDEs).

- Prior neural approaches for dynamical systems (RNNs, ResNets, neural ODEs, neural jump SDEs) predict the evolution of one specific system, not the response to new unseen input signals (p. 1).
- CNN image-to-image maps need the input function evaluated at fixed grid locations (p. 1); graph kernel networks and moving-least-squares CNNs do not learn general nonlinear operators (p. 1).
- The generic "concatenate $[u(x_1),\dots,u(x_m),y]$ into one network" baseline (FNN/ResNet) has no structure suited to the two different kinds of input (p. 3).
- Training setup is deliberately weak: the only requirement is that the $m$ sensor locations $\{x_j\}$ are the same for every input function $u$ (not necessarily a lattice); output locations $y$ are unconstrained and may differ per $u$ (p. 3, Fig. 1b).
- The universal approximation theorem controls only approximation error, not optimisation or generalisation error, which "are often dominant" in practice (p. 3).

## Method

### Theory

> [!theorem] Universal approximation theorem for operators (Chen-Chen; Theorem 1 of the paper)
> Let $\sigma$ be continuous and non-polynomial, $X$ a Banach space, $K_1\subset X$, $K_2\subset\mathbb{R}^d$ compact, $V\subset C(K_1)$ compact, and $G: V\to C(K_2)$ a continuous operator. Then for any $\epsilon>0$ there are $n,p,m\in\mathbb{Z}_+$, constants $c_i^k,\xi_{ij}^k,\theta_i^k,\zeta^k\in\mathbb{R}$, $w_k\in\mathbb{R}^d$, $x_j\in K_1$ with
> $$\Big| G(u)(y) - \sum_{k=1}^{p}\sum_{i=1}^{n} c_i^k\,\sigma\Big(\sum_{j=1}^{m}\xi_{ij}^k u(x_j)+\theta_i^k\Big)\,\sigma(w_k\cdot y+\zeta^k)\Big| < \epsilon$$
> for all $u\in V$, $y\in K_2$. The first factor is the "branch", the second the "trunk".
>
> (source: `26.10.22 - DeepONets.pdf`, Theorem 1, eq. 1, p. 2)

See [[Universal approximation for operators]]. Theorem 1 gives no guidance on learning efficiently: it covers approximation error only (p. 3).

> [!theorem] Generalized universal approximation theorem for operators (Theorem 2)
> Under the same compactness and continuity assumptions, for any $\epsilon>0$ there exist $m,p\in\mathbb{Z}_+$, continuous $g:\mathbb{R}^m\to\mathbb{R}^p$, $f:\mathbb{R}^d\to\mathbb{R}^p$ and $x_1,\dots,x_m\in K_1$ such that
> $$\big| G(u)(y) - \langle g(u(x_1),\dots,u(x_m)),\, f(y)\rangle \big| < \epsilon \quad \forall u\in V,\ y\in K_2,$$
> with $\langle\cdot,\cdot\rangle$ the dot product in $\mathbb{R}^p$. $g$ and $f$ can be any network class satisfying the classical universal approximation theorem (stacked/unstacked FNNs, ResNets, CNNs). Proof in Supplementary Section 2.
>
> (source: `26.10.22 - DeepONets.pdf`, Theorem 2, p. 3)

### Architecture

> [!definition] DeepONet (stacked and unstacked)
> A trunk net takes $y$ and outputs $[t_1,\dots,t_p]^T\in\mathbb{R}^p$. Branch net(s) take $[u(x_1),\dots,u(x_m)]^T$ and output scalars $b_k$. Then
> $$G(u)(y)\approx\sum_{k=1}^{p} b_k\big(u(x_1),\dots,u(x_m)\big)\,t_k(y) + b_0 .$$
> **Stacked**: $p$ separate branch nets, each outputting one scalar $b_k$ (Fig. 1c). **Unstacked**: one branch net with $p$ outputs (Fig. 1d); equivalent to a stacked net with all branch nets sharing parameters.
>
> (source: `26.10.22 - DeepONets.pdf`, p. 3 and Fig. 1, with bias $b_0\in\mathbb{R}$ added in the last stage)

Details stated in the paper (p. 3-4):
- Theorem 1's network is a stacked DeepONet with a one-layer trunk of width $p$ and one-hidden-layer branches of width $n$; DeepONet replaces these shallow nets with deep ones.
- The trunk applies an activation on its last layer ($t_k=\sigma(\cdot)$), so the model can be read as a trunk net whose last-layer weights are produced by branch nets.
- Bias is not in Theorem 1, but adding bias to the branch nets and the global $b_0$ lowers generalisation error (Fig. 2a).
- Loss: mean squared error between the true $G(u)(y)$ and the prediction on inputs $([u(x_1),\dots,u(x_m)],y)$. Implemented in DeepXDE.
- All sub-networks in the paper are plain FNNs; structured inputs could use convolutional layers in the branch (equispaced sensors) or attention.
- Inductive bias: $G(u)(y)$ has two independent inputs, so separate branch/trunk nets match the prior. DeepONet is also read as a conditional model, with embedding of $u$ and embedding of $y$ merged by a dot product (p. 4).
- Input-function representations used: values at sensors, spectral expansions (poly-fractonomials, Legendre, Zernike), Gaussian random fields (GRF), images, and Karhunen-Loeve coefficients for random processes (pp. 4-6, 9).

### Data

A data point is a triplet $(u, y, G(u)(y))$; one $u$ may appear with many $y$ values. For each $u$ the paper samples $P$ random $y$ points, so dataset size $=P\times\#u$ (p. 5).

### Sensor-count theorem

For the ODE operator $\frac{d}{dx}s=g(s,u,x)$, $s(a)=s_0$ (Problem 1, eq. 2), the paper approximates $u$ by its piecewise-linear interpolant $u_m$ on $m+1$ equispaced sensors and defines $\kappa(m,V)\ge\max_x|u-u_m|$ with $\kappa\to0$ as $m\to\infty$ (eq. 3). For a GRF with Gaussian kernel it states $\kappa(m,V)\sim 1/(m^2 l^2)$ (as read from the text extraction, p. 5).

> [!theorem] Sensor count for ODE operators (Theorem 3)
> Assume $g$ is Lipschitz in $s$ and $u$ with constant $c$. If $m$ is large enough that $c(b-a)\,\kappa(m,V)\,e^{c(b-a)}<\epsilon$, then for any $d\in[a,b]$ there exist $W_1\in\mathbb{R}^{n\times(m+1)}$, $b_1\in\mathbb{R}^{m+1}$, $W_2\in\mathbb{R}^{K\times n}$, $b_2\in\mathbb{R}^K$ with
> $$\big\|G(u)(d) - \big(W_2\,\sigma(W_1[u(x_0)\cdots u(x_m)]^T+b_1)+b_2\big)\big\|_2<\epsilon\quad\forall u\in V.$$
>
> (source: `26.10.22 - DeepONets.pdf`, Theorem 3, p. 5; proof in Supplementary Section 5)

So the number of sensors needed to reach accuracy $\epsilon$ is set by how smooth $V$ is, via $\kappa(m,V)$.

## Results

All training data come from numerical solvers, so DeepONet is a surrogate and "cannot be better than the numerical solvers in terms of accuracy" (p. 10). Sixteen problems are studied: 4 explicit operators, 8 deterministic ODE/PDE operators, 4 stochastic operators (p. 5).

**Antiderivative (Problem 1.A, eq. 4)** (pp. 5-6, Fig. 2a):
- Best FNN (depth 2, width 2,560, lr 0.001): test mse $\approx7\times10^{-5}$. Best ResNet (1 block, width 20): $\approx1\times10^{-4}$.
- DeepONets have much smaller generalisation error than FNN, ResNet and Seq2Seq. Seq2Seq is similar to stacked DeepONet; with ~10x more data it approaches unstacked DeepONet. Seq2Seq needs outputs on a dense grid ($P=100$) while DeepONet used $P=1$; Seq2Seq training costs more than 7x as much.
- Bias lowers train and test error and training variance. Unstacked beats stacked (smaller generalisation error, fewer parameters, less memory). Unstacked with bias is best and is used from then on.

**Distribution shift between training and test function spaces (Fig. 2c)**: trained on GRFs of correlation length $l$, tested on GRF with $l=0.1$. Test error grows with the 2-Wasserstein distance between the two GRF laws; "test m.s.e. grows exponentially with respect to the W2 metric" (p. 6).

**Fractional operators (Fig. 2d,e)**:
- 1D Caputo derivative (Problem 2): input spaces poly-fractonomials, Legendre, GRF all give small generalisation error; GRF slightly larger. $\hat y=[y,\alpha]$ goes into the trunk.
- 2D Riesz fractional Laplacian on the unit disk (Problem 3): inputs from Zernike polynomials. A CNN encoder-decoder is slightly more accurate than DeepONet because it exploits the lattice structure, but DeepONet is more flexible for unstructured data (pp. 6-7).

**Fast learning (Fig. 3, gravity pendulum, Problem 1.B, $k=1$, $T=3$)** (p. 7):
- Test and generalisation errors of DeepONet decay exponentially for small training sets, then polynomially; the polynomial rates exceed the classical $x^{-0.5}$ rate. Fitted rates in the figure: $e^{-x/1400}$ then $x^{-1.5}$ / $x^{-1.2}$ for width 50, and $e^{-x/3100}$ then $x^{-1.4}$ / $x^{-1.3}$ for width 200 ($x$ = number of training data).
- The transition point moves later for wider networks; smaller networks are more accurate on small datasets.
- An FNN of width 100 also shows initial exponential decay but with much larger error and slower convergence; Seq2Seq shows no exponential regime, only roughly polynomial decay ($x^{-1.3}$) with large run-to-run variation.
- Authors: "We cannot yet explain theoretically this convergence behaviour", speculating a link to the information bottleneck.

**Diffusion-reaction PDE (Problem 4, $D=k=0.01$, source $u(x)$ as input, Fig. 4)** (pp. 7-8):
- Data from a second-order implicit finite-difference solver on a $100\times100$ grid, with $P$ random points per solution.
- Test mse $\approx10^{-5}$ with only 100 $u$ samples and $P=1000$ (about 10 training points per grid location on average). ResNets of several sizes in the same setup give test error $\sim10^{-1}$ because of large generalisation error.
- Before saturation, polynomial convergence in both $P$ and $\#u$: exponents from $x^{-1.4}$ to $x^{-2.4}$ in $P$ and $x^{-2.6}$ to $x^{-3.7}$ in $\#u$ depending on the other factor (Fig. 4c,d). An initial exponential regime also appears (Supplementary Fig. 9); the paper cannot fully explain the $\ln(x)$ or $e^{-x}$ trend of the fitted coefficients.

**Stochastic operators (pp. 8-9)**:
- Random inputs are handled with a Karhunen-Loeve expansion $k(t;\omega)\approx\sum_{i=1}^N\sqrt{\lambda_i}e_i(t)\xi_i(\omega)$. The branch net gets $[\sqrt{\lambda_1}e_1,\dots,\sqrt{\lambda_N}e_N]\in\mathbb{R}^{N\times m}$; the trunk net gets $[t,\xi_1,\dots,\xi_N]\in\mathbb{R}^{N+1}$. The covariance function is not assumed known when training.
- Problem 5 (stochastic ODE $dy=k(t;\omega)y\,dt$, $y(0)=1$, $\sigma=1$, $l\in[1,2]$, $N=5$ keeps 99.9% of stochastic energy): 10,000 samples, one realization each; test mse $8.0\times10^{-5}\pm3.4\times10^{-5}$, average relative $L^2$ error $\sim0.5\%$.
- Problem 6 (elliptic $-\mathrm{div}(e^{b}\nabla u)=f$, $f=10$, $\sigma=0.1$, $l\in[1,2]$): test mse $2.0\times10^{-3}\pm1.7\times10^{-3}$, relative $L^2$ error $\sim1.1\%$. Clipping the $\xi_i$ to $[-3.1,3.1]$ lowers test mse to $9.4\times10^{-4}\pm3.0\times10^{-4}$.
- Mean and standard deviation of the stochastic solution are predicted by feeding only $t$ to the trunk (no $\xi_i$), using $l\in[0.2,2]$ and $N=8$ modes (Fig. 6b,c).
- The KL approach applies to coloured noise where a KL expansion exists; white noise "may require a different approach" (p. 9).

**Cost**: inference is a forward pass and "substantially lower" than the numerical solver (Supplementary Table 5, cited on p. 10; numbers not in the main text).

## Limitations

As stated by the authors (p. 10):
- Training is much more expensive than for function approximation because dataset size is $P\times\#u$; faster offline training and transfer learning are needed.
- No theory yet for network size needed for operator approximation, and no theory for why DeepONets generalise well.
- The exponential-then-polynomial error decay is observed but unexplained.
- Surrogate only: cannot beat the solver that generated the data.
- Claims about multiscale / multiphysics use are "ongoing work" and not demonstrated here.

Wiki note: (1) Evaluation is on in-distribution test functions except for the single GRF correlation-length shift study (Fig. 2c); out-of-distribution robustness is otherwise not tested. (2) The main text has no Materials and Methods section in the extracted PDF; architecture hyperparameters sit in the Supplementary Information, which was not available to the wiki. (3) Results are single-paper, mostly on 1D problems.

## Connections

- Builds on the Chen-Chen universal approximation theorem for operators ([[Universal approximation for operators]]) and the classical universal approximation theorem.
- Compared against FNN, ResNet, Seq2Seq (LSTM/GRU with attention) and a CNN encoder-decoder baseline.
- Uses [[Karhunen-Loève expansion]] to feed random processes into the branch/trunk nets, and the 2-Wasserstein distance to quantify the shift between GRF input spaces.
- Wiki note: this reading-group copy may duplicate a copy elsewhere in the library (e.g. `Operators/Karniadakis, Lu, Jin - DeepONets - Deep Operator Networks.pdf`); the coordinator will confirm whether to treat them as one source.
- In the same reading-group batch, [[Markovian homogenized viscoelasticity (Bhattacharya 2023)]] cites universal approximation results for operators ([6], Chen-Chen) when motivating operator learning.





%% refs:start %%
**Cites in this wiki**: [[Attention is all you need (Vaswani 2017)]], [[HNNs (Greydanus 2019)]], [[Neural ODEs (Chen 2018)]]
**Cited by in this wiki**: [[FNO (Li 2021)]], [[LNO (Cao 2023)]], [[NIF (Pan 2023)]], [[Neural operator (Kovachki 2022)]], [[Operator learning review (Kovachki 2024)]], [[PIFT (Alberts 2023)]], [[When and why PINNs fail (Wang 2022)]]
%% refs:end %%

**Sources**: `PSL Reading Group/26.10.22 - DeepONets.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DeepONet]]
- [[Universal approximation for operators]]
- [[Karhunen-Loève expansion]]
- [[Operator learning]]
- [[Markovian homogenized viscoelasticity (Bhattacharya 2023)]]
