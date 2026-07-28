# Headline Numbers

Core claim: - Outperforms all baselines in almost all of 25 drug perturbations (weighted kernel MMD). - Predicted-weight vs observed cell-count correlation: R = 0.95 (P = 2.2e-25) at 8h. - Correlation at 24h: R = 0.44 (P = 0.004), still capturing the trend under severe cell death.

Supporting detail: - 2 co-cultured melanoma cell lines (MelA⁺, Sox9⁺); 3 timepoints (0h, 8h, 24h) via 4i imaging. - Baselines compared: CellOT, ubOT GAN (prior SOTA), Identity, Observed.

Narration: The headline numbers tell a clear story. NubOT beats every baseline in almost all of the twenty-five drug perturbations on the distributional fit metric. Its predicted per-subpopulation weights correlate with observed cell counts at a coefficient of point nine five after eight hours, an extremely strong agreement, and still at point four four after twenty-four hours despite drug-induced cell death thinning the observable populations. The evaluation spans two co-cultured melanoma cell lines distinguished by the MelA and Sox9 markers, imaged at three time points with the 4i technology, and compares against four baselines including the prior state-of-the-art unbalanced GAN.
