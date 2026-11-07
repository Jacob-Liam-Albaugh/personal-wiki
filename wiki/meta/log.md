# Log

## 2026-11-06 — setup and first ingest
- Adapted the course-vault CLAUDE.md to the whole Papers library. The topic folders are left as they are and act as the raw layer; there is no `raw/` folder. Added area slugs and paper and lecture templates.
- Set up `wiki/`, `wiki/meta/` and `notes/`, and a local git repo that tracks only the wiki, the notes and CLAUDE.md.
- Built [[sources]] from a scan of 243 files: 13 ingested, 187 queued, 35 reference, 8 Finder aliases. Two scanned PDFs have no text layer: the BJS Linear Optimization book and MIT ch. 1-5.
- Ingested 10 papers:
  - the Poly DSL paper;
  - the two reading-group papers;
  - the two lab IFT papers;
  - Wang 2026;
  - Welling-Teh SGLD;
  - three Ruqi Zhang SG-MCMC papers.
- Wrote 48 pages in total, papers plus concept pages.
- Duplicates found:
  - SGLD exists in both Bayesian/ and IFT/.
  - The PIFT arXiv preprint is in Bayesian/.
  - The DeepONet arXiv preprint is in Operators/.
- Open flags, marked **[unverified]** on the pages:
  - the SGLD noise convention in Alberts & Bilionis eq. 22;
  - the exponents of the Cyclical SG-MCMC Thm 2;
  - one term in the Low-precision SGLD Thm 3;
  - noise values in the PIFT examples.
- Plan: [notes/001](../../notes/001-library-wiki-setup-and-ingest-plan.md).

## 2026-11-06 — Bayesian batch
- Ingested 9 papers from Bayesian/:
  - lab VI: [[Variational inverse problems (Tsilifis 2014)]], [[Amortized VI for inverse problems (Karumuri 2024)]];
  - [[Amortized VI when and why (Margossian 2024)]];
  - Kingma: [[VAE paper (Kingma 2014)]], [[Variational dropout (Kingma 2015)]], [[Intro to VAEs (Kingma 2019)]];
  - [[SDE-BNN (Xu 2022)]], [[Priors in Bayesian deep learning (Fortuin 2022)]], [[Bayesian DenseED surrogate (Zhu 2018)]].
- Wrote 13 concept pages: [[Variational inference]], [[ELBO]], [[KL divergence]], [[Reparameterization trick]], [[Amortized VI]], [[Normalizing flows]], [[Bayesian inverse problems]], [[VAE]], [[Local reparameterization trick]], [[Variational dropout]], [[Bayesian neural networks]], [[SVGD]], [[Gaussian process]]. The wiki now has 70 pages; [[sources]] shows 22 ingested and 178 queued.
- Incomplete PDFs:
  - Intro to VAEs has only ch. 1 and the appendix.
  - Variational Dropout has no appendices.
- Correction: the BJS and MIT ch. 1-5 books do have a text layer (748/764 and 587/605 pages). The first scan sampled only the cover. That old OCR garbles the math, so equations should be read from page images. A fresh PdfCraft OCR would not fix this, because its engine reads Latin text only.
- Open flags:
  - The Zhu & Zabaras equations were garbled in extraction. The SVGD form is standard and marked **[unverified]**.
  - The Fortuin NTK recursion is marked **[unverified]**.
  - Tsilifis Alg. 1 prints $w_i=1/N$ where $1/L$ is meant.

## 2026-11-06 — Operators and generative batch
- Ingested 4 papers from Operators/: [[Neural operator (Kovachki 2022)]], [[FNO (Li 2021)]], [[LNO (Cao 2023)]], [[Operator learning review (Kovachki 2024)]].
- Ingested 2 generative papers: [[Score SDE (Song 2021)]] (papers/Stochastic Methods/; the Generative ML/ entry is an alias) and [[Group equivariant GANs (Dey 2021)]] (papers/Symmetries/).
- New concept pages:
  - operators: [[Neural operator]], [[Kernel integral operator]], [[FNO]], [[LNO]], [[Laplace transform]], [[Discretization invariance]], [[Encoder-decoder operators]], [[PCA-Net]], [[Random features model]], [[Curse of parametric complexity]];
  - benchmarks: [[Darcy flow]], [[Burgers equation]], [[Navier-Stokes equations]];
  - generative: [[Score matching]], [[Fokker-Planck equation]], [[GAN]], [[Equivariance]].
