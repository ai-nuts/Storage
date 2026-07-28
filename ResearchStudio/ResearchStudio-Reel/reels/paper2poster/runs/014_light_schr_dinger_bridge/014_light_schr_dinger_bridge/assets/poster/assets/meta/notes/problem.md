# Problem

Core claim: Computational Schrödinger Bridge (SB) solvers are heavy: they stack several neural networks and need complex optimization, so there is no simple, principled baseline solver, analogous to k-means, logistic regression, or Sinkhorn.

Supporting detail: SB, the dynamic form of Entropic Optimal Transport (EOT), seeks a diffusion process between two distributions maximally similar to a Wiener prior; practitioners often just want the endpoint plan π*(x₁|x₀).

Narration: The Schrödinger Bridge problem asks for the diffusion process between two given distributions that stays as close as possible to a reference Wiener process. It is the dynamic version of entropic optimal transport, and it underpins applications from single-cell biology to image translation. The trouble is that almost all existing solvers are heavy-weighted. They parameterize the solution with several large neural networks and require complex, often adversarial optimization. As a result, the field lacks a simple, principled baseline, the kind of go-to method that k-means is for clustering or Sinkhorn is for discrete optimal transport.
