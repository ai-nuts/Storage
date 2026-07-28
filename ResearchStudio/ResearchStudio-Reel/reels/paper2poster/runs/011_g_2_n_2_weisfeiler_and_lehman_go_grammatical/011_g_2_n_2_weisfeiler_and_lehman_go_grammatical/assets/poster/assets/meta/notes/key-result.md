# Key Result

Core claim: On QM9 regression G2N2 obtains the best MAE on every target while training faster than PPGN; on the hardest R² target it cuts MAE from PPGN's 3.78 to 0.342 (single-target) and 16.07 to 1.19 (all-targets-at-once).

Supporting detail: On TUD it ranks better than 2nd on five of six datasets (e.g. MUTAG 92.5%, PTC 72.3%, Proteins 80.1%), and on spectral filtering it learns band-pass filters (R² 0.8206) where PPGN collapses (0.1041).

Narration: The headline result is that G2N2 does not just match the theory, it dominates in practice. On QM9, learning targets one at a time, it posts the best error on every single target while training faster than PPGN. On the notoriously hard R-squared target, its error drops to zero-point-three-four-two, where PPGN sits at three-point-seven-eight, more than a ten-fold improvement, and when all twelve targets are learned at once the gap widens further. On graph classification it beats the second-best network on five of the six TUD datasets. And on the spectral test it cleanly learns band-pass filters where PPGN, starved of the memory it would need, essentially fails.
