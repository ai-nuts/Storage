# Motivation

Core claim: The two dominant guidance approaches, external classifiers and classifier-free guidance, both ignore the geometry of a continuous condition space, leaving the benefits of continuity unexploited.

Supporting detail: In Stable Diffusion the text encoder induces a rich continuous space; if that space has a "cone" structure, guidance could be extended along it to gain new, valuable information.

Narration: There are two main ways to inject guidance into diffusion models: use an external trained classifier, or use classifier-free guidance that a single model learns jointly. Both work well, but neither says anything about the shape of the condition space. The authors' insight is that a text encoder maps prompts into a continuous space with structure, and if you identify that structure, you can move along it. That motivates inner classifier-free guidance.
