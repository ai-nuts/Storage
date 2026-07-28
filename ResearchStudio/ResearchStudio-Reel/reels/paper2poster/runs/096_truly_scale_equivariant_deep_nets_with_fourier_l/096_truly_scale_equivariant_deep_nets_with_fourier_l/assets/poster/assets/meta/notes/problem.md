# Problem

Core claim: Existing scale-equivariant CNNs are not truly scale-equivariant in practice: they achieve equivariance through weight-sharing and kernel resizing but incur non-negligible equivariance error.

Supporting detail: They derive resizing in the continuous domain, so they never account for anti-aliasing that a discrete down-scaling operation demands.

Narration: Scale-equivariance means that when an object in an image is resized, the network's features should transform consistently, and its label should stay the same. Recent scale-equivariant convolutional networks pursue this through weight-sharing and kernel resizing, using the same but resized kernel across scales. The trouble is that these methods are derived in the continuous domain, then discretized when implemented. That discretization step introduces a non-negligible equivariance error, so the networks are only approximately scale-equivariant, not truly so.
