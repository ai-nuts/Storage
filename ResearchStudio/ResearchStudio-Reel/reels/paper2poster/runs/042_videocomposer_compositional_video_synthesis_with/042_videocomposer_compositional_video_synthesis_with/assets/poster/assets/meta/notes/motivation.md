# Motivation

Core claim: To give users explicit control over motion, the paper introduces motion vectors from compressed video as a temporal condition, providing direct guidance on temporal dynamics that other conditions lack.

Supporting detail: Feeding many heterogeneous conditions naively breaks cross-frame consistency, motivating a single encoder that captures space-time relations across all sequential inputs.

Narration: To control a video, you must control its motion, not only its appearance. The authors' insight: motion vectors, computed inside compressed video to encode inter-frame change, are a cheap, explicit description of temporal dynamics. Turning them into a control signal lets users prescribe how things move. But mixing them with sketches, depth, and images naively hurts consistency, motivating a unified encoder for space and time.
