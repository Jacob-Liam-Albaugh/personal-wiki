---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [ml]
data-origin: [real]
tasks: [classification]
uses: 1
---

# CIFAR10

**Summary**: 1 use in Intro SciML (ME 539). Data: real. Tasks: classification.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/intro-to-scientific-machine-learning/notebooks/25 - Deep Neural Networks Continued/hands-on-25.ipynb`.
**Last updated**: 2026-11-18

---

## CIFAR10 image classification

`text_books/intro-to-scientific-machine-learning/notebooks/25 - Deep Neural Networks Continued/hands-on-25.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: classification
- **Technique**: dense 3072-1176-400-120-84-10 (2 epochs) and LeNet-style CNN (5 epochs), SGD lr 0.001 momentum 0.9, per-class accuracy
- **Data**: 60000 32x32x3 images, 10 classes, 6000 each, 10000 test; normalised to [-1,1]
- **Data origin**: real
- **Data file**: torchvision download ./data/cifar-10-batches-py
- **Data dimension**: 3072
- **Ground truth**: class labels, test set
- **What makes it hard**: dense net weak, CNN better
- **Libraries**: torch, torchvision
- **References**: Krizhevsky, cs.toronto.edu/~kriz/cifar.html

## Related pages
- [[Examples catalogue]]
- [[Momentum]] · [[SGD]] · [[Convolutional neural network]]
