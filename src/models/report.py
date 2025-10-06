from dataclasses import dataclass

@dataclass
class Report:
    report_id: int | None = None
    cust_id: int | None = None
    type: str | None = None
    content: str | None = None
    created_at: str | None = None
