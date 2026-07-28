# Motivation

Core claim: Temperature sampling tuned for head languages over-repeats the tail: at τ=3.33 with a trillion-token budget, the lowest-resource languages are repeated over 100 times.

Supporting detail: Excessive repetition causes overfitting that degrades downstream tasks, raises the risk of memorizing private content, and wastes compute on duplicate examples, and these harms worsen as models scale.

Narration: Temperature sampling reshapes the data distribution using a single exponent, tau. But there is a catch. When you tune tau to give the head languages more presence, you end up over-repeating the tail. At tau equals three point three three, with a trillion-token budget, the lowest-resource languages get repeated more than a hundred times. That much repetition causes overfitting that hurts downstream tasks, it raises the risk of memorizing private content, and it wastes compute on duplicate examples, and every one of these harms only gets worse as models scale.
