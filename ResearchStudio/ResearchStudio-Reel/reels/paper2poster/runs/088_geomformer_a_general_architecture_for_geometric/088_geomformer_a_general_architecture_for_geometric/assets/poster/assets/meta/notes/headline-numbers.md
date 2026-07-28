# Headline Numbers

Core claim: - PCQM4Mv2 Valid MAE 0.0734, the best among O(n²) models (6.7% relative reduction). - N-body simulation MSE 0.0047, a 33.8% reduction versus the previous best. - Molecule3D MAE 0.0252 (random) / 0.1045 (scaffold): 16.3% / 11.6% relative reductions.

Supporting detail: - OC20 IS2RE energy MAE 0.4141 eV average and EwT 8.59%, outperforming Graphormer-3D. - Cross-attention ablation: up to 60.8% relative improvement on MD17 force prediction.

Narration: A few numbers capture the impact. On PCQM4Mv2, GeoMFormer reaches a validation error of zero point zero seven three four, the best of any quadratic-complexity model, a six point seven percent relative reduction. On the N-body simulation it achieves a mean squared error of zero point zero zero four seven, a thirty-three point eight percent reduction over the previous best. On Molecule3D it records errors of zero point zero two five two on the random split and zero point one zero four five on the scaffold split, improvements of sixteen point three and eleven point six percent. And in the ablations, adding cross-attention yields up to a sixty point eight percent relative improvement on force prediction, underscoring how central that bridge is.
