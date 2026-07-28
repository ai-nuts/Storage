# Key Result

Core claim: The proposed test controls type-I error in every setting and correctly identifies the true change point even when the state dimension dS ≥ 10, whereas CUSUM-RL only succeeds at dS=1 and ODCP fails to control type-I error in high dimensions.

Supporting detail: In the toy example the test holds nominal size and power as long as either M1 (transition) or M2 (state-action distribution) is correctly specified, with highest power when both are correct.

Narration: The headline finding is about robustness to dimensionality. In every setting, the proposed test keeps the type-one error at the nominal level, and crucially it still pinpoints the true change point even when the state has ten, twenty, or thirty dimensions. By contrast, the CUSUM-RL baseline only recovers the change point when the state is one-dimensional, and the ODCP method fails to control the type-one error at all in high dimensions. The toy example confirms the double robustness in action: size and power hold as long as at least one of the two nuisance models is right, with the strongest power when both are correct.
