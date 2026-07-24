# Design Failure Modes: symptom → gate

Nine ways game design documentation goes wrong, what each looks like, and which gate or step catches it.

| # | Failure Mode | Symptom | Caught By |
|---|---|---|---|
| 1 | **Pillar drift** | Feature exists that doesn't trace to any pillar. The GDD becomes a wishlist. | Pillar Gate — every feature must name its pillar. |
| 2 | **Silent scope creep** | The feature count grew since the last review with no explicit approval. Nobody noticed until the timeline slipped. | Design Judge scope diff — compare against last checkpoint. |
| 3 | **Loop orphan** | A mechanic that doesn't connect to the core loop. Player progression that doesn't feed back into moment-to-moment gameplay. | Design Judge loop audit — every mechanic must map to a core loop phase. |
| 4 | **Tuning theater** | "Enemies get harder over time." "Resources become scarce." No numbers, no curves, no tuning ranges. The team builds blind. | Design Judge tuning check — prose without tables is flagged. |
| 5 | **System isolation** | A system documented in isolation with no interaction list. The crafting system that doesn't reference the economy, or the combat system that ignores movement. | Pillar Gate System Check — "None" is not a valid interaction list. |
| 6 | **Fun claimed without proof** | "This will be fun" as the sole justification for a mechanic. No observable, testable criteria. | Design Judge fun check — "fun" must resolve to a specific player behavior or reaction. |
| 7 | **Audience mismatch** | Core mechanics designed for a different audience than defined. A reflex-based twitch mechanic in a game defined for casual players. | Design Judge audience check — every major mechanic checked against the audience definition. |
| 8 | **Feature costume** | Complexity masquerading as depth. 12 weapon types with no meaningful difference between them. A skill tree where every node is a +5% stat bonus. | Design Judge — an interaction count that exceeds the player's ability to make informed decisions is complexity, not depth. |
| 9 | **Unchecked pairwise gap** | Two mechanics exist that can interact, and the interaction is undocumented. The designer assumes it "obviously" works. QA finds it doesn't. | Pairwise Interaction Matrix — every pair must have a STATUS. |
| 10 | **Matrix rot** | The pairwise matrix exists but hasn't been updated since new features were added. Old pairs reference features that changed. | Design Judge pairwise scan — diff the matrix against current feature list. |
| 11 | **Scope budget denial** | "Everything is essential." No feature is ever removed or deferred. The budget was set but never enforced. | Scope Budget — when budget reaches 0, new features require removal of equal cost. No exceptions. |
| 12 | **GDD fossilization** | The GDD was written once at the start and never updated. The game has drifted but the document hasn't. | Design Judge — a GDD that hasn't been modified since the last production milestone is a fossil, not a design tool. |
| 13 | **Prototype gap** | A core loop described in prose that has never been prototyped or playtested. The team commits to production based on a theoretical loop. | Step 1 — Core Loop must be verified (prototype, paper test, or equivalent) before features are designed. |
| 14 | **False consensus** | All features pass the Pillar Gate because the pillars are too vague. "Fun." "Engaging." "Immersive." These filter nothing. | Vision Lock — pillars must be specific, observable, and contradictable. A pillar that can't be violated is not a pillar. |
| 15 | **Design by meme** | "It's like Dark Souls meets Stardew Valley." The comparison replaces design thinking. Every feature is borrowed from the reference, none is owned. | Pillar Gate — comparisons identify the audience, not the features. Every feature still needs its own pillar trace. |
| 16 | **GDD-code drift** | The GDD says one thing, the code does another. A documented spec that the code silently contradicts. Designers argue from the GDD, engineers work from the code. | Code Audit — compare feature lists, tuning values, and behavior descriptions. Surface every delta. |
| 17 | **Silent removal** | A feature was cut from the code but still lives in the GDD. Future designers assume it exists. | Code Audit — `F_gdd \ F_code` shows documented-but-unimplemented features. |
| 18 | **Undocumented feature** | A feature was added to the code but never entered the GDD. Future designers don't know it exists. | Code Audit — `F_code \ F_gdd` shows implemented-but-undocumented features. Run through Pillar Gate + Pairwise Matrix. |
| 19 | **MDA mismatch** | The designer thinks the game evokes Challenge (deep tactics) but the mechanics actually produce Submission (grinding, repetition). | MDA Analysis — predict the aesthetic profile before building. Verify it in playtest. If the profile doesn't match pillars, change mechanics. |
| 20 | **Pillar-pillar denial** | Two pillars are in active tension but the designer pretends they aren't. Both are treated as absolute, with no trade-off acknowledged. Tension builds until one pillar silently dominates and the game drifts. | Pillar Judge — explicitly trace every pillar-pillar tension. Log to tensions.md. A tension that isn't named will be resolved by accident. |

## Reading these as a designer

The most expensive failures in practice are **system isolation** (5) — because it's discovered in integration testing months later — and **unchecked pairwise gaps** (9) — because it creates bugs that feel like edge cases but are actually design omissions. If an audit can only check two things, check those.
