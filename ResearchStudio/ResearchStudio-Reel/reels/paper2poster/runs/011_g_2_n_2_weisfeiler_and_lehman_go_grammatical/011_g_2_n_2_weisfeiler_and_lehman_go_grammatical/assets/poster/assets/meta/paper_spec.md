---
title: G2N2: Weisfeiler and Lehman Go Grammatical
authors: Jason Piquenot¹, Aldo Moscatelli¹, Maxime Bérar¹, Pierre Héroux¹, Jean-Yves Ramel², Romain Raveaux², Sébastien Adam¹
institutes: ¹LITIS Lab, University of Rouen Normandy; ²LIFAT Lab, University of Tours
venue: ICLR 2024
paper_url: https://arxiv.org/abs/2303.01590
code_url: https://github.com/JPiquenot/Wesfeiler-and-Lehman-go-grammatical
title_audio_script: This paper, G2N2, presented at ICLR 2024, asks a deceptively simple question: can we design a graph neural network whose expressive power is guaranteed by construction, rather than proved after the fact? The authors give a recipe. They take a fragment of an algebraic matrix language known to match the third-order Weisfeiler-Lehman test, write it as a context-free grammar, prune the grammar down to its essential rules, and then translate those rules directly into the layers of a neural network. The result is a provably three-W-L graph neural network that is both principled and, in practice, faster and more accurate than its competitors.
---

## Problem
**Necessary:** Building graph neural networks with guaranteed expressive power usually means proving a model matches the k-Weisfeiler-Lehman test after it is designed, and no systematic procedure exists to derive a GNN from a given expressive language fragment.
**Additional:** Existing 3-WL models like 3-IGN are memory-heavy (basis size grows as the 2k-th Bell number) and PPGN, though tractable, is only shown to mimic 2-FWL without a constructive language-to-model link.
**Audio script:** How expressive is a graph neural network? For years the field has answered that with the Weisfeiler-Lehman hierarchy, and the gold standard has been to design a model and then prove it matches, say, the third-order test. But that proof comes after the design, almost as an afterthought. What has been missing is a systematic way to go the other direction: to start from a language we already know is exactly as powerful as 3-W-L, and mechanically build a network that inherits that power. Without such a recipe, every expressive architecture is a fresh, hand-crafted proof.

## Motivation
**Necessary:** The Weisfeiler-Lehman hierarchy characterizes GNN expressiveness, and prior work reformulated the 1-WL and 3-WL tests as fragments ML(L1) and ML(L3) of the matrix language MATLANG — but turning such a fragment into a provably equivalent GNN was still done case by case.
**Additional:** GNNML3, derived from the same MATLANG view, was only shown to be more expressive than 1-WL, not provably 3-WL, precisely because there was no systematic derivation procedure.
**Audio script:** The seed of the idea comes from a groundbreaking observation: the 1-W-L and 3-W-L tests can each be rewritten as a fragment of a matrix language called MATLANG. Two graphs look the same to 3-W-L if and only if every sentence you can write in the fragment ML-of-L-three gives them the same value. That is a beautiful bridge between combinatorics and algebra. But a bridge is not a road. Turning one of these fragments into an actual, trainable network had been done only case by case, and the resulting models could not claim the full 3-W-L guarantee. The motivation here is to pave that road once and for all.

## Contribution
**Necessary:** (i) A generic framework that produces a GNN from any fragment of an algebraic language via context-free grammars; (ii) an instantiation on ML(L3) yielding G2N2, a provably 3-WL GNN; (iii) experimental validation of the grammar reduction / rule set; (iv) extensive experiments showing G2N2 outperforms existing 3-WL GNNs across regression, classification, and spectral tasks.
**Additional:** The grammar-reduction step both preserves 3-WL expressiveness and exposes which operations matter, enabling informed pruning of the model.
**Audio script:** The paper makes four contributions. First, a generic framework that turns any fragment of an algebraic language into a graph neural network through context-free grammars. Second, it runs that framework on the ML-of-L-three fragment and out comes G2N2, a network that is provably 3-W-L. Third, it validates the rule set experimentally, showing that the grammar reduction keeps expressiveness while trimming redundancy. And fourth, across a broad battery of downstream tasks, G2N2 beats the existing 3-W-L networks, often while running faster.

## Method
**Necessary:** From the operation set L3 = {·, ᵀ, 1, diag, ⊙} the authors build an exhaustive Context-Free Grammar that generates the MATLANG fragment ML(L3), then reduce it to a compact grammar r-G(L3) that stays equivalent to 3-WL. The reduced grammar's variables become the GNN inputs (a node/edge feature tensor) and its production rules become the layer update functions, giving the Grammatical Graph Neural Network G2N2.
**Additional:** A layer keeps an edge (matrix) memory C and a node (vector) memory H; learnable linear blocks L1–L7 combine tensor slices, the reduced rules (M⊙M), (MM), diag(Vc), (MVc) are computed, and MLPs merge them. Permutation-equivariant readouts on H and on the diagonal / off-diagonal of C feed a decision layer.
**Key equation:** `$C^{(l+1)} = \mathrm{MLP}_M\big(C^{(l)} \,\|\, L_1(C^{(l)})\!\cdot\!L_2(C^{(l)}) \,\|\, L_3(C^{(l)})\odot L_4(C^{(l)}) \,\|\, \mathrm{diag}(L_6(H^{(l)}))\big)$` ; `$H^{(l+1)} = \mathrm{MLP}_{V_c}\big(H^{(l)} \,\|\, L_5(C^{(l)})\!\cdot\!L_7(H^{(l)})\big)$`

