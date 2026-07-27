# The Game Design Workflow — as Flowcharts

Follow the arrows literally. Diamonds are decisions. Boxes name concrete artifacts.

## 1. The Master Router

```mermaid
flowchart TD
    IN["Any design ask"] --> DISC{"Run project<br/>discovery first?"}
    DISC -->|"new session"| DISCOV["Load GDD, context,<br/>code. Compare them.<br/>Deliver status report"]
    DISC -->|already loaded| ASK{"What shape is<br/>the ask?"}
    DISCOV --> ASK
    ASK -->|"New feature / system"| PILLARG["Pillar Gate"]
    ASK -->|"Analyze existing"| MDACHOICE{"MDA or<br/>Pillar Judge?"}
    ASK -->|"Full game design"| FULL["Full workflow<br/>Step 0→1→2→3→4→5→6→7"]
    ASK -->|"Review / audit"| JCHOICE{"Code audit,<br/>Design Judge, or<br/>both?"}
    ASK -->|"Design question"| PJ["Pillar Judge —<br/>deep trace through<br/>pillar network"]
    MDACHOICE -->|MDA| MDA["MDA analysis on<br/>feature or scenario"]
    MDACHOICE -->|Pillar Judge| PJ
    JCHOICE -->|Code audit| CODEAUDIT["Scan code vs GDD.<br/>Compare feature lists.<br/>Detect deltas"]
    JCHOICE -->|Design Judge| DJ["Full adversarial review:<br/>pillars, scope, pairs,<br/>tuning, GDD-code drift"]
    JCHOICE -->|Both| BOTH["Code audit first,<br/>then Design Judge"]
    PILLARG -->|pass| PAIRWISE["Pairwise matrix:<br/>new feature vs<br/>every existing"]
    PILLARG -->|fail| BLOCK["BLOCKED. Surface<br/>contradiction. Designer<br/>resolves or overrides"]
    PAIRWISE --> DOC["Document feature<br/>+ matrix + log<br/>to .design-context"]
```

## 2. The Pillar Gate

```mermaid
flowchart TD
    FEAT["Proposed feature"] --> PILLAR{"Serves a stated<br/>core pillar?"}
    PILLAR -->|"yes, which one?"| LOOPG{"Connects to or<br/>enhances core loop?"}
    PILLAR -->|"no"| CHAL1["CHALLENGE: 'Name the<br/>pillar or cut it. If it's<br/>a new pillar, log it in<br/>.design-context/pillars.md'"]
    LOOPG -->|"yes, how?"| SYSG{"Which existing<br/>systems does this<br/>touch?"}
    LOOPG -->|"no"| CHAL2["CHALLENGE: 'If this<br/>doesn't touch the loop,<br/>it's decoration. Log<br/>the reasoning.'"]
    SYSG -->|"list each"| SCOPE{"Complexity cost<br/>stated? Trade-off<br/>named?"}
    SYSG -->|"'none'"| CHAL3["CHALLENGE: 'Every<br/>feature touches<br/>something. Even UI<br/>and audio count.'"]
    SCOPE -->|"cost + trade-off"| CONTRAD{"Check all existing<br/>features + pillars:<br/>any contradiction or<br/>tension?"}
    SCOPE -->|"no trade-off"| CHAL4["CHALLENGE: 'What<br/>are we not doing<br/>because of this?'"]
    CONTRAD -->|"clean"| PASS["PASS. Log to<br/>.design-context/<br/>design-log.md"]
    CONTRAD -->|"conflict found"| BLOCK["BLOCKED. Surface<br/>contradiction. Designer<br/>resolves, or logs<br/>override to context"]
```

## 3. The Code Audit Flow

```mermaid
flowchart TD
    START["Run code audit"] --> SCANGDD["Extract feature list<br/>from GDD: F_gdd"]
    SCANGDD --> SCANCODE["Scan project source:<br/>extract F_code from<br/>classes, configs,<br/>state machines, assets"]
    SCANCODE --> COMPARE{"Compare sets"}
    COMPARE -->|"F_gdd ∩ F_code"| MATCH["Match each against<br/>GDD spec. Tuning<br/>drift? Behavior diff?"]
    COMPARE -->|"F_gdd \\ F_code"| UNIMPL["Documented but<br/>unimplemented.<br/>Flag as WIP or removed"]
    COMPARE -->|"F_code \\ F_gdd"| UNDOC["Implemented but<br/>undocumented.<br/>New features to<br/>add to GDD"]
    MATCH -->|"behavior matches"| OK["✅ Logged as match"]
    MATCH -->|"tuning differs"| DRIFT["⚠ Tuning drift.<br/>Code has different<br/>values than GDD"]
    MATCH -->|"behavior contradicts"| CONFLICT["❌ GDD-code conflict.<br/>Designer decides<br/>which is truth"]
    UNIMPL --> WIP{"Partially<br/>implemented?"}
    WIP -->|"skeleton/TODOs found"| PARTIAL["⚠ WIP feature.<br/>Document current state"]
    WIP -->|"no code exists"| GONE["❌ Not started or<br/>removed. Update GDD"]
    UNDOC --> ADD["Run through Pillar Gate<br/>→ add to GDD + matrix"]
    DRIFT --> RESOLVE{"Designer resolves:<br/>update GDD or<br/>update code?"}
    CONFLICT --> RESOLVE
    RESOLVE --> LOG["Log resolution to<br/>.design-context/<br/>design-log.md"]
```

