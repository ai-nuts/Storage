# Ablation Study

Core claim: Ablations show that adding the grounding point φ(gᵢ, gᵢ) as a normalizing constant in ψ's objective improves performance, and that the ℓ₁ metric loss for φ outperforms ℓ₂.

Supporting detail: Varying the latent dimensionality of φ and ψ does not significantly affect downstream control performance on the Drawer task.

Narration: Ablations confirm the design. Adding a grounding term, phi of a goal with itself, as a normalizing constant in psi's objective helps. An L1 metric loss for phi beats L2. And varying the latent dimensionality barely changes control.
