# Motivation

Core claim: Real auctions carry public contextual features on bidders and items and vary in size from round to round, so a practical designer must ingest features and accept a changing number of bidders and items.

Supporting detail: Prior neural designers (RegretNet, EquivariantNet) either fix the auction scale or ignore bidder/item identity, so they cannot exploit context or find the asymmetric mechanisms that context demands.

Narration: Real auctions are richer. In e-commerce advertising, many bidders compete for many ad slots described by features, and every round has a different number of participants. We need an architecture that absorbs context and handles varying auction sizes.
