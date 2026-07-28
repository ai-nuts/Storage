# Contribution

Core claim: The paper introduces Color Equivariant Convolutions (CEConvs), a novel building block enforcing equivariance to discrete hue shifts that shares shape features across colors while retaining color, and drops into existing architectures such as ResNets.

Supporting detail: It also shows CNNs benefit from color yet are not robust to color-based domain shifts, and demonstrates CEConvs improve robustness to train-test color shifts, complementing color augmentations.

Narration: The core contribution is the Color Equivariant Convolution, a new layer that hard-wires parameter sharing over hue shifts. It shares shape information across the color spectrum while keeping color in a dedicated group dimension of the feature map. Because it is formulated in the language of symmetry groups, it slots directly into standard networks like ResNet with no architectural surgery. The authors demonstrate, through both controlled toy experiments and realistic benchmarks, that this design improves robustness to color shifts between training and testing and works hand in hand with color augmentation.
