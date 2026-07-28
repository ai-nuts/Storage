# Problem

Core claim: Multilingual pretraining faces severe data imbalance: in mC4, English has ~9.7 trillion characters, over 92,000× the lowest-resource language, Yoruba. How to balance the languages is an open, expensive question.

Supporting detail: The dominant fix, temperature sampling with hyperparameter τ, has never been systematically evaluated across model scales.

Narration: So why does language sampling matter so much? Massively multilingual corpora are wildly imbalanced. In the mC4 dataset, English alone has about nine point seven trillion characters, more than ninety-two thousand times the data available for the lowest-resource language, Yoruba. If you train in proportion to the raw data, the tail languages barely register at all. Deciding how to balance them is an open and expensive question, and the field's default answer, temperature-based sampling, had never actually been evaluated systematically across model scales.
