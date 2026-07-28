# Ablation Study

Core claim: Ablating the max-epoch parameter N∈{1,5,10} on Large models gives TyDi QA of 82.2 (N=1), 81.5 (N=5), 81.8 (N=10) — best when disallowing repeats entirely, though the effect is small. At a 4× larger (1/2) budget, UniMax scores 83.1 vs 82.8 (τ=3.33) and 81.2 (τ=1).

Supporting detail: Loss curves show overfitting under high temperature grows more severe with model size, while UniMax stays stable; the optimal N depends on the character budget.

Narration: What about that max-epoch parameter, N? Ablating N over one, five, and ten on Large models gives TyDi QA scores of eighty-two point two, eighty-one point five, and eighty-one point eight. Disallowing repeats entirely, N equals one, comes out best, though the effect is small. At a four-times-larger budget, UniMax scores eighty-three point one, versus eighty-two point eight for temperature and eighty-one point two for tau equals one. The loss curves tell the story: high-temperature overfitting grows more severe with scale, while UniMax stays stable.
