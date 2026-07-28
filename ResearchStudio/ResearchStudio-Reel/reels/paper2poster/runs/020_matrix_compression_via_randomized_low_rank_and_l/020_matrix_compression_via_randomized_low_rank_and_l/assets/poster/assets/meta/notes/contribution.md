# Contribution

Core claim: The paper introduces LPLR, a randomized algorithm that jointly produces a low-rank and low-precision factorization A ≈ LR, derives upper bounds on its approximation error as a function of target rank and bit budget, and demonstrates it on images, embeddings, and LLM weights.

Supporting detail: It also proposes LPLR-SVD (LSVD), an SVD-based variant, and characterizes when direct-SVD quantization versus LPLR is preferable through the row-norm versus entry-bounded regimes (Tables 1 and 2).

Narration: The core contribution is LPLR, Low-Precision Low-Rank factorization: a randomized algorithm that exploits low-rank structure and quantizes the resulting factors. The authors derive rigorous upper bounds on the approximation error in terms of target rank and bit budget, exposing a tunable compression-accuracy tradeoff. They add an SVD-based variant, LPLR-SVD, and validate on images, embedding classification, and LlaMa-7b weights.
