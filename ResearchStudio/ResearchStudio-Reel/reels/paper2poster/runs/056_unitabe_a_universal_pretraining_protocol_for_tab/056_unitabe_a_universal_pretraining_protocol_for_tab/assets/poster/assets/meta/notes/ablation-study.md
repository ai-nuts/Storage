# Ablation Study

Core claim: Removing the linking layer drops average AUC from 0.83 to 0.75 and removing the fuse layer to 0.77; dropping both falls to 0.72, and removing the multi-cell-masking or contrastive-learning objective lowers it to 0.81 and 0.79 respectively, confirming every component contributes.

Supporting detail: A 1-layer decoder outperforms 3- and 6-layer decoders on downstream AUC, validating the shallow-decoder design, even though deeper decoders store more generative knowledge (higher BLEU).

Narration: Ablations confirm each part earns its place. Removing the linking layer, which ties names to values, causes the largest drop, from an AUC of zero point eight three down to zero point seven five. Removing the fuse layer that injects data-type information also hurts, and removing both is worse. Dropping either pretraining objective, multi-cell masking or contrastive learning, reduces performance too. Notably, a one-layer decoder beats three- or six-layer ones, supporting the choice to keep the decoder shallow.
