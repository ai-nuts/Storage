# Dataset / Benchmark

Core claim: QM9 (130K molecules, 12 regression targets, hardest target R²) for regression; the TUD benchmark (MUTAG, PTC, Proteins, NCI1, IMDB-B, IMDB-M) for graph classification; and a spectral node-regression dataset for band-pass filter learning.

Supporting detail: QM9 is split 0.8 / 0.1 / 0.1 for train / val / test as in prior work; TUD uses the standard evaluation protocol; the spectral task follows the 900-node-graph protocol used to stress PPGN.

Narration: The evaluation spans three very different arenas. For regression, the QM9 dataset of one hundred thirty thousand small molecules, with twelve quantum-chemical targets, including R-squared, the hardest one to predict. For classification, the classic TUD benchmark, six datasets ranging from molecules like MUTAG and PTC to social graphs like IMDB. And for a spectral stress test, a node-regression task on nine-hundred-node graphs that asks whether the model can act as a band-pass filter. Together they probe accuracy, generality, and a subtle spectral ability that trips up other 3-W-L models.
