# Key Result

Core claim: Rollout reward oscillates dramatically across consecutive gradient iterates while BC loss is flat, revealing a fractal reward landscape invisible to the single-step objective; taking an EMA of iterates drastically damps these oscillations across architectures, dataset sizes, and tasks with no learning-rate or batch-size change.

Supporting detail: The same "butterfly effect" appears in autoregressive language generation — nearby training iterates bifurcate in generated text — and EMA yields the lowest-perplexity model while enabling training without LR decay.

Narration: The headline finding is striking. Plotting rollout reward against training step reveals dramatic swings between consecutive iterates, and zooming in shows a jagged, almost fractal reward landscape, all while the behavior cloning loss sits flat and smooth. That jaggedness is completely invisible in the one-step objective. Now apply the exponential moving average, and those oscillations are dramatically damped, across architectures, dataset sizes, and multiple tasks, with no change to the learning rate schedule or batch size. And the same butterfly effect shows up in language generation, where two nearly identical training checkpoints produce stories that diverge into totally different plots. Here too the moving average tames the instability and even yields the lowest-perplexity model.
