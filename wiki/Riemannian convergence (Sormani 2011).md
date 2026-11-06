---
type: paper
area: math
areas: [math, ml]
source-ref: "Sormani 2011, arXiv:1006.0411v2, §1-4 (survey)"
tags: [ml]
authors: ["[[Christina Sormani]]"]
year: 2011
venue: "arXiv:1006.0411v2 [math.DG] (survey)"
file: "ML/Sormani - How Riemannian Manifolds Converge.pdf"
---

# Riemannian convergence (Sormani 2011)

**Summary**: An illustrated survey of ways a sequence of manifolds can converge when smooth convergence fails. Extrinsic notions (Hausdorff, flat, varifold) apply to submanifolds of Euclidean space. Intrinsic notions (Gromov-Hausdorff, metric measure, intrinsic flat, ultralimit) apply to abstract Riemannian manifolds. Each notion preserves some properties and loses others.

**Authors**: Christina Sormani · **Year**: 2011 · **File**: `ML/Sormani - How Riemannian Manifolds Converge.pdf`

---

## Problem

Smooth convergence ($\varphi_j^{*}g_j\to g$, eq. 21) is too strong for collapsing sequences, sequences with curvature bounds only from below, or ones with thin spikes. Weaker limits are needed, whose limit spaces need not be manifolds (source: Sormani 2011, §1, §3). The paper is explicitly "not meant to provide a thorough rigorous definition", only the flavour of each notion and key examples.

## Method (the notions surveyed)

**Extrinsic (§2).**
- *Hausdorff convergence* of sets, with distance $H(A_1,A_2)=\inf\{R: A_1\subset T_R(A_2),\ A_2\subset T_R(A_1)\}$. Preserves convexity and connectedness (Blaschke selection) but not length, dimension or topology: tori converge to a circle, and jagged paths of length 2 converge to a segment of length 1 (§2.1).
- *Flat convergence* of integral currents (Federer-Fleming). Flat distance $d_F(T_1,T_2)=\inf\{M(A)+M(B): A+\partial B=T_1-T_2\}$ (eq. 9). With bounded mass and boundary mass, subsequences converge, mass is lower semicontinuous, and the "disk with many splines" converges to the flat disk. Orientation can cause cancellation (Fig. 3).
- *Varifold convergence* (Almgren, Allard): measures on $\mathbb{R}^N\times\Gamma(k,N)$ with no cancellation; Allard's compactness theorem keeps integral varifolds under bounded first variation (§2.3).

**Intrinsic (§3).**
- *Gromov-Hausdorff*: $d_{GH}(M_1,M_2)=\inf H(\varphi_1(M_1),\varphi_2(M_2))$ over isometric embeddings into any common $Z$ (eq. 22). Gromov compactness holds under bounds on diameter and on the number $N(r)$ of disjoint $r$-balls; Ricci lower bounds imply this via Bishop-Gromov. Limits are geodesic metric spaces.
- *Metric measure convergence* (Fukaya, Cheeger-Colding, Sturm, Lott-Villani): adds measures, keeps Laplace spectra convergent under Ricci lower bounds; Wasserstein and Prokhorov variants.
- *Intrinsic flat convergence* (Sormani-Wenger 2008, eq. 31): handles Ilmanen's "3-sphere of many splines", which fails Gromov-Hausdorff. Limits are integral current spaces.
- *Ultralimits*: the weakest notion (§3.4; not read in detail).

**Speculative (§4).** Intrinsic varifold convergence, area convergence, Lorentzian manifolds.

## Results

No new theorems. Key examples: tori collapsing to a circle (eq. 24, $d_{GH}\le\pi/2j$), splines on a disk, and the collapsing example where Laplace eigenvalues of two sequences with the same limit $[0,1]$ differ (eq. 27), which motivated metric measure convergence.

## Limitations

- Survey: definitions are informal, proofs are cited, not given.
- Last sections are speculative by the author's own description.
- Pure geometry; no learning or sampling content.

## Connections

- Why it sits in `ML/`: Wiki note, probably background for manifold geometry. This is a **flag**; the source gives no link to machine learning.
- The Riemannian metric picture for samplers: [[Riemannian manifold HMC]] and [[RMHMC (Girolami 2011)]] treat parameter space as a manifold with a Fisher metric. Sormani's survey concerns convergence of sequences of manifolds, which is a different question. Wiki note.
- Manifold hypothesis for data: [[Spectral bias (Rahaman 2019)]] §4 assumes data on a lower-dimensional manifold.

**Sources**: `ML/Sormani - How Riemannian Manifolds Converge.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Riemannian manifold HMC]]
- [[RMHMC (Girolami 2011)]]
- [[Spectral bias (Rahaman 2019)]]
