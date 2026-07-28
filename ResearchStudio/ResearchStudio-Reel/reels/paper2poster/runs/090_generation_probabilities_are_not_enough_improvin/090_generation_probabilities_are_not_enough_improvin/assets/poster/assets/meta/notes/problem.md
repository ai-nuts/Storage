# Problem

Core claim: AI code-completion models produce erroneous suggestions that can inject bugs, and users, prone to automation bias, must first detect those errors, yet it is unclear how to surface uncertainty in generative output where each suggestion holds hundreds of token-level decisions.

Supporting detail: Prior uncertainty and explanation work targets single-decision support (one classification or diagnosis) and does not translate cleanly to token-by-token generative scenarios.

Narration: AI code assistants are now everywhere, but they are imperfect, and a wrong suggestion can quietly plant a bug or a security hole. To catch those mistakes, a programmer first has to notice them, and that is hard, because people tend to over-trust automation. The tricky part is that a single code suggestion is not one decision but hundreds of tiny ones, one per token. Earlier research on communicating AI uncertainty was built for single-shot decisions like a diagnosis, and it does not obviously carry over to this token-by-token world.
