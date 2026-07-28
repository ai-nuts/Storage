# Takeaway

Core claim: Applying differentially private, patch-level randomized CutMix to a vision transformer's smashed data simultaneously strengthens the DP guarantee over vanilla split learning and improves accuracy, with the privacy gain upper-bounded by a Mixup-based counterpart.

Supporting detail: The patch-level, global-attention nature of ViT is what makes patch CutMix work where it hurts CNNs, so the method is tailored to transformer-based distributed learning.

Narration: The takeaway: for vision transformers, you need not trade accuracy for privacy in split learning. Adding Gaussian noise and mixing randomly masked patches across clients amplifies the differential-privacy guarantee over plain split learning and raises accuracy, with the gain provably bounded by a Mixup baseline. It works because transformers use global self-attention at the patch level, so swapping patches costs little, though it would hurt a CNN. Patch-level CutMix is a privacy regularizer built for the transformer era.
