# Motivation

Core claim: Models trained on surrogate objectives (next-token prediction, single-step imitation) ignore the feedback loops of the real task, so surrogate loss improving monotonically hides large swings in the metric that actually matters.

Supporting detail: Prior imitation-learning work attributes the loss-vs-reward gap to error amplification, but the role of optimizer noise as the driver of iterate-to-iterate instability had not been isolated.

Narration: Modern deep learning is full of feedback loops. A language model's next token depends on the tokens it already generated. A robot's next observation depends on the action it just took. But when we train these systems, we almost always optimize a surrogate objective, like next-token prediction, that pretends the feedback loop is not there. That surrogate tends to improve smoothly, which lulls us into thinking training is well behaved. The authors argue this is a dangerous illusion, and that the real culprit behind the instability is not the data or the model, but the noise in the optimizer itself.
