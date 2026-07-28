# Key Result

Core claim: With the same model size, NPC²s achieve higher log-likelihoods than monotonic PCs across the density-estimation tasks, and negative parameters (not just squaring) are what capture complex "holes" in the target densities.

Supporting detail: On GPT2 distillation, NPC²s scale better than monotonic PCs and reach log-likelihoods closer to GPT2's own, better approximating the intractable model.

Narration: The headline finding is consistent: at the same model size, squared non-monotonic circuits reach higher log-likelihoods than monotonic circuits across the density-estimation tasks. On the two-dimensional ring distributions, plain squaring already helps, but it is the negative parameters that let the model actually carve out the holes in the density. And on the GPT2 distillation task, the squared circuits scale better and get closer to GPT2's own likelihood, approximating the intractable model more faithfully than monotonic circuits do.
