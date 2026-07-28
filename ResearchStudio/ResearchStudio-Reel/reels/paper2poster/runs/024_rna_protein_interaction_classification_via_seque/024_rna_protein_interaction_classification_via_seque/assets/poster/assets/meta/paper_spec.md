---
title: RNA-Protein Interaction Classification via Sequence Embeddings
authors: Dominika Matus¹, Frederic Runge¹, Jörg K.H. Franke¹, Lars Gerne¹, Michael Uhl¹, Frank Hutter²¹, Rolf Backofen¹
institutes: ¹University of Freiburg; ²ELLIS Institute Tübingen
venue: ICLR 2024
paper_url: https://www.biorxiv.org/content/10.1101/2024.11.08.622607v1
code_url:
title_audio_script: RNA-protein interactions drive gene regulation, yet measuring them in the lab is slow and costly, and existing predictors lean on small, protein-specific datasets. This work introduces RNAInterAct, a large curated dataset of non-coding RNA-protein interactions, and RPIembeddor, a transformer model that classifies whether any RNA and protein interact using only their sequences. By feeding embeddings from two foundation models, RNA-FM for RNA and ESM-2 for proteins, into an attention-based network, RPIembeddor outperforms prior state-of-the-art methods and generalizes to unseen RNA families and data distributions.
---

## Problem
**Necessary:** Predicting whether an arbitrary non-coding RNA and protein interact, from sequence alone, is largely unsolved: most methods are protein-specific and need large per-protein interaction datasets that exist for only a few hundred of the ~2,000 human RNA-binding proteins.
**Additional:** Experimental assays like SELEX and CLIP-seq are time-consuming and expensive, and RNA structural features that drive interactions are not available at scale.
**Audio script:** Non-coding RNAs regulate the cell largely through their interactions with proteins, but mapping these interactions experimentally is slow and costly. Most computational predictors sidestep the general problem by training one model per protein, which requires a large interaction dataset for that specific protein. Such datasets exist for only a few hundred of the roughly two thousand human RNA-binding proteins. What is missing is a method that decides, for any given RNA and protein pair, whether they interact using nothing but their sequences.

## Motivation
**Necessary:** A sequence-only classifier that works across diverse RNA and protein types would unlock the vast, unexplored space of RNA-protein interactions without per-protein training data, but meta-learning across interaction types for this task remains largely unexplored.
**Additional:** Foundation models trained on massive unlabeled corpora can inject structural and functional priors that are otherwise unavailable for RNAs at scale.
**Audio script:** Recent progress shows two useful ideas. First, learning across many tasks, rather than one protein at a time, can help when labeled data is scarce. Second, foundation models trained on huge unlabeled biological corpora capture structural and functional signal that raw sequences do not expose directly. Combining these ideas, a single model could learn general rules of RNA-protein binding and apply them to interaction types it has never seen, which is exactly what a broad, sequence-only predictor needs.

## Contribution
**Necessary:** The paper delivers (1) RNAInterAct, a large curated ncRNA-protein interaction dataset with rigorously homology-separated train/test splits; (2) RPIembeddor, an attention-based classifier built on two foundation-model embeddings that outperforms state-of-the-art methods and generalizes to unseen distributions; and (3) an ablation confirming both embeddings are essential.
**Additional:** Train and test sets are split by RNA family to eliminate homology bias, giving a true test of generalization rather than the optimistic estimates from random splits.
**Audio script:** The work makes three contributions. It builds RNAInterAct, an extensive dataset of non-coding RNA-protein interactions derived from the RNAInter database and enriched with carefully generated negatives. It introduces RPIembeddor, a transformer that classifies interactions from sequence embeddings and beats existing tools while generalizing to new data. And through an ablation study it shows that the two foundation-model embeddings are not optional add-ons but the core of the model's ability to classify correctly.

## Method
**Necessary:** RPIembeddor embeds RNA sequences with RNA-FM and protein sequences with the 150M-parameter ESM-2 (both 640-dimensional), normalizes them through parallel feed-forward layers, then processes them symmetrically in attention-based encoder layers so each modality has equal influence. The latent representations are concatenated, passed through feed-forward layers, and a linear layer with sigmoid activation outputs the interaction probability.
**Additional:** The resulting model has only 1.4M parameters and is trained with a binary loss and the AdamW optimizer using linear warm-up plus cosine annealing; ESM-2 is chosen over AlphaFold because it needs no multiple sequence alignments.
**Key equation:** `$\hat{p} = \sigma\big(\mathbf{W}\,\mathbf{h} + b\big)$`  <!-- interaction probability: a linear layer with sigmoid activation over the concatenated latent representation h; trained with a binary (cross-entropy) loss -->
**Audio script:** RPIembeddor turns sequences into knowledge by leaning on two pre-trained foundation models. RNA sequences are embedded with RNA-FM, trained on twenty-three million non-coding RNAs, and protein sequences with ESM-2, which predicts folding without multiple sequence alignments. Both produce embeddings of size N by six hundred forty. Two parallel feed-forward layers normalize their sizes, and encoder layers process the RNA and protein embeddings symmetrically so attention can focus on the parts of each sequence most relevant to interaction. The latent representations are concatenated and passed through further feed-forward layers, ending in a linear layer with a sigmoid that outputs the probability of interaction. The whole model has just one-point-four million parameters.

