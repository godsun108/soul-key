from __future__ import annotations
from dataclasses import dataclass

KINDS=("conventional","physiological","environmental","experimental","quantum_rng")

@dataclass(frozen=True)
class Channel:
    name: str
    kind: str
    description: str

    def validate(self) -> None:
        if self.kind not in KINDS: raise ValueError("unknown channel kind")
        if not self.name or not self.description: raise ValueError("channel metadata required")

@dataclass(frozen=True)
class AblationStage:
    name: str
    allowed_kinds: tuple[str,...]
    forbidden_names: tuple[str,...]=()

    def permits(self, channel: Channel) -> bool:
        channel.validate()
        return channel.kind in self.allowed_kinds and channel.name not in self.forbidden_names

DEFAULT_LADDER=(
    AblationStage("all_declared", KINDS),
    AblationStage("no_direct_identity", KINDS, ("face","voice","device_id","network_id")),
    AblationStage("physical_only", ("physiological","environmental","experimental","quantum_rng")),
    AblationStage("experimental_only", ("experimental","quantum_rng")),
    AblationStage("qrng_only", ("quantum_rng",)),
)
