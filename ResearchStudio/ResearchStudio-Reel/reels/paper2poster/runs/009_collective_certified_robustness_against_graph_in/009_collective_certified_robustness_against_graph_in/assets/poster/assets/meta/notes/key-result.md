# Key Result

Core claim: Both collective certificates dramatically outperform the sample-wise baseline as the injected-node count grows. On Citeseer at ρ = 140, Collective-LP1 and Collective-LP2 certify 73.0% and 81.2% of target nodes respectively, while the sample-wise approach certifies 0.0%.

Supporting detail: The customized Collective-LP2 consistently matches or beats Collective-LP1 — on Cora-ML (pe=0.7, pn=0.9, ρ=140) it improves the certified ratio by 216% over LP1 — while running far faster, solving even ρ=140 in roughly 1 minute versus LP1's ~700+ seconds.

Narration: The headline result is a night-and-day improvement. As the number of injected nodes grows, the sample-wise baseline collapses to zero certified nodes, while the collective certificates hold strong. On Citeseer with a hundred and forty injected nodes, the standard collective relaxation certifies seventy-three percent of targets and the customized version reaches eighty-one point two percent, both against zero percent for sample-wise. The customized Collective-LP-two consistently matches or beats the standard one, in one setting by over two hundred percent relative, and it does so far faster, solving even the largest budgets in about a minute.
