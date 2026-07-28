# Motivation

Core claim: Natural images contain heavy spatial redundancy that a shared, sparse representation can exploit; a few prior parameterization methods use cross-image relationships but none address redundancy irrespective of spatial location.

Supporting detail: Concentrating the storage budget on a compact shared dictionary plus sparse per-image codes lets SPEED synthesize far more informative images than the naive one-image-per-parameter scheme.

Narration: The key insight is that images are highly redundant. Patches repeat, textures recur, and similar structures appear across many images. Classical representation learning, dictionary learning and sparse coding, was built exactly to capture this: represent many signals as sparse combinations of a shared dictionary. A handful of recent distillation methods started exploiting relationships between synthetic images, but none tackled redundancy in a spatially-agnostic way, no matter where a feature appears. SPEED asks: what if we spend almost none of the storage budget on a shared dictionary and per-image sparse codes, and let a small network reconstruct rich images from them? That reframing is where the gains come from.
