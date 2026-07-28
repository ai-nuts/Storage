# Problem

Core claim: Machine learning models achieve high accuracy on static benchmarks yet break on production data. The mismatch is usually called distribution shift, but that framing is simultaneously over-specified and under-specified.

Supporting detail: Formal shift definitions (covariate, prior probability, concept shift) precisely compare two samples but say nothing about the data-generating process that caused the mismatch.

Narration: Benchmark datasets play two roles: they let researchers compare methods, and they stand in as an imperfect model of the real world. The trouble is that a single static benchmark can never fully capture the dynamic, high-dimensional complexity of real tasks. So models that appear to match or beat human-level accuracy on a benchmark routinely err on out-of-distribution and adversarially perturbed production data. The field describes this gap as distribution shift, with subcategories like covariate shift, prior probability shift, and concept shift. But these definitions are over-specified for comparing two data samples and under-specified for evaluating the data-generating process that actually drives the mismatch.
