# Ablation Study

Core claim: MeZO is compatible with parameter-efficient tuning: MeZO with LoRA and MeZO with prefix tuning perform on par with full-parameter MeZO. Using n=1 perturbation per step is the most compute-efficient choice.

Supporting detail: MeZO can directly optimize non-differentiable objectives such as accuracy and F1, and outperforms the prior zeroth-order method BBTv2 by up to 11% absolute.

Narration: Several ablations probe MeZO's flexibility. Combining MeZO with parameter-efficient methods, namely LoRA and prefix tuning, gives accuracy on par with tuning all parameters, showing the two approaches compose well. Using a single random perturbation per step, rather than averaging several, turns out to be the most efficient setting for a fixed number of forward passes. Because MeZO only needs loss values and never actual gradients, it can optimize non-differentiable objectives directly, such as maximizing accuracy or F1 score. And against a prior zeroth-order baseline, BBTv2, MeZO improves accuracy by up to eleven percentage points.
