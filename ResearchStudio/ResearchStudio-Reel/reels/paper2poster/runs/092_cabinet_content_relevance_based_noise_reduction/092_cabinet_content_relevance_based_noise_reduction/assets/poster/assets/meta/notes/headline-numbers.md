# Headline Numbers

Core claim: - WikiTQ: 69.1% accuracy (new SoTA, +6.4% over OmniTab) - FeTaQA: 40.5 Sacre-BLEU (new SoTA) - WikiSQL: 89.5% accuracy (new SoTA) - Model size: 560M parameters (OmniTab backbone)

Supporting detail: More robust under table perturbations (row/column permutation, cell replacement) and maintains its lead as table size grows; ~11.5% smaller performance drop than OmniTab under perturbation on WikiTQ.

Narration: The headline numbers are sixty-nine point one percent accuracy on WikiTQ, a Sacre-BLEU of forty point five on FeTaQA, and eighty-nine point five percent accuracy on WikiSQL, each a new state of the art achieved with just five hundred sixty million parameters. Beyond raw accuracy, CABINET is markedly more robust: under table perturbations such as row and column permutation and cell replacement it degrades far less than baselines, with roughly an eleven and a half percent smaller performance drop than OmniTab on WikiTQ, and it holds its advantage as tables grow larger.
