# Problem

Core claim: Reinforcement learning agents are sample-inefficient. Prior methods that inject external knowledge policies cannot freely combine, rearrange, or replace those policies, blocking generalization and transfer.

Supporting detail: Human learning is knowledge-acquirable, sample-efficient, generalizable, compositional, and incremental; RL agents lack the flexibility to reuse and update a knowledge set on the fly.

Narration: Reinforcement learning has succeeded across physics and robotics, yet agents still need enormous numbers of samples to solve tasks that humans master quickly. Part of the gap is that humans learn by observing others and freely reuse, combine, and swap the strategies they already know. Earlier reinforcement learning methods did incorporate external knowledge policies to improve efficiency, but they made it hard to perform arbitrary combinations and replacements of those policies. That rigidity is exactly the property this paper set out to fix.
