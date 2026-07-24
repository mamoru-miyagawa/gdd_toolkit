# Balance & Tuning Table Template

Numbers in a GDD are **placeholders** — they will change during balancing. What matters is the **relationship** between values and the **intent** behind them.

Use this template to capture that intent. Hard numbers are optional; relative ordering and rough magnitude are essential.

---

## System: <name>

### Intent

Describe what this system is supposed to feel like. This is the most important part — numbers will change but the intent shouldn't:

```
The pistol is the baseline: fast, reliable, low damage per shot.
The rifle is slower but hits harder — about 2x the pistol's damage.
The shotgun is devastating up close (3-4x pistol) but useless at range.
```

### Relative Power Ranking

How things compare to each other, without hard numbers:

| Weapon | Damage (relative) | Speed (relative) | Range | Role |
|---|---|---|---|---|
| Pistol | 1x (baseline) | Fastest | Medium | Default, reliable |
| Rifle | 2x pistol | Slower than pistol | Long | Precision, pick off targets |
| Shotgun | 3-4x pistol | Slowest | Short | Burst damage, close quarters |

### Optional: Hard Numbers (Placeholders)

Fill these in if you have them, but **don't treat them as truth**. They will change.

| Variable | Rough Value | Notes |
|---|---|---|
| Pistol damage | ~10 per hit | Tune to feel good against basic enemies |
| Rifle damage | ~20 per hit | Should 2-shot basic enemies |
| Shotgun damage | ~35 (7 pellets × 5) | Point-blank should feel devastating |
| TTK (time to kill) | ~1.5s vs basic enemy | Target for all weapons |

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
