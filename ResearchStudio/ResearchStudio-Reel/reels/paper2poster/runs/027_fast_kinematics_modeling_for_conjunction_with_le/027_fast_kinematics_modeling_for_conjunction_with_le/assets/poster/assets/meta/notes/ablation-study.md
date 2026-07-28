# Ablation Study

Core claim: The paper is a proof-of-concept and reports no formal ablation table; performance is characterized by the per-pixel error distribution across the 500-image test set (median ~0.47%, 90th percentile ~1.1%) and by contrasting GPU vs CPU inference.

Supporting detail: GPU inference is roughly 10× faster than CPU; the accuracy analysis distinguishes the constrained innermost two-arcsecond region (±1% error) from outer regions where errors can reach a few percent.

Narration: As a proof-of-concept workshop paper, this work does not present a formal ablation study. Instead, performance is characterized by the distribution of per-pixel errors across the five hundred test images, and by comparing inference on GPU versus CPU, where the GPU is about ten times faster. The analysis also distinguishes the innermost two-arcsecond region, where errors stay within one percent, from the outer parts of the image, where errors can rise to a few percent but the data provides little constraint anyway.
