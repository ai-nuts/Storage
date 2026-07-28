# Ablation Study

Core claim: Three ablations show a) more hue rotations increase test-time hue-shift robustness at a slight capacity cost, b) removing group coset pooling breaks hue invariance, and c) hue-equivariant networks need weaker color-jitter augmentation to match the same robustness and accuracy.

Supporting detail: Hybrid CE-ResNets using CEConvs in only one or two early stages give the best accuracy-robustness trade-off on most datasets, and color equivariance benefits datasets whose neurons are more color-selective (e.g. Flowers-102, color selectivity 0.70).

Narration: The ablations clarify the design choices. Increasing the number of discrete hue rotations makes the network more robust to test-time hue shifts, though it slightly reduces capacity because channels must shrink to keep parameters fixed. Group coset pooling turns out to be the mechanism that yields hue invariance; remove it, and the network behaves like a regular one. Finally, color equivariance and color-jitter augmentation are complementary: an equivariant network needs a lower intensity of augmentation to reach the same robustness. A color-selectivity analysis further explains when the method helps, showing that datasets with more color-selective neurons benefit from equivariance up to later stages.