- Rewrote [[Diffusion models]] as a hub. Small sub-topics are sections on hub pages, not separate pages (e.g. graph and low-rank NO on [[Neural operator]], VE/VP SDEs on [[Diffusion models]]).
- Updated [[Operator learning]], [[DeepONet]], [[Universal approximation for operators]], [[Flow matching]], [[Diffusion posterior sampling]], [[Langevin dynamics]], [[Normalizing flows]], [[Karhunen-Loève expansion]], [[Gaussian process]].
- Checked against page images: Score-SDE Table 1; LNO eq. 3 really omits the factor $s$ (noted on [[Laplace transform]]).
- Open flags:
  - LNO Fig. 3 values were read by eye (±0.02, **[unverified]**). By those readings the GRU beats LNO in 3 cases.
  - LNO's "exponential convergence" claim is never analysed in the paper.
  - Review eq. 5.12 exponent (p. 27) is unverified.
  - Review Thm 4.1 prints the composition in the wrong order.
  - Burgers FNO error is about 8× lower in the JMLR paper than in ICLR (0.0018 vs 0.0139-0.0160); the text does not say why.
  - Kovachki JMLR table page cites are approximate.

## 2026-11-06 — Diffusion batch, renames, topic tags
- Ingested 5 papers from Diffusion/: [[DDPM (Ho 2020)]], [[DDIM (Song 2021)]], [[Classifier-free guidance (Ho 2022)]], [[CLIP (Radford 2021)]] (main text and supplement), and [[Step-by-step diffusion (Nakkiran 2025)]]. The Diffusion/ copies of Song 2021 and Wang 2026 are duplicates.
- New concept pages: [[DDPM]], [[DDIM]], [[Noise prediction]], [[Noise schedule]], [[Classifier guidance]], [[Classifier-free guidance]], [[Contrastive learning]], [[Zero-shot transfer]].
- Updated:
  - [[Diffusion models]]: discrete-time links, a Guidance section, DDIM Prop. 1;
  - [[Flow matching]]: linear flows, DDIM as a flow;
  - [[Score matching]]: a Tweedie's formula section;
  - [[ELBO]]: the diffusion bound.
- Renamed all pages to short readable titles, rewrote every link, and added topic tags. Graph view colours nodes by tag, and meta/ is excluded from it.
- Open flag: the DDIM γ-independence claim depends on there being no parameter sharing across $t$ (p. 4).

## [2026-11-06] tags | topic tags only
- Removed the `paper`, `lab`, `reading-group` and `meta` tags. Tags are now topics only; stubs use `status: lead` frontmatter.
- Checked links across the rename: all 734 earlier page-to-page links survive, and there are 868 now. Restored graph.json, which Obsidian had overwritten (tag nodes on, colour groups gone).

