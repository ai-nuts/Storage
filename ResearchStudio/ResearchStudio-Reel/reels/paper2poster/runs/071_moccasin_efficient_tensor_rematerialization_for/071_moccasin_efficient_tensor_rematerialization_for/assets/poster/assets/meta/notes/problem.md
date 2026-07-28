# Problem

Core claim: Given a neural network compute graph and a fixed local memory budget, choose which tensors to keep versus recompute (rematerialize) so total execution time is minimized while never exceeding the budget.

Supporting detail: Memory is the primary limiting factor for deploying and training large models on low-memory edge devices; the underlying scheduling problem is PSPACE-complete.

Narration: Neural networks running on edge devices are constrained above all by memory. One way to fit a large model into a small memory footprint is rematerialization: instead of storing every intermediate tensor, you recompute some of them on demand. The catch is that recomputation costs time. So the core problem is a scheduling one: for a given compute graph and a fixed memory budget, decide which tensors to retain and which to recompute so that total execution time is as small as possible while peak memory never exceeds the budget. This is a hard combinatorial optimization, in general PSPACE-complete.
