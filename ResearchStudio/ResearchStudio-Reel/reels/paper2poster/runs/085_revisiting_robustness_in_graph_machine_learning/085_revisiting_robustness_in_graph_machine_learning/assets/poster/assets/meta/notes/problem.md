# Problem

Core claim: It is unclear whether the small, low-budget structure perturbations used to attack graph neural networks actually preserve a node's semantic content, the core assumption behind any adversarial example.

Supporting detail: Graphs cannot be manually inspected like images, so the de facto ℓ₀-pseudonorm budgets on inserted/deleted edges may silently change a node's true label rather than leave it intact.

Narration: An adversarial example is supposed to be a small change that does not alter the true category of the input. For images a human can verify this by looking. For graphs there is no such visual check, so the community settled on counting edited edges with an ℓ-zero budget. But real graphs are dominated by low-degree nodes, and for those nodes even a tiny edge budget can completely rewire the neighbourhood. That raises a fundamental and previously unanswered question: do these standard perturbations really keep a node's semantic content unchanged, or are we attacking nodes whose true label has already flipped?
