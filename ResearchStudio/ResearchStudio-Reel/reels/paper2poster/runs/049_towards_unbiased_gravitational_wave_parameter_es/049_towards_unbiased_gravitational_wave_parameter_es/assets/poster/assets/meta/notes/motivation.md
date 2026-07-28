# Motivation

Core claim: As detector catalogs grow, even small departures from the Gaussian assumption accumulate into systematic biases, so a likelihood that handles real noise without special-casing each artifact is increasingly essential.

Supporting detail: Next-generation observatories such as Cosmic Explorer and the Einstein Telescope will produce far more events, making a scalable, assumption-free noise model a foundational requirement.

Narration: Why now? Gravitational-wave astronomy is scaling fast, and analyzing large catalogs makes the pipeline sensitive to tiny departures from Gaussian noise that quietly accumulate into bias. The authors wanted to keep the trusted deterministic waveform models while dropping the unrealistic noise assumption, and to prepare for next-generation detectors like Cosmic Explorer and the Einstein Telescope.
