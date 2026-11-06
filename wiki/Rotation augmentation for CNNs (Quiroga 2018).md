---
type: paper
area: symmetry
areas: [symmetry, ml]
source-ref: "Quiroga et al., Revisiting Data Augmentation for Rotational Invariance in CNNs, pp. 1-16"
tags: [symmetry, ml]
authors: ["[[Facundo Quiroga]]", "[[Franco Ronchetti]]", "[[Laura Lanzarini]]", "[[Aurelio Fernandez-Bariviera]]"]
year: 2018
venue: "not printed in the PDF text; year unverified"
file: "Symmetries/Quiroga, Ronchetti - Data Augmentaion for Rotational Invariance in CNNs.pdf"
---

# Rotation augmentation for CNNs (Quiroga 2018)

**Summary**: Random-rotation data augmentation alone lets plain CNNs classify rotated MNIST and CIFAR10 nearly as well as unrotated data. Spatial Transformer Networks and group CNNs give no significant accuracy gain at equal parameter count. The cost of augmentation is training time only.

**Authors**: Facundo Quiroga, Franco Ronchetti, Laura Lanzarini, Aurelio Fernandez-Bariviera · **Year**: 2018 **[unverified]** · **File**: `Symmetries/Quiroga, Ronchetti - Data Augmentaion for Rotational Invariance in CNNs.pdf`

---

## Claim

Convolutional layers are translation equivariant by design but lack other invariances (source: p. 1, abstract). The paper asks how best to add rotation invariance for image classification. Answer: train with rotated copies of the data (source: abstract).

## Setup

- Networks: SimpleConv (F=32, D=64 for MNIST; F=64, D=128 for CIFAR10) and AllConvolutional (F=16 for MNIST; F=96 for CIFAR10).
- Optimiser: Adam, learning rate $10^{-4}$.
- Datasets: MNIST and CIFAR10, with a rotated variant (random angle in 0-360 degrees).
- Specialised comparators, with parameter count held fixed:
  - Spatial Transformer Networks with a rotation-only localisation network.
  - Group CNN variants ([[Group equivariant CNNs (Cohen 2016)]], p4m), halved in parameters to match.

## Results

- MNIST: nets trained on rotated data lose only about 1-2% on unrotated test data.
- MNIST: nets trained on unrotated data drop about 55% on rotated tests (about 40% accuracy against 10% chance).
- CIFAR10: the drop is larger. AllConvolutional reached about 80% versus the original authors' 91%, because epochs were reduced.
- STN and group CNNs: no significant accuracy increase over augmentation (source: pp. 9-11, Fig. 4).
- The unrotated-trained AllGConv model generalises better to rotations (+0.1) than other models, but SimpleGConv does not. The authors attribute this to fully convolutional layers compensating for poor filters (source: p. 11).

## Retraining experiment

A base model is trained on unrotated data, copied, then some layers are retrained on rotated data (source: §3.3, p. 12).

- Retraining higher layers, nearer the output, recovers accuracy best (source: p. 13).
- This implies lower layers hold redundant information from which rotated versions can be reconstructed. Either the filters are naturally equivariant or equivariance of filters matters little.
- Retraining only the final layer does worse. For SimpleConv, the previous fully connected layer may collapse equivariances. For AllConv, the final $1\times1$ convolution to 10 maps cannot recapture them.
- CIFAR10 follows the same trend at lower accuracy (source: p. 13-14).

## Conclusions

- Augmentation needs more training but reaches similar accuracy; test time is not affected by extra localisation networks or convolutions (source: §4, p. 14).
- Invariance should be added late in the network where possible (source: pp. 14-15).
- Open items: deliberately placing invariance early or late; comparing learned filters for equivariance; datasets with natural rotations; constrained parameter budgets (source: p. 15).

## Wiki note

This is the empirical counterpoint to built-in [[Equivariance]]: the architectural route ([[Group equivariant CNN]], [[e3nn]]) buys data efficiency and exactness, while augmentation buys simplicity. Only classification accuracy on small image sets is tested, so conclusions for physics-style regression are not covered.





%% refs:start %%
**Cites in this wiki**: [[Group equivariant CNNs (Cohen 2016)]]
%% refs:end %%

**Sources**: Quiroga et al. PDF (pp. 1-16).
**Last updated**: 2026-11-06

---

## Related pages
- [[Equivariance]]
- [[Group equivariant CNN]]
- [[Group equivariant CNNs (Cohen 2016)]]
- [[e3nn Euclidean networks (Geiger 2022)]]
- [[Group equivariant GANs (Dey 2021)]]
