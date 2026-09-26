from __future__ import annotations
from dataclasses import dataclass
from hashlib import sha256
import json
import random
from typing import Mapping, Sequence

LABELS = ("present", "other", "empty")

def _canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))

def digest(value: object) -> str:
    return sha256(_canonical(value).encode()).hexdigest()

def blinded_schedule(n_each: int, seed: int) -> list[str]:
    if n_each < 1: raise ValueError("n_each must be positive")
    labels = [x for x in LABELS for _ in range(n_each)]
    random.Random(seed).shuffle(labels)
    return labels

def label_commitment(trial_id: str, label: str, nonce: str) -> str:
    if label not in LABELS: raise ValueError("invalid label")
    return digest({"trial_id": trial_id, "label": label, "nonce": nonce})

def verify_reveal(trial_id: str, label: str, nonce: str, commitment: str) -> bool:
    return label_commitment(trial_id, label, nonce) == commitment

def fingerprint_features(features: Mapping[str, float]) -> str:
    return digest({k: float(features[k]) for k in sorted(features)})

@dataclass(frozen=True)
class Prediction:
    trial_id: str
    probabilities: Mapping[str, float]
    feature_fingerprint: str
    model_version: str

    def validate(self) -> None:
        if set(self.probabilities) != set(LABELS): raise ValueError("exactly three labels required")
        values=[float(self.probabilities[x]) for x in LABELS]
        if any(x < 0 or x > 1 for x in values) or abs(sum(values)-1)>1e-9:
            raise ValueError("invalid probabilities")
        if not self.feature_fingerprint or not self.model_version:
            raise ValueError("fingerprint and model version required")
