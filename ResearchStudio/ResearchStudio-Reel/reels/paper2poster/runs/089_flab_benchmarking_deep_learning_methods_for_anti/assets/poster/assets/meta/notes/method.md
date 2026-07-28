# Method

Core claim: Each antibody variable-region sequence (or structure) is scored by a model's (pseudo-)perplexity, averaged over all heavy- and light-chain residues; a well-calibrated model should assign low perplexity (high confidence) to high-fitness antibodies. These likelihoods are then correlated against experimentally measured fitness using Pearson (r), Spearman (ρ), and Kendall tau (τ) coefficients.

Supporting detail: Six pretrained models are tested with no fine-tuning: decoder-only (ProGen2 suite, IgLM, ProtGPT2), encoder-only (AntiBERTy), and inverse-folding (ESM-IF, ProteinMPNN), all compared to physics-based Rosetta energy.

Narration: The core idea is simple. Every antibody sequence, or its structure, is fed to a model, and the model reports a perplexity score averaged over all residues in the heavy and light chains. Perplexity measures how surprised the model is by the sequence, so a well-behaved model should be confident, meaning low perplexity, about high-fitness antibodies. The authors then correlate these scores against real experimental fitness using three coefficients: Pearson for linear trends, Spearman for monotonic trends, and Kendall tau for ordinal agreement. Crucially, the models are used exactly as released, with no additional fine-tuning, across decoder-only, encoder-only, and inverse-folding architectures.
