# Takeaway

Core claim: Unlabeled industrial test images can score each other to detect anomalies, so MuSc achieves state-of-the-art zero-shot classification and segmentation with no training, no prompts, and no reference images.

Supporting detail: Because normal patches recur across images while abnormal ones do not, mutual scoring turns a batch of unlabeled test images into its own supervision signal.

Narration: The lasting idea: a set of unlabeled test images can supervise itself. By letting images score one another, repeating normal structure is separated from rare defects, with no training or prompts, giving state-of-the-art zero-shot detection that rivals full-shot methods.
