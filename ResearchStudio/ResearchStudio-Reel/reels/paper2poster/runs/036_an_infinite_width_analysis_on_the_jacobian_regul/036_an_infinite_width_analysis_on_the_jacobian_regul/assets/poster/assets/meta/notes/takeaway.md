# Takeaway

Core claim: Infinite-width theory extends to a network's Jacobian: robust (Jacobian-regularised) training of a wide MLP behaves like kernel regression with a Jacobian NTK, and this regularisation makes accuracy and robustness align rather than trade off.

Supporting detail: The work supplies the first infinite-width characterisation of why Jacobian regularisation improves adversarial robustness, plus practical tests for when its key full-rank assumption holds.

Narration: The bottom line is that infinite-width theory now reaches the Jacobian. Train a wide network with a Jacobian regulariser and, in the limit, it behaves like kernel regression with a Jacobian Neural Tangent Kernel. And that same regulariser makes accuracy and robustness pull in the same direction instead of fighting each other, giving us the first principled explanation, from the infinite-width viewpoint, of why penalising the Jacobian yields networks that are both accurate and robust.
