# Ablation Study

Core claim: Comparing evaluation protocols, contrastive weights beat ImageNet weights slightly under kNN (0.864 vs 0.859) and linear evaluation (0.841 vs 0.836), but this reverses under full fine-tuning, where ImageNet edges ahead (0.931 vs 0.929).

Supporting detail: The advantage of self-supervised pretraining only appears when the backbone is frozen; once all weights are fine-tuned, the initialization barely matters.

Narration: The most informative comparison is across the three evaluation protocols. When the backbone is frozen, the self-supervised contrastive weights hold a small edge, scoring zero point eight six four versus zero point eight five nine under nearest-neighbor classification and zero point eight four one versus zero point eight three six under linear evaluation. But once all weights are fine-tuned end to end, that gap not only disappears but slightly reverses, with the ImageNet initialization reaching zero point nine three one against the contrastive model's zero point nine two nine. In other words, the benefit of self-supervised pretraining vanishes once the whole network is allowed to adapt.
