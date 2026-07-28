# Takeaway

Core claim: You can bolt a simple explanation generator onto a strong VQA model and get human-readable explanations for free, but today's string-matching metrics can't tell good explanations from bad ones, so better evaluation metrics are the real bottleneck.

Supporting detail: Concrete examples show BLEU/ROUGE rewarding wrong explanations and penalizing valid ones, reinforcing the call for human-grounded or reasoning-aware metrics.

Narration: The lasting message is twofold. Practically, explanation generation can be added to a state-of-the-art VQA backbone with almost no loss in answer accuracy, giving users a human-readable reason alongside each answer. But methodologically, the paper shows through concrete examples that string-matching metrics like BLEU and ROUGE can reward a wrong explanation and penalize a valid one, so they are unreliable for this task. The authors therefore argue that the real bottleneck for explainable VQA is not the generator but the evaluation, and they urge the community to develop proper reasoning-aware metrics for judging explanations.
