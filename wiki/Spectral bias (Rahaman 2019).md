---
type: paper
area: ml
areas: [ml]
source-ref: "Rahaman et al. 2019, ICML, §2-4"
tags: [ml, optimization, signals]
authors: ["[[Nasim Rahaman]]", "[[Aristide Baratin]]", "[[Devansh Arpit]]", "[[Felix Draxler]]", "[[Min Lin]]", "[[Fred Hamprecht]]", "[[Yoshua Bengio]]", "[[Aaron Courville]]"]
year: 2019
venue: "ICML 2019 (PMLR 97)"
file: "papers/ML/Rahaman et.al. - On the Spectrial Bias of NNs.pdf"
---

# Spectral bias (Rahaman 2019)

**Summary**: Uses Fourier analysis of ReLU networks to show that gradient descent fits low-frequency components of a target first, whatever their amplitude. High frequencies need finely tuned parameters and large weight norms, so they arrive late. The shape of the data manifold changes this: high-frequency signals on a wiggly manifold need only low frequencies in input space.

**Authors**: Nasim Rahaman, Aristide Baratin, Devansh Arpit, Felix Draxler, Min Lin, Fred Hamprecht, Yoshua Bengio, Aaron Courville · **Year**: 2019 · **File**: `papers/ML/Rahaman et.al. - On the Spectrial Bias of NNs.pdf`

---

## Problem

Networks can fit random labels yet generalize on natural data. The paper proposes that part of the reason is a learning-speed bias: simple (low-frequency) functions are learned faster than complex ones (source: Rahaman 2019, §1).

## Method

**Fourier form of a ReLU net.** A ReLU network is continuous piecewise linear, $f(x) = 1_{P_\epsilon}(x)\,(W_\epsilon x + b_\epsilon)$ on convex polytopes $P_\epsilon$ (§2.1).

> [!theorem] Spectrum of ReLU networks (Theorem 1)
> $$\tilde f_\theta(k) = \sum_{n=0}^{d} \frac{C_n(\theta,k)\, 1_{H^n_\theta}(k)}{k^{\,n+1}}$$
> Here $C_n$ is $\Theta(1)$ as $k\to\infty$ and $H^n_\theta$ is a union of $n$-dimensional subspaces orthogonal to codimension-$n$ faces of the polytopes (source: Rahaman 2019, §2.2, Thm 1).

- The decay is anisotropic: about $k^{-d-1}$ in almost all directions, but as slow as $k^{-2}$ orthogonal to the $(d-1)$-dimensional faces.
- The numerator is bounded by $N_f L_f$ (number of linear regions times Lipschitz constant). $L_f$ is bounded by a product of layer spectral norms, so it grows exponentially in depth (p. 2-3).
- Rate argument (eq. 9): the parameter gradient of $\tilde f(k)$ decays at most one power of $k$ faster than $\tilde f$, so the residual at frequency $k$ changes at rate $O(k^{-\Delta})$ under gradient flow. High frequencies move slowly (p. 3).

## Results

- **Exp. 1** (6 layers, 256 units, target $\sum_i A_i\sin(2\pi k_i z+\varphi_i)$, $k_i = 5,\dots,50$, $N=200$): low frequencies are fit first even when higher ones have larger amplitude. Layer spectral norms grow as higher frequencies are fit (Fig. 1).
- **Exp. 2**: random parameter perturbations destroy high frequencies much more than low ones, so high-frequency solutions occupy a small parameter volume (Fig. 3).
- **Exp. 3-4** (MNIST): with a noisy target, validation loss dips early (true low-frequency target learned) then rises as the network fits high-frequency noise (Fig. 4-5). Low-frequency noise hurts most. A generalized "frequency" uses eigenfunctions of the Gaussian RBF kernel.
- **Exp. 5-6**: for a target on a flower-shaped curve $\gamma_L$ with $L$ petals, training gets easier as $L$ grows; classification accuracy of a high-frequency sine rises with $L$ (Fig. 8-9).

> [!theorem] Manifold effect
> The Fourier transform of $f\circ\gamma$ is
> $$\widetilde{(f\circ\gamma)}(l) = \int dk\, \tilde f(k)\, P_\gamma(l,k)$$
> By stationary phase, the kernel is non-zero where $l = J_\gamma(z)\,k$. If the embedding coordinates have high-frequency content, large latent frequencies $l$ arise from modest input frequencies $k$ (source: Rahaman 2019, §4, eq. 14-15).

## Limitations

- Theory is for ReLU networks; experiments use one architecture family and small data (synthetic 1D, MNIST, some CIFAR in the appendix).
- The gradient-flow argument is an informal rate heuristic, not a full convergence theorem. **[unverified]** as a general statement beyond the paper's setting.
- Appendix E compares with kernel machines and KNN only qualitatively; not read in detail.

## Connections

- Concept page: [[Spectral bias]].
- Remedies: [[Fourier features (Tancik 2020)]] lift inputs to sinusoids; [[SIREN paper (Sitzmann 2020)]] uses sine activations. See [[Fourier features]] and [[SIREN]].
- Kernel view of the same bias: [[Neural tangent kernel]], [[Kernel methods]].
- Implicit regularization of [[Gradient descent]]/[[SGD]]; the dropout and early-stopping links are Wiki notes, see [[Dropout]].
- Fourier tools: [[Fourier transform]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Universal approximation (Hornik 1989)]]
**Cited by in this wiki**: [[Expert's guide to PINNs (Wang 2023)]], [[Fourier features (Tancik 2020)]], [[NIF (Pan 2023)]], [[When and why PINNs fail (Wang 2022)]]
%% refs:end %%

**Sources**: `papers/ML/Rahaman et.al. - On the Spectrial Bias of NNs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Spectral bias]]
- [[Fourier features]]
- [[SIREN]]
- [[Neural tangent kernel]]
- [[Fourier transform]]
- [[Gradient descent]]
