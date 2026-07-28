# Dataset / Benchmark

Core claim: Validation spans 2D synthetic von Mises mixtures, StyleGAN2-ADA and iDDPM trained on CIFAR10, and Stable Diffusion v1.5 on large-scale image data; for Stable Diffusion, 86 "matching verbatim" memorized LAION images (from Webster, 2023) are contrasted against non-memorized images.

Supporting detail: The non-memorized pool mixes 2000 images from LAION-Aesthetics 6.5+, 2000 from COCO, and all 251 images from the Tuxemon dataset; the normal-bundle (NB) and FLIPD estimators are used for LID.

Narration: The experiments deliberately sweep across scales. At the small end, two-dimensional synthetic von Mises mixtures let the authors compute ground-truth local dimension exactly. In the middle, StyleGAN2-ADA and an iDDPM diffusion model on CIFAR10. At the large end, Stable Diffusion version 1.5, where they study 86 verbatim-memorized LAION images against thousands of non-memorized images drawn from LAION Aesthetics, COCO, and the Tuxemon dataset.
