# Motivation

Core claim: Safely deploying LLMs requires reliably extracting their latent knowledge of truth; understanding why CCS works is a prerequisite for trusting and improving such probes.

Supporting detail: Prior work framed CCS around clustering activations and learning calibrated probabilities. The authors show both framings are misleading, motivating a cleaner account of CCS's true optimization target.

Narration: Safely deploying capable models means catching confident falsehoods, and probes that read a model's own truth representation could help, but only if we understand them. CCS was explained through clustering activations and learning probabilities. The authors argue both pictures mislead, motivating a cleaner account of its target.
