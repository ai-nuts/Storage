# Motivation

Core claim: Generalizing Euclidean convolution to graphs is hard: convolution is sensitive to spatial order, yet GNNs must stay permutation invariant, and prior graph-regularization methods are decoupled from the convolution and cannot be optimized per task.

Supporting detail: Earlier node-sequence-selection schemes produce fixed, less informative regularized graphs because their ordering is independent of the downstream learning objective.

Narration: So why not borrow Euclidean convolution for graphs? Convolution is sensitive to spatial order, but graph networks must be permutation invariant. Earlier methods picked a node ordering independently of the convolution, so it could not be tuned for the task and often lost information. What is missing is an ordering that is differentiable and learned end to end.
