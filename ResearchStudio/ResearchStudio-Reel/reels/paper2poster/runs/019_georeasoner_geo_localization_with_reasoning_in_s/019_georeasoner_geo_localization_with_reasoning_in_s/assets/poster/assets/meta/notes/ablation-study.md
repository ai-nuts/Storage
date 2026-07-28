# Ablation Study

Core claim: Removing either fine-tuning stage hurts: starting from the Qwen-VL baseline (country/city F1 0.7225 / 0.5270), reasoning tuning alone reaches 0.8215 / 0.5813 and location tuning alone reaches 0.8766 / 0.8255, but the full two-stage GeoReasoner is best at 0.9033 / 0.8585.

Supporting detail: Location tuning is the dominant driver of fine-grained city-level accuracy, while reasoning tuning adds a consistent further lift, confirming the two stages are complementary rather than redundant.

Narration: An ablation isolates the contribution of each fine-tuning stage. Starting from the Qwen-VL baseline, adding only reasoning tuning improves country and city F1 modestly. Adding only location tuning produces a much larger jump, especially at the fine-grained city level, confirming that location tuning is essential for pinpointing cities. But the full model, with both stages stacked, is the strongest of all, reaching a country F1 of zero point nine zero and a city F1 of zero point eight six. The two stages are complementary: location tuning supplies precision, reasoning tuning supplies explanations and a further accuracy lift.
