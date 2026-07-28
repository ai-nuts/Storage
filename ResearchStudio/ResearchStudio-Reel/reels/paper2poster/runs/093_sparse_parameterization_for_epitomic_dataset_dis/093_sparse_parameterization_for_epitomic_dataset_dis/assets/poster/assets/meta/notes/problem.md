# Problem

Core claim: Dataset distillation compresses a large dataset into a small synthetic one, but prior methods obsess over the matching objective and use naive image-independent parameterization, ignoring spatial redundancy within and between synthetic images.

Supporting detail: This redundancy wastes the tiny storage budget, capping how much informative synthetic data can be packed in, and hurts most on high-resolution real-world images.

Narration: The goal of dataset distillation is to shrink a big dataset into a small synthetic set that still trains models well. Most existing work pours its energy into the matching objective, the loss that aligns the synthetic and real datasets. But how the synthetic images are actually parameterized has been an afterthought. The standard approach optimizes each synthetic image independently, a naive scheme that never exploits the fact that natural images share enormous amounts of visual structure, both within a single image and across different images. This spatial redundancy silently wastes the already tiny storage budget, and the problem gets worse as image resolution grows.
