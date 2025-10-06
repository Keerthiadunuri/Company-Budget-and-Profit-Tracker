from dataclasses import dataclass
from typing import Optional

@dataclass
class Simulation:
    simulation_id: Optional[int] = None
    cust_id: int = 0
    scenario: str = ""
    projected_amount: float = 0.0
    created_at: Optional[str] = None
