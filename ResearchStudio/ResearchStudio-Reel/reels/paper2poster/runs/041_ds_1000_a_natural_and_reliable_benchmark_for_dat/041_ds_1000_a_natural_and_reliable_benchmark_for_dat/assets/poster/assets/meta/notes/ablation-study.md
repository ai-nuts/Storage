# Ablation Study

Core claim: On the numpy-100 probe, Codex-002 accuracy drops from 72.5% to 40.6% after perturbation (50.8% surface, 23.6% semantic), and in 36% of semantic cases the model still emits the original answer, exposing memorization on web-sourced problems.

Supporting detail: On DS-1000 itself the perturbation drop is milder (3.4% surface, 9.0% semantic), indicating less memorization because these problems are less repeated online than numpy-100.

Narration: To show why memorization matters, the authors probe the popular numpy-100 problem set. Codex-002 scores seventy-two point five percent there, but accuracy collapses to forty point six percent after perturbation, and in thirty-six percent of semantic cases the model still returns the original, now-incorrect answer, evidence that it is recalling memorized solutions rather than reasoning. On DS-1000 the perturbation drop is much gentler, about three to nine percent, because these problems appear less often online. This confirms perturbation as a practical defense against memorization by future models.