## 4. MDA Analysis Flow

```mermaid
flowchart TD
    START["MDA analysis requested"] --> SCOPE{"Feature-level<br/>or scenario-level?"}
    SCOPE -->|"Feature"| FEATURE["Name the feature/mechanic"]
    SCOPE -->|"Scenario"| SCENARIO["Define: context +<br/>all features active<br/>in the scenario"]
    FEATURE --> MECH["MECHANICS: List rules,<br/>inputs, tuning values.<br/>What does the system do?"]
    SCENARIO --> MECH
    MECH --> DYN["DYNAMICS: What emerges<br/>when a player engages?<br/>Expected, unexpected,<br/>dominant strategy,<br/>skill ceiling, failure"]
    DYN --> AESTH["AESTHETICS: Map to<br/>8 aesthetic types.<br/>Which are evoked?<br/>Which are missing?"]
    AESTH --> PILLAR{"Aesthetics match<br/>the pillars?"}
    PILLAR -->|"yes"| REC["Tuning recommendations:<br/>strengthen weak aesthetics,<br/>reduce unwanted dynamics"]
    PILLAR -->|"no"| CHAL{"CHALLENGE: 'Pillars say<br/><experience>, MDA produces<br/><experience>. Gap found.'"}
    CHAL -->|"designer accepts gap"| OVERRIDE["Log to .design-context/<br/>tensions.md. Proceed<br/>with awareness"]
    CHAL -->|"designer wants to fix"| RETUNE["Adjust mechanics to<br/>shift aesthetic profile<br/>toward pillars"]
    RETUNE --> REC
    REC --> WRITE["Write full analysis to<br/>.design-context/<br/>mda-analyses/<feature>.md"]
```

## 5. The Pillar Judge

```mermaid
flowchart TD
    START["Pillar Judge: deep trace"] --> STATEMENT["Restate the feature/<br/>scenario/question.<br/>Verify understanding"]
    STATEMENT --> P1{"First pillar?"}
    P1 -->|"yes"| TRACE["TRACE: support /<br/>contradict / neutral /<br/>tension. Intensity 1-5"]
    TRACE --> P1
    P1 -->|"done all pillars"| TENSIONS{"Does this change<br/>any pillar-pillar<br/>tension?"}
    TENSIONS -->|"yes"| DELTA["Describe: previously<br/>A and B conflicted<br/>over X. Now: shifted<br/>in Y direction"]
    TENSIONS -->|"no"| TRADEOFF["TRADE-OFF STATEMENT:<br/>'This strengthens <X><br/>at cost of <Y>.<br/>Mitigations: <...>'"]
    DELTA --> TRADEOFF
    TRADEOFF --> CALL["DESIGNER CALL:<br/>Proceed / Modify / Reject.<br/>Override logs to<br/>.design-context/tensions.md"]
```

## 6. Project Discovery (Session Start)

```mermaid
flowchart TD
    START["New session start"] --> READGDD{"GDD exists?"}
    READGDD -->|"yes"| LOADGDD["Load GDD.<br/>Extract pillars,<br/>features, systems,<br/>tuning tables"]
    READGDD -->|"no"| NOPROMPT["Prompt: create<br/>Vision Lock first.<br/>No design work<br/>without pillars"]
    LOADGDD --> READCTX{".design-context/<br/>exists?"}
    READCTX -->|"yes"| LOADCTX["Load context:<br/>design-log, pillars.md,<br/>tensions, open-questions,<br/>recent reviews"]
    READCTX -->|"no"| PROMPTCTX["Offer to create<br/>.design-context/<br/>structure"]
    LOADCTX --> READCODE{"Project codebase<br/>accessible?"}
    READCODE -->|"yes"| AUDIT["Run code audit.<br/>Compare GDD vs code.<br/>Report deltas"]
    READCODE -->|"no"| SKIPAUDIT["Skip code audit.<br/>Work from GDD +<br/>context only"]
    AUDIT --> STATUS["DELIVER STATUS:<br/>Pillars, GDD health,<br/>code alignment,<br/>open questions"]
    SKIPAUDIT --> STATUS
    PROMPTCTX --> READCODE
```

## Reading these as a designer

Follow the arrows literally. When a box says CHALLENGE or BLOCKED, the agent must deliver that challenge — not soften it, not proceed silently. When a box says "log to .design-context/", the log entry must be written before proceeding to the next step.
