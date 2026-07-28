# Problem

Core claim: Organizations want to jointly train ML models on complementary data, but privacy policies and IP laws block sharing the raw sensitive features that would improve predictions.

Supporting detail: Two peers holding different variables for the same users cannot merge datasets, so the collaboration, and the accuracy gain it promises, is cancelled.

Narration: A common real-world situation is two companies that each hold a different set of variables about the same group of users. If they could combine their features, both could predict a shared target variable far more accurately and make better decisions. But the data is sensitive, so privacy policies and intellectual property laws forbid handing over the raw features, even when the communication channel between them is secure. The collaboration is cancelled, and the potential boost in model performance is lost. The core problem this paper tackles is how to let such peers share their information, and keep the predictive power of the original features, without ever exposing the raw sensitive data.
