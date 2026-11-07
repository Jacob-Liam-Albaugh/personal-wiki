# Source inventory

Every source file under `papers/`, `courses/` and `text_books/` and its ingest status. Status values: **ingested** (source page exists), **queued** (not yet read), **reference** (textbook; ingested by chapter on request), **alias** (Finder alias, ~1 KB, not a PDF), **duplicate** (another copy is the canonical source).

Regenerate the file list when files are added; keep the status column in sync on every ingest.

## papers/PSL Reading Group

| File | Pages | Status | Notes |
|---|---|---|---|
| `26.10.22 - DeepONets.pdf` | 12 | ingested → [[DeepONet (Lu 2021)]] |  |
| `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf` | 39 | ingested → [[Markovian homogenized viscoelasticity (Bhattacharya 2023)]] |  |

## papers/Bayesian

| File | Pages | Status | Notes |
|---|---|---|---|
| `Baysian Data Analysis 3rd ed` |  | alias | points to text_books/Mathmatics/Baysian Data Analysis 3rd ed.pdf |
| `Bilionis, Alberts - Physics Informed Information Field Theory.pdf` | 32 | ingested → [[PIFT (Alberts 2023)]] | arXiv preprint of the JCP 2023 paper in papers/IFT/ |
| `Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf` | 49 | ingested → [[Amortized VI for inverse problems (Karumuri 2024)]] |  |
| `Bilionis, Lee, Buganza - Propagation of Uncertainty in Tissues Reponse via multi-fidelity GP Regression` |  | alias | points to papers/Guassian Processes/ copy |
| `Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf` | 23 | ingested → [[Variational inverse problems (Tsilifis 2014)]] |  |
| `Chen, Xu, Li, Duvenaud - inf Deep Bayseian NN with Stochastic Diff. Eqns.pdf` | 18 | ingested → [[SDE-BNN (Xu 2022)]] |  |
| `Fortuin - Priors in Bayesian Deep Learning.pdf` | 28 | ingested → [[Priors in Bayesian deep learning (Fortuin 2022)]] |  |
| `Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf` | 14 | ingested → [[VAE paper (Kingma 2014)]] |  |
| `Kingma, Welling - Intro to Variational Autoencoders.pdf` | 44 | ingested → [[Intro to VAEs (Kingma 2019)]] | incomplete: front matter, ch. 1 and appendix only; ch. 2-5 missing |
| `Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick.pdf` | 9 | ingested → [[Variational dropout (Kingma 2015)]] | main text only; appendices A-F missing |
| `Margossian, Blei - Amortized Variational Inference When & Why.pdf` | 16 | ingested → [[Amortized VI when and why (Margossian 2024)]] |  |
| `Welling, Teh - Baysian Learning via Stochastic Gradient Langevin Dynamics.pdf` | 8 | ingested → [[SGLD (Welling 2011)]] | duplicate (identical file) of the papers/IFT/ copy |
| `Zhu, Zabaras - Bayseian Deep Convolutional Encoder-Decoder Networks for Surrogate Modeling and Uncertainty Quantification.pdf` | 52 | ingested → [[Bayesian DenseED surrogate (Zhu 2018)]] |  |

## papers/DSL

| File | Pages | Status | Notes |
|---|---|---|---|
| `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf` | 16 | ingested → [[Polynomial equipment interfaces (Bilionis 2026)]] |  |

## papers/Diffusion

| File | Pages | Status | Notes |
|---|---|---|---|
| `Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf` | 25 | ingested → [[DDPM (Ho 2020)]] |  |
| `Ho, Salimans - Classifier-Free Diffusion Guidance.pdf` | 14 | ingested → [[Classifier-free guidance (Ho 2022)]] |  |
| `Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf` | 77 | ingested → [[Step-by-step diffusion (Nakkiran 2025)]] |  |
| `Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP) - Supplementary.pdf` | 25 | ingested → [[CLIP (Radford 2021)]] |  |
| `Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP).pdf` | 16 | ingested → [[CLIP (Radford 2021)]] |  |
| `Ronneberger, Fischer, Brox - U-Net Convolutional Networks for Biomedical Image Segmentation.pdf` | 8 | ingested → [[U-Net paper (Ronneberger 2015)]] |  |
| `Song et al - Score-Based Generative Modeling through Stochastic Differential Equations.pdf` | 36 | ingested → [[Score SDE (Song 2021)]] | same ICLR 2021 text as the papers/Stochastic Methods/ copy (different file bytes) |
| `Song, Meng, Ermon - Denoising Diffusion Implicit Models.pdf` | 22 | ingested → [[DDIM (Song 2021)]] |  |
| `Wang - Generative priors for spatiotemporal turbulence.pdf` | 24 | ingested → [[Generative priors for turbulence (Wang 2026)]] | duplicate (identical file) of the papers/IFT/ copy |

## papers/Generative ML

