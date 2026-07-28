# Motivation

Core claim: Humans imitating a route can detour around an unexpected obstacle and then rejoin the original path; agents need this same adaptive tracing ability rather than blind replay.

Supporting detail: Prior OSIL work embeds a demonstration as a free context vector and clones actions, offering no guarantee of sensible behavior in unseen states.

Narration: Consider a person following a demonstrated route from a start point to a destination. Partway there, a truck is parked where the demonstration had none. A human simply detours around it and then rejoins the original path at a convenient point. This is easy for people but hard for current one-shot imitation techniques, which mostly clone demonstrated actions and have no principled way to behave in states the demonstration never showed. The authors distill this human behavior into a three-stage decision process — identify which demonstrated states are relevant, analyze how the expert behaved there, and trace back onto the demonstration — and use it as the blueprint for their method.
