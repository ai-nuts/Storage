# Motivation

Core claim: Real user problems, such as those on StackOverflow, carry diverse contexts including buggy code, error messages, and input-output examples that prior benchmarks omit, and reliable metrics are needed as models grow stronger.

Supporting detail: Surface-form metrics increasingly diverge from programmer intent as model capability improves, so execution-based evaluation becomes essential.

Narration: Real data science questions rarely look like clean textbook prompts. On StackOverflow, users describe messy contexts: their broken code, the error they hit, and concrete input-output examples of what they want. Prior benchmarks strip that richness away. At the same time, as models get better, surface-form scores like BLEU become misleading, rewarding text that looks right but does not run. This motivates a benchmark built from natural problems and judged by actually executing the code.
