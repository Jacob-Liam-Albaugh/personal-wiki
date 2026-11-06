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

**Sources**: `Symmetries/Dey, Chen, Ghafurian - Group Equivariant GANs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[GAN]] · [[Diffusion models]]
