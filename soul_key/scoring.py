from __future__ import annotations
from .protocol import LABELS, Prediction

def multiclass_brier(p: Prediction, truth: str) -> float:
    p.validate()
    if truth not in LABELS: raise ValueError("invalid truth")
    return sum((float(p.probabilities[x])-(1.0 if x==truth else 0.0))**2 for x in LABELS)/len(LABELS)

def score(rows: list[tuple[Prediction,str]]) -> dict[str,float]:
    if not rows: raise ValueError("no trials")
    b=[multiclass_brier(p,t) for p,t in rows]
    correct=sum(max(LABELS,key=lambda x:p.probabilities[x])==t for p,t in rows)
    return {"trials":float(len(rows)),"brier":sum(b)/len(b),"accuracy":correct/len(rows)}

def uniform_baseline_brier() -> float:
    probs={x:1/3 for x in LABELS}
    p=Prediction("baseline",probs,"baseline","uniform")
    return multiclass_brier(p,"present")
