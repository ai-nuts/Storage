# Key Result

Core claim: On the single-cell drug-response task NubOT outperforms all baselines (CellOT, the state-of-the-art ubOT GAN, Identity, Observed) in almost all drug perturbations under weighted kernel MMD, while accurately recovering per-subpopulation mass changes that the ubOT GAN only captures as a coarse trend.

Supporting detail: On synthetic data NubOT maps clusters without transporting mass across non-corresponding clusters and predicts the correct per-cluster weights, whereas ubOT GAN gets locations right but misestimates the reweighting.

Narration: Across the real single-cell task, NubOT outperforms every baseline, including the current state-of-the-art unbalanced GAN, in almost all of the twenty-five drug perturbations, measured by a weighted version of kernel maximum mean discrepancy between predicted and observed perturbed cells. Just as importantly, it does so while getting the mass changes right: on the synthetic benchmark it maps each cluster to its correct target without leaking mass between clusters, and it predicts the exact reweighting each cluster needs, where the GAN baseline only captures the broad direction of growth and shrinkage. This combination of accurate feature mapping and accurate mass rescaling is what sets NubOT apart.
