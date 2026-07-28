# Ablation Study

Core claim: Adding label propagation on top of a GNN sharply reduces over-robustness: GCN+LP at K = 0.5 drops to R_over = 20.9%, and label propagation alone achieves the lowest over-robustness of all methods.

Supporting detail: Adding LP does not decrease test accuracy and often increases adversarial robustness while structure matters; under stronger attacks over-robustness persists (Nettack leaves a GCN at K = 0.5 with 11.4% over-robustness, and an MLP under Nettack at K = 2 still shows 19.2%).

Narration: The most informative ablation concerns label propagation. Applying it on top of a graph neural network sharply lowers over-robustness. For instance, a GCN combined with label propagation at K equal to zero-point-five drops its over-robustness to about twenty-one percent, and label propagation on its own achieves the lowest over-robustness of any method. Crucially, this comes for free: adding label propagation does not hurt test accuracy and often improves genuine adversarial robustness while structure still matters. The effect is robust to stronger attacks too, though some over-robustness always remains, such as eleven-point-four percent for a GCN under Nettack and nineteen-point-two percent for an MLP.
