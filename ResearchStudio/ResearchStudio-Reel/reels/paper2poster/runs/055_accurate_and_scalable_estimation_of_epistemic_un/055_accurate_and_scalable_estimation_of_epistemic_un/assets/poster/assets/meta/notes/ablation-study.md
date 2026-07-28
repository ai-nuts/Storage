# Ablation Study

Core claim: The choice of anchoring layer matters: on the severe D&D size shift, anchoring after the READOUT layer (last layer) dramatically improves both accuracy and calibration as depth increases, whereas earlier-layer anchoring converges worse; last-layer anchoring is recommended for size shifts.

Supporting detail: Partial stochasticity (the pretrained, classifier-head-only variant) is shown to be both effective and scalable, and NTK analysis confirms that constant shifts at intermediate layers genuinely change the GNN's function.

Narration: The paper carefully ablates where stochastic anchoring should be applied. On the D and D dataset, which has the most severe size shift, applying anchoring after the readout layer dramatically improves both accuracy and calibration as network depth grows, while earlier-layer anchoring converges less well. This leads to a practical recommendation to anchor at the last layer for size-shift settings. The authors also validate that partial stochasticity, in the form of the pretrained variant that only trains an anchored classifier head, is both effective and scalable, and a neural tangent kernel analysis confirms that intermediate constant shifts truly alter the model's function rather than acting as a trivial reparameterization.
