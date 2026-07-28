# Contribution

Core claim: SPEED is a universal sparse parameterization framework for epitomic dataset distillation that introduces Spatial-Agnostic Epitomic Tokens (SAETs), Sparse Coding Matrices (SCMs), and a Feature-Recurrent Network (FReeNet) to remove spatial redundancy within and between synthetic images.

Supporting detail: It is compatible with a wide range of matching objectives (gradient, distribution, trajectory), consistently boosting them, and achieves state-of-the-art distillation, especially on high-resolution ImageNet subsets.

Narration: SPEED makes three main contributions. First, it introduces spatial-agnostic epitomic tokens, a shared dictionary of tokens reused by every synthetic image patch, together with sparse coding matrices that select only the most significant tokens per image. Second, it proposes a feature-recurrent network, a compact transformer-style network that recurrently assembles those tokens into hierarchical, high-resolution synthetic images while reusing the same shared tokens and codes. Third, it shows this parameterization is a drop-in module: it plugs into gradient, distribution, and trajectory matching objectives alike and improves all of them. The framework sets new state-of-the-art results and is especially strong on high-resolution data.
