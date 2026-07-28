# Problem

Core claim: Deep generative models memorize and reproduce training datapoints, creating privacy and copyright risks, yet the field lacks a unified, formal language to define and reason about "how memorized" a sample is.

Supporting detail: Prior definitions rely on pixel-space distance to a specific training point, which cannot capture reconstructive memorization (copied layout/style, not the whole image) and does not scale to LAION-2B / Stable Diffusion.

Narration: Generative models, and diffusion models in particular, are increasingly deployed in public-facing applications, but with enough capacity they memorize training data. That memorization can expose private information and reproduce copyrighted works, exposing model builders to legal liability. The trouble is that the community has lacked a single formal framework to say precisely how memorized a datapoint is. Past definitions lean on distance to a nearest training image in pixel space, which fails to capture subtler forms of memorization and cannot be computed at the scale of models like Stable Diffusion.
