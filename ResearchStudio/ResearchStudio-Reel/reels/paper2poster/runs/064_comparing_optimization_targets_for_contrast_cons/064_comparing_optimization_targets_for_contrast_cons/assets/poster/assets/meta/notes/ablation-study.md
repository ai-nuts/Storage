# Ablation Study

Core claim: MD-CCS and MD-Acc differ only in the hyper-parameter λ, yet give very different cosine similarities to CCS (0.63 vs 0.38 average) — showing CCS's target is governed by the σ_d²/σ_m² trade-off. Swapping MD-CCS's λ for the accuracy-tuned value raises average test accuracy from 0.7178 to 0.7557.

Supporting detail: The MD-CCS hyper-parameter is stable across datasets and models, suggesting the identified proxy target is robust.

Narration: The two Midpoint-Displacement variants differ only in lambda. Tuned to mimic CCS, cosine similarity is about zero point six three; tuned for accuracy, it drops to zero point three eight, showing the displacement-versus-midpoint trade-off defines CCS's target. Retuning lambda raises test accuracy to zero point seven six.
