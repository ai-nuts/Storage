# Problem

Core claim: Street-view geo-localization models are black boxes that predict a location without any reasoning, and the street-view datasets used to train them are polluted with low-quality images that carry no visual clues.

Supporting detail: Retrieval-based methods depend on hard-to-curate geo-tagged galleries; classification-based methods ignore semantic cues like signboard text and cannot explain their predictions.

Narration: Predicting where a street-view photo was taken is useful for urban planning, navigation, and social studies. But today's approaches have two blind spots. First, the data problem: street-view datasets are stuffed with images captured in tunnels, against blank walls, or of generic vegetation, none of which contain clues a model could use to locate them. Second, the reasoning problem: retrieval and classification models operate as black boxes, handing back a coordinate with no explanation a person could inspect or trust. This paper argues that both quality and interpretability must be fixed together.
