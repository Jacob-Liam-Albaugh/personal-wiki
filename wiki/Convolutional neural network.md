---
type: concept
area: ml
areas: [ml, symmetry]
source-ref: "Krizhevsky et al. 2012, §2, §4-5; Ronneberger et al. 2015, §1-3"
tags: [ml]
---

# Convolutional neural network

**Summary**: A network built from convolutional layers (local, weight-shared filters), pointwise nonlinearities and pooling. Weight sharing encodes the prior that image statistics are stationary and pixel dependencies local, so a CNN has far fewer connections than a dense net of the same layer sizes.

**Sources**: `papers/ML/Krizhevsky et al - ImageNet Classification with Deep Convolutional Neural Networks.pdf`, `papers/Diffusion/Ronneberger, Fischer, Brox - U-Net Convolutional Networks for Biomedical Image Segmentation.pdf`.
**Last updated**: 2026-11-07

---

## Ingredients

- **Convolutional layer**: each kernel is applied at every position; the feature map is translation-equivariant. The underlying operation is [[Convolution]] (strictly, cross-correlation in most libraries **[unverified]**). Krizhevsky et al.: "stationarity of statistics and locality of pixel dependencies" are the built-in assumptions, and capacity is tuned by depth and breadth (source: AlexNet.pdf, p. 2).
- **Nonlinearity**: [[ReLU]].
- **Pooling**: summarizes neighbourhoods of a kernel map. AlexNet uses overlapping max pooling, stride $s=2$, window $z=3$ (§4.4). U-Net uses $2\times2$ max pooling, stride 2, and doubles channels at each step.
- **Receptive field and stride**: AlexNet's first layer is $11\times11\times3$ with stride 4.
- **Regularizers**: [[Dropout]] in dense layers; data augmentation (below).

## Two canonical designs

| | [[AlexNet (Krizhevsky 2012)]] | [[U-Net paper (Ronneberger 2015)]] |
|---|---|---|
| Output | one label per image | one label per pixel |
| Shape | conv stack then 3 dense layers | contracting path, expanding path, skip concatenations |
| Dense layers | yes (4096-4096-1000) | none (fully convolutional) |
| Training data | 1.2M images | 30 images (EM), 20-35 (cell tracking) |
| Key trick | ReLU, GPU training, dropout | elastic-deformation augmentation, border-weighted loss |

See [[U-Net]] for the segmentation/decoder family.

## Data augmentation as a prior

Both papers treat augmentation as the way to inject invariances the data do not show:
- AlexNet: random crops and flips (factor 2048) and PCA colour jitter, on the premise that object identity is invariant to illumination colour and intensity (source: AlexNet.pdf, §5.1).
- U-Net: shifts, rotations, gray-value changes and random elastic deformations, "the key concept to train a segmentation network with very few annotated images" (source: U-Net.pdf, §3.1).

For exact rather than learned invariance to rotations and reflections see [[Group equivariant CNN]] and [[Rotation augmentation for CNNs (Quiroga 2018)]].

## Variants

- Residual CNNs: [[ResNet]].
- Group-equivariant CNNs: [[Group equivariant CNN]].
- Spectral/Fourier convolution layers for functions on grids: [[Neural operator]], FNO; both operator papers list a U-Net as a convolutional baseline whose error grows with resolution (source: [[Neural operator (Kovachki 2022)]], Table 5).
- Generative use: convolutional discriminators and "deconvolutional" generators in [[GAN paper (Goodfellow 2014)]]; U-Net denoisers in [[DDPM (Ho 2020)]].

## Where it appears
- [[AlexNet (Krizhevsky 2012)]]: the ImageNet-scale demonstration.
- [[U-Net paper (Ronneberger 2015)]]: fully convolutional encoder-decoder for segmentation.
- [[GAN paper (Goodfellow 2014)]]: convolutional discriminator for CIFAR-10.

## Related pages
- [[Convolution]] · [[ReLU]] · [[Dropout]] · [[U-Net]] · [[ResNet]] · [[Group equivariant CNN]] · [[Neural operator]] · [[GAN]]
