# Motivation

Core claim: Many applications with incrementally-arriving data or mixed-integer subproblems solve a sequence of closely related SDPs, so being able to warm-start from the previous solution is essential for speed.

Supporting detail: Spectral bundle methods have low per-iteration cost and fast empirical convergence, but prior versions handled only equality or only inequality constraints and lacked an efficient standalone implementation for massive SDPs.

Narration: In practice, you rarely solve a single SDP in isolation. Data arrives incrementally, or you solve a sequence of tightly-related subproblems inside a mixed-integer or interactive loop. In all these settings, each new problem is nearly identical to the last, so being able to warm-start from the previous solution should give a huge speedup. Spectral bundle methods are an appealing framework here: they have low per-iteration cost and fast empirical convergence. But previous spectral bundle methods handled either only equality constraints or only inequality constraints, and none had an efficient standalone implementation that could be evaluated on truly massive SDPs.
