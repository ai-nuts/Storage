# Ablation Study

Core claim: Removing any component hurts accuracy. Dropping informative selection costs up to −3.2% (PubMed), informative training up to −2.9%, information quantity up to −2.1%, and normalized label up to −2.4%.

Supporting detail: Informative selection is the single most important component (−2.5% on Cora vs smaller gaps for others), confirming that propagation-aware selection, not just soft-label training, drives the gains.

Narration: An ablation disables one component at a time. Removing informative selection, the propagation-aware node choice, causes the largest drop, up to 3.2 percent on PubMed, making it the most important ingredient. Removing informative training with soft labels costs up to 2.9 percent, dropping the influence-magnitude information quantity up to 2.1, and removing the normalized label up to 2.4. Every piece contributes.
