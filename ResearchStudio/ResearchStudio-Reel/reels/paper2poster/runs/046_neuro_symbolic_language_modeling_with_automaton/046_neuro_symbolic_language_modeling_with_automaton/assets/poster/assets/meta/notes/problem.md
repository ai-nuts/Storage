# Problem

Core claim: Retrieval-based language models improve quality by searching an external datastore, but that nearest-neighbor search runs as often as every time step and is the dominant computational bottleneck at inference.

Supporting detail: The search is far slower than the LM's forward pass, which blocks retrieval LMs from practical deployment despite their accuracy, domain-adaptability, and provenance benefits.

Narration: Retrieval-based language models improve on standard neural models by fetching nearest-neighbor examples from an external datastore and blending them into the prediction. The catch is cost: that datastore search can fire at every single time step, and it is far slower than the model's own forward pass. This frequent search is the single most critical bottleneck that keeps these otherwise powerful models out of practical settings.
