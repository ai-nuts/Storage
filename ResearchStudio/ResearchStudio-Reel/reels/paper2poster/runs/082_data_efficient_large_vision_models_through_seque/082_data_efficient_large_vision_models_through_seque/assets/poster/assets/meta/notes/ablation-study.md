# Ablation Study

Core claim: Prompt background color strongly shapes outputs (black-background prompts ease post-processing); without data shuffling the model catastrophically forgets, performing well only on its most recently trained task; and distillation helps even at 80M parameters.

Supporting detail: Table 5 shows continual (unshuffled) training drives perplexity on earlier tasks to 1000+, confirming catastrophic forgetting; Table 6 shows the LLaMA-80M student improves on all three tasks with KD.

Narration: Several ablations sharpen the picture. Changing the prompt background color changes the generated background, and using black-background prompts makes a simple grayscale-threshold post-processing step reliable. Training without shuffling the task data triggers catastrophic forgetting: the model becomes proficient only on its most recently seen task, with perplexity on earlier tasks exploding into the thousands, underscoring that shuffling is essential for multi-task LVMs. Finally, even at just eighty million parameters, knowledge distillation still improves validation perplexity across segmentation, pose estimation, and deraining.
