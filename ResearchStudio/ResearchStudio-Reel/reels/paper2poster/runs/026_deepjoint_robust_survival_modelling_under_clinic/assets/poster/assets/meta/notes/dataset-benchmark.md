# Dataset / Benchmark

Core claim: MIMIC-III ICU laboratory tests: 38,597 patients at Beth Israel Deaconess (2001–2012), filtered to 30,834 patients surviving the first 24 hours after admission. Survival is predicted from the embedding at the last observation in that 24-hour window.

Supporting detail: A 90%–10% patient-level train–test split; evaluation by time-dependent C-index and Brier score at horizons of 1, 7, and 14 days.

Narration: Experiments use MIMIC-three, an intensive-care database of anonymised laboratory tests for over thirty-eight thousand patients at Beth Israel Deaconess between 2001 and 2012. Restricting to those surviving the first twenty-four hours leaves a cohort of 30,834 patients. Models predict in-hospital survival from the embedding at the last observation in that first day, compared by time-dependent concordance index and Brier score at one, seven, and fourteen days.
