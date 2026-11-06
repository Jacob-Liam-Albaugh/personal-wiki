---
type: paper
area: symmetry
areas: [symmetry, ml]
source-ref: "Dey, Chen, Ghafurian 2021, ICLR, §3-4, Tables 1-4"
tags: [paper, symmetry, generative, ml]
authors: [Dey, Chen, Ghafurian]
year: 2021
venue: "ICLR 2021 (arXiv:2005.01683v2, 30 Mar 2021)"
file: "Symmetries/Dey, Chen, Ghafurian - Group Equivariant GANs.pdf"
---

# Group Equivariant GANs (Dey 2021)

**Summary**: Replaces every convolution in a GAN generator and discriminator with a p4 or p4m group convolution, so rotation (and reflection) equivariance is built in rather than learned from augmentation or consistency regularizers. Gives better FID and sample efficiency on rotation-symmetric data (RotMNIST, histology ANHIR, LYSTO) and mixed results on natural images (CIFAR-10, Food-101); the equivariant discriminator carries most of the gain (pp. 5-7).

**Authors**: Neel Dey (NYU; work done during an internship at Merck), Antong Chen, Soheil Ghafurian (Merck & Co.) · **Year**: 2021 · **File**: `Symmetries/Dey, Chen, Ghafurian - Group Equivariant GANs.pdf`

---

## Problem

Data often has a symmetry group (rotations of microscopy slides) but a standard CNN GAN must spend capacity learning it. Prior remedies, standard augmentation (leaks into samples) and consistency regularizers such as bCR and AR GANs (Zhao 2020c, Chen 2019), do not encode symmetry in the architecture (pp. 1-2). Question: do group-equivariant layers in G and D help, and how should they be combined with regularizers?

## Method

> [!definition] Equivariance and invariance
> $\Phi(g\cdot x)=g\cdot\Phi(x)$ (equivariant); $\Phi(g\cdot x)=\Phi(x)$ (invariant), for $g\in G$.
>
> (source: Group Equivariant GANs PDF, §3, p. 3)

> [!definition] p4 and p4m groups
> Elements as $3\times3$ matrices, $0\le r<4$, $m\in\{0,1\}$, $(u,v)\in\mathbb Z^2$:
> $$g(r,u,v)=\begin{bmatrix}\cos\frac{r\pi}{2}&-\sin\frac{r\pi}{2}&u\\ \sin\frac{r\pi}{2}&\cos\frac{r\pi}{2}&v\\0&0&1\end{bmatrix}$$
> $g'(m,r,u,v)$ has first row $\big((-1)^m\cos\frac{r\pi}2,\ (-1)^{m+1}\sin\frac{r\pi}2,\ u\big)$ and the same second and third rows. p4: translations and 90-degree rotations; p4m adds mirror reflections.
>
> (source: PDF, §3, p. 3)

