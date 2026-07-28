# Motivation

Core claim: Rather than trading quality for speed by reducing steps, the authors ask whether additional parallel compute can perform the same number of denoising steps in less wall-clock time.

Supporting detail: Sampling latency, not throughput, is the bottleneck; naive parallelism only raises throughput because denoising proceeds sequentially, so cutting single-sample latency looks hard.

Narration: The authors pursue an orthogonal direction. Instead of trading quality for speed, they ask whether we can trade compute for speed. The goal is to lower the latency of generating a single sample, not just the throughput of generating many. At first this seems impossible, because denoising is inherently sequential: each step depends on the previous one. Naive parallelization can generate multiple samples at once, but making a single sample appear faster in wall-clock time is a much harder problem.
