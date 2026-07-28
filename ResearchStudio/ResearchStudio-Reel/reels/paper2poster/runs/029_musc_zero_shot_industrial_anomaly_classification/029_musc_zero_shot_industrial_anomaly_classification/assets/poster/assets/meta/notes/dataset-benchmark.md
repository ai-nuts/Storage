# Dataset / Benchmark

Core claim: Evaluated on two standard industrial benchmarks: MVTec AD (15 categories, 10 objects + 5 textures) and VisA (12 objects). Both contain normal and anomalous test images.

Supporting detail: Classification is scored with AUROC, AP, and F1-max; segmentation with pixel-wise AUROC, F1-max, AP, and Per-Region Overlap (PRO).

Narration: MuSc is evaluated on the two most-used industrial benchmarks. MVTec AD spans fifteen categories, ten objects and five textures. VisA covers twelve object categories across three domains. Both mix normal and defective images. Classification uses AUROC and F1-max; segmentation adds pixel-level metrics and per-region overlap.
