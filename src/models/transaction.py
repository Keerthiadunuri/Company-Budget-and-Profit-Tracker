from dataclasses import dataclass

@dataclass
class Transaction:
    trans_id: int | None = None
    cust_id: int | None = None  # Link to Customer
    type: str | None = None     # "revenue" or "expense"
    amount: float | None = None
    category: str | None = None
    date: str | None = None      # Format: YYYY-MM-DD
    description: str | None = None
