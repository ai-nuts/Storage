# Motivation

Core claim: The authors observe that temporal gradients in SNNs are largely unimportant, so the temporal dynamics of most neurons can be switched off without hurting accuracy, freeing both memory and compute.

Supporting detail: Prior work decouples training from timestep (OTTT/SLTT) to cut memory, or fine-tunes to fewer inference steps, but each tackles only the training OR the inference dilemma, never both simultaneously.

Narration: The key insight behind this work is surprisingly simple. When the authors examined the gradients that flow backward through time in a spiking network, they found that for most neurons those temporal gradients barely matter. Only the neurons at a few key positions carry temporal information that is actually important. If that is true, then a natural question follows: why pay the full temporal cost for every neuron? Prior methods either decouple training from the timestep to save memory, or shrink the number of inference steps to save energy, but each one solves only half of the problem. This paper asks whether both halves can be solved together.
