# Dataset / Benchmark

Core claim: Evaluated on CIFAR-10 (in-distribution) with SVHN as far-OOD and CIFAR-100 as near-OOD, on CIFAR-10 misclassification prediction, and on large-scale ImageNet-1K with ImageNet-O as the OOD set.

Supporting detail: DAB uses a narrow 8-dimensional latent bottleneck with only 10 distributional codes; baselines include Deep Ensembles, DDU, DUQ, DUE, SNGP, and vanilla VIB.

Narration: The method is tested across several settings. On CIFAR-10 as the in-distribution data, SVHN serves as a far out-of-distribution set and CIFAR-100 as a harder near out-of-distribution set. The authors also study misclassification prediction on CIFAR-10 and scale up to ImageNet-1K with ImageNet-O as the out-of-distribution set. Notably, DAB works with a very narrow eight-dimensional latent bottleneck and just ten distributional codes, and is compared against strong baselines including deep ensembles, DDU, DUQ, DUE, SNGP, and the vanilla variational Information Bottleneck.
