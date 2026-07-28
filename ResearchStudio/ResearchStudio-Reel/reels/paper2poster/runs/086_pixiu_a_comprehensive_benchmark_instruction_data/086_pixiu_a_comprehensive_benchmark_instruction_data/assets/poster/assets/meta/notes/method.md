# Method

Core claim: PIXIU collects open financial data across five tasks, wraps each sample with domain-expert-written task-specific instructions to build FIT, then fine-tunes LLaMA (7B and 30B) with multi-task instruction tuning to produce FinMA.

Supporting detail: Data spans multiple modalities (text plus tabular reports and historical stock-price time series) and text types (reports, news, tweets, filings); variants include FinMA-7B, FinMA-30B (NLP tasks), and FinMA-7B-full (NLP + prediction).

Narration: The method has three stages. First, PIXIU gathers open-released data across five financial tasks: sentiment analysis, news headline classification, named entity recognition, question answering, and stock movement prediction. Domain experts write diverse task-specific instructions for each task, which are assembled with the data samples to form the FIT instruction dataset. This data is multi-modal, spanning text, tables from financial reports, and historical stock prices as time series. Second, LLaMA checkpoints at seven and thirty billion parameters are fine-tuned on FIT with multi-task instruction tuning, producing the FinMA model family. Third, FinMA and other LLMs are evaluated on the FLARE benchmark, which unifies four financial NLP tasks with six datasets and one prediction task with three datasets.