## Dataset / Benchmark
**Necessary:** RNAInterAct is built from the RNAInter database (over 47 million RNA interactions), cross-referenced with NCBI, UniProt and Ensembl for sequences and annotated with Rfam families and Pfam clans to generate biologically plausible negatives. It totals 122,217 ncRNA-protein interactions at a 1:2 positive-to-negative ratio, split by RNA family into TRinter (training) and TSfam (test) with no family overlap; models are additionally tested on the external, positives-only RPI2825 set.
**Additional:** Curation applies a 1024 nucleotide/amino-acid length cutoff, caps interactions per interactor at 150, and excludes mRNAs. TRinter holds 109,214 interactions over 976 RNA families; TSfam holds 13,003 over 172 families; RPI2825 holds 871 positive interactions.
**Audio script:** The dataset is the backbone of the study. Starting from RNAInter, with over forty-seven million RNA interactions, the authors recover sequences by cross-referencing NCBI, UniProt and Ensembl, and assign RNA families from Rfam and protein clans from Pfam. Those annotations let them generate negatives that are biologically meaningful rather than random. The final RNAInterAct set holds about one hundred twenty-two thousand interactions at a one-to-two positive-to-negative ratio. Crucially, it is split by RNA family, so no family appears in both training and testing. This homology-aware split, plus evaluation on the external RPI2825 dataset, tests true generalization instead of memorization.

## Key Result
**Necessary:** On the homology-separated TSfam test set RPIembeddor clearly outperforms prior methods, reaching F1 0.586 (±0.010) and accuracy 0.667 (±0.009) with ROC AUC 0.70 (±0.01), versus AUC 0.48 for XRPI and 0.50 for IPMiner — the competitors perform at or below chance.
**Additional:** RPIembeddor correctly classifies 2,971 of 4,887 positive and 5,586 of 8,116 negative TSfam interactions, while XRPI collapses to predicting ~91% of pairs as positive despite ~62% being negative.
**Audio script:** On the hardest test, TSfam, where no RNA family overlaps with training, RPIembeddor reaches an F1 score of about zero-point-five-nine and an accuracy of about zero-point-six-seven. Its ROC area under the curve is zero-point-seven-zero, while the competing tools XRPI and IPMiner sit at zero-point-four-eight and zero-point-five-zero, essentially chance. In concrete terms, RPIembeddor correctly labels nearly three thousand of the positive interactions and over five thousand of the negatives, whereas XRPI simply predicts almost everything as interacting. The model clearly learns real signal that generalizes to unseen RNA families.

## Ablation Study
**Necessary:** Replacing either the RNA-FM or ESM-2 embedding with a random embedding, or both with one-hot encodings, causes the model to collapse into a negative-only classifier: precision, recall and F1 all drop to 0.0, with accuracy stuck at 0.624 (merely the negative class fraction). The full two-embedding model instead reaches F1 0.605 and accuracy 0.678.
**Additional:** This shows both foundation-model embeddings are individually necessary — neither structural/functional signal can be dropped or replaced by a simpler representation without breaking the model.
**Audio script:** To test whether the two embeddings really matter, the authors retrain the model after swapping out the RNA embedding, the protein embedding, or both, for random vectors or one-hot encodings. In every one of these variants the model stops working, predicting only the negative class, so its F1 score falls to zero and its accuracy merely reflects the fraction of negatives in the data. Only when both the RNA-FM and ESM-2 embeddings are present does the model classify correctly. This confirms that the foundation-model embeddings carry the structural and functional information the task depends on.

## Headline Numbers
**Necessary:**
- ROC AUC 0.70 on TSfam, versus 0.48 (XRPI) and 0.50 (IPMiner)
- F1 0.586 and accuracy 0.667 on TSfam — best among all methods
- 122,217 ncRNA-protein interactions in RNAInterAct across 976 RNA families
- 1.4M-parameter model built on RNA-FM + ESM-2 (150M) embeddings
**Additional:** Second-best F1 of 0.8 on the external positives-only RPI2825 set, demonstrating cross-distribution generalization.
**Audio script:** A few numbers capture the impact. RPIembeddor scores a ROC area under the curve of zero-point-seven-zero on the homology-separated test set, where the best competitor manages only zero-point-five-zero. Its F1 of zero-point-five-nine and accuracy of zero-point-six-seven lead all methods. The RNAInterAct dataset contributes over one hundred twenty-two thousand interactions spanning nine hundred seventy-six RNA families. And all of this runs in a compact one-point-four-million-parameter model powered by the RNA-FM and ESM-2 foundation models.

## Takeaway
**Necessary:** Feeding RNA and protein foundation-model embeddings into a small attention-based classifier yields the first strong sequence-only predictor that generalizes across unseen RNA families, and the released RNAInterAct dataset provides the homology-aware benchmark to drive further progress.
**Additional:** Both embeddings are indispensable; future work aims to add RNA-structure models and lift the sequence-length limit.
**Audio script:** The lasting message is that general RNA-protein interaction prediction from sequence alone is achievable when you stand on the shoulders of foundation models. A compact attention network fed with RNA-FM and ESM-2 embeddings outperforms specialized tools and, unlike them, generalizes to RNA families it has never seen. The companion RNAInterAct dataset, split to remove homology bias, gives the community a fair benchmark. Both embeddings are essential, and the authors point toward adding RNA-structure models and longer sequences next.
