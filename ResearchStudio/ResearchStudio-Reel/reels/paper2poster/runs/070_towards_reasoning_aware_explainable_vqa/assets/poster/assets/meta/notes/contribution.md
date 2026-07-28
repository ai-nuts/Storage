# Contribution

Core claim: The paper presents easy-to-implement explanation-generation modules on top of a SOTA VQA framework that maintain accuracy while producing human-readable explanations, and shows via experiments plus human studies that new metrics are needed to evaluate VQA explanations.

Supporting detail: It compares LSTM and Transformer-decoder explanation generators and demonstrates concrete failure cases of string-matching metrics.

Narration: The contribution is two-fold. First, the authors present simple, easy-to-implement methods that sit on top of a state-of-the-art VQA framework and maintain VQA accuracy while generating human-readable textual explanations. Second, they provide both quantitative experimental results and a large human study of the proposed explainable VQA method. Together these illustrate the urgency of proposing new metrics to evaluate predicted explanations in vision-language reasoning problems like VQA, since the metrics in common use today do not reliably reflect explanation quality.
