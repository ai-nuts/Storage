# Contribution

Core claim: A preregistered, mixed-methods study with 30 participants comparing three code-completion conditions (no highlights, generation-probability highlights, and edit-model highlights), plus a new "edit model" that predicts which tokens a user is likely to edit.

Supporting detail: The work shows edit-likelihood is a stronger highlighting signal than raw generation probability and argues the approach can generalize by learning from large-scale telemetry such as Copilot edit data.

Narration: The authors ran a preregistered, mixed-methods study with thirty programmers, comparing three ways of presenting the same AI code completions: no highlights at all, highlights based on generation probability, and highlights based on a new edit model. The edit model is the key idea: instead of asking how confident the model was, it predicts which tokens a human is actually likely to change. This reframes the whole problem, from surfacing model uncertainty to surfacing human intervention, and the authors argue the same recipe could scale up by learning from edit telemetry that products already collect.
