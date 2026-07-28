# Problem

Core claim: Spherical CNNs compute convolutions in the spectral domain, which is far costlier than planar convolution, so applications were confined to small, low-resolution, low-capacity problems.

Supporting detail: No spherical CNN existed at the scale of common planar architectures like VGG-19, blocking their use on large scientific datasets.

Narration: Spherical CNNs replace the plane with the sphere as the domain of the signal, which is exactly right for data like molecules and the atmosphere. The catch is that their core operation, spherical convolution, is most accurate in the spectral domain, and that is far more expensive than an ordinary planar convolution. Because of this cost, spherical CNNs had been limited to small, low-resolution problems with modest model capacity. There simply was no large-scale spherical architecture analogous to the deep planar networks that power modern computer vision.
