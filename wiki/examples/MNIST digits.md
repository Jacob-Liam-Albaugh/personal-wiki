---
type: example
area: me697
areas: [me697, me539]
source-ref: "ASML (ME 697); Intro SciML (ME 539)"
tags: [ml, generative]
data-origin: [real]
tasks: [classification, dimensionality reduction, generative, clustering]
uses: 7
---

# MNIST digits

**Summary**: 7 uses in ASML (ME 697) and Intro SciML (ME 539). Data: real. Tasks: classification, dimensionality reduction, generative, clustering.

**Covered in**: ASML (ME 697), Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ml-software/optimization/09_gpu_training.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## MNIST CNN classification

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ml-software/optimization/09_gpu_training.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: classification
- **Technique**: AdamW lr 3e-4, batch 64, MAX_STEPS=100, seed 5678; CPU vs GPU timing
- **Data**: 60000 train and 10000 test images, 28x28 grayscale, 10 classes
- **Data origin**: real
- **Data file**: torchvision MNIST (downloaded at runtime)
- **Forward model**: CNN: Conv2d(1,32,3)-ReLU-MaxPool2-Conv2d(32,64,3)-ReLU-MaxPool2-flatten(30976)-Linear(128)-ReLU-Linear(10)-log_softmax; Equinox/JAX
- **Unknown dimension**: ~4M parameters (30976\*128 dominant)
- **Data dimension**: 28x28 images, 10 classes
- **Ground truth**: held-out test set
- **Libraries**: JAX, Equinox, Optax, torchvision
- **Notes**: Reported: CPU 5m28.7s, test acc ~0.939 at step 90; GPU 31.7s, acc ~0.938 (about 10x; text says 5-10x).

## PCA on toy Gaussian and MNIST

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/hup/funcin/03_pca.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: dimensionality reduction
- **Technique**: centered SVD PCA, 2D projection coloured by digit, explained variance threshold 0.9
- **Data**: Toy 2D correlated Gaussian (Cholesky of [ [1,.9],[.9,1]], mean [3,3], 500 samples); MNIST 70000 x 784.
- **Data origin**: real
- **Data file**: sklearn fetch_openml('mnist_784'); toy data generated
- **Forward model**: none
- **Unknown dimension**: number of components
- **Data dimension**: 70000 x 784
- **Ground truth**: digit labels
- **Libraries**: numpy, scikit-learn, matplotlib
- **Notes**: Bug: explained variance uses cumsum(S)/sum(S), not S^2. Near-duplicate of the other PCA notebook (typo only).

## PCA on toy Gaussian and MNIST

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/reduced_order_modeling/02_pca.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: dimensionality reduction
- **Technique**: centered SVD PCA, 2D projection coloured by digit, explained variance threshold 0.9
- **Data**: Toy 2D correlated Gaussian (Cholesky of [ [1,.9],[.9,1]], mean [3,3], 500 samples); MNIST 70000 x 784.
- **Data origin**: real
- **Data file**: sklearn fetch_openml('mnist_784'); toy data generated
- **Forward model**: none
- **Unknown dimension**: number of components
- **Data dimension**: 70000 x 784
- **Ground truth**: digit labels
- **Libraries**: numpy, scikit-learn, matplotlib
- **Notes**: Bug: explained variance uses cumsum(S)/sum(S), not S^2. Near-duplicate of the other PCA notebook (typo only).

## MNIST autoencoder

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/homework/01_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: dimensionality reduction
- **Technique**: Adam 1e-3, batch 32; GMM with 10 components on latent space
- **Data**: MNIST digits 784-pixel; test 10000, val 10000.
- **Data origin**: real
- **Data file**: fetch_openml mnist_784
- **Forward model**: Autoencoder 784 -> 2 latent -> 784, 2x128 ReLU layers.
- **Unknown dimension**: network weights
- **Data dimension**: 784
- **Ground truth**: held-out test/validation sets
- **Libraries**: jax, equinox, optax, sklearn
- **Notes**: Problem 5.

## MNIST PCA on the digit 3

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/18 - Dimensionality Reduction/hands-on-18.1.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: dimensionality reduction
- **Technique**: PCA n_components=0.98 (227 kept), eigen-images, reconstruction error vs components
- **Data**: 70000 handwritten digit images, 784 pixels scaled to [0,1]; 70/30 split seed 0 (49000 train); only threes used
- **Data origin**: real
- **Data file**: fetch_openml mnist_784 (not in data/)
- **Unknown dimension**: 227 retained components
- **Data dimension**: 784
- **Ground truth**: digit labels unused; validation reconstruction error
- **What makes it hard**: high-dimensional, linear PCA only
- **Libraries**: sklearn
- **References**: MNIST (LeCun)

## MNIST PCA to 2D plus k-means over all digits

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/18 - Dimensionality Reduction/hands-on-18.2.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: dimensionality reduction + clustering
- **Technique**: PCA(2), KMeans(10), Voronoi plot, centres shown as digits
- **Data**: same 70000 MNIST images, all ten digits
- **Data origin**: real
- **Data file**: fetch_openml mnist_784
- **Unknown dimension**: 2 components, 10 centres
- **Data dimension**: 784
- **Ground truth**: digit labels for judging clusters
- **What makes it hard**: 2D projection overlaps classes
- **Libraries**: sklearn

## MNIST threes: PCA + GMM generative sampling

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/18 - Dimensionality Reduction/hands-on-18.3.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: density estimation / generative sampling
- **Technique**: PCA(2), GMM with BIC over 1-10 components, sample then pca.inverse_transform
- **Data**: MNIST threes only
- **Data origin**: real
- **Data file**: fetch_openml mnist_784
- **Unknown dimension**: GMM parameters in 2D latent
- **Data dimension**: 784
- **Ground truth**: none; visual realism
- **What makes it hard**: samples are blurry because PCA is linear
- **Libraries**: sklearn

## Related pages
- [[Examples catalogue]]
- [[Principal component analysis]] · [[Singular value decomposition]] · [[Adam]] · [[Convolutional neural network]] · [[VAE]]
