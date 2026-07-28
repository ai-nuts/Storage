# Problem

Core claim: Existing statistical learning guarantees give loose, often vacuous bounds on the test error of finite-rank kernel ridge regression (KRR), especially in the ridgeless regime and without matching lower bounds.

Supporting detail: Finite-rank kernels arise naturally when only the final layer of a pre-trained deep network is fine-tuned for transfer learning, so tight guarantees here matter in practice.

Narration: Kernel ridge regression helps explain generalization, and tuning a network's last layer behaves like it with a finite-rank kernel. But classical bounds are far too loose here: they keep the ridge above zero, give only upper bounds, and go vacuous as regularization vanishes.
