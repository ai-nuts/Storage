# Key Result

Core claim: LPLR compresses matrices to as low as one bit per coordinate while matching or surpassing baselines: on CIFAR-10 embeddings at Bnq = 1 bit it retains 92% accuracy (unquantized 91%) versus 11% for naive quantization, and on LlaMa-7b weights LPLR-SVD achieves 0.537 mean relative Frobenius error versus 0.836 for naive quant.

Supporting detail: On the Shepp-Logan phantom LPLR shows the least visual distortion at aggressive budgets, preserving fine semantic features (the small ellipses) at an average of ~1 bit per pixel where naive 2-bit quantization visibly degrades.

Narration: The headline: LPLR delivers extreme compression, near one bit per coordinate, while preserving performance. On CIFAR-10 embeddings at a single bit, it retains ninety-two percent accuracy, matching the unquantized ninety-one, while naive quantization collapses to eleven. On CIFAR-100, seventy-nine percent versus about one. On LlaMa-7b weights, LPLR-SVD reaches mean relative Frobenius error near zero point five four, against zero point eight four for naive quant, with lower variance.
