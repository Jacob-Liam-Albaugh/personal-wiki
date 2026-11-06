---
type: method
area: operators
areas: [operators, ml]
source-ref: "Kovachki et al. 2022, eqs. 6, 10, pp. 9-10; §4, pp. 14-22"
tags: [operators, ml]
---

# Neural operator

> [!definition] Neural operator (Kovachki et al. 2022, eq. 6, p. 9)
> $$\mathcal G_\theta=Q\circ\sigma_T(W_{T-1}+\mathcal K_{T-1}+b_{T-1})\circ\cdots\circ\sigma_1(W_0+\mathcal K_0+b_0)\circ P$$
> $P$ lifts pointwise to $d_v$ channels, $Q$ projects pointwise back. Each layer (eq. 10):
> $$v_{t+1}(x)=\sigma\Big(W_tv_t(x)+\int_D\kappa^{(t)}(x,y)\,v_t(y)\,d\nu_t(y)+b_t(x)\Big)$$
>
> (source: `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`, pp. 9-10)

**Intuition**: a deep network in which the hidden state is a function. The pointwise part $W_t$ is local; the [[Kernel integral operator]] $\mathcal K_t$ mixes information across the domain. The parameters do not depend on any grid, which gives [[Discretization invariance]].

The review form is the same: $L_\ell(v)(x)=\sigma(W_\ell v(x)+b_\ell+\mathcal K(v)(x;\gamma_\ell))$ (source: `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`, eq. 4.2, p. 14).

## Parametrizations of the kernel integral
The four schemes differ only in how $\int\kappa(x,y)v(y)\,dy$ is evaluated cheaply. Direct Monte Carlo over $J$ points costs $O(J^2)$ (eq. 14).

### Graph neural operator
Truncate the integral to a ball, $u(x)=\int_{B(x,r)\cap D}\kappa(x,y)v(y)\,dy$ (eq. 16), and evaluate it by message passing with mean aggregation over neighbours. The cost is $c_sJ^2$ with $c_s\approx r^d$. With $L$ layers and $2^{L-1}r\ge1$ the receptive field covers $D$ (§4.1, pp. 14-17). A CNN is the special case of a compactly supported $\kappa(x-y)$ on a fixed grid, which is not discretization consistent (eq. 17).

### Low-rank neural operator
$\kappa(x,y)=\sum_{j=1}^r\varphi^{(j)}(x)\psi^{(j)}(y)$, so $u(x)=\sum_j\langle\psi^{(j)},v\rangle\varphi^{(j)}(x)$, at cost $O(rJ)$ (eq. 18). Rank 4 in the experiments. Li et al. call it "similar to unstacked DeepONet" (FNO paper).

### Multipole graph neural operator
Split $K=K_1+\dots+K_L$ by range (eq. 19) and factor through nested coarser graphs, $K\approx K_{1,1}+K_{1,2}K_{2,2}K_{2,1}+\dots$ (eq. 20). The evaluation is a V-cycle (eqs. 24-25) at total cost $O(J)$ (§4.3, pp. 18-22).

### Fourier neural operator
$\kappa(x-y)$ evaluated as a truncated Fourier multiplier. See [[FNO]]. It is the best of the four in nearly all of Kovachki et al.'s benchmarks.

## Other kernels
- [[LNO]]: a pole-residue kernel in the Laplace domain.
- Averaging neural operator: the kernel is a constant matrix, $V_\ell\int_Dv(y)\,dy$. It is already universal (review Thm 4.5, Cor. 4.6, p. 15); see [[Universal approximation for operators]].

## DeepONet as a neural operator
With $W_0=0$, constant-in-$y$ kernels and sum projection, a two-layer neural operator reproduces [[DeepONet]] (Kovachki et al. Prop. 5, pp. 25-26). The sensor version is not discretization invariant.

## Where it appears
- [[Neural operator (Kovachki 2022)]]: defines the framework, four parametrizations, universality.
- [[FNO (Li 2021)]]: the Fourier instance.
- [[LNO (Cao 2023)]]: the Laplace instance.
- [[Operator learning review (Kovachki 2024)]]: places it against [[Encoder-decoder operators]] models as a nonlinear approximation.

**Sources**: `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`, `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Operator learning]] · [[Kernel integral operator]] · [[FNO]] · [[LNO]] · [[Discretization invariance]] · [[DeepONet]]
