# Contribution

Core claim: CABINET, a framework that suppresses irrelevant table content via a differentiable Unsupervised Relevance Scorer plus a weakly-supervised parsing-statement module that highlights question-relevant cells, trained end-to-end with the QA LLM.

Supporting detail: It establishes new state of the art on WikiTQ, FeTaQA, and WikiSQL, and demonstrates markedly greater robustness to table perturbations and to increasing table size.

Narration: The paper contributes CABINET, short for Content Relevance-Based Noise Reduction. It has two cooperating parts. First, an Unsupervised Relevance Scorer assigns a soft relevance weight to every table token and is trained differentiably alongside the question-answering model. Second, a weakly-supervised module generates a parsing statement describing which rows and columns matter, then highlights the corresponding cells to produce a cell-based relevance signal. Together they let the model focus without discarding content, and they deliver new state of the art on three benchmarks along with stronger robustness to noise and to large tables.
