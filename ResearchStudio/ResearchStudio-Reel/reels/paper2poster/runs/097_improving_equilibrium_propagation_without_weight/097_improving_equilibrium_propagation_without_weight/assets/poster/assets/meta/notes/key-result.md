# Key Result

Core claim: On CIFAR-10 the asymmetric hEP network jumps from 60.4% (no homeostatic loss) to 84.3% Top-1 with the homeostatic loss, only 4.3 points below the symmetric architecture, and for the first time hEP trains on ImageNet 32×32 (31.4% Top-1 / 55.2% Top-5).

Supporting detail: The homeostatic loss increases the Jacobian symmetry measure and the layer-wise alignment between hEP's and backprop's neuronal error vectors over training, while having no measurable effect when networks are already trained with RBP.

Narration: The headline result is striking. On CIFAR-10, the asymmetric network trained with EP but without the homeostatic loss reaches only sixty point four percent accuracy. Add the homeostatic loss, and accuracy jumps to eighty-four point three percent, just four point three points shy of the fully symmetric architecture, and all with only approximate weight symmetry. Even more importantly, this is the first time this family of methods trains at all on ImageNet thirty-two by thirty-two, reaching thirty-one point four percent Top-1 and fifty-five point two percent Top-5. Throughout training, the homeostatic loss steadily raises the Jacobian's symmetry and tightens the alignment between EP's error signals and true backprop.
