# Contribution

Core claim: The paper delivers (1) RNAInterAct, a large curated ncRNA-protein interaction dataset with rigorously homology-separated train/test splits; (2) RPIembeddor, an attention-based classifier built on two foundation-model embeddings that outperforms state-of-the-art methods and generalizes to unseen distributions; and (3) an ablation confirming both embeddings are essential.

Supporting detail: Train and test sets are split by RNA family to eliminate homology bias, giving a true test of generalization rather than the optimistic estimates from random splits.

Narration: The work makes three contributions. It builds RNAInterAct, an extensive dataset of non-coding RNA-protein interactions derived from the RNAInter database and enriched with carefully generated negatives. It introduces RPIembeddor, a transformer that classifies interactions from sequence embeddings and beats existing tools while generalizing to new data. And through an ablation study it shows that the two foundation-model embeddings are not optional add-ons but the core of the model's ability to classify correctly.
