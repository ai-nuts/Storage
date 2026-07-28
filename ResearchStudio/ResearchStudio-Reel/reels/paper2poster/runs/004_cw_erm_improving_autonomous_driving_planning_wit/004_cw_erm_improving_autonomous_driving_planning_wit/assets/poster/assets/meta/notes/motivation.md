# Motivation

Core claim: Existing closed-loop training remedies, such as backpropagation-through-time in a differentiable simulator, are expensive, need differentiable metrics, and scale poorly; a simple, metric-agnostic alternative is missing.

Supporting detail: Collecting on-policy data or adding human oracles is costly, and prior debiasing methods like LfF and JTT target classifier group robustness rather than closed-loop driving behavior.

Narration: "There have been attempts to close this gap. Methods like Urban Driver run a differentiable simulator directly inside the training loop using backpropagation through time. This works, but it is expensive: it requires a differentiable simulator, it does not scale well, and it carries the heavy memory cost of unrolling policies during training. Other approaches collect on-policy data or add extra human oracles, which are slow and costly. The authors ask a simpler question: can we get closed-loop benefits by only using a simulator to decide which training scenes matter, without changing the loss function or requiring differentiability? That question motivates CW-ERM."
