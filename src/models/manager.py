from dataclasses import dataclass
from typing import Optional

@dataclass
class Manager:
    manager_id: Optional[int] = None
    name: str = ""
    email: str = ""
    phone: Optional[str] = None
