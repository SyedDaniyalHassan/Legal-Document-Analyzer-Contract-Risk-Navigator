from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class State:
    text: str = ""
    clauses: Dict[str, Any] = field(default_factory=dict)
    overall_risk: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    json_report: Optional[str] = None
    pdf_report: Any = None 