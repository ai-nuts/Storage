# Key Result

Core claim: InfinityGAN surpasses the strongest baseline beyond 4× extension, reaching 61.41 ScaleInv FID at 4× versus 79.83 for StyleGAN2+NCI and 121.18 versus 189.65 at 8×, while maintaining constant O(1) memory as image size grows.

Supporting detail: A user study with 50 participants shows over 90% preference for InfinityGAN over every baseline; StyleGAN2 runs out of memory at the 16× setting whereas InfinityGAN composes a 1024×1024 image from 121 seamless independently-synthesized patches.

Narration: On the Flickr-Landscape benchmark, InfinityGAN holds a steady quality slope as output grows, while baselines drift far from realistic structure. Beyond four-times extension it beats the strongest baseline, scoring a scale-invariant FID of sixty-one point four at four-times versus seventy-nine point eight for StyleGAN2, and one twenty-one versus one eighty-nine at eight-times. Its memory stays constant, while StyleGAN2 runs out of memory at sixteen-times. And over ninety percent preferred it over every method.
