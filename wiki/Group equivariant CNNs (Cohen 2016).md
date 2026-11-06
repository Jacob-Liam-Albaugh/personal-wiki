---
type: paper
area: symmetry
areas: [symmetry, ml]
source-ref: "Cohen & Welling 2016, ICML, arXiv:1602.07576, §4-8"
tags: [symmetry, ml]
authors: ["[[Taco S. Cohen]]", "[[Max Welling]]"]
year: 2016
venue: "ICML 2016 (PMLR 48); arXiv:1602.07576"
file: "papers/Symmetries/Welling, Cohen - Group Equivariant CNNs.pdf"
---

# Group equivariant CNNs (Cohen 2016)

**Summary**: Generalises convolution from translations to a larger symmetry group $G$ (90-degree rotations and mirror flips on a square grid). Feature maps become functions on the group, and every layer is shown to commute with $G$. Replacing ordinary convolutions with p4 or p4m convolutions improved results on rotated MNIST and CIFAR10 at roughly fixed parameter count.

**Authors**: Taco S. Cohen, Max Welling · **Year**: 2016 · **File**: `papers/Symmetries/Welling, Cohen - Group Equivariant CNNs.pdf`

---

## Idea

Ordinary convolution layers share weights across translations and are translation equivariant, so the symmetry is preserved through depth. G-CNNs do the same for a bigger group (source: Cohen PDF, p. 1). This gives a higher degree of weight sharing and more expressive capacity at the same parameter count.

Equivariance of a layer $\Phi$:

$$\Phi(T_g x)=T'_g\,\Phi(x)$$

(source: eq. 1, p. 2). Invariance is the special case $T'_g=\text{id}$. The paper argues that general equivariance is more useful than invariance, since invariant features cannot tell whether features are in the right spatial configuration (source: p. 2).

## Groups

- $\mathbb Z^2$: integer translations, the group of an ordinary CNN.
- **p4**: translations plus rotations by 90 degrees, with $g(r,u,v)$, $0\le r<4$, $(u,v)\in\mathbb Z^2$. The group operation is matrix multiplication (source: §4.2).
- **p4m**: p4 plus mirror reflections, $g(m,r,u,v)$ with $m\in\{0,1\}$ (source: §4.3).

Feature maps are functions $f:\mathbb Z^2\to\mathbb R^K$. A transformation acts by

$$[L_g f](x)=f(g^{-1}x)$$

(source: eq. 4), and $L_gL_h=L_{gh}$. In a G-CNN, hidden feature maps are functions on $G$ itself. A p4 map has four planar patches (one per rotation), and a p4m map has eight.

## Why ordinary CNNs fail for rotations

Correlation commutes with translation:

$$[L_tf]\star\psi=L_t[f\star\psi]$$

but rotating the input is not the same as rotating the output. In fact

$$[L_rf]\star\psi=L_r\big[f\star[L_{r^{-1}}\psi]\big]$$

(source: §5). So a CNN that learns rotated copies of a filter has an equivariant stack, but individual maps are not equivariant.

## Layers

**G-correlation.** First layer, input on $\mathbb Z^2$:

$$[f\star\psi](g)=\sum_{y\in\mathbb Z^2}\sum_k f_k(y)\,\psi_k(g^{-1}y)$$

(source: eq. 10). Later layers, input and filter on $G$:

$$[f\star\psi](g)=\sum_{h\in G}\sum_k f_k(h)\,\psi_k(g^{-1}h)$$

(source: eq. 11). Equivariance follows from the substitution $h\to uh$ (eq. 12).

**Nonlinearities.** A pointwise nonlinearity is post-composition with $\nu$. It commutes with $L_h$, which acts by pre-composition (source: eq. 14-15).

**Pooling.** Max-pooling over a neighbourhood commutes with $L_h$ (eq. 16-17). Strided pooling is subsampling on a subgroup $H$, and the result is equivariant to $H$ only. Pooling over the cosets $gH$ gives a map on the quotient $G/H$. Example: pooling over the four rotations of a p4 map gives a function on $\mathbb Z^2\cong p4/R$, which transforms like the input image (source: §6.3).

**Other layers.** Biases and batch normalisation need one parameter per G-feature map, not per planar slice. Sums of equivariant maps are equivariant, so residual blocks are compatible (source: p. 5).

## Implementation

For a split group, $g=ts$ with $t$ a translation and $s$ in the stabiliser of the origin. Then

$$f\star\psi(ts)=\sum_h\sum_k f_k(h)\,L_t[L_s\psi_k(h)]$$

(source: eq. 18). Method: transform the filter by all $s$ (a cheap permutation of entries), then call an ordinary fast planar correlation on the enlarged filter bank. The cost is about that of a planar convolution with the enlarged bank (source: §7). Filter array shape is $K_l\times K_{l-1}\times S_{l-1}\times n\times n$, with $S=1,4,8$ for $\mathbb Z^2$, p4, p4m.

## Results

- Rotated MNIST (62000 digits; train 10000, validation 2000, test 50000). Test errors: Z2CNN 5.03%, P4CNN with rotation pooling after every layer 3.21%, P4CNN 2.28%, previous best 3.98% (source: Table 1, §8.1). Filters were halved to keep parameters fixed.
- The comparison supports the claim that premature invariance hurts: pooling over rotations in intermediate layers was clearly worse than keeping equivariance until the end.
- CIFAR10: All-CNN Z2 / p4 / p4m error 9.44 / 8.84 / 7.59 (plain), 8.86 / 7.67 / 7.04 (augmented). ResNet44 Z2 9.45 / 5.61 versus p4m 6.46 / 4.94 (source: Table 2; column alignment of the extracted table is my reading). A wider p4m ResNet reached 4.19% against 5.27% for planar convolution (source: p. 8).
- G-CNNs gain from data augmentation as long as the augmentation group is larger than $G$ (source: §9).

## Wiki note

- The continuous-group and 3D successor is [[e3nn]]. See [[e3nn Euclidean networks (Geiger 2022)]].
- The paper's scattering-network related work uses wavelets plus group averaging; compare [[Wavelet transform]].
- A GAN version of the same idea is [[Group equivariant GANs (Dey 2021)]].

%% refs:start %%
**Cited by in this wiki**: [[Deep Sets paper (Zaheer 2017)]], [[Group equivariant GANs (Dey 2021)]], [[Rotation augmentation for CNNs (Quiroga 2018)]]
%% refs:end %%

**Sources**: Cohen PDF, §1-9.

**Last updated**: 2026-11-06

---

## Related pages
- [[Group equivariant CNN]]
- [[Equivariance]]
- [[e3nn]]
- [[Group equivariant GANs (Dey 2021)]]
- [[Rotation augmentation for CNNs (Quiroga 2018)]]
- [[Discretization invariance]]
