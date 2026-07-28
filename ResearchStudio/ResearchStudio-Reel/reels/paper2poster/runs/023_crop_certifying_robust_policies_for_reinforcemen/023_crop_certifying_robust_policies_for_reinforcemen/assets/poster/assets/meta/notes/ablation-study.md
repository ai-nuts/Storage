# Ablation Study

Core claim: Varying the smoothing parameter σ shows a trade-off: on Freeway larger σ (up to 1.0) steadily raises certified robustness for SA-MDP and RadialRL, while on Pong a moderate σ around 0.01 to 0.03 is best for almost all methods.

Supporting detail: Among the reward bounds, the percentile bound Jp is much tighter than the loose expectation bound JE, and the absolute lower bound J shows a zero gap to empirical PGD results over a wide range of attack magnitudes.

Narration: A central ablation studies the smoothing variance sigma. On Freeway, robustness for the strong methods keeps improving as sigma grows all the way to one point zero, since Freeway tolerates large noise. On Pong the story differs: too much smoothing hurts, and a moderate sigma between about zero point zero one and zero point zero three works best for nearly all methods. The authors also compare their three reward bounds. The percentile bound is far tighter than the loose expectation bound, and the absolute lower bound from CROP-LoRe often matches the empirical reward under PGD attack exactly, a zero gap that demonstrates the certificates are tight rather than merely valid.
