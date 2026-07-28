# Dataset / Benchmark

Core claim: Optimal losses are computed for MNIST and CIFAR-10 under an L2-constrained test-time attacker at varying strengths ε, in both a 3-class setting (1000 samples per class) and the full 10-class setting.

Supporting detail: 3-class MNIST uses classes 1, 4, 7; 3-class CIFAR-10 uses plane, bird, ship. Adversarially trained baselines use TRADES (3-layer CNN on MNIST, WRN-28-10 on CIFAR-10) evaluated with APGD-CE from AutoAttack.

Narration: The experiments use two standard vision benchmarks, MNIST and CIFAR-10, under an L-two constrained attacker evaluated across a sweep of perturbation budgets. For the 3-class studies they take one thousand samples per class, using digits one, four, and seven for MNIST and the plane, bird, and ship classes for CIFAR-10. They also compute bounds for the full 10-class problem on the complete training sets. As reference defenses, they train classifiers with TRADES adversarial training, a small convolutional network for MNIST and a wide residual network for CIFAR-10, and evaluate them with the strong APGD attack from AutoAttack.
