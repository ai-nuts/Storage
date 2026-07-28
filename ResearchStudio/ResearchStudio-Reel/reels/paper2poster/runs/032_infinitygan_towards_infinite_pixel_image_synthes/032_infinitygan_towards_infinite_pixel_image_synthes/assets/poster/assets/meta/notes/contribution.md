# Contribution

Core claim: InfinityGAN is a framework for arbitrary-sized image synthesis that disentangles global appearance, local structure, and texture, trains and infers patch-by-patch with constant memory, and enables seamless composition of independently generated patches.

Supporting detail: It introduces a coordinate-conditioned neural-implicit structure synthesizer, a padding-free fully-convolutional texture synthesizer, a ScaleInv FID evaluation metric, and unlocks spatial style fusion, multi-modal outpainting, and arbitrary-length inbetweening.

Narration: InfinityGAN makes five contributions. First, it reframes generation as disentangling global appearance, local structure, and fine texture, each with a dedicated component. Second, a structure synthesizer built as a neural implicit function driven by continuous coordinates, so any sub-region can be queried directly. Third, a padding-free generator removing all zero-padding, letting patches synthesize independently yet combine seamlessly. Fourth, a scale-invariant FID metric for sizes where no real reference images exist. Finally, applications the design unlocks, from spatial style fusion to outpainting.
