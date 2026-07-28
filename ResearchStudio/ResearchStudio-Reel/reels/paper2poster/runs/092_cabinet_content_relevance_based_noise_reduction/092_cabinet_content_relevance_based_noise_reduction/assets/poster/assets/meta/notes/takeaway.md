# Takeaway

Core claim: Softly weighting table content by learned relevance, rather than hard-decomposing tables, lets an LLM focus on the cells that matter and sets new state of the art on table QA with a compact model.

Supporting detail: Combining an unsupervised, differentiable relevance scorer with a weakly-supervised parsing-statement cell highlighter is both more accurate and more robust to noise than prior removal-based approaches.

Narration: The core lesson of CABINET is that you do not need to cut a table down to answer questions about it. By softly weighting every cell according to a learned relevance score, instead of hard-decomposing the table and risking the loss of useful information, the model keeps full access to the data while being steered toward what matters. Pairing a differentiable unsupervised relevance scorer with a weakly-supervised parsing-statement cell highlighter yields both higher accuracy and greater robustness to noise, setting new state of the art on three table QA benchmarks with a compact five hundred sixty million parameter model.
