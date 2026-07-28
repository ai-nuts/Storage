# Takeaway

Core claim: There is a large, quantifiable gap between current robust classifiers and the optimal achievable loss in multi-class settings, and edge-only conflict-hypergraph bounds efficiently pin down that optimum in the practical regime.

Supporting detail: The framework gives practitioners a fast diagnostic for how much robustness headroom remains, refocusing effort on closing the gap rather than on the attack-defense arms race.

Narration: The takeaway is that multi-class robust classification has a large and now-measurable gap between what current defenses achieve and what is theoretically possible, a gap that is far worse than in the binary case. The paper's conflict-hypergraph framework computes the optimal 0-1 loss as a linear program, and its efficient truncated bounds pin that optimum down tightly using only edges in the practical low-budget regime. This gives practitioners a fast diagnostic tool to see how much robustness is still on the table, and it points future research toward closing the gap rather than endlessly iterating attacks and defenses.
