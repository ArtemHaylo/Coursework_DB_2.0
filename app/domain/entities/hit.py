from dataclasses import dataclass

@dataclass
class Hit:
    """Один результат повнотекстового пошуку."""
    medicine_id: str
    score: float
    snippet: str | None = None