# Motivation

Core claim: ViT is displacing CNN in vision, so privacy-preserving distributed training must be rethought for transformer architectures whose patch-level, pooling-free design breaks the assumptions behind prior SL privacy.

Supporting detail: ViT's three distinctive properties, low feature distortion at the cut-layer, global self-attention that is robust to localized noise, and patch-level operation, together point to one solution: a patch-scale regularizer.

Narration: As transformers displace CNNs, do the old privacy recipes still hold? The authors note three things about ViT. First, without pooling its hidden representation is barely distorted, so regularizing it works as well as regularizing the input, yet high mutual information leaks. Second, global self-attention makes ViT robust to large noise on part of the image, ideal for Cutout and CutMix. Third, every operation is patch-level. Together these point to a patch-level randomized CutMix of the hidden representation.
