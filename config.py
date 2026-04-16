# Cells: EHJdFwWrZBWa, CMshlQIJOpAR, Eqw_Dv4zPhvW, GNOlJtEDfq1U
from dataclasses import dataclass, field
from pathlib import Path

@dataclass(frozen=True)
class MoexConfig:
    base_url: str = "https://iss.moex.com/iss"
    board: str = "RFUD"
    retry: int = 3

@dataclass
class PipelineConfig:
    moex: MoexConfig = field(default_factory=MoexConfig)
    out_dir: Path = field(default_factory=lambda: Path("/content/si_vol_analytics"))