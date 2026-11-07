---
type: paper
area: stochastic
areas: [stochastic, ml]
source-ref: "Ronneberger, Fischer, Brox 2015, MICCAI, §2-4, Figs. 1-2, eqs. 1-2, Tables 1-2"
tags: [ml, diffusion]
authors: ["[[Olaf Ronneberger]]", "[[Philipp Fischer]]", "[[Thomas Brox]]"]
year: 2015
venue: "MICCAI 2015"
file: "papers/Diffusion/Ronneberger, Fischer, Brox - U-Net Convolutional Networks for Biomedical Image Segmentation.pdf"
---

# U-Net paper (Ronneberger 2015)

**Summary**: A fully convolutional network with a contracting path, a symmetric expanding path and skip connections that concatenate high-resolution features into the decoder, for per-pixel biomedical segmentation. Heavy elastic-deformation augmentation and a border-weighted loss let it train from a few dozen annotated images. It won the ISBI 2012 EM segmentation ranking and the ISBI 2015 cell-tracking categories it entered. In this wiki it matters mainly because the same shape is the denoiser backbone of [[DDPM (Ho 2020)]].

**Authors**: Olaf Ronneberger, Philipp Fischer, Thomas Brox · **Year**: 2015 · **File**: `papers/Diffusion/Ronneberger, Fischer, Brox - U-Net Convolutional Networks for Biomedical Image Segmentation.pdf`

---

## Problem

Classification CNNs output one label per image, but biomedical work needs a label per pixel, and only tens to hundreds of annotated images exist. The sliding-window net of Ciresan et al. localizes and multiplies the training set via patches, but is slow (redundant overlapping patches) and trades localization accuracy against context: large patches need more pooling, small patches see little context (source: U-Net.pdf, pp. 1-2).

## Method

Builds on the fully convolutional network of Long et al.: add layers where pooling is replaced by upsampling, and combine high-resolution contracting-path features with upsampled output so a later convolution can assemble a precise map (p. 2). See [[U-Net]] for the architecture as a method page.

### Architecture (§2, Fig. 1, p. 4)

- **Contracting path**: repeated two unpadded $3\times3$ convolutions, each followed by ReLU, then $2\times2$ max pooling with stride 2. Channels double at each downsampling.
- **Expansive path**: upsample, $2\times2$ "up-convolution" halving channels, concatenate the cropped feature map from the contracting path, two $3\times3$ convs with ReLU. Cropping is needed because every unpadded conv loses border pixels.
- **Head**: $1\times1$ conv maps each 64-component vector to the class count. 23 conv layers in total, no fully connected layers.
- **Tiling**: input tile size must make every max-pool act on an even-sized map. Because only valid convolution outputs are kept, arbitrarily large images are segmented by the overlap-tile strategy, extrapolating missing border context by mirroring (Fig. 2, p. 3).

### Loss and weight map (§3, eqs. 1-2, pp. 4-5)

Pixel-wise softmax over the final map, $p_k(x)=\exp(a_k(x))/\sum_{k'=1}^K\exp(a_{k'}(x))$, with weighted cross entropy

> [!definition] Weighted cross entropy
> $$E=\sum_{x\in\Omega}w(x)\,\log p_{\ell(x)}(x)$$
> where $\ell:\Omega\to\{1..K\}$ is the true label. The paper writes it with this sign and minimizes it as the energy; the usual convention is the negative of this expression (**Wiki note**).
>
> (source: eq. 1, p. 4)

> [!definition] Border weight map
> $$w(x)=w_c(x)+w_0\exp\!\Big(-\frac{(d_1(x)+d_2(x))^2}{2\sigma^2}\Big)$$
> $w_c$ balances class frequencies; $d_1,d_2$ are distances to the nearest and second-nearest cell border. $w_0=10$, $\sigma\approx5$ px. Forces the net to learn the thin background gaps between touching cells.
>
> (source: eq. 2, p. 5)

### Training details

- [[SGD]] in Caffe with batch size one image (large tiles preferred over large batches) and high [[Momentum]] 0.99 (p. 4).
- Initialization: Gaussian with standard deviation $\sqrt{2/N}$, $N$ the number of incoming nodes (e.g. $N=9\cdot64=576$ for a $3\times3$ conv on 64 channels), so feature maps have about unit variance with conv+ReLU (p. 5). See [[Weight initialization]].
- **Data augmentation** (§3.1, pp. 5-6): shifts, rotations, gray-value changes and, above all, random elastic deformations from displacement vectors on a coarse $3\times3$ grid (Gaussian, 10 px standard deviation, bicubic per-pixel interpolation). [[Dropout]] layers at the end of the contracting path add implicit augmentation. See [[Convolutional neural network]] for augmentation as a prior.

## Results

- **EM segmentation (ISBI 2012)** (Table 1, p. 6): 30 training images of $512\times512$. U-Net averaged over 7 rotations: warping error 0.000353 (rank 1, 2015-03-06), Rand error 0.0382, pixel error 0.0611. Ciresan et al.: 0.000420 / 0.0504 / 0.0613. Human: 0.000005 / 0.0021 / 0.0010. Methods with lower Rand error use dataset-specific post-processing of the Ciresan probability map.
- **ISBI cell tracking 2015** (Table 2, p. 7), mean IOU: PhC-U373 0.9203 (second best 0.83); DIC-HeLa 0.7756 (second best 0.46).
- Speed: a $512\times512$ image segments in under a second; training takes 10 hours on an NVIDIA Titan (6 GB) (abstract and p. 7).

## Limitations

The paper lists none beyond the data-hungry caveat it addresses; it asserts applicability to many more tasks without evidence beyond the three datasets. Wiki note: the unpadded design shrinks the output relative to the input and needs the cropping and mirror-tiling machinery; most later users (including the diffusion denoisers below) use padded convolutions instead **[unverified against the cited sources]**.

## Connections

- Credits [[AlexNet (Krizhevsky 2012)]] for the breakthrough that made large supervised CNNs work (p. 1).
- Skip connections that concatenate encoder features into the decoder are the feature that distinguishes it from a plain encoder-decoder. Residual shortcuts in [[ResNet]] add instead of concatenate.
- Reused as the noise-prediction network $\epsilon_\theta$ in [[DDPM (Ho 2020)]] (PixelCNN++-style U-Net with Wide ResNet blocks, group norm, time embedding and self-attention at 16x16). The [[FNO (Li 2021)]] and [[Neural operator (Kovachki 2022)]] tables use a U-Net as a baseline.

%% refs:start %%
**Cites in this wiki**: [[AlexNet (Krizhevsky 2012)]]
**Cited by in this wiki**: [[Bayesian DenseED surrogate (Zhu 2018)]], [[DDIM (Song 2021)]], [[DDPM (Ho 2020)]], [[FNO (Li 2021)]], [[Neural operator (Kovachki 2022)]]
**Software cited**: [[software#Caffe|Caffe]]
%% refs:end %%

**Sources**: `papers/Diffusion/Ronneberger, Fischer, Brox - U-Net Convolutional Networks for Biomedical Image Segmentation.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[U-Net]] · [[Convolutional neural network]] · [[ReLU]] · [[Dropout]] · [[Diffusion models]] · [[DDPM (Ho 2020)]] · [[AlexNet (Krizhevsky 2012)]]
