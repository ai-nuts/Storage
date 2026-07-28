# Problem

Core claim: What fundamentally distinguishes transformers from other neural sequence models is unclear. Prior expressivity results are either about impractically large models or show basic algorithmic tasks are impossible at constant depth.

Supporting detail: Existing fine-grained results fix depth and grow context length, a regime where matching parentheses or evaluating Boolean formulas are provably out of reach, revealing little about what transformers uniquely gain.

Narration: Transformers dominate sequence modeling, yet the theory explaining why has been unsatisfying. One line of work proves universality, but only for enormous models, and that tells us nothing about which tasks are solvable size-efficiently. A second line studies a constant-depth regime where context length grows, and there many basic algorithmic tasks, like matching parentheses, are simply impossible. Neither picture isolates the property that actually sets transformers apart from recurrent networks or other architectures. This paper asks: is there a single, clean computational property that captures the strengths and the limits of transformers at the same time?
