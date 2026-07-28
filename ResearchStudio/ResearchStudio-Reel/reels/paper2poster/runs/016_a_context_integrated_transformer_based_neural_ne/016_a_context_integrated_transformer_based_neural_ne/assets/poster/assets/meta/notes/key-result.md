# Key Result

Core claim: In single-item settings CITransNet essentially recovers the Myerson-optimal revenue (0.593 vs 0.594 optimal in Setting A) with regret below 0.001, and in every multi-item setting it beats the strong Item-wise Myerson baseline and the context-integrated CIRegretNet and CIEquivariantNet variants.

Supporting detail: Gains over Item-wise Myerson reach roughly +9.9% (Setting G: 1.177 vs 1.071) and +5.6% (Setting E: 6.872 vs 6.509), while plain RegretNet and EquivariantNet, lacking context, fail to reach the optimum even on the simple settings.

Narration: Results come in two parts. On single-item settings, CITransNet nearly recovers Myerson's optimal revenue, 0.593 against 0.594, with regret below one thousandth, while context-blind baselines fall short. On the harder multi-item settings, it beats the Item-wise Myerson baseline in all six configurations, with gains reaching ten percent.
