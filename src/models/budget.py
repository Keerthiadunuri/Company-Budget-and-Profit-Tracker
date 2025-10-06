

from dataclasses import dataclass

@dataclass
class Budget:
    budget_id: int | None = None
    cust_id: int | None = None         # <-- Add this field
    category: str | None = None
    planned_amount: float | None = None
    actual_amount: float | None = None
    start_date: str | None = None
    end_date: str | None = None
