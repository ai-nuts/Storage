# Problem

Core claim: No method existed to compute the lowest achievable 0-1 loss under a test-time (adversarial) attacker for multi-class classification; prior optimal-loss results covered only the binary case.

Supporting detail: Without this benchmark, practitioners cannot tell whether a robust model is near-optimal or how much headroom remains, keeping them stuck in the attack-defense arms race.

Narration: Determining whether a classifier is truly robust to adversarial examples requires knowing the best that is even possible. For binary classification, prior work characterized this optimal robust loss, giving a reference point to measure progress against. But real problems have many classes, and the multi-class case was left open. There was no way to compute the lowest 0-1 loss achievable by any classifier against a test-time attacker on a multi-class dataset, so practitioners had no way to know how far current defenses sit from the theoretical limit.
