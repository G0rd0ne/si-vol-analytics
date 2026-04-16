# Cell 1/5: Imports, Config, Utils
from __future__ import annotations
import json, logging, math, time, uuid, warnings
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Optional
import numpy as np, pandas as pd, requests

SCHEMA_VERSION = '2.6.0'
ENGINE_VERSION = 'dual_vol_engine_0.6.0'

def setup_logging(level='INFO'):
    logging.basicConfig(level=getattr(logging, level.upper()), format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s')
    return logging.getLogger('si_vol_pipeline')

log = setup_logging()

@dataclass(frozen=True)
class MoexConfig:
    base_url: str = 'https://iss.moex.com/iss'
    board: str = 'RFUD'
    retry: int = 3
    timeout: int = 30

@dataclass
class PipelineConfig:
    moex: MoexConfig = field(default_factory=MoexConfig)
    out_dir: Path = field(default_factory=lambda: Path('/content/si_vol_analytics'))
