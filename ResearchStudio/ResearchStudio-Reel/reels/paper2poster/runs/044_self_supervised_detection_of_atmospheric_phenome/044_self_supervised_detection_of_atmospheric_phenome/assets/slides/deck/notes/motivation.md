# Motivation

Core claim: Self-supervised contrastive learning can exploit vast unlabeled imagery to build reusable embeddings, and has never been widely tested on remote-sensing SAR data despite its success on natural and medical images.

Supporting detail: Sentinel-1 collects nearly 120,000 Wave-mode images every month, an enormous unlabeled resource that contrastive learning could turn into a strong SAR representation.

Narration: Contrastive self-supervised learning has transformed computer vision by training networks on huge pools of unlabeled data to produce embeddings that transfer well to downstream tasks. It has worked for natural images and medical images, but has rarely been applied to remote sensing. That gap matters here, because Sentinel-1 alone collects roughly a hundred and twenty thousand Wave-mode ocean images every single month. This study tests the hypothesis that contrastive learning on that unlabeled stream can overcome the scarcity of expert labels for SAR analysis.
