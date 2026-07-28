# Problem

Core claim: As language models grow, fine-tuning with backpropagation needs prohibitively large memory to store activations, gradients, and optimizer states, up to 12x the memory required for inference.

Supporting detail: On a single 80GB A100, inference runs a 30B model, but Adam fine-tuning fits only a 2.7B model, a roughly 11x gap in trainable model size.

Narration: Fine-tuning has driven much of the recent success of language models, but it comes at a steep memory cost. Backpropagation must cache intermediate activations and store gradients and optimizer states, which together can require up to twelve times the memory of plain inference. As models scale into the tens of billions of parameters, this becomes the binding constraint. Concretely, a single eighty-gigabyte A100 GPU can run inference on a thirty-billion-parameter model, yet standard Adam fine-tuning on the same hardware is limited to only a two-point-seven-billion-parameter model.
