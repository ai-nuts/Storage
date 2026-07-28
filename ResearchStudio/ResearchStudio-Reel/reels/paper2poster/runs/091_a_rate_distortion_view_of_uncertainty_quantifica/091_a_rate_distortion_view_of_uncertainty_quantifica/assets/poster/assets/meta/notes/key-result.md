# Key Result

Core claim: On CIFAR-10, DAB outperforms all baselines on both OOD tasks, reaching AUROC 0.986 / AUPRC 0.994 on SVHN and AUROC 0.922 / AUPRC 0.915 on CIFAR-100, beating even a 5-model Deep Ensemble.

Supporting detail: It achieves this with a single forward pass and ~36.5M parameters versus the ensemble's ~182M, at comparable 95.9% accuracy.

Narration: The headline result is that DAB outperforms every baseline on both out-of-distribution tasks. Trained on CIFAR-10, it reaches an AUROC of 0.986 and AUPRC of 0.994 against SVHN, and an AUROC of 0.922 and AUPRC of 0.915 against the harder CIFAR-100, beating even a five-model deep ensemble. Crucially, it does this in a single forward pass with about thirty-six and a half million parameters, versus the ensemble's roughly one hundred and eighty-two million, while keeping accuracy on par at about ninety-six percent.
