# Cell: 45178ceb
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class SiVolatilityReport(BaseModel):
    meta: Dict[str, Any]