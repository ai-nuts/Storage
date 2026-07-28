# Takeaway

Core claim: Certifying a set of nodes jointly, rather than one at a time, turns a near-useless 0% guarantee into an 80%+ certified ratio against graph injection attacks, and a customized LP relaxation makes it solvable in about a minute.

Supporting detail: This is a concrete step toward practical, provable defenses for message-passing GNNs, and it composes with existing sample-wise certificates to stay strong across both small and large attack budgets.

Narration: The lesson is simple but powerful. Certifying a whole set of nodes together, instead of one at a time, transforms a near-useless zero percent guarantee into an eighty percent certified ratio against graph injection attacks. A customized linear relaxation keeps this tractable, solving in about a minute even for large attacks. It is a concrete step toward provable defenses that are practical, and because it shares the same smoothed model, it plugs right in alongside existing sample-wise certificates to stay strong across every attack budget.
