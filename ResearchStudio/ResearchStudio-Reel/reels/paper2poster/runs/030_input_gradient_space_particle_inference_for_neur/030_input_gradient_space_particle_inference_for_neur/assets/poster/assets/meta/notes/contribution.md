# Contribution

Core claim: The paper proposes FoRDE, a particle-based ensemble method that performs repulsion in first-order input-gradient space, and derives a practical input-gradient kernel with a data-driven PCA lengthscale selection scheme.

Supporting detail: It shows both theoretically and empirically that input-gradient repulsion increases functional diversity, and that the PCA kernel connects to feature-robustness priors such as EmpCov.

Narration: The paper makes three main contributions. First, it introduces First-order Repulsive Deep Ensembles, a method that adds a repulsion term defined on input gradients rather than weights or function outputs. Second, it develops a practical kernel that compares the normalized input gradients of the true label across training data, keeping computation linear in the number of samples. Third, it proposes a principled way to choose the kernel lengthscales using the principal components of the data, which lets FoRDE emphasize high-variance features and become especially robust to input corruptions.
