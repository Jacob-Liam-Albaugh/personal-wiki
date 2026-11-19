---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [ml, optimization]
data-origin: [synthetic, analytic]
tasks: [regression, optimization]
uses: 8
---

# Optimizer test problems

**Summary**: 8 uses in ASML (ME 697). Data: synthetic, analytic. Tasks: regression, optimization.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ml-software/differentiation/04_jax_grad.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## RBF regression of noisy cubic

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ml-software/differentiation/04_jax_grad.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: regression
- **Technique**: jax.grad of MSE w.r.t. w, c, sigma2; plain gradient descent, 10000 iterations, lr=0.01
- **Data**: 20 points, x~U(-1,1), y=x^3+0.1\*N(0,1)
- **Data origin**: synthetic
- **Forward model**: Generalized linear model f(x)=sum_i w_i exp(-/x-c_i/^2/sigma2) with 10 RBF centres on [-1,1], sigma2=0.01 initially; MSE loss; implemented in JAX
- **Unknown dimension**: 10 weights (+10 centres + sigma2 when also differentiated)
- **Data dimension**: 20
- **Ground truth**: true function x^3 known
- **Libraries**: JAX, matplotlib
- **Notes**: Only w is updated in the GD loop; a later cell re-initialises sigma2=0.1 and random centres. Mainly demonstrates grad w.r.t. several arguments.

## Quartic test functions (1D and 2D with saddle)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ml-software/optimization/02_gradient_descent.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: optimization
- **Technique**: gradient descent with fixed lr; Armijo backtracking line search (c1=0.1, c2=0.9, lr=0.3)
- **Data origin**: analytic
- **Forward model**: 1D f(x)=x^4-3x^3+2 (starts -0.5, 0.5, 2.8; lr 0.01 and 0.1; 100 iters). 2D f(x)=x1^4-2x1^2+x2^2 with minima at x1=+-1 and a saddle/maximum along x1 at (0,0); starts (-1.5,-1.5),(0,1),(0.01,1),(1.5,1.5), lr 0.1, 50 iters. JAX grad.
- **Unknown dimension**: 1 and 2
- **Ground truth**: analytic minima known
- **What makes it hard**: non-convexity, saddle point, lr sensitivity (divergence at large lr)
- **Libraries**: JAX
- **Notes**: Gradient stuck at the saddle when started exactly on x1=0.

## Quartic test functions with momentum

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ml-software/optimization/03_momentum.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: optimization
- **Technique**: heavy-ball momentum (alpha=0.1, beta=0.5, 100 iters) and Nesterov momentum
- **Data origin**: analytic
- **Forward model**: Same 1D and 2D quartics as 02_gradient_descent
- **Unknown dimension**: 1 and 2
- **Ground truth**: analytic minima known
- **What makes it hard**: saddle trapping when started exactly at x1=0
- **Libraries**: JAX
- **Notes**: 1D optimum quoted as 9/4.

## Quartic 2D function with optax SGD

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ml-software/optimization/04_optax.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: optimization
- **Technique**: optax.sgd(lr 0.1, momentum 0.5, nesterov); initial momentum injected via optax.TraceState(trace=[0.1,0.0]) to escape the saddle
- **Data origin**: analytic
- **Forward model**: f(x)=x1^4-2x1^2+x2^2
- **Unknown dimension**: 2
- **Ground truth**: analytic minima at x1=+-1, x2=0
- **What makes it hard**: saddle at origin
- **Libraries**: JAX, Optax

## Quadratic regression (SGD)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ml-software/optimization/05_sgd.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: regression
- **Technique**: online SGD with Nesterov (lr 0.01, mom 0.5, 20 epochs); exponential_decay(0.01, 20\*N, 0.01) schedule; minibatch size 10, 50 epochs with decay
- **Data**: Synthetic quadratic regression: N=1000, X~N(0,1), y=1.5X^2-2X+0.5\*N(0,1); test set of 50 points on linspace(-3,3), noisy. Generated in-notebook.
- **Data origin**: synthetic
- **Forward model**: Equinox model theta0+theta1\*x+theta2\*x^2 (3 params), MSE loss; JAX
- **Unknown dimension**: 3
- **Data dimension**: 1000 train, 50 test
- **Ground truth**: true coefficients known (intercept 0, linear -2, quadratic 1.5)
- **Libraries**: JAX, Equinox, Optax
- **Notes**: Without lr decay SGD wiggles and does not converge. Theta_0/theta_1 axis labels in the 2D plot do not match coefficient order (bug).

## Quadratic regression (adaptive optimizers)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ml-software/optimization/06_adaptive.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: regression
- **Technique**: Adam (lr 0.01, b1 0.9, b2 0.999, eps 1e-8), batch 10, 20 epochs
- **Data**: Same generator as 05_sgd: Synthetic quadratic regression: N=1000, X~N(0,1), y=1.5X^2-2X+0.5\*N(0,1); test set of 50 points on linspace(-3,3), noisy. Generated in-notebook.
- **Data origin**: synthetic
- **Forward model**: Quadratic model, 3 params; JAX/Equinox
- **Unknown dimension**: 3
- **Data dimension**: 1000 train, 50 test
- **Ground truth**: true coefficients known
- **Libraries**: JAX, Equinox, Optax
- **Notes**: AdaGrad, RMSProp, delta-bar-delta only described in text.

## Quadratic regression (second order)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ml-software/optimization/07_second_order.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: regression
- **Technique**: hand-written damped Newton-Raphson (alpha=0.5, 10 iters; converges in one step with alpha=1) and jaxopt.LBFGS (maxiter=10, 20 outer iterations)
- **Data**: Same generator as 05_sgd: Synthetic quadratic regression: N=1000, X~N(0,1), y=1.5X^2-2X+0.5\*N(0,1); test set of 50 points on linspace(-3,3), noisy. Generated in-notebook.
- **Data origin**: synthetic
- **Forward model**: Quadratic model, 3 params; jax.hessian
- **Unknown dimension**: 3
- **Data dimension**: 1000
- **Ground truth**: true coefficients known
- **Libraries**: JAX, jaxopt
- **Notes**: Loss is quadratic in parameters so Newton is exact in one step.

## Weight initialization on 1D regression with MLP

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ml-software/optimization/08_initialization.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: regression
- **Technique**: compares zero init (dying ReLU, zero gradients), constant 0.1 init (symmetry), Xavier/Glorot uniform (bias 0.1), He/default Equinox init; Adam 0.01, batch 100, 100 epochs; gradient histograms
- **Data**: Same generator as 05_sgd: Synthetic quadratic regression: N=1000, X~N(0,1), y=1.5X^2-2X+0.5\*N(0,1); test set of 50 points on linspace(-3,3), noisy. Generated in-notebook.
- **Data origin**: synthetic
- **Forward model**: Equinox MLP Linear(1,10)-ReLU-Linear(10,10)-ReLU-Linear(10,1): 2 hidden layers of width 10 (markdown says 3 hidden layers)
- **Unknown dimension**: ~220 weights
- **Data dimension**: 1000
- **Ground truth**: true function known
- **What makes it hard**: initialization pathologies (dead units, symmetry)
- **Libraries**: JAX, Equinox, Optax
- **Notes**: Notebook itself notes a polynomial would be a better model.

## Related pages
- [[Examples catalogue]]
- [[Sensitivity analysis]] · [[Adam]] · [[Momentum]] · [[SGD]] · [[Newton's method]] · [[Weight initialization]]
