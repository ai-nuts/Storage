# Dataset and Benchmark

Core claim: Pretraining uses a refreshed mC4 corpus (29 trillion characters, 107 languages). Evaluation spans TyDi QA GoldP, WMT21 multilingual translation, XNLI, XQuAD, MLQA, and PAWS-X.

Supporting detail: Sampling strategies are compared while varying model scale from Small up to XXL, isolating whether benefits persist with size.

Narration: For evaluation, pretraining uses that refreshed mC4 corpus, twenty-nine trillion characters across one hundred seven languages. The trained models are then tested on a broad suite of tasks: TyDi QA GoldP, WMT21 multilingual translation, XNLI, XQuAD, MLQA, and PAWS-X. Crucially, every sampling strategy is compared while sweeping the model scale from Small all the way up to XXL, so the study can isolate whether the benefits actually persist as the models get bigger.
