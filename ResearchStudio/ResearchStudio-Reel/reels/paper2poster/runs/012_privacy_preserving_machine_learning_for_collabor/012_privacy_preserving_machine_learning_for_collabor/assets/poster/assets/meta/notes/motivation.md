# Motivation

Core claim: Existing privacy tools fall short: encryption is heavy to deploy, federated learning assumes peers share the same features, and differential privacy or linear dimensionality reduction distort or degrade the data.

Supporting detail: These methods mainly protect data in transit, alter individual observation patterns, or carry high maintenance requirements, leaving room for a representation-learning solution.

Narration: Academia and industry have built several privacy-preserving strategies, but each has limits. Encryption approaches like homomorphic encryption offer strong security yet are hard to deploy in real settings because of their technology requirements. Federated learning decentralizes training across devices, but it assumes every peer holds the same kind of information, so it cannot handle two peers that contribute different features. Differential privacy masks individual values by adding noise, which can significantly reduce data utility. Linear dimensionality reduction such as Principal Component Analysis obfuscates features but may lose important nonlinear relationships. These gaps motivate a new approach that uses deep representation learning to encode data while keeping its predictive structure intact.
