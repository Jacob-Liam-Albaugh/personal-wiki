---
type: concept
area: symmetry
areas: [symmetry, ml]
source-ref: "Cohen & Welling 2016, §4-8"
tags: [symmetry, ml]
---

# Group equivariant CNN

**Summary**: A convolutional network whose layers commute with a symmetry group $G$ larger than translations, by making feature maps functions on $G$ and replacing convolution with G-correlation.

---

## Core idea

A layer $\Phi$ is equivariant if

$$\Phi(T_gx)=T'_g\Phi(x)$$

(source: Cohen & Welling 2016, eq. 1). G-correlation (eq. 10-11):

$$[f\star\psi](g)=\sum_{h\in G}\sum_kf_k(h)\,\psi_k(g^{-1}h)$$

Pointwise nonlinearities and pooling preserve equivariance (eq. 14-17).

## Groups used

- p4: translations plus 90-degree rotations (four patches per map).
- p4m: p4 plus mirror flips (eight patches per map).

Details and results: [[Group equivariant CNNs (Cohen 2016)]].

## Context

- General principle: [[Equivariance]].
- Rotation by augmentation instead: [[Rotation augmentation for CNNs (Quiroga 2018)]].
- Continuous 3D groups and irreps: [[e3nn]].
- Generative variant: [[Group equivariant GANs (Dey 2021)]].

**Sources**: Cohen & Welling 2016.
**Last updated**: 2026-11-06

---

## Related pages
- [[Group equivariant CNNs (Cohen 2016)]]
- [[Equivariance]]
- [[e3nn]]
- [[Rotation augmentation for CNNs (Quiroga 2018)]]
