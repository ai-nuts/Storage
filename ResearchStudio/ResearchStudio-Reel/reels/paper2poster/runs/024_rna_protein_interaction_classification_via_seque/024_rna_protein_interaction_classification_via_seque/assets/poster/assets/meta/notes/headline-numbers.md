# Headline Numbers

Core claim: - ROC AUC 0.70 on TSfam, versus 0.48 (XRPI) and 0.50 (IPMiner) - F1 0.586 and accuracy 0.667 on TSfam — best among all methods - 122,217 ncRNA-protein interactions in RNAInterAct across 976 RNA families - 1.4M-parameter model built on RNA-FM + ESM-2 (150M) embeddings

Supporting detail: Second-best F1 of 0.8 on the external positives-only RPI2825 set, demonstrating cross-distribution generalization.

Narration: A few numbers capture the impact. RPIembeddor scores a ROC area under the curve of zero-point-seven-zero on the homology-separated test set, where the best competitor manages only zero-point-five-zero. Its F1 of zero-point-five-nine and accuracy of zero-point-six-seven lead all methods. The RNAInterAct dataset contributes over one hundred twenty-two thousand interactions spanning nine hundred seventy-six RNA families. And all of this runs in a compact one-point-four-million-parameter model powered by the RNA-FM and ESM-2 foundation models.
