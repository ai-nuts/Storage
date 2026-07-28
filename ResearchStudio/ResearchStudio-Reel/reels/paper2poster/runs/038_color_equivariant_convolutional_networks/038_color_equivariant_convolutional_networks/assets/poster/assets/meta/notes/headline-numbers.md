# Headline Numbers

Core claim: - Flowers-102 hue-shifted accuracy: 13.41% (baseline) -> 33.33% (CEConv), roughly 2.5x. - Long-tailed ColorMNIST: 91.35±0.40% (CECNN) vs 71.59±0.61% (CNN), +19.76 points. - CIFAR-100 hue-shifted accuracy: 47.01% (baseline) -> 62.11% (CEConv-2), +15.1 points. - Stanford Cars hue-shifted accuracy: 55.59% (baseline) -> 68.17% (CEConv-2), +12.6 points.

Supporting detail: Compute overhead is modest: MACs increase by only |Hn|/k² + |Hn| and parameters by |Hn|/k² + 1 thanks to the spatial/pointwise filter decomposition.

Narration: A few numbers capture the impact. On Flowers-102 under hue shifts, accuracy nearly triples, from thirteen to thirty-three percent. On the long-tailed color experiment the equivariant network gains almost twenty points over the baseline. CIFAR-100 improves by fifteen points and Stanford Cars by roughly thirteen points on hue-shifted tests. And all of this comes at a modest compute overhead, since the filter decomposition keeps the increase in operations and parameters to a small factor of the number of hue rotations.
