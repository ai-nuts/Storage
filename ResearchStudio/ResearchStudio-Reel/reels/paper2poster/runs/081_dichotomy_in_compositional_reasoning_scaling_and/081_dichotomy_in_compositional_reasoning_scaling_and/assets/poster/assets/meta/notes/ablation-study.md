# Ablation Study

Core claim: Varying model scale within families cleanly separates the two regimes: on separable tasks accuracy rises with scale, while on compose-by-step tasks it stays flat or degrades. Switching from composite to composite-in-context demonstrations recovers performance, isolating composition (not capability) as the bottleneck.

Supporting detail: Across word-level, arithmetic, and translation task families the same separable-vs-step dichotomy holds, and larger models improve on the composite task only when the underlying simple tasks improve, matching the confined-support scaling theory.

Narration: The scale sweep is the key ablation. On separable tasks accuracy rises with scale; on compose-by-step tasks it stays flat or degrades. Swapping simple-task demos for composite ones recovers performance, isolating composition, not capability, as the bottleneck.
