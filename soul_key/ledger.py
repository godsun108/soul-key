from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

GENESIS="0"*64

def canonical(x: object)->str:
    return json.dumps(x,sort_keys=True,separators=(",",":"))

def append(path: str|Path, payload: dict[str,Any])->dict[str,Any]:
    path=Path(path); previous=GENESIS
    if path.exists() and path.stat().st_size:
        previous=json.loads(path.read_text().splitlines()[-1])["record_hash"]
    body={"previous_hash":previous,"payload":payload}
    record_hash=sha256(canonical(body).encode()).hexdigest()
    record={**body,"record_hash":record_hash}
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("a") as f: f.write(canonical(record)+"\n")
    return record

def validate(path: str|Path)->bool:
    path=Path(path); previous=GENESIS
    if not path.exists(): return True
    for line in path.read_text().splitlines():
        r=json.loads(line)
        body={"previous_hash":r.get("previous_hash"),"payload":r.get("payload")}
        expected=sha256(canonical(body).encode()).hexdigest()
        if r.get("previous_hash")!=previous or r.get("record_hash")!=expected: return False
        previous=expected
    return True
