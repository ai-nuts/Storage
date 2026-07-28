# Ablation Study

Core claim: Comparing NAS Prune against NAS One-shot shows the expensive iterative pruning gives no consistent advantage over the far cheaper one-shot top-4 selection when good attentions are correctly identified.

Supporting detail: Variants that weight the mixture toward the best homogeneous attentions or add more heads of stronger mechanisms gave no consistent improvement over NAS One-shot.

Narration: A useful practical takeaway comes from comparing the two heterogeneous search procedures. The expensive NAS Prune method, which repeatedly removes the worst block and fine-tunes, offers no consistent advantage over the far cheaper NAS One-shot method that just takes the top-scoring attentions in a single pass, at least when good attentions are correctly identified. Attempts to tilt the mixture toward the strongest attentions or give them more heads also failed to produce consistent gains, reinforcing that the cheap method is good enough.
