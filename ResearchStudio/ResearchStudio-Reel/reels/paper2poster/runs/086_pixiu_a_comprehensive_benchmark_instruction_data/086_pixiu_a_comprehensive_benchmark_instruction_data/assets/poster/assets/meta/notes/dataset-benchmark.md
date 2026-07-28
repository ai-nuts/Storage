# Dataset / Benchmark

Core claim: FIT holds 136,609 instruction samples across 5 tasks and 9 datasets; FLARE evaluates on those 9 datasets covering sentiment (FPB, FiQA-SA), headline classification, NER, question answering (FinQA, ConvFinQA), and stock movement prediction (BigData22, ACL18, CIKM18).

Supporting detail: Metrics are task-specific: weighted F1 and accuracy for sentiment, average F1 for headlines, entity F1 for NER, exact-match accuracy for QA, and accuracy plus Matthews correlation coefficient for stock prediction.

Narration: FIT, the financial instruction tuning dataset, contains one hundred thirty-six thousand instruction samples across five tasks and nine datasets. The FLARE evaluation benchmark covers four financial NLP tasks with six datasets and one financial prediction task with three datasets. Sentiment analysis uses the Financial Phrase Bank and FiQA-SA, news headline classification uses the Headline dataset, named entity recognition uses a financial NER dataset, question answering uses FinQA and ConvFinQA, and stock movement prediction uses BigData22, ACL18, and CIKM18. Each task is scored with its standard metric, such as weighted F1, entity-level F1, exact-match accuracy, and the Matthews correlation coefficient for prediction.
