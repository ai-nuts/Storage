# Ablation Study

Core claim: Parameter size affects performance more than architecture or training-data composition: encoder-only AntiBERTy and decoder-only IgLM (both trained on the same 558M OAS sequences) perform similarly, while scaling ProGen2 from 151M to 6.4B parameters noticeably improved only polyreactivity and thermostability prediction.

Supporting detail: Some models are biased toward evolutionary signal: AntiBERTy, IgLM, and the ProGen2 suite assign higher confidence to wild-type golimumab than to more thermostable mutants, whereas physics-based Rosetta correctly ranks the stabilized mutants.

Narration: Digging into what drives performance, the authors find that parameter count matters more than architecture or training data. Encoder-only AntiBERTy and decoder-only IgLM, both trained on the same five hundred fifty eight million antibody sequences, behave almost identically. Scaling ProGen2 from one hundred fifty million up to over six billion parameters helped only two properties, polyreactivity and thermostability. They also uncover an evolutionary bias: several language models rank the wild-type golimumab antibody as fitter than mutants that are actually more thermostable, while physics-based Rosetta gets the ranking right. It's a reminder that evolutionary likelihood and physical fitness are not the same thing.