| File | Pages | Status | Notes |
|---|---|---|---|
| `Goodfellow et al - Generative Adversarial Nets.pdf` | 9 | ingested → [[GAN paper (Goodfellow 2014)]] |  |
| `Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations` |  | alias | points to papers/Stochastic Methods/ copy |

## papers/Guassian Processes

| File | Pages | Status | Notes |
|---|---|---|---|
| `Bilionis, Lee, Buganza - Propagation of Uncertainty in Tissues Reponse via multi-fidelity GP Regression.pdf` | 22 | ingested → [[Multi-fidelity GP for tissue expansion (Lee 2020)]] |  |
| `Duvenaud - Thesis - Automatic Model Construction with Gaussian Processes.pdf` | 157 | ingested → [[Duvenaud thesis (Duvenaud 2014)]] |  |
| `Gaussian Processes for Machine Learning` |  | alias | points to text_books/Mathmatics/Gaussian Processes for Machine Learning.pdf |
| `Greengard, O'Neil - Efficient reduced-rank methods for Gaussian processes with eigenfunction expansions.pdf` | 20 | ingested → [[Reduced-rank GPs (Greengard 2022)]] |  |
| `Kanagawa, Hennig, Sejdinovic, Sriperumbudur - GPs & Kernel Methods.pdf` | 64 | ingested → [[Gaussian processes and kernel methods (Kanagawa 2018)]] |  |
| `Matthews et al - Gaussian Process Behaviour in Wide Deep Neural Networks.pdf` | 36 | ingested → [[Wide networks as GPs (Matthews 2018)]] |  |

## papers/IFT

| File | Pages | Status | Notes |
|---|---|---|---|
| `Bilionis, Alberts - IFT Thermal Conductivity.pdf` | 25 | ingested → [[IFT thermal conductivity (Alberts 2026)]] |  |
| `Bilionis, Alberts - IFT.pdf` | 30 | ingested → [[PIFT (Alberts 2023)]] |  |
| `Ruqi Zhang - AMAGOLD.pdf` | 10 | ingested → [[AMAGOLD (Zhang 2020)]] |  |
| `Ruqi Zhang - Cyclical Stochastic Gradient MCMC.pdf` | 27 | ingested → [[Cyclical SG-MCMC (Zhang 2020)]] |  |
| `Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf` | 21 | ingested → [[Low-precision SGLD (Zhang 2022)]] |  |
| `Wang - Generative priors for spatiotemporal turbulence.pdf` | 24 | ingested → [[Generative priors for turbulence (Wang 2026)]] |  |
| `Welling - Bayesian Learning via Stochastic Gradient Langevin Dynamics.pdf` | 8 | ingested → [[SGLD (Welling 2011)]] |  |

## papers/LLMs

| File | Pages | Status | Notes |
|---|---|---|---|
| `Gu, Dao - Mamba.pdf` | 36 | ingested → [[Mamba (Gu 2023)]] |  |
| `LLMs - Attention is All You Need.pdf` | 15 | ingested → [[Attention is all you need (Vaswani 2017)]] |  |
| `LLMs - DeepSeek - MoE Language Model.pdf` | 52 | ingested → [[DeepSeek-V2 (DeepSeek-AI 2024)]] |  |
| `LLMs - DeepSeek - Multi-Head Latent Attention.pdf` | 16 | ingested → [[MHA2MLA (Ji 2025)]] |  |

## papers/ML

