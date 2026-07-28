# Dataset / Benchmark

Core claim: Evaluated on three table QA benchmarks: WikiTableQuestions (WikiTQ) and WikiSQL, scored by exact-match accuracy, and FeTaQA, scored by Sacre-BLEU for long free-form answers.

Supporting detail: WikiTQ is among the most complex table QA datasets requiring compositional reasoning; the authors also release a dataset of ~300 manually written parsing statements to bootstrap the weakly-supervised module.

Narration: CABINET is evaluated on three challenging table question-answering benchmarks. WikiTableQuestions, or WikiTQ, requires compositional reasoning over tables and uses short one-to-two-word answers scored by exact-match accuracy. WikiSQL similarly uses exact-match accuracy. FeTaQA asks for long, free-form descriptive answers, which are scored with Sacre-BLEU. The authors additionally release a small dataset of about three hundred manually written parsing statements used to bootstrap the weakly-supervised cell-highlighting module.
