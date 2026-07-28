# Ablation Study

Core claim: Ablations on Traffic (in-domain forecasting) show masked past-to-current reconstruction outperforms self-reconstruction, a moderate 25% masking ratio works best (15% oversimplifies, 75% is too hard), and lineage embeddings give consistent gains over random initialization.

Supporting detail: Increasing the number of lineage embeddings improves ECL and Traffic performance up to a point, confirming that modeling multiple temporal distances helps.

Narration: Careful ablations on the Traffic benchmark tell us which design choices matter. Reconstructing the current window from a past one clearly beats plain self-reconstruction, validating the core Siamese idea. The masking ratio has a sweet spot around twenty-five percent: masking only fifteen percent makes the task too easy to teach anything useful, while masking seventy-five percent makes it too hard. Lineage embeddings deliver consistent gains over random initialization, and adding more of them keeps improving results on Electricity and Traffic up to a point, confirming that explicitly modeling multiple temporal distances is worthwhile.
