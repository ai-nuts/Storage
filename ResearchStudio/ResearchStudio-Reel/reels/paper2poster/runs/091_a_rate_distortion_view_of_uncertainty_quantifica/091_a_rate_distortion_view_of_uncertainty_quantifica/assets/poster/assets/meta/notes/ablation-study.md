# Ablation Study

Core claim: For misclassification prediction on CIFAR-10, DAB reaches Calibration AUROC 0.930, closing the gap to Deep Ensembles (0.951) and far surpassing other single-pass DUMs such as DDU (0.632), DUE (0.856), DUQ (0.889), and SNGP (0.897).

Supporting detail: A codebook visualization shows each of the 10 centroids progressively attracting test points of a single class over training epochs, confirming the codes meaningfully represent the data.

Narration: On the task of predicting its own mistakes on CIFAR-10, DAB reaches a calibration AUROC of 0.930. That nearly closes the gap to a deep ensemble at 0.951, while dramatically outperforming other single-pass deterministic methods such as DDU at 0.632, DUE at 0.856, DUQ at 0.889, and SNGP at 0.897. A visualization of the learned codebook further shows each of the ten centroids progressively attracting test points of a single class as training proceeds, confirming that the codes capture meaningful structure in the data.
