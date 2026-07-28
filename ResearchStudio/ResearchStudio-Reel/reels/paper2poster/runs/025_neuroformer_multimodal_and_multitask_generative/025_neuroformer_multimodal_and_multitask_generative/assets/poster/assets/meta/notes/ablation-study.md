# Ablation Study

Core claim: Adding each architectural component (Current State, Past State, Video, Behavior, and the Contrastive objective) consistently improves predictive performance across datasets and brain regions; joint training on neural responses and behavior outperforms training on either alone.

Supporting detail: The contrastive alignment objective is especially helpful in low-data settings, mitigating over-fitting on variable neural signals.

Narration: An ablation removes components one at a time: the Current State, Past State, video stream, behavior stream, and contrastive objective each add measurable predictive power. Two findings stand out. Jointly training on neural responses and behavior beats either alone, and the contrastive objective helps most when data is scarce.
