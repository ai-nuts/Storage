# Key Result

Core claim: BADGE is the only acquisition function that clearly beats random selection and even exceeds full-training performance, reaching the ceiling with far fewer labels; MNLP only slightly edges Rand after about 500 labels.

Supporting detail: MNLP+ (forced maximum table diversity) is by far the worst, showing that over-enforcing table diversity is detrimental; MNLP also shows higher variance, indicating greater sensitivity to the initial seed in this high-imbalance regime.

Narration: Performance is micro-averaged F1 on the held-out test set across active learning iterations. BADGE is the standout: it beats random selection and even surpasses the ceiling from training on the full dataset, using far fewer labels. Pure uncertainty sampling with MNLP disappoints, edging past random only after around 500 labels, and with high variance. Most striking, MNLP-plus, which forces maximum table diversity, is the worst of all.
