# Headline Numbers

Core claim: - ~1 bit per matrix coordinate compression while maintaining task performance. - CIFAR-10 embeddings, 1-bit: 92% accuracy (LPLR) vs 11% (naive quant); unquantized 91%. - CIFAR-100 embeddings, 1-bit: 79% accuracy (LPLR) vs ~1% (naive quant). - LlaMa-7b weights (B=B′=8, Bnq=4): mean relative Frobenius error 0.537 (LPLR-SVD) vs 0.836 (naive quant).

Supporting detail: LPLR computational cost is O(ndm) versus O(nd²) for direct-SVD; error bound scales as (1 + k/(m−k−1))·‖A_k − A‖²_F + ε.

Narration: By the numbers: LPLR compresses to one bit per coordinate. On CIFAR-10 at one bit, ninety-two percent accuracy versus eleven for naive quant, matching the unquantized ninety-one. On CIFAR-100, seventy-nine versus one. On LlaMa-7b, mean Frobenius error zero point five four for LPLR-SVD versus zero point eight four. And it runs in order n d m time, far cheaper than a full SVD.
