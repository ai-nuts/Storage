# Dataset / Benchmark

Core claim: Fashion MNIST (bias-isolation MLP experiments), and CIFAR-10, CIFAR-100, and ImageNet 32×32 for the recurrent convolutional architecture with asymmetric feedback weights.

Supporting detail: Predictive coding networks (Appendix D) further confirm the homeostatic loss generalizes beyond reciprocal architectures.

Narration: The experiments span four datasets of increasing difficulty. On Fashion MNIST, small multilayer networks are used to cleanly isolate and measure each source of bias. Then a recurrent convolutional architecture with genuinely asymmetric feedback weights is trained on CIFAR-10, CIFAR-100, and finally ImageNet at thirty-two by thirty-two, which is where the homeostatic loss really earns its keep. The authors also confirm in the appendix that the same loss helps predictive coding networks, which have no reciprocal connections at all.
