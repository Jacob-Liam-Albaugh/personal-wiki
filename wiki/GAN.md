---
type: concept
area: ml
areas: [ml, stochastic]
source-ref: "Dey et al. 2021, §3-4; Song et al. 2021, Table 3"
tags: [generative, ml]
---

# Generative adversarial network (GAN)

**Summary**: a generator $G(z)$ maps noise to samples and a discriminator $D$ tells real from fake. The two train against each other. No likelihood is computed. This wiki meets GANs as a baseline family and as the testbed for [[Equivariance|equivariant]] layers.

**Sources**: `Symmetries/Dey, Chen, Ghafurian - Group Equivariant GANs.pdf`, `Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`.
**Last updated**: 2026-11-06

---

## Losses tested by Dey et al. (pp. 6, 21-22)
The paper names these and does not restate them:
- non-saturating (Goodfellow 2014);
- Wasserstein (Arjovsky 2017);
- relativistic average, RaGAN (Jolicoeur-Martineau 2018): used for ANHIR, LYSTO and Food-101;
- hinge (Lim and Ye 2017): used for CIFAR-10.

## Discriminator regularizers (Dey et al., pp. 3-4)
```
R1 = (γ/2) E_real ||∇D(x)||²
W_SN = W / σ(W)
```
R1 penalizes the gradient on real data. Spectral norm divides each weight by its top singular value. Dey et al. note spectral norm keeps a group filter bank equivariant.

## Versus diffusion models
On CIFAR-10, Song et al. Table 3 (p. 7) gives:
- StyleGAN2-ADA unconditional: FID 2.92.
- StyleGAN2-ADA conditional: FID 2.42.
- Best score SDE, NCSN++ cont. deep VE, unconditional: FID 2.20.

The NCSN++ score network reuses BigGAN residual blocks and StyleGAN2 FIR resampling (App. H).

## Where it appears
- [[Group equivariant GANs (Dey 2021)]]: G-CNN generator and discriminator.
- [[Score SDE (Song 2021)]]: as baselines.

## Related pages
- [[Diffusion models]] · [[Equivariance]] · [[Normalizing flows]]
