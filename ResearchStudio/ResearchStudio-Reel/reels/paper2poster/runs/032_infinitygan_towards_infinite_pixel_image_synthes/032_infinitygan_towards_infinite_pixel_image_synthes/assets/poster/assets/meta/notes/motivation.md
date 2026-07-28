# Motivation

Core claim: Large images should be locally and globally consistent, avoid repetitive patterns, and look realistic, yet prior generators rely on zero-padding for positional cues that break down once the output size differs from training.

Supporting detail: Because the image border is effectively infinitely far away when synthesizing infinite-pixel images, padding-based position encoding cannot generalize, producing repetitive textures in image centers.

Narration: Why do existing models fail when asked to grow? The insight: generators like StyleGAN2 secretly rely on zero-padding at the borders to encode position. During training the padding pattern is fixed, so the network memorizes it. But synthesize a larger image, and the feature size changes, the padding-derived position shifts, and the image center no longer gets sensible positional information, producing repetitive, broken content. Truly infinite synthesis needs position valid infinitely far from any border, plus patches that combine seamlessly.
