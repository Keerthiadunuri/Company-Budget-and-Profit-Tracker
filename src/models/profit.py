from dataclasses import dataclass

@dataclass
class Profit:
    profit_id: int | None = None
    cust_id: int | None = None
    period: str | None = None  # e.g., "2025-09"
    amount: float | None = None
    created_at: str | None = None
