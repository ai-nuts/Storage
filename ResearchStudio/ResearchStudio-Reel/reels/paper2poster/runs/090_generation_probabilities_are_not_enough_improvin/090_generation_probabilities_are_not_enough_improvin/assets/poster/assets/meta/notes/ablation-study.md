# Ablation Study

Core claim: A token-survival analysis shows the edit model steers people to more precise edits: non-highlighted tokens survive more often under the edit model (0.87) than under generation probability (0.81) or prediction-only (0.79), while highlighted tokens survive far less under the edit model (0.35) than under generation probability (0.74), all p < .0001.

Supporting detail: This confirms the edit model is a much stronger signal of what people will actually change, whereas generation-probability highlights are only weakly aligned with real edits.

Narration: To understand why, the authors tracked which tokens survived, meaning they were left unchanged by the participant. Under the edit model, tokens it left un-highlighted survived far more often, about eighty-seven percent of the time, while tokens it did highlight survived only about thirty-five percent of the time. Compare that to generation-probability highlighting, where highlighted tokens still survived seventy-four percent of the time. In other words, the edit model's highlights closely predict what people actually change, while generation-probability highlights barely move the needle, and all of these differences are extremely significant.