## [2026-11-06] ingest | ME 697 book part 1 (ml-software)
- Sources: `text_books/advanced-scientific-machine-learning/book/ml-software/` (functional_programming, types_and_models, differentiation, optimization).
- Lecture pages: [[JIT compilation]], [[Pytree]], [[Automatic differentiation]], [[Gradient descent]].
- Concept pages: [[JIT compilation]], [[vmap]], [[JAX random keys]], [[Pytree]], [[Automatic differentiation]], [[Gradient descent]], [[Momentum]], [[SGD]], [[Adam]], [[Newton's method]], [[Weight initialization]].
- New topic tags: `optimization`, `software` (CLAUDE.md, graph colours).
- Flags on the source: the jvp signature (returns a pair), where ε sits in Adam, and the book's "He" bound, which is LeCun-uniform.

## [2026-11-06] ingest | everything else, authors, references
- Ingested the rest of the library:
  - Papers from Bayesian/, papers/Physics Informed Architectures/, papers/Stochastic Methods/, papers/ML/, papers/Guassian Processes/, papers/Symmetries/, papers/LLMs/, papers/Math/, papers/Transforms/.
  - ME 697 book parts 2-6 (31 lecture pages in all).
  - Course notes: ECE 438 (50 pages), ECE 311 (41), ECE 270 (20).
  - Books by chapter: *Poly* ch1-9, *Seven Sketches* ch1-7, Bertsimas-Tsitsiklis ch1-12, Bazaraa-Jarvis-Sherali ch1-12.
- The wiki now has 121 paper pages, 142 lecture pages, and 240 concept, method, definition and theorem pages. [[sources]] lists 208 ingested, 35 reference, 8 alias and 0 queued.
- `text_books/` reference items are not ingested.
- Authors: `tools/authors.py` builds `authors/` (205 author pages) from each page's **Authors** line and links them from `authors:` frontmatter. In graph view, hide them with `-path:authors`.
- References: `tools/refs.py --n 2` writes **Cites / Cited by in this wiki** blocks (128 links) and [[wanted-papers]], which lists 176 outside works cited by 2 or more sources. Rerun both tools after every ingest.
- Open flags:
  - [unverified] items in the BT/BJS chapters. Printed page = pdf page − 16.
  - Polynomial Functors ch9: `Mod` and the general form of Yoneda.
  - IFT.1-3 and 5.3 are stubs.
  - Slide errors are noted on the topic pages (Image compression, Fourier transform, DFT, FFT, Z-transform).

## [2026-11-06] restructure | Course notes folded into topic pages
- All 142 lecture pages (ME 697 31, ECE 438 50, ECE 311 41, ECE 270 20) were merged into topic pages and removed. Links were rewritten to the topic that now holds the content.
- New topic pages: [[Digital image]], [[Image interpolation]], [[Image transforms]]. Topic pages carry a plain-text **Covered in** line naming the class material.
- ME 697 homework sits on the topic it exercises as `[!example]` callouts, citing the ASML book section.
- Course logistics (exam dates, quizzes, rooms, grading) dropped. [[index]] sections are named by topic, not course.


## [2026-11-06] reorg | Sources split into papers/, courses/, text_books/
- Root folder renamed `Papers` → `personal-wiki`. Topic folders moved under `papers/`; ECE 270/311/438 and ME 697 (with the `advanced-scientific-machine-learning` repo) under `courses/`; `_text books` → `text_books/`, joined by Linear Optimization, the three Spivak books and Basu.
- Every source path in pages, [[sources]] and tools rewritten; all `file:` paths resolve.
- The `advanced-scientific-machine-learning` repo moved from `courses/ME 697/` to `text_books/`.

## [2026-11-06] restructure | Textbook chapter pages folded into topic pages
- Removed all 43 per-chapter book pages (Bertsimas-Tsitsiklis ch1-12, Bazaraa-Jarvis-Sherali ch1-12, Basu ch2-4, Polynomial Functors ch1-9, Seven Sketches ch1-7). Their content now lives on topic pages, each with a `**Covered in**` line naming the book and chapter.
- Where two books cover a topic (simplex method, LP duality, polyhedra, network flows), they are merged on one page.
- New topic pages: LP modelling, Simplex initialization and anticycling, Revised simplex method, LP sensitivity analysis, Complexity of linear programming, LP in practice, Affine scaling method, Path-following interior point methods, Network simplex method, Transportation problem, Assignment problem, Maximum flow problem, Shortest path problem, Out-of-kilter algorithm, Multicommodity flow, Column generation, Benders decomposition, Branch and bound, Lagrangian relaxation, Lagrangian duality, Subgradient method, Cutting-plane methods, Vertical and cartesian lens, Retrofunctor, Cofree comonoid on a polynomial, Topos, Signal flow graph, Hypergraph category.
- Links to chapter pages were retargeted to the topic page holding that chapter's main content. [[sources]] and [[index]] were regenerated, and CLAUDE.md now says books fold into topics like course notes.

## [2026-11-07] ingest | Twelve inbox papers on network theory, CNNs and physics-informed learning
- Sorted by `make sort` into papers/ (four refiled by hand: Hornik, NTK → ML; GAN → Generative ML; Matthews → Guassian Processes). Batch ingest, no discussion step.
- Papers: [[Universal approximation (Hornik 1989)]], [[NTK (Jacot 2018)]], [[Wide networks as GPs (Matthews 2018)]], [[AlexNet (Krizhevsky 2012)]], [[U-Net paper (Ronneberger 2015)]], [[GAN paper (Goodfellow 2014)]], [[SINDy (Brunton 2016)]], [[Eureqa (Schmidt 2009)]], [[Deep Koopman (Lusch 2018)]], [[Hidden fluid mechanics (Raissi 2020)]], [[Cardiovascular flow PINNs (Kissas 2020)]], [[Cardiac activation PINN (Sahli Costabal 2020)]].
- New pages: [[Universal approximation theorem]], [[Neural network Gaussian process]], [[Convolutional neural network]], [[U-Net]], [[ReLU]], [[Koopman operator]], [[Eikonal equation]], [[Randomized prior functions]], [[Windkessel model]].
- Updated: Neural tangent kernel, Gaussian process, Bayesian neural networks, Spectral bias, Weight initialization, Universal approximation for operators, GAN, Dropout, Convolution, Group equivariant CNN, ResNet, VAE, KL divergence, SINDy, Symbolic regression, Dynamic mode decomposition, LASSO, PINN, Non-dimensionalization, Active learning, Latin hypercube sampling, Navier-Stokes equations, and 14 paper pages that cite the new ones.
- All 12 left [[wanted-papers]]; it now lists 183 (new entries cited by the new pages, e.g. LeCun 1998, Lee 2018 NNGP, ImageNet 2009).
- Gaps: NTK PDF lacks its appendix; SINDy PDF has no SI; Matthews appendices skimmed; Kissas Windkessel table numbers lost in extraction. Koopman eq. 4 and AlexNet LRN/momentum checked against page images.
- `inbox/20.3.pdf` left in the inbox: a 2019 copy of the TTUR paper (Heusel et al. 2017) published under another author's name, not the original.
- `tools/inbox.py`: dehyphenates references, rejects junk/PII metadata titles, prefers the longer author list, substring surname match for OCR text, ignores PSL Reading Group for topic votes. CLAUDE.md ingest step 8 now checks that ingested papers leave the wanted list.

## [2026-11-07] tooling | Software citations split from wanted papers
- `tools/refs.py` recognises 36 packages (JAX, TensorFlow, PyTorch, NumPy, Matplotlib, scikit-learn, DeepXDE, ...) from a curated `SOFTWARE` pattern list.
- Each paper's refs block gains a **Software cited** line linking into [[software]], which lists every package with the pages that cite it and one reference with a link.
- Software no longer reaches [[wanted-papers]]; with the threshold at 4 it lists 2 papers (Krizhevsky 2009 tiny images, Heusel 2017 TTUR).

## [2026-11-07] ingest | PISD (Gallon 2026)
- Paper: [[PISD (Gallon 2026)]] (ICML 2026): diffusion on data-scaled spectral coefficients with PDE and observation guidance applied through frequency-aware Adam.
- New page: [[Spectral diffusion]] (scaled encoding, Lemma 3.2 with proof).
- Updated: Diffusion models, Diffusion posterior sampling, Adam, PINN, Navier-Stokes equations, Poisson and Laplace equations, Fourier transform, FNO, Generative priors for turbulence (Wang 2026).
- Discussion step skipped at the user's request ("continue").

## [2026-11-07] ingest | Alberts MAP uniqueness (2025) and dissertation (2024)
- Papers: [[MAP uniqueness in IFT (Alberts 2025)]] (arXiv 2401.14224v3): weakly well-posed IFT inverse problems, gradient/Hessian of the parameter posterior as field expectations, unique MAP for potentials linear in the parameters, Poisson model-trust example. [[IFT for engineering inverse problems (Alberts 2024)]] (Purdue PhD dissertation): chapter map onto existing IFT pages plus the PINN/B-PINN correspondence.
- New pages: [[Generalized random fields]], [[Operator calculus for free theory]], [[Model-form error detection]].
- Updated: Information field theory, Physics-informed prior, PIFT (Alberts 2023), Nested SGLD, PINN, Identifiability, Bayesian inverse problems, IFT thermal conductivity (Alberts 2026).
- Batch of two: discussion step skipped.
