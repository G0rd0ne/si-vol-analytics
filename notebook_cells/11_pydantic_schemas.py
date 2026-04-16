# Cell 11: Pydantic Schemas
from pydantic import BaseModel, Field
from typing import Dict, Any

class SiVolatilityReport(BaseModel):
    meta: Dict[str, Any]
    contracts: Dict[str, Any]