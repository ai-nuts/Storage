# Motivation

Core claim: A subtractive mixture that can cancel mass models complex distributions with far fewer components, but naively negative mixture weights can make the function negative and no longer a valid distribution.

Supporting detail: Prior fixes (energy-based exponentiation) lose tractable normalization; several disconnected communities reinvented squaring-style tricks without a unified, tractable treatment.

Narration: So why revisit this now? Because subtraction pays off: a mixture that can cancel mass captures complex shapes with far fewer components. The problem is guaranteeing the result stays non-negative. Energy-based models enforce non-negativity by exponentiation, but then lose tractable normalization. Meanwhile several separate communities, from signal processing to kernel methods to quantum mechanics, each rediscovered a squaring trick to enforce non-negativity, but without a common, tractable framework tying them together.
