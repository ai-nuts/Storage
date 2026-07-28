# Problem

Core claim: In table question answering, only a few cells matter for a given question; the rest act as noise, and LLMs are vulnerable to this irrelevant content, producing sub-optimal answers.

Supporting detail: Degradation worsens on large tables where even more irrelevant data is present, amplifying the distraction for the QA model.

Narration: Tables organize information across rows and columns, but for any single question only a small number of cells actually contain the answer. Everything else is irrelevant to that question and behaves like noise. Large language models are known to be susceptible to such distracting information, so their table reasoning degrades, and the problem gets worse as tables grow larger and carry even more irrelevant content. CABINET is built to address exactly this vulnerability.
