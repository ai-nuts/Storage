# Ablation Study

Core claim: As a baseline comparison, inference is repeated with a standard Gaussian likelihood using a Welch PSD; on a glitch-free segment both methods recover the true values, but SLIC yields a tighter posterior.

Supporting detail: This head-to-head against the conventional Gaussian likelihood isolates the effect of the learned non-Gaussian noise model on posterior width and bias.

Narration: The key comparison is against the conventional approach. For the injected signal they run inference twice: once with the learned SLIC likelihood, and once with a standard Gaussian likelihood from a Welch spectrum. They pick a glitch-free segment, so both recover the true parameters, but SLIC's posterior comes out tighter, hinting at gains on noisy, glitch-contaminated data.