| File | Pages | Status | Notes |
|---|---|---|---|
| `Brunton, Proctor, Kutz - Discovering governing equations from data by sparse identification of nonlinear dynamical systems.pdf` | 6 | ingested → [[SINDy (Brunton 2016)]] |  |
| `Cranmer - PySR.pdf` | 24 | ingested → [[PySR (Cranmer 2023)]] |  |
| `Cranmer, Gonzalez, Ho - Discovering Symbolic Models from DL with Inductive Biases.pdf` | 14 | ingested → [[Symbolic models from deep learning (Cranmer 2020)]] |  |
| `Girolami, Calderhead - Riemann Manifold Langevin & Hamiltonian Monte Carlo Methods.pdf` | 92 | ingested → [[RMHMC (Girolami 2011)]] |  |
| `Glorot, Bengio - Understanding the Difficulty of Training DFFNN.pdf` | 8 | ingested → [[Glorot init (Glorot 2010)]] |  |
| `He, Zhang, Ren, Sun - ResNets.pdf` | 12 | ingested → [[ResNet paper (He 2016)]] |  |
| `Hinton, Srivastava, Krizhevsky, Sutskever, Salakhutdinov - Dropout.pdf` | 30 | ingested → [[Dropout paper (Srivastava 2014)]] |  |
| `Hinton, Sutskever, Martens, Dahl - On the Importance of Initialization and Momentum in DL.pdf` | 14 | ingested → [[Init and momentum (Sutskever 2013)]] |  |
| `Hornik, Stinchcombe, White - Multilayer Feedforward Networks are Universal Approximators.pdf` | 8 | ingested → [[Universal approximation (Hornik 1989)]] |  |
| `Jacot, Gabriel, Hongler - Neural Tangent Kernel Convergence and Generalization in Neural Networks.pdf` | 10 | ingested → [[NTK (Jacot 2018)]] |  |
| `Kingma, Lei Ba - Adam.pdf` | 15 | ingested → [[Adam paper (Kingma 2015)]] |  |
| `Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick` |  | alias | points to papers/Bayesian/ copy |
| `Krizhevsky et al - ImageNet Classification with Deep Convolutional Neural Networks.pdf` | 7 | ingested → [[AlexNet (Krizhevsky 2012)]] |  |
| `Rahaman et.al. - On the Spectrial Bias of NNs.pdf` | 23 | ingested → [[Spectral bias (Rahaman 2019)]] |  |
| `Schmidt, Lipson - Distilling Free-Form Natural Laws from Experimental Data.pdf` | 6 | ingested → [[Eureqa (Schmidt 2009)]] |  |
| `Sitzmann - SIREN - Implicit Neural Representations with Periodic Activation Functions.pdf` | 35 | ingested → [[SIREN paper (Sitzmann 2020)]] |  |
| `Sormani - How Riemannian Manifolds Converge.pdf` | 27 | ingested → [[Riemannian convergence (Sormani 2011)]] |  |
| `Tanicik, Srinivasan, Midenhall, et. al. - Fourier Features Let Netowrks Learn High Frequency Functions in Low Dimensional Domains.pdf` | 24 | ingested → [[Fourier features (Tancik 2020)]] |  |
| `Welling, Kipf - Variational Graph Auto-Encoders.pdf` | 3 | ingested → [[Variational graph auto-encoder (Kipf 2016)]] |  |
| `Zaheer, Kottur, Ravanbhakhsh, Poczos, Salakhutdinov, Smola - Deep Sets.pdf` | 29 | ingested → [[Deep Sets paper (Zaheer 2017)]] |  |

## papers/Math

| File | Pages | Status | Notes |
|---|---|---|---|
| `Convexity/Polyhedral_Representation_Theorem.pdf` | 3 | ingested → [[Polyhedral representation theorem (n.d.)]] |  |

## papers/Operators

| File | Pages | Status | Notes |
|---|---|---|---|
| `Gallon, Wurstemberger, Cheridito, Jentzen - Physics-Informed Diffusion Models in Spectral Space.pdf` | 18 | ingested → [[PISD (Gallon 2026)]] |  |
| `Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf` | 19 | ingested → [[LNO (Cao 2023)]] |  |
| `Karniadakis, Lu, Jin - DeepONets - Deep Operator Networks.pdf` | 22 | ingested → [[DeepONet (Lu 2021)]] | arXiv preprint of the Nature MI 2021 paper read in the reading group |
| `Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf` | 16 | ingested → [[FNO (Li 2021)]] |  |
| `Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf` | 97 | ingested → [[Neural operator (Kovachki 2022)]] |  |
| `Stuart - Operator Leraning - Algorithms and Analysis.pdf` | 36 | ingested → [[Operator learning review (Kovachki 2024)]] |  |

## papers/Physics Informed Architectures

