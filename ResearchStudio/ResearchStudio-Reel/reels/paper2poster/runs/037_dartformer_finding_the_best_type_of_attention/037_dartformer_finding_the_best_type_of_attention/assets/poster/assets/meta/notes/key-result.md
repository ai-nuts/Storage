# Key Result

Core claim: The masked-validation-drop search reliably identifies the best homogeneous attention for text classification and ListOps, but every heterogeneous Transformer (NAS Prune and NAS One-shot) fails to beat the best homogeneous model on all three tasks.

Supporting detail: On ListOps the search is decisive — Reformer, the best model (37.8% accuracy), receives a masked-validation-drop score of 11.85 versus under 0.5 for every other mechanism. On document matching (lower-magnitude scores) the single layer fails to place a true top-3 attention in its top-3 picks.

Narration: The headline finding splits in two. On the positive side, the masked-validation-drop search is genuinely effective at homogeneous selection: it correctly identifies the best attention for text classification and for ListOps, where Reformer stands out with a drop score of nearly twelve while every other attention scores below half a point. On the negative side, when the authors assemble heterogeneous Transformers that mix several attention types, none of them beats the best single-attention model on any of the three tasks. Mixing attention helps you beat the average choice, but not the best one.
