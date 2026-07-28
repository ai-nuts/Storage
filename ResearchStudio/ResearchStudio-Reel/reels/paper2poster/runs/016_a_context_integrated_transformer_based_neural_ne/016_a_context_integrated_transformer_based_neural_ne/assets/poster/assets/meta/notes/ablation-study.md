# Ablation Study

Core claim: Swapping CITransNet's transformer interaction layers for RegretNet's fully-connected layers (CIRegretNet) or EquivariantNet's layers (CIEquivariantNet) lowers revenue in every multi-item setting, isolating the transformer as the source of the gain.

Supporting detail: Removing context entirely (RegretNet, EquivariantNet) drops revenue even on single-item settings, and the symmetric EquivariantNet underperforms RegretNet, confirming asymmetric solutions matter in contextual auctions.

Narration: To isolate why it works, the authors replace the transformer layers with RegretNet's fully-connected and EquivariantNet's equivariant layers, giving CIRegretNet and CIEquivariantNet. Both still get context, yet earn less revenue everywhere, pinning the gain on the transformer layers. Removing context hurts even easy settings.
