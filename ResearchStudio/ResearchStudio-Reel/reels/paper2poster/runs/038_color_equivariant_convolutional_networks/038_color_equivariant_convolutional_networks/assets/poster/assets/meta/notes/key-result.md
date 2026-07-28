# Key Result

Core claim: On the hue-shifted test sets CE-ResNets are far more robust than vanilla ResNets while matching them on the original data; e.g. on Flowers-102 average hue-shift accuracy rises from 13.41% (baseline) to 33.33% (CEConv), and on CIFAR-100 from 47.01% to 62.11% (CEConv-2).

Supporting detail: In the long-tailed ColorMNIST toy setting CECNN reaches 91.35±0.40% versus 71.59±0.61% for the vanilla CNN, with the largest gains on the rarest classes; on Flowers-102 the CE-CNN accuracy peaks at -120°, 0°, and 120° hue shifts.

Narration: The headline finding is robustness without a cost to clean accuracy. On the original, unshifted test sets, color equivariant ResNets perform on par with vanilla ResNets. But when the test images are hue-shifted, the gap opens dramatically. On Flowers-102, average accuracy across hue shifts jumps from about thirteen percent for the baseline to thirty-three percent for the fully equivariant model, and similar gains appear on CIFAR-100 and Stanford Cars. In the controlled long-tailed experiment the equivariant network reaches ninety-one percent against the baseline's seventy-two percent, with the biggest improvements exactly on the rare classes that shape sharing is meant to help.
