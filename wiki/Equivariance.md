---
type: definition
area: symmetry
areas: [symmetry, ml]
source-ref: "Dey et al. 2021, §3, p. 3"
tags: [symmetry, ml]
---

# Equivariance

> [!definition] Equivariance and invariance (Dey et al. 2021, §3, p. 3)
> For a group $G$ acting on inputs and outputs, a map $\Phi$ is
> $$\text{equivariant: }\Phi(g\cdot x)=g\cdot\Phi(x)$$
> $$\text{invariant: }\Phi(g\cdot x)=\Phi(x)$$
> for all $g\in G$.
>
> (source: `Symmetries/Dey, Chen, Ghafurian - Group Equivariant GANs.pdf`, p. 3)

**Intuition**: transform then process equals process then transform. Building this into a network means it never has to learn the symmetry from data.

Ordinary convolution is equivariant to translations. Pooling over the group turns an equivariant feature map into an invariant one.

## Group equivariant convolution
> [!definition] G-convolution (Dey et al. 2021, p. 3; after Cohen and Welling 2016)
> First layer, input on $\mathbb Z^2$:
> $$[f*\psi](g)=\sum_{y\in\mathbb Z^2}\sum_kf_k(y)\,\psi_k(g^{-1}y)$$
> Later layers, input on $G$:
> $$[f*\psi](g)=\sum_{h\in G}\sum_kf_k(h)\,\psi_k(g^{-1}h)$$
> Strictly these are correlations.

Groups used by Dey et al.:
- p4: translations and 90° rotations.
- p4m: p4 plus mirror reflections.

To keep the parameter count equal to a CNN, the number of filters is divided by $\sqrt{|G|}$ (p. 4). p4m costs about 4× compute per iteration (App. C.2).

## Evidence (Dey et al.)
- Rotation-symmetric data (RotMNIST, ANHIR, LYSTO): better FID and sample efficiency.
- Natural images (CIFAR-10): small gains, mostly from the equivariant discriminator.

## Where it appears
- [[Group equivariant GANs (Dey 2021)]].
- Wiki note: [[Discretization invariance]] is a different notion, invariance to the mesh rather than to a group action.
- [[Group equivariant CNN]] ([[Group equivariant CNNs (Cohen 2016)]]): equivariance to p4 and p4m via G-correlation.
- [[e3nn]] ([[e3nn Euclidean networks (Geiger 2022)]]): E(3) equivariance with irreps and tensor products.
- [[Tensor basis NN turbulence (Ling 2016)]]: invariance built in through an integrity basis.
- [[Rotation augmentation for CNNs (Quiroga 2018)]]: augmentation as the alternative to built-in symmetry.
- Groups, $E(n)=T(n)\rtimes O(n)$, invariance versus equivariance with the atoms-to-forces example, and an e3nn tetris classifier: [[ME697 2.6 - Symmetries]] (source: `up/symmetries/01_symmetries.md`, `02_e3nn.ipynb`).
- Wiki note: the book's action $(\mathbf b,A)\mathbf x=A(\mathbf x+\mathbf b)$ does not match its composition law, which is that of $\mathbf x\mapsto A\mathbf x+\mathbf b$. Also, the e3nn notebook says the network "learned" to drop `1e` outputs; the `Linear` layer drops them by construction.

## Examples
- Deep Sets gives permutation invariance as rho(sum phi(x)) (Thm 2) and the equivariant layer Theta = lambda I + gamma 11^T (Lemma 3) (source: Zaheer 2017). Link [[Deep Sets]], [[Graph neural network]].
- a GP prior can be made invariant under a finite group by summing, multiplying or projecting the kernel over group orbits; the periodic kernel is an SE kernel on (sin x, cos x) (source: Duvenaud 2014, §2.7, eqs. 2.36-2.41, pp. 22-26). The sum-over-orbit recipe doubles marginal variance near symmetry lines and the product recipe can give zero variance in regions (pp. 23-25). Wiki note: this is invariance of a scalar function, not equivariance of a vector-valued map.

> [!example] Homework 4, permutation group (source: homework/04_homework.ipynb)
> The symmetric group $S_n$, cycles and transpositions, permutation matrices (Cayley's theorem), and a faithful $2\times2$ complex representation of $S_3$.

**Sources**: `Symmetries/Dey, Chen, Ghafurian - Group Equivariant GANs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[GAN]] · [[Diffusion models]]
- [[Kernel composition]].
