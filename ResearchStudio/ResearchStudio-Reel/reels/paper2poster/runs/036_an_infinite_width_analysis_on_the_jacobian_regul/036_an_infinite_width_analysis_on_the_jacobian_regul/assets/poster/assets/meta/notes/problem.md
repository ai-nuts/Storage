# Problem

Core claim: Infinite-width theory (NNGP, NTK) explains the training of a network's output, but nothing is known about the limiting behaviour of its input-output Jacobian, or of training that regularises that Jacobian.

Supporting detail: The Jacobian encodes a network's smoothness and is widely used to measure and enforce robustness to input noise and adversarial attacks.

Narration: Over the last few years, infinite-width theory has given us remarkably clean answers about deep networks. Tools like the Neural Tangent Kernel tell us how a network initialises, how it trains, and where gradient descent ends up. But there is a catch: all of this describes a network's output. It says nothing about the network's input-output Jacobian, the object that captures how smooth the network is. And smoothness is exactly what we care about when we want robustness to noise or to adversarial attacks. So a natural question is left wide open: can we extend infinite-width theory to the Jacobian itself, and to training that deliberately regularises it?
