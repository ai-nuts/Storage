# Problem

Core claim: Recurrent neural networks struggle to learn sequence relationships with long-term memory, but it was unknown whether this is merely an optimization failure or a fundamental limit of the model class.

Supporting detail: Prior approximation guarantees were forward (Jackson-type) and, for the one existing inverse result, restricted to purely linear RNNs and linear targets.

Narration: Recurrent neural networks are among the most basic models for learning from sequential and temporal data, with applications from time series and speech to text and sentiment. But a long-standing empirical observation is that they falter when the data has long-term dependencies. The open question this paper confronts is whether that failure is only about training dynamics, like exploding or vanishing gradients, or whether it reflects a deeper, structural limitation of what RNNs can represent at all. Answering this requires an approximation-theoretic lens rather than an optimization one.
