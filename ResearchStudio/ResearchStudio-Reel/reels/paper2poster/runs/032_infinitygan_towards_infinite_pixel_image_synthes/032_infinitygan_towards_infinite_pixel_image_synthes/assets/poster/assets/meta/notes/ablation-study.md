# Ablation Study

Core claim: Removing all padding from StyleGAN2+NCI to form StyleGAN2+NCI+PFG destroys positional information and collapses structure quality across all FID settings; adding the implicit structure synthesizer G_S restores it by supplying position through z_S.

Supporting detail: This confirms the hypothesis that conventional generators depend on zero-padding for position, and that a coordinate-driven implicit function is a valid, extensible replacement.

Narration: The central ablation isolates where positional information comes from. Starting from StyleGAN2 with non-constant input, the authors strip out all zero-padding, creating a padding-free variant with no positional cues. It fails to generate reasonable structure and degrades sharply across every FID setting, confirming the original generator leaned entirely on padding for position. Add the structure synthesizer back, and position is now supplied through the coordinate-driven structural latent, so quality returns, validating the design.
