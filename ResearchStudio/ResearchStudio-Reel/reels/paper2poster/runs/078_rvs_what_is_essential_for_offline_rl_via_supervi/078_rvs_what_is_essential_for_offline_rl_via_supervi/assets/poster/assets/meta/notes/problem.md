# Problem

Core claim: Supervised learning can solve offline RL without temporal-difference learning, but it is unclear when this works and which algorithmic components are actually necessary for good performance.

Supporting detail: Prior RvS methods disagree on whether advantage weighting or Transformer sequence models are needed, leaving practitioners without a clear recipe.

Narration: Recent work showed that plain supervised learning, with no temporal-difference bootstrapping at all, can be remarkably effective for offline reinforcement learning. But the picture was muddy. Different papers reached contradictory conclusions about what actually makes these methods work: some emphasized advantage weighting, others reached for large Transformer sequence models. The core question this paper asks is simple, yet still unanswered. When does supervised learning for offline RL actually work, and which of its many algorithmic components are truly essential versus merely incidental complexity that could be stripped away without cost?
