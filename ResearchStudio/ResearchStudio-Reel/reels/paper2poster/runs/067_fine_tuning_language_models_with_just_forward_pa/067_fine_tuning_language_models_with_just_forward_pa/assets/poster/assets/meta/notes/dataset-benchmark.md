# Dataset / Benchmark

Core claim: Experiments span RoBERTa-large on sentence classification (SST-2, SST-5, SNLI, MNLI, RTE, TREC) in few-shot (k=16) and many-shot (k=512) settings, and OPT models from 1.3B to 66B on SuperGLUE tasks plus multiple-choice (COPA, ReCoRD) and generation (SQuAD, DROP).

Supporting detail: Comparisons include zero-shot, in-context learning, linear probing, and full Adam fine-tuning, each evaluated with the paper's task prompts.

Narration: The evaluation is deliberately broad. On the masked-language-model side, it uses RoBERTa-large on six sentence-classification and inference tasks, tested in both a few-shot regime with sixteen examples per class and a many-shot regime with five hundred and twelve. On the autoregressive side, it uses OPT models ranging from one-point-three billion up to sixty-six billion parameters, evaluated on SuperGLUE classification tasks, multiple-choice tasks like COPA and ReCoRD, and generation tasks including SQuAD and DROP. Baselines include zero-shot prediction, in-context learning, linear probing, and standard Adam fine-tuning.
