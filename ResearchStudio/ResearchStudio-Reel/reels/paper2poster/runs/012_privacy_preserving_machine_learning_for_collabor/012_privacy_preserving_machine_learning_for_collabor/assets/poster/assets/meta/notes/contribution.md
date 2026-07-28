# Contribution

Core claim: The paper proposes a framework that uses autoencoders to create privacy-preserving latent embeddings peers can share and join to train a collaborative downstream model without losing predictive power.

Supporting detail: It further defines and evaluates five scenarios, including non-naive multitask autoencoders, across three public benchmarks to demonstrate applicability.

Narration: The paper makes three main contributions. First, it reviews existing privacy-preserving machine learning approaches to expose their limitations and the room for improvement. Second, it proposes a concrete framework in which each peer trains an autoencoder, shares only the latent-space representation of its data, and then joins these embeddings to train a shared supervised model. Third, it validates the framework on three public datasets spanning regression and classification, and across five experimental scenarios, ranging from a raw-data baseline to non-naive multitask autoencoders that also predict the target variable during encoding.
