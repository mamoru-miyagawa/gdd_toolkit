# Balance & Tuning Table Template

Prose-only tuning ("enemies get harder") is not accepted. Every tunable value resolves to a table with ranges, defaults, and the curve that governs it.

---

## System: <name>

### Stat Block

| Variable | Min | Max | Default | Unit | Scaling |
|---|---|---|---|---|---|
| <name> | <value> | <value> | <value> | <seconds, HP, %, etc.> | <none / linear / exponential / custom> |
| <name> | <value> | <value> | <value> | <seconds, HP, %, etc.> | <none / linear / exponential / custom> |

### Scaling Curve

```yaml
variable: <name>
formula: |
  result = base * (multiplier ^ (level - 1))
example:
  level 1: <value>
  level 5: <value>
  level 10: <value>
  level 20: <value>
graph: <optional reference to a plot or tool>
```

### Balance Goals

| Goal | Target | Measurement |
|---|---|---|
| Time-to-kill at level parity | <N seconds> | Playtest timer |
| Resource economy surplus/deficit | <ratio> | Income / spend per session |
| Downtime between actions | <N seconds max> | Time without meaningful input |
| Difficulty curve slope | <rate of increase> | HP / damage per level |

### Known Dependencies

If this table changes, these other tables must be updated:

| Dependency | Relationship |
|---|---|
| <system>.<variable> | <if X goes up, this Y goes down> |
| <system>.<variable> | <this value is calculated FROM that value> |

---

## Tuning Sheet (per enemy / item / weapon)

| ID | Name | Stat1 | Stat2 | Stat3 | Special |
|---|---|---|---|---|---|
| ENEMY_001 | Grunt | 10 HP | 5 ATK | 1 SPD | No special |
| ENEMY_002 | Soldier | 25 HP | 8 ATK | 1.5 SPD | Drops shield on death |
| ENEMY_003 | Elite | 50 HP | 15 ATK | 1 SPD | Phase shift at 50% HP |
| ... | ... | ... | ... | ... | ... |

### Curve Visualization (text approximation)

```
Damage Scaling
Level:  1   2   3   4   5   6   7   8   9   10
Value:  10  12  14  17  20  24  29  35  42  50
        ■   ■   ■   ■   ■   ■   ■   ■   ■   ■
                  (exponential curve: base * 1.15^(level-1))
```

---

## Verification

**How will we verify these numbers are correct?**
- <Playtest with target audience>
- <Automated simulation (N simulated fights, check time-to-kill distribution)>
- <Compare against balance goals table above>

**What would tell us a number is wrong?**
- <Player never uses a weapon = it's underpowered>
- <Every player uses the same strategy = dominant strategy, need to rebalance>
- <Players avoid combat = time-to-kill too punishing>
- <Resource never depletes = sink too weak, economy broken>
