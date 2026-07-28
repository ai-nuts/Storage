# Motivation

Core claim: A rigorous curvature-memorization-privacy link would justify using cheap curvature as a memorization proxy and reveal how privacy mechanisms suppress memorization.

Supporting detail: Influence functions, the usual counterfactual tool, assume Hessian convexity and positive-definiteness, conditions that fail for deep nets; curvature needs no such assumptions.

Narration: Proving curvature bounds memorization would license the cheap proxy over the expensive score. Because memorization is a privacy risk, linking differential privacy to curvature explains why privacy reduces leakage. Unlike influence functions, which assume Hessian convexity that fails for deep nets, this framework needs no such assumptions.
