# Takeaway

Core claim: Framing tensor rematerialization as a constraint program over retention intervals cuts the discrete-variable count from quadratic to linear, letting Moccasin solve much larger neural-network compute graphs up to 10× faster while keeping the runtime overhead under 5%.

Supporting detail: The formulation is hardware-agnostic: once solved, the resulting execution sequence can run on any CPU or GPU.

Narration: The lasting takeaway is that the right problem formulation changes what is tractable. By expressing rematerialization decisions as a small set of retention intervals in a constraint program, Moccasin reduces the number of discrete variables from quadratic to linear in the graph size. That single change lets it scale to compute graphs far larger than prior methods could handle, solving them up to ten times faster while keeping the added runtime overhead under five percent. And because the output is just an execution sequence, the resulting schedule can run on any CPU or GPU.
