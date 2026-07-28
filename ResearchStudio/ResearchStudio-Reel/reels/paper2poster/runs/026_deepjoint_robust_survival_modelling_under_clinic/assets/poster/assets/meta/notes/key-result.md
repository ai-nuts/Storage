# Key Result

Core claim: Modelling clinical presence gives state-of-the-art discrimination on short horizons, DeepJoint variants top the C-index at 1 day (up to 0.878), beating input-matched baselines including GRU-D. The edge fades at longer horizons as clinical presence chiefly signals short-term instability.

Supporting detail: Even DeepJoint using only laboratory values (no missingness inputs) beats the "Ignore" LSTM and GRU-D, showing the observation process improves the embedding without being fed as an input.

Narration: On a random population split, the three proposed methods deliver competitive-to-best discrimination against models using the same inputs. Strikingly, DeepJoint, which sees only laboratory values, already outperforms both an LSTM that ignores clinical presence and GRU-D, which consumes missingness as input. So modelling the observation process, even without feeding it in, yields a more predictive embedding. Fine-tuning adds a further edge, reaching a one-day C-index of 0.878.