> [!definition] Group convolution ([[Equivariance#Group equivariant convolution|group equivariant convolution]])
> First layer (input on $\mathbb Z^2$), filter $\psi$, $K$ channels:
> $$[f*\psi](g)=\sum_{y\in\mathbb Z^2}\sum_k f_k(y)\,\psi_k(g^{-1}y)$$
> Later layers (input on $G$):
> $$[f*\psi](g)=\sum_{h\in G}\sum_k f_k(h)\,\psi_k(g^{-1}h)$$
> Formally correlations. Pooling over $G$ maps back to a $\mathbb Z^2$ feature map. Equivariance of the layer follows Cohen and Welling 2016.
>
> (source: PDF, §3, p. 3)

Wiki note: see [[Equivariance]]; the layers are the G-CNN of Cohen and Welling 2016, as the paper cites.

> [!definition] Training ingredients
> R1 penalty on D: $R_1:=\frac{\gamma}{2}\,\mathbb E_{x\sim P_{real}}\big[\|\nabla D(x)\|_2^2\big]$ (p. 3). Spectral norm: $W_{SN}=W/\sigma(W)$ (p. 4), which preserves group equivariance of the filter bank.
>
> (source: PDF, §3-4, pp. 3-4)

### Architecture (pp. 4, 8, 21)

- BigGAN-style baseline ([[GAN]]) with all convolutions replaced by p4 (or p4m) group convs.
- G: FC projection of $[z,\text{class embedding}]$ to spatial maps on $\mathbb Z^2$, spectrally normalised group convs, nearest-neighbour upsampling, group-equivariant class-conditional batch norm, max-pool over the group at the output.
- D: spectrally normalised group convs, spatial pooling (not strided), group pooling, global average pooling, projection conditioning.
- Batch-norm moments are computed per group feature map. The number of group filters is divided by $\sqrt{|G|}$ so parameter counts match the CNN baseline.
- For CIFAR-10 and Food-101, which have canonical pose, D pools over rotations before the last residual block so it can still detect non-canonical pose.
- p4m for ANHIR and LYSTO; p4 for CIFAR-10, Food-101 and RotMNIST (p4m is precluded for digits since mirrored digits change class).
- Optimiser: Adam, $\beta_1=0,\beta_2=0.9$; D updated twice per G step (four times on CIFAR-10); EMA 0.9999 of G weights. Losses: relativistic average (ANHIR, LYSTO, Food-101), hinge (CIFAR-10), NSGAN/WGAN/RaGAN (RotMNIST). Learning rates $\eta_G=10^{-4}$, $\eta_D=4\times10^{-4}$ for RotMNIST and ANHIR; LYSTO halves them with $\gamma=1.0$.

### Datasets (Table 1, p. 5)

| Dataset | Resolution | Classes | Train / Val | Canonical pose |
|---|---|---|---|---|
| RotMNIST | 28x28 | 10 | 12,000 / 50,000 | no |
| ANHIR | 128x128x3 | 5 | 28,407 / 9,469 | no |
| LYSTO | 256x256x3 | 3 | 20,000 / - | no |
| CIFAR-10 | 32x32x3 | 10 | 50,000 / 10,000 | yes |
| Food-101 | 64x64x3 | 101 | 75,747 / 25,250 | yes |

Metrics: FID with a fine-tuned Inception-v3 (medical sets), a p4-CNN feature extractor (RotMNIST) and the official TF Inception (natural sets); precision/recall of Kynkaanniemi 2019; KID for the Maps task.

## Results

**Table 2: RotMNIST Frechet distance, (min, mean) over 3 seeds, by training-set fraction (p. 5).** Real-data reference: 0.6854 / 0.3208 / 0.1324 / 0.1296.

| Loss | G, D | 10% | 33% | 66% | 100% |
|---|---|---|---|---|---|
| RaGAN | CNN, CNN | (2.04, 11.40) | (1.42, 11.65) | (1.20, 11.10) | (1.36, 11.68) |
| RaGAN | CNN, G-CNN | (1.84, 4.26) | (0.88, 3.26) | (0.52, 2.85) | (0.53, 3.12) |
| RaGAN | G-CNN, CNN | (1.49, 9.75) | (1.08, 9.29) | (0.90, 8.70) | (0.95, 9.62) |
| RaGAN | G-CNN, G-CNN | (1.61, 4.25) | (0.76, 3.40) | (0.54, 2.92) | (0.53, 2.90) |
| NSGAN | CNN, CNN | (1.00, 7.02) | (0.74, 8.25) | (0.84, 8.07) | (0.97, 8.49) |
| NSGAN | CNN, G-CNN | (2.77, 5.48) | (1.02, 3.51) | (0.55, 2.85) | (0.54, 3.08) |
| NSGAN | G-CNN, CNN | (1.00, 7.00) | (0.96, 7.42) | (0.87, 6.83) | (0.94, 7.52) |
| NSGAN | G-CNN, G-CNN | (2.85, 5.67) | (1.04, 4.24) | (0.82, 3.27) | (0.64, 3.32) |
| WGAN | CNN, CNN | (3.42, 16.21) | (3.90, 18.32) | (3.87, 17.81) | (4.88, 19.40) |
| WGAN | CNN, G-CNN | (2.87, 5.98) | (0.76, 4.11) | (0.50, 3.57) | (0.39, 3.51) |
| WGAN | G-CNN, CNN | (2.67, 16.02) | (3.40, 17.03) | (3.77, 17.76) | (3.74, 17.82) |
| WGAN | G-CNN, G-CNN | (2.51, 5.67) | (0.58, 3.32) | (0.56, 3.52) | (0.54, 3.76) |

(Column "G, D" lists the architecture of generator then discriminator.) At 33-100% of the data most of the gain comes from the p4 discriminator; at 10% an equivariant generator matters more (p. 6). 20,000 generator iterations, batch 64. NSGAN-GP and RaGAN-GP behave similarly; WGAN-GP is worse initially.

**Table 3: FID, lower is better (p. 7).**

| Model | ANHIR | LYSTO | CIFAR-10 | Food-101 |
|---|---|---|---|---|
| CNN G&D | 7.32 | 7.27 | 20.89 | 27.34 |
| G-CNN G, CNN D | 6.93 | 6.68 | 21.20 | 24.16 |
| CNN G, G-CNN D | 5.56 | 5.02 | 17.09 | 16.91 |
| G-CNN G&D | 5.54 | 3.90 | 17.49 | 17.73 |
| CNN + standard aug | 7.57 | 6.59 | 37.41 | 35.18 |
| CNN + bCR | 5.86 | 4.78 | 19.64 | 21.18 |
| CNN + AR | - | - | 19.59 | 20.39 |
| G-CNN G&D + bCR | 5.19 | 4.53 | 17.94 | 15.55 |

Findings (pp. 7-9):

- Equivariant D alone or with equivariant G beats the CNN baseline on all four datasets; the largest relative FID gain is on LYSTO (7.27 to 3.90) and Food-101 (27.34 to 16.91).
- Standard augmentation hurts on CIFAR-10 and Food-101 (37.41, 35.18) because of "leakage" of the augmentation into samples.
- bCR with its suggested weights collapsed training on ANHIR, LYSTO and CIFAR-10 and needed much lower strength. G-CNN plus bCR is additive on ANHIR and Food-101, not on LYSTO and CIFAR-10.
- Equivariant GANs converge faster in FID against generator updates on all datasets except ANHIR.
- Precision/recall: G-CNN G&D gives higher recall on ANHIR and LYSTO.
- Image translation (App. B, Table 4, p. 19), Maps Map2Sat KID (lower better; 1096 train / 1098 val pairs at 256x256): Pix2Pix 0.1584 $\pm$ 0.0026; Pix2Pix optimised 0.0663 $\pm$ 0.0038; CNN G with G-CNN D 0.0333 $\pm$ 0.0005; G-CNN G&D 0.0399 $\pm$ 0.0024.

Other details: LYSTO organ labels validated by a VGG16 at 98% accuracy (App. C.1.1); p4m GANs cost about 4x compute per iteration (App. C.2); in the CIFAR-10 D, global sum versus average pooling changes FID by about 5-8 (App. C.2.4).

## Limitations

Stated by the authors: group-equivariant attention is not scalable; continuous groups may be memory-bound; results are empirical with no theory; p4/p4m do not capture diffeomorphic warps; compute cost is higher. Future work names ADA (Karras 2020a), equivariant VAEs (Lafarge 2020b) and scattering networks.

Wiki note: improvement on CIFAR-10 is smaller and the G-CNN G&D variant is slightly worse than D-only (17.49 vs 17.09), so for canonical-pose images the benefit is mostly from the discriminator. Numbers are from single runs for FID (Table 3 has no error bars).

## Connections

- Group convolutions generalise ordinary translation-equivariant convolutions: see [[Equivariance#Group equivariant convolution|group equivariant convolution]], [[Equivariance]].
- Baseline family and losses: [[GAN]]; the R1 penalty and spectral norm are discriminator regularizers.
- Wiki note: [[Score SDE (Song 2021)]] reports GAN baselines (StyleGAN2-ADA FID 2.92 unconditional on CIFAR-10) and uses the same BigGAN-style blocks in its NCSN++, so the equivariant-layer idea could in principle transfer to [[Diffusion models]] score networks; the paper does not test this. **[unverified]**
- Equivariant generative priors for physical fields: [[Generative priors for turbulence (Wang 2026)]] (Wiki note, check relevance).

**Sources**: `Symmetries/Dey, Chen, Ghafurian - Group Equivariant GANs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[GAN]]
- [[Equivariance#Group equivariant convolution|group equivariant convolution]]
- [[Equivariance]]
- [[Diffusion models]]
- [[Score SDE (Song 2021)]]
- [[Generative priors for turbulence (Wang 2026)]]
