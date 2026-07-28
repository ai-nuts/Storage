# Key Result

Core claim: LLMs show divergent behavior. On separable composite tasks they compose well and improve with scale, approaching the composite in-context gold standard. On compose-by-step tasks they largely fail: Llama models solve each simple task at ~90% accuracy but drop to ~20% or below on the composite, and scaling up does not help.

Supporting detail: Supplying composite in-context examples restores near-simple-task accuracy, showing the models have the representation power but fail to compose it from simple-task demonstrations alone. The same composition failure appears in GPT-4 and Claude 3.

Narration: A sharp split. On separable composite tasks, models compose well and improve with scale, approaching the gold standard. On compose-by-step tasks they collapse: Llama solves each simple task near ninety percent, but the composite drops below twenty percent, and scaling doesn't help.
