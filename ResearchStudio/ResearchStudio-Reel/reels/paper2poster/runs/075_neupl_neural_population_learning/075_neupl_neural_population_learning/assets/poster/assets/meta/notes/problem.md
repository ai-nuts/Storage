# Problem

Core claim: Learning in strategy games requires a diverse population of policies, usually grown by iteratively best-responding to existing ones — an approach that breaks down under real-world budgets.

Supporting detail: Approximate best-responses must be truncated on hand-crafted schedules, leaving under-trained "good-responses" in the population, and each iteration wastefully relearns basic skills from scratch.

Narration: "Classical population-learning methods such as Policy Space Response Oracles grow a set of strategies by repeatedly training a new policy to best-respond to a mixture over the existing ones. In toy normal-form games this works cleanly because best-responses can be solved exactly. But real-world games are temporal and partially observed, so best-responses can only be approximated with expensive deep reinforcement learning. This creates two failures: under a finite budget you cannot tell a truly converged best-response from one stuck at a local plateau, so iterations get truncated prematurely and pollute the population with weak policies; and every new policy relearns basic skills from scratch, which becomes intractable as opponents grow stronger."
