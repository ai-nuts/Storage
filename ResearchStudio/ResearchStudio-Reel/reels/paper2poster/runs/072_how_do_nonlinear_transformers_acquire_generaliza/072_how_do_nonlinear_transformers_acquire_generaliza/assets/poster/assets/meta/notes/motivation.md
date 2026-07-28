# Motivation

Core claim: Prior ICL theory simplifies away the hard parts: it either drops nonlinear self-attention or uses a linear MLP, studies only linear regression, and cannot explain training under distribution shift or the effect of pruning.

Supporting detail: As LLMs are increasingly pruned to cut inference cost while preserving ICL, a theoretical account of when pruning is safe for ICL is missing entirely.

Narration: Recent works began to explain in-context learning, but each keeps only part of the picture. Some ignore the nonlinear self-attention, others replace the nonlinear MLP with a linear one, and most study linear regression rather than classification. None can characterize how to train a model that generalizes under a distribution shift between training and test data, and none analyze how pruning a trained model changes its in-context ability. Since practitioners routinely prune large language models to save compute while hoping to keep their in-context skills, closing this theoretical gap matters in practice.
