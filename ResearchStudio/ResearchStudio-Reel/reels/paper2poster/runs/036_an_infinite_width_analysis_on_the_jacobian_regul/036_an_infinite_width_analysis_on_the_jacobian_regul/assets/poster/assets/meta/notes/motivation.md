# Motivation

Core claim: Jacobian regularisation is a simple and strong defence against adversarial attacks, yet why it works is not understood theoretically.

Supporting detail: The powerful infinite-width tools that answered analogous questions for standard training had never been extended to the Jacobian or to Jacobian-regularised ("robust") training.

Narration: Jacobian regularisation is one of those methods that just works. Add a penalty on the network's input-output Jacobian and you get a simple, strong defence against adversarial examples. The problem is that nobody could really explain why. The theory that had cracked open ordinary training, the infinite-width limit, had never been pushed to cover the Jacobian, let alone training that penalises it. This paper asks whether that same lens can finally explain what Jacobian regularisation is doing.
