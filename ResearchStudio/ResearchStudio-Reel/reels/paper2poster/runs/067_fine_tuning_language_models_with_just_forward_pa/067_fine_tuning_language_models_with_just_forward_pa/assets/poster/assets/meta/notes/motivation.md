# Motivation

Core claim: Zeroth-order methods can estimate gradients from just two forward passes, but classical theory predicts their convergence slows in proportion to the number of parameters, making them seem hopeless for billion-parameter models.

Supporting detail: In-context learning and linear probing avoid full fine-tuning but leave accuracy on the table; a truly memory-light optimizer that still matches fine-tuning was missing.

Narration: Zeroth-order optimization offers a tempting escape: it can estimate a gradient using only two forward passes, requiring no backpropagation at all. The catch is that classical analyses suggest zeroth-order methods converge catastrophically slowly for large models, with the rate degrading in proportion to the number of parameters. That pessimism, combined with a naive implementation that still doubles memory, is why zeroth-order methods have been overlooked for modern language models. This paper asks whether that pessimism actually holds when fine-tuning pre-trained models on downstream tasks.
