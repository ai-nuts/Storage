# Motivation

Core claim: 3DMMs are the workhorse of VFX and AR because they give creators disentangled control over pose, expression, and appearance; bringing that control to 3D-aware GANs without 3D supervision would unlock editable, category-general synthesis.

Supporting detail: Prior deformation-based methods either handle a single dynamic scene or assume a pre-existing deformable template already exists for the category, so they do not learn the morphable model itself from scratch.

Narration: Morphable models are the workhorse of visual effects and augmented reality because they hand creators clean, separate dials for pose, expression, and appearance. The question that motivates this work is simple: can we get that same level of control inside a modern 3D-aware GAN, but without any of the 3D supervision that morphable models normally need? Prior work that added 3D deformations to synthesis either stayed limited to a single dynamic scene, or leaned on a deformable template that already existed for the category. StyleMorph instead turns the morphable model itself into something the network discovers from unlabeled 2D images, making it a first-class citizen of generative modelling.
