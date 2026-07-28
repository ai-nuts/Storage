# Motivation

Core claim: As reasoning demands in VQA grow, interpretability becomes urgent for diagnosing and trusting models, yet explanation quality has no reliable evaluation metric.

Supporting detail: Prior explainable-VQA work either reuses image captions as weak explanations or relies on external knowledge that gives no direct evidence for the answer.

Narration: Two open questions drive the paper. First, can a VQA model generate a human-readable explanation while still maintaining its answer accuracy? Second, how good are those generated explanations, and how should we even evaluate them? Existing explainable-VQA datasets suggest using conventional natural language metrics such as BLEU and ROUGE, but these were designed for string matching over overlapping n-grams, not for judging whether an explanation truly supports an answer. The authors argue that as reasoning problems in VQA grow more complex, having an interpretable, well-evaluated explanation is no longer optional but urgent.
