---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [operators, uq]
data-origin: [simulated, real]
tasks: [operator learning, uncertainty propagation]
uses: 2
---

# Darcy flow FNO

**Summary**: 2 uses in ASML (ME 697). Data: simulated, real. Tasks: operator learning, uncertainty propagation.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/homework/05_homework.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Darcy flow operator learning (FNO)

`text_books/advanced-scientific-machine-learning/book/homework/05_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: operator learning
- **Technique**: FNO via neuraloperator or JAX; L2 error
- **Data**: Binary permeability inputs to pressure; 16x16 train (n_train=1000), tests 16x16 (100) and 32x32 (50).
- **Data origin**: simulated
- **Data file**: neuralop darcy_train_16.pt, darcy_test_16.pt, darcy_test_32.pt
- **Forward model**: div(K grad p)=f, K takes two values.
- **Ground truth**: held-out test sets, zero-shot 32x32
- **What makes it hard**: Resolution generalisation
- **Libraries**: neuraloperator, torch
- **Notes**: Problem 4A.

## Darcy flow uncertainty propagation through FNO

`text_books/advanced-scientific-machine-learning/book/homework/05_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: uncertainty propagation
- **Technique**: tinygp GP ExpSquared scale 0.2 diag 0.5 conditioned on observation, thresholded; 1000 samples; argmax-pressure heatmap
- **Data**: 24x24 binary (0/1) noisy permeability observation.
- **Data origin**: real
- **Data file**: data/darcy_flow/obs_24x24.npy
- **Forward model**: Trained FNO from 4A.
- **Unknown dimension**: 576 pixels
- **Ground truth**: none
- **Libraries**: tinygp, jax
- **Notes**: Problem 4B. Resolution 24x24 differs from training 16/32.

## Related pages
- [[Examples catalogue]]
- [[FNO]] · [[Operator learning]] · [[Gaussian process]] · [[Darcy flow]]
