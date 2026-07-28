# Dataset / Benchmark

Core claim: Evaluated on CIFAR-10, CIFAR-100 and TinyImageNet image classification, with corrupted variants CIFAR-10-C, CIFAR-100-C and TinyImageNet-C covering 19 corruption types across 5 severity levels, plus 1D/2D toy tasks and a transfer-learning setup.

Supporting detail: Backbones are ResNet18 for CIFAR, PreActResNet18 for TinyImageNet, and WideResNet16x4 for the ensemble-size study; metrics are accuracy, NLL and expected calibration error (ECE), with corrupted counterparts cA, cNLL and cECE.

Narration: The method is tested across a broad range of settings. Illustrative one-dimensional regression and two-dimensional classification tasks show how input-gradient repulsion increases uncertainty away from the data. The main image classification experiments use CIFAR-10, CIFAR-100, and TinyImageNet, with ResNet and PreActResNet backbones and an ensemble of ten members. To measure robustness, the authors use the corrupted benchmarks CIFAR-10-C, CIFAR-100-C, and TinyImageNet-C, which apply nineteen types of image corruption at five severity levels. They report accuracy, negative log-likelihood, and expected calibration error, both on clean data and averaged over all corruptions.
