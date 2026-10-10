from dataclasses import dataclass, field

@dataclass
class Medicine:
    """Центральна сутність: картка лікарського засобу"""
    medicine_id: str
    name: str
    therapeutic_class: str
    source_id: int | None = None
    chemical_class: str | None = None
    action_class: str | None = None
    is_habit_forming: bool = False
    is_prescription: bool = False
    manufacturer: str | None = None
    price: float = 0.0
    uses: list[str] = field(default_factory=list)
    side_effects: list[str] = field(default_factory=list)
    substitutes: list[str] = field(default_factory=list)