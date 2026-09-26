"""Synthetic plumbing test only — deliberately contains a signal."""
from soul_key.protocol import Prediction, fingerprint_features
from soul_key.scoring import score, uniform_baseline_brier

rows=[]
examples=[
 ("present",{"a":.9},{"present":.8,"other":.1,"empty":.1}),
 ("other",{"a":.5},{"present":.1,"other":.8,"empty":.1}),
 ("empty",{"a":.1},{"present":.1,"other":.1,"empty":.8}),
]
for i,(truth,features,probs) in enumerate(examples):
    p=Prediction(str(i),probs,fingerprint_features(features),"synthetic-v1")
    rows.append((p,truth))
print("SYNTHETIC PIPELINE TEST — NOT REAL EVIDENCE")
print(score(rows))
print("uniform baseline brier:",uniform_baseline_brier())
