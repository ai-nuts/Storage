# Contribution

Core claim: RetoMaton builds an unsupervised weighted finite automaton over any datastore by (1) saving a pointer from each entry to its successor in the text and (2) clustering entries with close keys into automaton states that share pointers.

Supporting detail: Traversed in parallel with LM inference, the automaton approximates the next nearest neighbors so most searches are skipped; it needs no training data and can be built from the training corpus or a new domain.

Narration: RetoMaton makes two changes to the datastore. First, it saves a pointer from every entry to the entry that came right after it in the text. Second, it clusters entries with similar key vectors into states, and those states share their outgoing pointers. Together these turn the flat datastore into a weighted finite automaton. Building it is completely unsupervised, requires no extra training data, and works whether the automaton is constructed from the model's own training corpus or from a brand-new domain.
