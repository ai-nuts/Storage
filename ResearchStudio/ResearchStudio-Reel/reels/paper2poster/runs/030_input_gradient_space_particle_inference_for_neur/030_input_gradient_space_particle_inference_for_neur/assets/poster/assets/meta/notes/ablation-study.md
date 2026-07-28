# Ablation Study

Core claim: Comparing lengthscale choices, FoRDE-PCA is most robust to corruptions, FoRDE-Identity has the best accuracy on CIFAR-100 and best NLL on CIFAR-10 but is slightly less corruption-robust, and FoRDE-Tuned (a weighted average of the two) does best on both clean and corrupted data in most cases.

Supporting detail: Under varying ensemble size on WideResNet16x4, a 10-member FoRDE matches or beats the corruption robustness of a 30-member deep ensemble, though it slightly trails deep ensembles on clean data.

Narration: The paper carefully ablates the kernel lengthscales, which govern how repulsion is distributed across input dimensions. The PCA lengthscales give the best robustness to corruptions, because they emphasize high-variance features. The identity lengthscales instead give the best clean accuracy on CIFAR-100 and the best likelihood on CIFAR-10, but sacrifice some robustness. Tuning between the two extremes yields the best of both worlds in most cases. A separate study varies the ensemble size and finds that a FoRDE with ten members matches or exceeds the corruption robustness of a deep ensemble with thirty members, showing that the diversity gain is substantial.