| File | Pages | Status | Notes |
|---|---|---|---|
| `Bilionis, Alberts - Physics Informed Information Field Theory` |  | alias | points to papers/Bayesian/ preprint (same paper as papers/IFT/Bilionis, Alberts - IFT.pdf) |
| `Brunton, Bakarji, Champion, Kutz -SINDy - Discovering Governing Equations Deep Delay Autoencoders.pdf` | 23 | ingested → [[SINDy delay autoencoders (Bakarji 2022)]] |  |
| `Brunton, Champion, Lusch, Kutz - SINDy - Data-Driven Discovery of Coordinates and Governing Equations.pdf` | 26 | ingested → [[SINDy autoencoders (Champion 2019)]] |  |
| `Brunton, Otto, Kutz - ML in Viscoelastic Fluids via Kernel Embeding.pdf` | 32 | ingested → [[Energy-based kernels for viscoelastic flow (Otto 2024)]] |  |
| `Brunton, Pan, Kutz - NIF - Neural Implicit Flow.pdf` | 60 | ingested → [[NIF (Pan 2023)]] |  |
| `Chen, Rubanova, Bettencourt, Duvenaud - Neural ODEs.pdf` | 18 | ingested → [[Neural ODEs (Chen 2018)]] |  |
| `Costabal et al - Physics-Informed Neural Networks for Cardiac Activation Mapping.pdf` | 12 | ingested → [[Cardiac activation PINN (Sahli Costabal 2020)]] |  |
| `Cranmer, Greydanus, Ho - LNNs.pdf` | 9 | ingested → [[LNNs (Cranmer 2020)]] |  |
| `Greydanus, Dzamba, Yosinski - HNNs.pdf` | 16 | ingested → [[HNNs (Greydanus 2019)]] |  |
| `Karniadakis, Lu, Kevrekidis, Perdikaris - Physics-Informed Machine Learning.pdf` | 20 | ingested → [[Physics-informed ML review (Karniadakis 2021)]] |  |
| `Karniadakis, Raissi, Perdikaris - PINNs - Physics-Informed Neural Networks.pdf` | 45 | ingested → [[PINNs (Raissi 2019)]] |  |
| `Kissas et al - Machine learning in cardiovascular flows modeling Predicting arterial blood pressure from non-invasive 4D flow MRI data.pdf` | 28 | ingested → [[Cardiovascular flow PINNs (Kissas 2020)]] |  |
| `Lusch, Kutz, Brunton - Deep learning for universal linear embeddings of nonlinear dynamics.pdf` | 10 | ingested → [[Deep Koopman (Lusch 2018)]] |  |
| `Raissi, Yazdani, Karniadakis - Hidden fluid mechanics Learning velocity and pressure fields from flow visualizations.pdf` | 5 | ingested → [[Hidden fluid mechanics (Raissi 2020)]] |  |
| `Wang, Sankaran, Perdikaris - An Expert's Guide to Training PINNs.pdf` | 36 | ingested → [[Expert's guide to PINNs (Wang 2023)]] |  |
| `Wang, Sankaran, Perdikaris - Respecting Causality is All You Need for Training PINNs.pdf` | 35 | ingested → [[Respecting causality (Wang 2022)]] |  |
| `Wang, Yu, Perdikaris - When and Why PINNs Fail to Train - A Neural Tangent Kernel Perspective.pdf` | 29 | ingested → [[When and why PINNs fail (Wang 2022)]] |  |

## papers/Stochastic Methods

| File | Pages | Status | Notes |
|---|---|---|---|
| `Alexanderian - the Karhunen-Loéve Expansion.pdf` | 14 | ingested → [[KL expansion note (Alexanderian 2015)]] |  |
| `Betz, Papaioannou, Straub - Karhunen-Loève Expansion for Discretization of RFs.pdf` | 21 | ingested → [[Random field discretization (Betz 2014)]] |  |
| `Chen, Xu, Li, Duvenaud - inf Deep Bayseian NN with Stochastic Diff. Eqns` |  | alias | points to papers/Bayesian/ copy |
| `Deheuvels - Karhunen-Loeve Expantions of mean-centered Wiener Processes.pdf` | 15 | ingested → [[KL expansions of the Wiener process (Deheuvels 2006)]] |  |
| `Einstein - Brownian Movement.pdf` | 11 | ingested → [[Brownian movement (Einstein 1905)]] |  |
| `Karniadakis, Xiu - The Weiner - Askey Polynomial Chaos for Stochastic Differential Equations.pdf` | 26 | ingested → [[Wiener-Askey chaos (Xiu 2002)]] |  |
| `Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf` | 36 | ingested → [[Score SDE (Song 2021)]] |  |
| `Li - Construction of Brownian Motion.pdf` | 12 | ingested → [[Brownian motion construction (Li n.d.)]] |  |
| `Prakash, Sun, Chakrabarti, Che - Quantum Option Pricing via the Karhunen-Loéve Expansion.pdf` | 25 | ingested → [[Quantum option pricing KL (Prakash 2025)]] |  |
| `Welling, Teh - Baysian Learning via Stochastic Gradient Langevin Dynamics` |  | alias | points to papers/Bayesian/ copy |

## papers/Symmetries

| File | Pages | Status | Notes |
|---|---|---|---|
| `Dey, Chen, Ghafurian - Group Equivariant GANs.pdf` | 28 | ingested → [[Group equivariant GANs (Dey 2021)]] |  |
| `Geiger, Smidt - e3nn Euclidean Neural Networks.pdf` | 22 | ingested → [[e3nn Euclidean networks (Geiger 2022)]] |  |
| `Ling - Reynolds Turbulence Modelling DNN with Embedded Invariance.pdf` | 12 | ingested → [[Tensor basis NN turbulence (Ling 2016)]] |  |
| `Quiroga, Ronchetti - Data Augmentaion for Rotational Invariance in CNNs.pdf` | 16 | ingested → [[Rotation augmentation for CNNs (Quiroga 2018)]] |  |
| `Welling, Cohen - Group Equivariant CNNs.pdf` | 12 | ingested → [[Group equivariant CNNs (Cohen 2016)]] |  |

## papers/Transforms

| File | Pages | Status | Notes |
|---|---|---|---|
| `Strang - Wavelet Transforms vs Fourier Transforms.pdf` | 18 | ingested → [[Wavelets vs Fourier (Strang 1993)]] |  |

## courses/ECE 270

| File | Pages | Status | Notes |
|---|---|---|---|
| `zz_Syllabus.pdf` | 15 | ingested → [[Number systems and codes]] |  |
| `week 01/08_22.pdf` | 35 | ingested → [[Number systems and codes]] |  |
| `week 01/08_24.pdf` | 43 | ingested → [[CMOS logic]] |  |
| `week 02/08_29.pdf` | 29 | ingested → [[CMOS logic]] |  |
| `week 02/08_31.pdf` | 26 | ingested → [[Boolean algebra]] |  |
| `week 03/09_07.pdf` | 25 | ingested → [[Karnaugh map]] |  |
| `week 04/09_12.pdf` | 28 | ingested → [[Hazards]] |  |
| `week 04/09_14.pdf` | 29 | ingested → [[Verilog]] |  |
| `week 05/09_19.pdf` | 34 | ingested → [[Verilog]] |  |
| `week 05/09_21.pdf` | 30 | ingested → [[Decoder and multiplexer]] |  |
| `week 06/09_28(2).pdf` | 28 | ingested → [[Latches and flip-flops]] |  |
| `week 07/10_03.pdf` | 26 | ingested → [[Counters and registers]] |  |
| `week 07/10_05.pdf` | 26 | ingested → [[Finite state machine]] |  |
| `week 08/10_12.pdf` | 36 | ingested → [[Finite state machine]] |  |
| `week 09/10_17.pdf` | 25 | ingested → [[Finite state machine]] |  |
| `week 10/10_24.pdf` | 26 | ingested → [[Verilog]] |  |
| `week 10/10_26.pdf` | 29 | ingested → [[Number systems and codes]] |  |
| `week 11/10_31.pdf` | 24 | ingested → [[Number systems and codes]] |  |
| `week 11/11_02.pdf` | 30 | ingested → [[Adders and arithmetic circuits]] |  |
| `week 12/11_07.pdf` | 16 | ingested → [[Adders and arithmetic circuits]] |  |
| `week 12/11_09(1).pdf` | 8 | ingested → [[Finite state machine]] |  |

## courses/ECE 311

| File | Pages | Status | Notes |
|---|---|---|---|
| `ECE311_Spring2023_Syllabus.pdf` | 9 | ingested → [[Vector calculus for EM]] |  |
| `ECE311_Spring2024_Schedule.pdf` | 1 | ingested → [[Vector calculus for EM]] |  |
| `Lectures Slides/lect_1.pdf` | 8 | ingested → [[Vector calculus for EM]] |  |
| `Lectures Slides/lect_10.pdf` | 8 | ingested → [[Dielectric polarization]] |  |
| `Lectures Slides/lect_11.pdf` | 8 | ingested → [[Electrostatic energy]] |  |
| `Lectures Slides/lect_12.pdf` | 9 | ingested → [[Poisson and Laplace equations]] |  |
| `Lectures Slides/lect_14.pdf` | 10 | ingested → [[Capacitance]] |  |
| `Lectures Slides/lect_15.pdf` | 8 | ingested → [[Ohm's law and current density]] |  |
| `Lectures Slides/lect_16.pdf` | 7 | ingested → [[Ohm's law and current density]] |  |
| `Lectures Slides/lect_17.pdf` | 7 | ingested → [[Biot-Savart law and Lorentz force]] |  |
| `Lectures Slides/lect_18.pdf` | 7 | ingested → [[Ampere's law]] |  |
| `Lectures Slides/lect_19.pdf` | 8 | ingested → [[Magnetic vector potential]] |  |
| `Lectures Slides/lect_2.pdf` | 10 | ingested → [[Vector calculus for EM]] |  |
| `Lectures Slides/lect_20.pdf` | 8 | ingested → [[Magnetic materials]] |  |
| `Lectures Slides/lect_21.pdf` | 8 | ingested → [[Magnetic materials]] |  |
| `Lectures Slides/lect_22.pdf` | 9 | ingested → [[Magnetic materials]] |  |
| `Lectures Slides/lect_23.pdf` | 8 | ingested → [[Inductance]] |  |
| `Lectures Slides/lect_24.pdf` | 8 | ingested → [[Biot-Savart law and Lorentz force]] |  |
| `Lectures Slides/lect_25.pdf` | 9 | ingested → [[Faraday's law]] |  |
| `Lectures Slides/lect_27.pdf` | 7 | ingested → [[Maxwell's equations]] |  |
| `Lectures Slides/lect_28.pdf` | 8 | ingested → [[Maxwell's equations]] |  |
| `Lectures Slides/lect_29.pdf` | 9 | ingested → [[Electromagnetic wave]] |  |
| `Lectures Slides/lect_3.pdf` | 10 | ingested → [[Vector calculus for EM]] |  |
| `Lectures Slides/lect_30.pdf` | 9 | ingested → [[Electromagnetic wave]] |  |
| `Lectures Slides/lect_31.pdf` | 8 | ingested → [[Electromagnetic wave]] |  |
| `Lectures Slides/lect_32.pdf` | 8 | ingested → [[Electromagnetic wave]] |  |
| `Lectures Slides/lect_33.pdf` | 8 | ingested → [[Wave polarization]] |  |
| `Lectures Slides/lect_34.pdf` | 8 | ingested → [[Poynting theorem]] |  |
| `Lectures Slides/lect_35.pdf` | 10 | ingested → [[Poynting theorem]] |  |
| `Lectures Slides/lect_36.pdf` | 11 | ingested → [[Reflection and transmission of waves]] |  |
| `Lectures Slides/lect_37.pdf` | 8 | ingested → [[Reflection and transmission of waves]] |  |
| `Lectures Slides/lect_38.pdf` | 10 | ingested → [[Transmission line]] |  |
| `Lectures Slides/lect_39.pdf` | 10 | ingested → [[Transmission line]] |  |
| `Lectures Slides/lect_4.pdf` | 10 | ingested → [[Coulomb's law]] |  |
| `Lectures Slides/lect_41.pdf` | 7 | ingested → [[Transmission line]] |  |
| `Lectures Slides/lect_42.pdf` | 10 | ingested → [[Transmission line]] |  |
| `Lectures Slides/lect_43.pdf` | 7 | ingested → [[Impedance matching]] |  |
| `Lectures Slides/lect_44.pdf` | 8 | ingested → [[Transmission line]] |  |
| `Lectures Slides/lect_5.pdf` | 10 | ingested → [[Gauss's law]] |  |
| `Lectures Slides/lect_6.pdf` | 7 | ingested → [[Gauss's law]] |  |
| `Lectures Slides/lect_7.pdf` | 8 | ingested → [[Electric potential]] |  |
| `Lectures Slides/lect_8.pdf` | 8 | ingested → [[Electric potential]] |  |
| `Lectures Slides/lect_9.pdf` | 8 | ingested → [[Dielectric polarization]] |  |

## courses/ECE 438

| File | Pages | Status | Notes |
|---|---|---|---|
| `Probability mini review Apr 11, 2025.pdf` | 2 | ingested → [[Histogram equalization]] |  |
| `Topic DSP.1 DT signals Jan 14, 2025.pdf` | 10 | ingested → [[Discrete-time signal]] |  |
| `Topic DSP.2 DT systems UPDATED Jan 22, 2025.pdf` | 17 | ingested → [[LTI system]] |  |
| `Topic DSP.3.A DT frequency analysis Part 1 Jan 31, 2025.pdf` | 14 | ingested → [[DFT]] |  |
| `Topic DSP.3.B DT frequency analysis Part 2 Jan 31, 2025.pdf` | 9 | ingested → [[DFT]] |  |
| `Topic DSP.3.C Python Examples Spectral Leakage Feb 6, 2025.pdf` | 2 | ingested → [[Spectral leakage]] |  |
| `Topic DSP.3.C more on DFT Feb 2, 2025.pdf` | 10 | ingested → [[DFT]] |  |
| `Topic DSP.3.D Convolution with DFT Feb 9, 2025.pdf` | 8 | ingested → [[Convolution]] |  |
| `Topic DSP.3.E the FFT Feb 12, 2025.pdf` | 9 | ingested → [[FFT]] |  |
| `Topic DSP.4.A Sampling CT.pdf` | 22 | ingested → [[Sampling theorem]] |  |
| `Topic DSP.4.B Sampling DT.pdf` | 8 | ingested → [[Sampling theorem]] |  |
| `Topic DSP.5 Quantization Feb 23, 2025.pdf` | 11 | ingested → [[Quantization]] |  |
| `Topic DSP.6 z-transforms March 7, 2025.pdf` | 15 | ingested → [[Z-transform]] |  |
| `Topic IP.1 Image processing overview Mar 23, 2025.pdf` | 7 | ingested → [[Digital image]] |  |
| `Topic IP.2 Sampling, quantization, interpolation Mar 23, 2025 .pdf` | 17 | ingested → [[Image interpolation]] |  |
| `Topic IP.2 aliasing-ece438-250328-share.pdf` | 11 | ingested → [[Aliasing]] |  |
| `Topic IP.3 Continuous-space FT Mar 25, 2025.pdf` | 19 | ingested → [[Fourier transform]] |  |
| `Topic IP.4.A Histograms Apr 2, 2025.pdf` | 12 | ingested → [[Histogram equalization]] |  |
| `Topic IP.4.B spatial filtering Apr 4, 2025.pdf` | 12 | ingested → [[Spatial filtering]] |  |
| `Topic IP.5 image transforms and wavelets Apr 14, 2025.pdf` | 23 | ingested → [[Image transforms]] |  |
| `Topic IP.6 Image compression Apr 23, 2025.pdf` | 32 | ingested → [[Image compression]] |  |
| `Topic IP.7 Multiresolution image processing Apr 18, 2025.pdf` | 15 | ingested → [[Wavelet transform]] |  |
| `exam_1_review_transcribed.pdf` | 11 | ingested → [[LTI system]] |  |
| `reibman_purdue08-examples.pdf` | 11 | ingested → [[Image compression]] |  |
| `301 Review/Topic 2.1 power and energy Jul 17, 2022.pdf` | 5 | ingested → [[Discrete-time signal]] |  |
| `301 Review/Topic 2.2 time transformations.pdf` | 10 | ingested → [[Discrete-time signal]] |  |
| `301 Review/Topic 2.3 period of a signal Note Jul 23, 2022.pdf` | 7 | ingested → [[Discrete-time signal]] |  |
| `301 Review/ece301final_equation-sheet.pdf` | 8 | ingested → [[Fourier transform]] |  |
| `front page/L15 Feb 19, 2025.pdf` | 1 | ingested → [[Sampling theorem]] |  |
| `front page/L16 Feb 21, 2025.pdf` | 1 | ingested → [[Sampling theorem]] |  |
| `front page/L17 Feb 24, 2025.pdf` | 1 | ingested → [[Sampling theorem]] |  |
| `front page/L18 Feb 26, 2025.pdf` | 1 | ingested → [[Sampling theorem]] |  |
| `front page/L19 Feb 28, 2025.pdf` | 1 | ingested → [[Quantization]] |  |
| `front page/L20 Mar 3, 2025.pdf` | 1 | ingested → [[Quantization]] |  |
| `front page/L21 Mar 5, 2025.pdf` | 1 | ingested → [[Quantization]] |  |
| `front page/L22 Mar 7, 2025.pdf` | 1 | ingested → [[Z-transform]] |  |
| `front page/L23 Mar 10, 2025.pdf` | 1 | ingested → [[LTI system]] |  |
| `front page/L24 Mar 24, 2025.pdf` | 1 | ingested → [[Z-transform]] |  |
| `front page/L25 Mar 26, 2025.pdf` | 1 | ingested → [[Digital image]] |  |
| `front page/L26 Mar 26, 2025.pdf` | 1 | ingested → [[Fourier transform]] |  |
| `front page/L27 Mar 31, 2025.pdf` | 1 | ingested → [[Fourier transform]] |  |
| `front page/L28 Apr 2, 2025.pdf` | 1 | ingested → [[Histogram equalization]] |  |
| `front page/L29 Apr 4, 2025.pdf` | 1 | ingested → [[Histogram equalization]] |  |
| `front page/L30 Apr 7, 2025.pdf` | 1 | ingested → [[Spatial filtering]] |  |
| `front page/L31 Apr 9, 2025.pdf` | 1 | ingested → [[Spatial filtering]] |  |
| `front page/L32 Apr 11, 2025.pdf` | 1 | ingested → [[Image transforms]] |  |
| `front page/L33 Apr 14, 2025.pdf` | 8 | ingested → [[Image transforms]] |  |
| `front page/L34 Apr 18, 2025.pdf` | 2 | ingested → [[Image compression]] |  |
| `front page/L35 Apr 21, 2025.pdf` | 1 | ingested → [[Image compression]] |  |
| `front page/L36 Apr 23, 2025.pdf` | 1 | ingested → [[Image compression]] |  |
| `front page/L37 Apr 25, 2025.pdf` | 6 | ingested → [[Image compression]] |  |
| `front page/L38 Apr 28, 2025.pdf` | 1 | ingested → [[Wavelet transform]] |  |
| `front page/L39 Apr 30, 2025.pdf` | 1 | ingested → [[Wavelet transform]] |  |
| `front page/L40 May 2, 2025.pdf` | 1 | ingested → [[Wavelet transform]] |  |

## courses/ME 697

| File | Pages | Status | Notes |
|---|---|---|---|
| `S25 Syllabus_ME697_BS_Bilionis.pdf` |  | reference |  |
| `Group Theory/KondorThesis.pdf` |  | reference |  |
| `Group Theory/MLSS2024_OIST_fukumizu.pdf` |  | reference |  |
| `Homework/05_homework.pdf` |  | reference |  |
| lecture videos, homework notebooks, data | | reference | 79 non-PDF files: syllabus, Modules 3-7 videos, HW 1-7 |

## text_books/Category Theory

| File | Pages | Status | Notes |
|---|---|---|---|
| `Spivak - Poly.pdf` | 14 | ingested → [[Poly (Spivak 2020)]] |  |
| `Spivak, Fong - Seven Sketches in Compositionality.pdf` | 354 | ingested → [[Galois connection]] |  |
| `Spivak, Niu - Polynomial Functors.pdf` | 375 | ingested → [[Polynomial comonoid]] |  |

## text_books/Computer Science

| File | Pages | Status | Notes |
|---|---|---|---|
| `Microservices.Patterns.Examples.Chris.Richardson.pdf` |  | reference |  |

## text_books/Engineering

| File | Pages | Status | Notes |
|---|---|---|---|
| `Bare Essentials of Electrical Engineering.pdf` |  | reference |  |
| `Circuits Signals & Systems.pdf` |  | reference |  |
| `ECE 20875   Python Essential Reference.pdf` |  | reference |  |
| `ECE 270 Digital Design Principles and Practices.pdf` |  | reference |  |
| `ECE 29401   Sensible Strategies.pdf` |  | reference |  |
| `Elements of Electromagnetics.pdf` |  | reference |  |
| `Intro to Mechanics and Symetry.pdf` |  | reference |  |
| `Introduction to Operations Research.pdf` |  | reference |  |
| `Vacuum Tubes.pdf` |  | reference |  |
| `Electromagetic Fields for Engineers/a Preface Ch. 1, 2.pdf` |  | reference |  |
| `Electromagetic Fields for Engineers/b Ch. 3, 4, 5.pdf` |  | reference |  |
| `Electromagetic Fields for Engineers/c Ch. 6, 7, 8.pdf` |  | reference |  |
| `Electromagetic Fields for Engineers/d Ch. 9, 10, 11, 12.pdf` |  | reference |  |
| `Electromagetic Fields for Engineers/e Appendix.pdf` |  | reference |  |

## text_books/Linear Optimization

| File | Pages | Status | Notes |
|---|---|---|---|
| `BJS full book.pdf` | 764 | ingested → [[Linear programming]] | old OCR text layer (748/764 pages); math garbled, read equations from page images |
| `MIT (ch 1-2).pdf` | 80 | ingested → [[Linear programming]] |  |
| `MIT (ch 1-5).pdf` | 605 | ingested → [[Linear programming]] | old OCR text layer (587/605 pages); math garbled, read equations from page images |

## text_books/Mathmatics

| File | Pages | Status | Notes |
|---|---|---|---|
| `Basu - Intro to Convexity.pdf` | 94 | ingested → [[Lagrangian duality]] |  |
| `Baysian Data Analysis 3rd ed.pdf` |  | reference |  |
| `Differential Equations.pdf` |  | reference |  |
| `Functional Inegration & Quantum Physics.pdf` |  | reference |  |
| `Gaussian Processes for Machine Learning.pdf` |  | reference |  |
| `Graph Theory.pdf` |  | reference |  |
| `Intro to Probability for Data Science.pdf` |  | reference |  |
| `Linear Alngebra.pdf` |  | reference |  |
| `MIT Real Analysis.pdf` |  | reference |  |
| `Prob & Stats & Random Processes.pdf` |  | reference |  |
| `Random Fields & Geometry - Adler, Taylor.pdf` |  | reference |  |

## text_books/Programming

| File | Pages | Status | Notes |
|---|---|---|---|
| `Advanced Lectures on Machine Learning.pdf` |  | reference |  |
| `AoCP- V1 (Fundamental Algorithms).pdf` |  | reference |  |
| `AoCP- V2 (Seminumerical Algorithms).pdf` |  | reference |  |
| `lets-go-further.pdf` |  | reference |  |
| `cribsheets/database-sql.pdf` |  | reference |  |
| `cribsheets/net-http.pdf` |  | reference |  |
| code, cribsheets, HTML books | | reference | 387 non-PDF files, not listed individually |

## text_books/advanced-scientific-machine-learning (ME 697 book repo)

Jupyter-book source in `text_books/advanced-scientific-machine-learning/book/`, chapters from `_toc.yml`, ingested chapter by chapter.

| Chapter | Folder | Status |
|---|---|---|
| Modern Machine Learning Software | `ml-software/` | ingested → [[Automatic differentiation]], [[Gradient descent]], [[JIT compilation]], [[Pytree]] |
| Uncertainty Propagation through Scientific Models | `up/` | ingested → [[Active learning]], [[Equivariance]], [[Multi-fidelity modeling]], [[Polynomial chaos]], [[Sensitivity analysis]], [[Surrogate model]] |
| High-dimensional Uncertainty Propagation | `hup/` | ingested → [[Karhunen-Loève expansion]], [[Operator learning]] |
| Inverse Problems in Deterministic Scientific Models | `inverse/` | ingested → [[Bayesian inverse problems]], [[Hierarchical Bayesian model]], [[Identifiability]], [[Markov chain Monte Carlo]], [[SINDy]], [[Variational inference]] |
| Physics-informed Neural Networks (PINNs) | `pinns/` | ingested → [[PINN]], [[Parametric PINN]] |
| Inverse Problems in Stochastic Scientific Models | `sinverse/` | ingested → [[Expectation-maximization]], [[Particle filter]], [[Stochastic differential equation]] |
| Homework Problems | `homework/` | ingested → [[PINN]] |
| Information field theory (not in `_toc.yml`) | `ift/` | ingested → [[Information field theory]], [[Physics-informed prior]] |
| Dynamics and reduced-order models (not in `_toc.yml`) | `dynamics/` | ingested → [[Dynamic mode decomposition]] |
| (not in `_toc.yml`) | `reduced_order_modeling/` | ingested → [[Proper orthogonal decomposition]] |

## Totals

alias: 8, ingested: 208, reference: 35
