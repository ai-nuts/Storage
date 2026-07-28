# Motivation

Core claim: Orthogonal Weight Modification (OWM) overcomes forgetting without replay but ignores that genuine audio often shares a similar feature distribution across datasets, wasting an exploitable regularity.

Supporting detail: Conversely, a few datasets contain genuine audio recorded under very different acoustic conditions, so treating all classes identically skews the feature distribution and hurts retention.

Narration: Existing weight-modification methods like OWM treat every input the same when constraining updates. But in fake audio detection, genuine speech tends to look similar from one dataset to the next, while the fake speech varies. That regularity is an opportunity: the direction of a weight update should adapt to how much of a batch is genuine versus fake. At the same time, some datasets collect genuine audio under acoustic conditions so different that a naive rule backfires, motivating an extra safeguard.
