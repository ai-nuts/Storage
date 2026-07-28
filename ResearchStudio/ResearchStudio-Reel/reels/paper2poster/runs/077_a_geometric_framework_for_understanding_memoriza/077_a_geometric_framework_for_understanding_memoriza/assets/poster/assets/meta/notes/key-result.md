# Key Result

Core claim: Across every scale, estimates of LID are strongly predictive of memorization: memorized images consistently receive small LIDθ values (and large CFG vector norms), directly confirming the MMH.

Supporting detail: Crucially, the unconditional LIDθ detects memorized training images well even without access to their captions — a novel capability that the CFG-vector-norm technique of prior work cannot provide, since it requires the conditioning caption.

Narration: The headline empirical finding is that local intrinsic dimension tracks memorization everywhere the authors look, from toy 2D data to Stable Diffusion. Memorized images reliably get low LID estimates and high classifier-free guidance vector norms. Even more striking, the unconditional LID estimate flags memorized training images without needing their captions at all. That is a genuinely new capability, because the previous state of the art, the CFG vector norm, depends on having the caption in hand.
