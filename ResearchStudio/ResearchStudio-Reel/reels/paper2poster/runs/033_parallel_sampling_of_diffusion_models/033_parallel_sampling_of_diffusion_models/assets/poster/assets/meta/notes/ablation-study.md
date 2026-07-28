# Ablation Study

Core claim: Lowering the convergence tolerance trades speed for fidelity; a relaxed tolerance still preserves quality while a tolerance that is too high starts to degrade samples, confirming the tolerance as the key speed-quality knob.

Supporting detail: On LSUN Church, ParaDDPM matches DDPM FID (12.8 vs 12.9) at 3.9x speedup, while 500-step DDIM alone gives a noticeably worse FID, showing the speedup does not come from simply cutting steps.

Narration: The main ablation studies the effect of the error tolerance in the fixed-point iteration. A lower tolerance means more iterations and slower sampling but higher fidelity, while a looser tolerance is faster. The paper shows there is a comfortable regime where a fairly relaxed tolerance still preserves sample quality. Importantly, on LSUN Church, ParaDDPM matches full DDPM's FID score at nearly four times the speed, whereas simply reducing DDIM to 500 steps produces visibly worse images, demonstrating that the gains genuinely come from parallelism rather than fewer steps.
