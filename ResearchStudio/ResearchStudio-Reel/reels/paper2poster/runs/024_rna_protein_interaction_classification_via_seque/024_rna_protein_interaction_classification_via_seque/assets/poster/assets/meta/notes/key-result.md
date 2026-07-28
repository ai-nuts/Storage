# Key Result

Core claim: On the homology-separated TSfam test set RPIembeddor clearly outperforms prior methods, reaching F1 0.586 (±0.010) and accuracy 0.667 (±0.009) with ROC AUC 0.70 (±0.01), versus AUC 0.48 for XRPI and 0.50 for IPMiner — the competitors perform at or below chance.

Supporting detail: RPIembeddor correctly classifies 2,971 of 4,887 positive and 5,586 of 8,116 negative TSfam interactions, while XRPI collapses to predicting ~91% of pairs as positive despite ~62% being negative.

Narration: On the hardest test, TSfam, where no RNA family overlaps with training, RPIembeddor reaches an F1 score of about zero-point-five-nine and an accuracy of about zero-point-six-seven. Its ROC area under the curve is zero-point-seven-zero, while the competing tools XRPI and IPMiner sit at zero-point-four-eight and zero-point-five-zero, essentially chance. In concrete terms, RPIembeddor correctly labels nearly three thousand of the positive interactions and over five thousand of the negatives, whereas XRPI simply predicts almost everything as interacting. The model clearly learns real signal that generalizes to unseen RNA families.
