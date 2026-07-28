# Motivation

Core claim: Instruction tuning is critical for zero-shot ability on downstream financial tasks, and real-world finance needs prediction tasks such as stock movement that existing NLP-only benchmarks ignore.

Supporting detail: Prior benchmarks (FLUE, BBT-CFLEB) cover only financial NLP tasks and omit prediction tasks aligned with real trading scenarios.

Narration: Two gaps motivate this work. First, instruction tuning has proven essential for improving a model's zero-shot ability on downstream tasks, yet no financial instruction data exists to enable it. Second, existing financial benchmarks such as FLUE cover only natural language processing tasks. They ignore financial prediction tasks like stock movement prediction, which require exploiting both text and time-series data and are far more aligned with real-world financial scenarios. PIXIU is built to close both gaps with open resources, multi-task coverage, multi-modal data, and greater task diversity.
