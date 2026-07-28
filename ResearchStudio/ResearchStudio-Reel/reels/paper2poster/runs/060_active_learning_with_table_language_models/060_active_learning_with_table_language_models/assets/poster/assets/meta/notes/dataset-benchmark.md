# Dataset / Benchmark

Core claim: A real-world industrial dataset of downsampled spreadsheets from multiple plants (max 5 rows per table), expert-annotated cell-by-cell with prodi.gy; a random split yields 55 training tables and 24 test tables.

Supporting detail: The 55 training tables hold 4,774 cells but only 1,112 NER span labels (0.23 labels per cell), so roughly 77% of cells contain only O-tagged tokens, an extreme class imbalance typical of industrial settings.

Narration: Evaluation uses a real industrial dataset, not an academic benchmark. Spreadsheets from several plants were downsampled to at most five rows each, and expert annotators labeled every cell with the Prodigy span-based tool. A random split gives 55 training tables and 24 for testing. The training set holds 4,774 cells but only about 1,100 entity labels, just 0.23 per cell, meaning roughly 77 percent of cells contain no entity, an extreme imbalance typical of industrial data.
