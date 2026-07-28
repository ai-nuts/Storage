# Motivation

Core claim: Prior finite-rank analyses either rely on asymptotic, high-dimensional limits, hold only for specific ridge schedules, or bound only the expected error, none of which certify a given finite-sample KRR run.

Supporting detail: Because deep transfer learning freezes early layers and retrains only the head, the induced kernel is genuinely finite-rank, so a non-asymptotic theory tailored to this regime is needed.

Narration: Freezing a pre-trained backbone and retraining only the final layer is everywhere, and it defines a finite-rank kernel. Yet the theory lags: many results need the input dimension to grow, others fix how the ridge decays, and almost none give a lower bound, without which tightness cannot be claimed.
