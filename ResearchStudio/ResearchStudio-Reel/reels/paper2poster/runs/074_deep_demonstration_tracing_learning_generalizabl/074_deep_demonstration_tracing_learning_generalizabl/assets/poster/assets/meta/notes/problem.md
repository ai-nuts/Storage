# Problem

Core claim: One-shot imitation learning (OSIL) trains an agent to perform a task from a single demonstration, but existing methods assume the deployment environment closely resembles demonstration collection and break down when unforeseen changes occur.

Supporting detail: After a demonstration is collected, unexpected obstacles, disturbances, or pedestrians can push the agent into states never shown, where naive replay of demonstrated actions fails.

Narration: One-shot imitation learning asks an agent to carry out a task after seeing just a single demonstration. It works well when deployment looks like the demonstration, but the real world is dynamic. After the demonstration is provided, an unexpected obstacle can appear, or a grasped object can slip, pushing the agent into situations the demonstration never covered. Traditional one-shot imitation methods excel in stationary settings, yet their ability to handle these unforeseen changes is limited and rarely studied. This paper focuses squarely on that gap: making one-shot imitation robust when the environment changes at runtime.
