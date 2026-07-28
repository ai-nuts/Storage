# Dataset / Benchmark

Core claim: Probes are trained and evaluated on hidden-state activations from four models — UnifiedQA T5-Large (encoder and decoder), DeBERTa, and GPT-Neo — averaged over five datasets (including BoolQ), following the CCS contrast-pair setup.

Supporting detail: Contrast pairs are formed by appending mutually exclusive answers to a question; the two answer sets are independently normalized so the probe cannot simply detect the answer token.

Narration: Experiments use hidden-state activations from four models: the encoder and decoder of UnifiedQA T5-Large, DeBERTa, and GPT-Neo, averaged over five datasets including BoolQ. Contrast pairs append two exclusive answers, each set normalized independently so the probe cannot detect the answer token.