**Audio script:** Here is the recipe in three moves. Start from the operation set L-three: matrix product, transpose, the all-ones vector, diagonal, and element-wise product. Write down an exhaustive grammar whose sentences are exactly the fragment ML-of-L-three. Then reduce that grammar, stripping away redundant rules and variables until only the essential productions remain, while proving each step keeps the 3-W-L guarantee. Now the magic: the surviving variables tell you what the network's inputs should be, and each surviving rule becomes a piece of a layer. Concretely, a layer carries an edge memory C and a node memory H; learnable linear blocks combine slices of these tensors, the reduced rules like M-times-M and M-Hadamard-M are computed, and two small MLPs stitch everything back together. Stack these layers, add permutation-equivariant readouts, and you have G2N2.

## Dataset / Benchmark
**Necessary:** QM9 (130K molecules, 12 regression targets, hardest target R²) for regression; the TUD benchmark (MUTAG, PTC, Proteins, NCI1, IMDB-B, IMDB-M) for graph classification; and a spectral node-regression dataset for band-pass filter learning.
**Additional:** QM9 is split 0.8 / 0.1 / 0.1 for train / val / test as in prior work; TUD uses the standard evaluation protocol; the spectral task follows the 900-node-graph protocol used to stress PPGN.
**Audio script:** The evaluation spans three very different arenas. For regression, the QM9 dataset of one hundred thirty thousand small molecules, with twelve quantum-chemical targets, including R-squared, the hardest one to predict. For classification, the classic TUD benchmark, six datasets ranging from molecules like MUTAG and PTC to social graphs like IMDB. And for a spectral stress test, a node-regression task on nine-hundred-node graphs that asks whether the model can act as a band-pass filter. Together they probe accuracy, generality, and a subtle spectral ability that trips up other 3-W-L models.

## Key Result
**Necessary:** On QM9 regression G2N2 obtains the best MAE on every target while training faster than PPGN; on the hardest R² target it cuts MAE from PPGN's 3.78 to 0.342 (single-target) and 16.07 to 1.19 (all-targets-at-once).
**Additional:** On TUD it ranks better than 2nd on five of six datasets (e.g. MUTAG 92.5%, PTC 72.3%, Proteins 80.1%), and on spectral filtering it learns band-pass filters (R² 0.8206) where PPGN collapses (0.1041).
**Audio script:** The headline result is that G2N2 does not just match the theory, it dominates in practice. On QM9, learning targets one at a time, it posts the best error on every single target while training faster than PPGN. On the notoriously hard R-squared target, its error drops to zero-point-three-four-two, where PPGN sits at three-point-seven-eight, more than a ten-fold improvement, and when all twelve targets are learned at once the gap widens further. On graph classification it beats the second-best network on five of the six TUD datasets. And on the spectral test it cleanly learns band-pass filters where PPGN, starved of the memory it would need, essentially fails.

## Ablation Study
**Necessary:** The grammar-reduction study (Q1) shows G(L3), the intermediate grammar, and the reduced r-G(L3) reach comparable MAE on QM9 R², confirming reduction preserves expressiveness, while over-reducing (removing rules) degrades MAE — validating each rule's contribution.
**Additional:** Removing rules also reveals each operation's weight in the model, guiding principled pruning when full 3-WL expressiveness is not required for a task.
**Audio script:** The most instructive experiment is the grammar-reduction ablation. The authors compare the full grammar, an intermediate one, and the reduced grammar r-G-of-L-three on the QM9 R-squared target. Their errors are essentially the same, which confirms that reduction throws away redundancy without touching expressive power. But when you push past the reduced grammar and start deleting essential rules, performance degrades in a measurable way. That degradation is actually useful information: it tells you how much each operation contributes, so you can prune the model deliberately when a task does not demand the full 3-W-L strength.

## Headline Numbers
**Necessary:**
- QM9 R² MAE: 0.342 (G2N2) vs 3.78 (PPGN), single-target — a ~11× reduction.
- QM9 mean epoch time: 98 s (G2N2) vs 129 s (PPGN), single-target.
**Additional:**
- Spectral band-pass R²: 0.8206 (G2N2) vs 0.1041 (PPGN).
- TUD: better than rank 2 on 5 of 6 datasets (MUTAG 92.5±5.5, Proteins 80.1±3.7).
**Audio script:** A few numbers capture the impact. On QM9's R-squared target, error falls from three-point-seven-eight to zero-point-three-four-two, roughly an eleven-fold reduction, and the model does it in ninety-eight seconds per epoch versus PPGN's one hundred twenty-nine. On the spectral band-pass task, its R-squared score of zero-point-eight-two towers over PPGN's zero-point-one-zero. And on the TUD classification suite it lands better than second place on five of six datasets, including ninety-two-and-a-half percent on MUTAG.

## Takeaway
**Necessary:** By writing an expressive matrix-language fragment as a reduced context-free grammar and translating its rules into layers, G2N2 becomes a provably 3-WL GNN that is also faster and more accurate than prior 3-WL models.
**Additional:** The framework is generic — any algebraic language fragment can, in principle, be turned into a GNN with matching expressive power.
**Audio script:** The lasting message is a change of workflow. Instead of designing a graph network and then hoping to prove it is expressive, you can start from a language whose expressive power you already know, reduce it to a clean grammar, and read the network straight off the rules, expressiveness guaranteed by construction. G2N2 is the concrete payoff of that idea: a provably 3-W-L model that is faster and more accurate than its predecessors. And because the framework is generic, the same grammatical route could turn other algebraic fragments into other networks, each carrying its expressive power by design.
