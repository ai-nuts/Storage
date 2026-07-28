# Problem

Core claim: Industrial anomaly classification and segmentation usually need many normal reference images (one-class methods) or hand-crafted text prompts (CLIP-based zero-shot methods), both of which limit real-world deployment.

Supporting detail: In a true zero-shot setting no training data, prompts, or normal references are available, yet defects still must be localized at the pixel level and flagged at the image level.

Narration: Detecting defects is a core vision task, but existing methods are demanding. One-class approaches need a bank of normal images per product; CLIP-based zero-shot methods rely on hand-written prompts. Many factories have neither. The goal: segment anomalies with no training, prompts, or references.
