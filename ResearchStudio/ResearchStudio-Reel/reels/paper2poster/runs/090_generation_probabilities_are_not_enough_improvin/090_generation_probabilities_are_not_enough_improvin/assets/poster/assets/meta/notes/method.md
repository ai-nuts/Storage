# Method

Core claim: All three tools use the same OpenAI Davinci-002 Codex model and differ only in how completions are presented. The Generation-probability tool highlights the most uncertain tokens (probability threshold 71%) as output by Codex; the Edit-model tool highlights tokens most likely to be edited (threshold 66%) according to a learned edit model; the Prediction-only tool shows the raw completion with no highlights.

Supporting detail: The edit model was trained on data from nine coders in a preliminary phase who edited Codex output until each task was solved correctly. Highlighting thresholds were tuned so the total number of highlights shown across all three tasks was equal in every condition.

Narration: Under the hood, all three tools used the very same Codex model, so any difference in behavior comes purely from how the completion was displayed. The generation-probability tool highlighted tokens the model was least confident in, at a seventy-one percent threshold. The edit-model tool highlighted tokens most likely to be edited, at a sixty-six percent threshold, using a model trained on nine coders who had previously edited Codex output until their tasks passed. Crucially, the thresholds were chosen so that every condition showed the same total number of highlights, so the comparison is about which tokens get highlighted, not how many.
