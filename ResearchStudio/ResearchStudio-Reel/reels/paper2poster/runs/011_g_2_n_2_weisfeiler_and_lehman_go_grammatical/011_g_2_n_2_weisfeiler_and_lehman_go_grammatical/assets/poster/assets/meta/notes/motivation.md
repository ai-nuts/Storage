# Motivation

Core claim: The Weisfeiler-Lehman hierarchy characterizes GNN expressiveness, and prior work reformulated the 1-WL and 3-WL tests as fragments ML(L1) and ML(L3) of the matrix language MATLANG — but turning such a fragment into a provably equivalent GNN was still done case by case.

Supporting detail: GNNML3, derived from the same MATLANG view, was only shown to be more expressive than 1-WL, not provably 3-WL, precisely because there was no systematic derivation procedure.

Narration: The seed of the idea comes from a groundbreaking observation: the 1-W-L and 3-W-L tests can each be rewritten as a fragment of a matrix language called MATLANG. Two graphs look the same to 3-W-L if and only if every sentence you can write in the fragment ML-of-L-three gives them the same value. That is a beautiful bridge between combinatorics and algebra. But a bridge is not a road. Turning one of these fragments into an actual, trainable network had been done only case by case, and the resulting models could not claim the full 3-W-L guarantee. The motivation here is to pave that road once and for all.
