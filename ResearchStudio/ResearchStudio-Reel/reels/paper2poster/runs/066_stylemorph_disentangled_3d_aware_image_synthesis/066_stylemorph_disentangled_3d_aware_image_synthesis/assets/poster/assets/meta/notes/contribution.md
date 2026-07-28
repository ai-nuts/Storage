# Contribution

Core claim: StyleMorph learns a 3D morphable model of non-rigid shape variation for an object category purely from 2D image supervision, and introduces Template Object Coordinates (TOCS), a deformable variant of Normalized Object Coordinates that serves as a deformation-equivariant descriptor of 3D shape.

Supporting detail: Using 2D TOCS maps as a conditioning signal for a style-based deferred neural renderer, it achieves unprecedented joint disentanglement of pose, shape, object appearance, and scene appearance for high-resolution, photorealistic synthesis.

Narration: StyleMorph makes three linked contributions. First, it learns a 3D morphable model of an object category's non-rigid shape variation using nothing but 2D images, by morphing a canonical template through backpropagation. Second, it introduces Template Object Coordinates, or TOCS: a deformable cousin of Normalized Object Coordinates that gives every surface point a stable template identity and acts as a powerful, deformation-equivariant descriptor of shape. Third, it feeds 2D TOCS maps as a purely geometric conditioning signal into a StyleGAN-based deferred neural renderer, cleanly separating shape from appearance. Together these deliver disentangled control over pose, shape, object appearance, and background, all at high resolution.
