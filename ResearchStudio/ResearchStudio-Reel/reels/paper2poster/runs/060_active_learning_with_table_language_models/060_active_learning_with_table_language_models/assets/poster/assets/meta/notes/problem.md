# Problem

Core claim: Fine-tuning tabular language models for industrial tasks needs many labels, but only experts can annotate the highly technical, domain-specific spreadsheet tables, making label acquisition prohibitively expensive.

Supporting detail: Sub-cell named entity recognition on tables is a novel nested multi-instance problem: each table holds many cells, and each cell carries multiple token labels, so it is unclear whether to acquire at the token, cell, or table level.

Narration: Industry runs on spreadsheets. Operators track equipment, sensors, and vessels in loosely structured tables, and extracting that information automatically means fine-tuning tabular language models on labeled examples. But these tables use highly technical language only a few experts can annotate, so labeling gets expensive fast. The paper frames this as sub-cell named entity recognition, a genuinely new active learning problem, since each cell carries multiple token-level labels at once.
