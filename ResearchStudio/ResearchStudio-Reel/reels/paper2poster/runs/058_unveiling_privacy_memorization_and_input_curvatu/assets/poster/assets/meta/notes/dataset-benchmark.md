# Dataset / Benchmark

Core claim: Standard image classification benchmarks: CIFAR10, CIFAR100, and ImageNet, using Feldman & Zhang (2020) precomputed memorization scores and their released model ensembles.

Supporting detail: Architectures include Small Inception and ResNet50 (CIFAR100 / ImageNet memorization ensembles) and ResNet18 trained with DP-SGD for the privacy experiments.

Narration: Validation uses CIFAR10, CIFAR100, and ImageNet. Memorization relies on Feldman and Zhang's precomputed scores and ensembles, a thousand models on CIFAR100 and a hundred on ImageNet, using Small Inception and ResNet50. Privacy experiments train ResNet18 with DP-SGD across several budgets.
