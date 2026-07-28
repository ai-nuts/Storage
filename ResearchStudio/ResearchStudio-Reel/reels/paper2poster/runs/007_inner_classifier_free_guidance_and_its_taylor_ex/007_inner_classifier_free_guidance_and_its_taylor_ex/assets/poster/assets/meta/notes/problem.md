# Problem

Core claim: Classifier-free guidance (CFG) balances diversity and fidelity in conditional diffusion models, but it imposes no structure on the condition space, so it underutilizes continuity when the condition is continuous.

Supporting detail: For text-based models like Stable Diffusion, a structured continuous condition space could further improve the fidelity–diversity trade-off, yet CFG cannot exploit it.

Narration: Conditional diffusion models rely on classifier-free guidance to control how diverse and faithful their samples are. The problem is that CFG treats the condition as an opaque label; it places no constraints on the condition space. So when that space is continuous, like a text prompt embedding, all that continuity goes to waste. The authors ask a pointed question: if the condition lives in a structured continuous space, can we do better than plain CFG?
