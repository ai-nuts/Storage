# Problem

Core claim: Vision transformers (ViTs) lack the inductive biases of ConvNets and only outperform them when huge labeled datasets are available; labeling data at that scale is expensive and time-consuming.

Supporting detail: Existing self-supervised pretext tasks (jigsaw, colorization, image-rotation) were designed for ConvNets, which emit a single feature map, and do not exploit the patch-token structure that makes ViTs distinctive.

Narration: Vision transformers have overtaken convolutional networks on many vision tasks, but only when trained on very large labeled datasets. With limited labels their performance falls behind ConvNets, because they lack built-in inductive biases like locality and translation equivariance. Labeling data at the scale ViTs need is expensive and slow. Self-supervised learning can help by learning useful features without labels, but the popular self-supervised pretext tasks were all designed for convolutional networks and ignore the patch-token structure that makes transformers special.
