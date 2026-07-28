# Ablation Study

Core claim: Oscillations persist across dataset sizes, architectures (4-layer MLP and 4-layer Transformer), model scales, and regularizers, and are only strongly mitigated by variance-reduction strategies. EMA ablations show it should update every iterate with a burn-in and a tuned decay; skipping burn-in or updating infrequently degrades stabilization.

Supporting detail: Aggressive LR decay and large-batch gradient accumulation also reduce GVA but at large compute cost; shallower models are less susceptible. Some tasks (e.g. higher-dimensional Humanoid-v4) show more benign oscillations.

Narration: The ablations are what make the diagnosis convincing. The oscillations refuse to go away as you vary dataset size, swap a multilayer perceptron for a Transformer, scale the model, or add regularizers. Only genuine variance reduction consistently calms them, which is exactly what you would predict if gradient noise is the cause. On the fix side, the moving average works best when you update it every single step, use an initial burn-in period, and anneal the averaging rate with a polynomial decay. Skip the burn-in, or update the average only occasionally, and its stabilizing power degrades. Learning rate decay and giant batches also work, but they cost far more compute for the same benefit.
