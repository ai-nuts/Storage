# Ablation Study

Core claim: Varying noise variance (Fig. 3a), DP-CutMixSL gives the best accuracy at almost every level and a tighter RDP bound ε than DP-SL, but a larger ε than DP-MixSL, exposing an accuracy-privacy trade-off; enlarging the mixing group (Fig. 3b) lowers both accuracy and ε for both mixing methods.

Supporting detail: A reconstruction-attack study (Table 2) ranks robustness, measured by reconstruction MSE, as Cutout > patch CutMix > Mixup > raw smashed data, and scalability (Fig. 3c) improves as clients grow from 2 to 10, further boosted by adding SplitFed-style weight averaging (CutMixSFL).

Narration: Ablations probe the privacy-accuracy trade-off. Sweeping noise variance, DP-CutMixSL has the best accuracy at nearly every level and always beats DP-MixSL. Its RDP epsilon is tighter than DP-SL but looser than DP-MixSL, exactly the trade-off theory predicts, since Mixup melts information across the whole representation. Larger mixing groups lower both accuracy and epsilon, a hiding-in-the-crowd effect. A reconstruction attack shows robustness rising from raw data to Mixup, patch CutMix, then Cutout. Finally, accuracy grows as clients scale from two to ten, and SplitFed-style averaging helps further.
