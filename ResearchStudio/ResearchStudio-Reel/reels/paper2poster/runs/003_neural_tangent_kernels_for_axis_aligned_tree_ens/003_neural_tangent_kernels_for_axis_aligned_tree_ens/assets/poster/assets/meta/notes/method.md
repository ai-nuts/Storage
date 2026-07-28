# Method

Core claim: The authors consider the limit of infinitely many perfect binary soft trees (M → ∞) and derive the TNTK, a deterministic kernel with separate contributions from inner splitting nodes and from leaves. The soft split uses a scaled error (sigmoid-like) function whose hardness is controlled by a scaling parameter α, and the kernel is obtained in closed form independent of tree depth's recursion.

Supporting detail: Because the TNTK is fixed during training, learning dynamics reduce to kernel regression; positive definiteness of the TNTK yields global convergence, and the closed form makes computation independent of tree depth.

Narration: The method takes the number of trees to infinity. For perfect binary soft trees of depth d, the authors prove the Tree Neural Tangent Kernel converges to a deterministic kernel with two parts: one from the inner splitting nodes and one from the leaves. The soft split uses a scaled error function, a smooth sigmoid whose sharpness is set by alpha, and its expectations have closed forms, so the kernel is analytic. Because the kernel stays constant and positive definite, training reduces to kernel regression with global convergence, and the formula is not recursive in depth, so its cost is depth-independent.
