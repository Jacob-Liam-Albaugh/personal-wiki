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
- Ingested 2 generative papers: [[Score SDE (Song 2021)]] (Stochastic Methods/; the Generative ML/ entry is an alias) and [[Group equivariant GANs (Dey 2021)]] (Symmetries/).
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
