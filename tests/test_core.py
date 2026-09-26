import tempfile, unittest
from pathlib import Path
from soul_key.protocol import *
from soul_key.channels import *
from soul_key.scoring import *
from soul_key.ledger import append, validate

class Tests(unittest.TestCase):
 def test_commit_reveal(self):
  c=label_commitment("1","present","n")
  self.assertTrue(verify_reveal("1","present","n",c))
  self.assertFalse(verify_reveal("1","empty","n",c))
 def test_balanced_schedule(self):
  s=blinded_schedule(4,7)
  self.assertEqual({x:s.count(x) for x in LABELS},{x:4 for x in LABELS})
 def test_fingerprint_order(self):
  self.assertEqual(fingerprint_features({"b":2,"a":1}),fingerprint_features({"a":1,"b":2}))
 def test_scoring(self):
  p=Prediction("1",{"present":1,"other":0,"empty":0},"x","v1")
  self.assertEqual(score([(p,"present")])["accuracy"],1)
  self.assertGreater(uniform_baseline_brier(),0)
 def test_ablation(self):
  q=Channel("qrng","quantum_rng","documented random source")
  face=Channel("face","conventional","camera identity")
  self.assertTrue(DEFAULT_LADDER[-1].permits(q))
  self.assertFalse(DEFAULT_LADDER[-1].permits(face))
 def test_ledger_tamper(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"l.jsonl"; append(p,{"x":1}); append(p,{"x":2})
   self.assertTrue(validate(p))
   p.write_text(p.read_text().replace('"x":1','"x":9'))
   self.assertFalse(validate(p))

if __name__=="__main__": unittest.main()
