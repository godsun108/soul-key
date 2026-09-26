# Experiment 001 — Presence Ablation Ladder

Status: **FROZEN SCAFFOLD / NO REAL RESULTS**

## Question

Can a frozen classifier distinguish the enrolled participant's presence from another participant and an empty condition, prospectively?

## Conditions

PRESENT, OTHER, EMPTY. The prediction process must not receive the condition before its prediction is committed.

## Primary score

Multiclass Brier score. Secondary: accuracy. Uniform 1/3 probabilities are the primary chance baseline.

## Ablation ladder

The experiment starts permissively and removes channels in later, separately scored stages:

1. all declared channels;
2. remove direct identity channels (face, voice, device/network identity);
3. physical channels without direct identity;
4. experimental channels only;
5. documented QRNG only.

Stages are not silently skipped. A failed stage is retained as a result.

## Information firewall

Each sensor is declared before scored collection as conventional, physiological, environmental, experimental, or quantum_rng. QRNG means a documented quantum randomness source; it does **not** mean the source measures consciousness.

Training/test separation, preprocessing, model version, trial eligibility, and promotion thresholds must be frozen before real scored trials.

## Interpretation firewall

Classifier performance is not evidence of a soul by itself. Before extraordinary interpretation, ordinary leakage, experimenter cues, environmental confounds, multiple testing, sensor artifacts, and chance must be excluded, followed by prospective and independent replication.

## Wallet firewall

No stage of Experiment 001 can sign, approve, unlock, or transfer financial assets.
