# Ablation Study

Core claim: Varying the Huber parameter κ (Figure 3) shows the H²_κ and H¹_κ losses systematically lower MSE on contaminated Iris versus the plain squared loss; varying the number of components s (Figure 2) shows L-BFGS keeps its time advantage over RSVD until very large s, where the per-iteration s×s SVD begins to bite.

Supporting detail: The eigenspectrum-decay study (Figure 1) isolates why the method scales well: RSVD's required oversamples grow steeply as decay slows, while L-BFGS iterations stay flat.

Narration: Several controlled studies dissect the behavior. Sweeping the Huber loss parameter kappa shows that both Huber variants consistently reduce mean squared error on the contaminated Iris data compared to the ordinary squared loss, confirming the robustness the framework is designed to induce. Varying the number of components shows that the L-BFGS solver keeps its speed advantage over randomized SVD across a wide range, and only at very large numbers of components does the per-iteration small SVD start to slow it down. And the eigenspectrum study pinpoints the scaling advantage: as the spectrum decays more slowly, randomized SVD's oversample count climbs sharply while the proposed solver's iteration count stays essentially flat.
