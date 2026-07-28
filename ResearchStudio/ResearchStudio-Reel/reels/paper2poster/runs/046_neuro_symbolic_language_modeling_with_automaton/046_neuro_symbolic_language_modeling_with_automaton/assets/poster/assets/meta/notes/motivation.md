# Motivation

Core claim: kNN-LM treats the datastore as a flat list and searches it token by token, ignoring that consecutive retrieved entries are highly correlated in time and that nearby keys behave alike.

Supporting detail: Prior retrieval-saving work (AdaptRet) trains an MLP to skip searches, but when it skips it backs off to the base LM alone, losing the retrieval signal exactly when it helps most.

Narration: The key observation is that a flat datastore throws away structure. If a retrieved entry was useful now, the entry that follows it in the original text is very likely useful next. And entries whose key vectors are close tend to be followed by the same token. Existing approaches like Adaptive Retrieval simply learn when to skip the search, but when they skip they fall back entirely on the base language model and discard the retrieval distribution, which hurts most in domains where the base model is weak.
