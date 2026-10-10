from pydantic import BaseModel

class MedicineCard(BaseModel):
    """Картка препарату для відповіді користувачу."""
    medicine_id: str
    name: str
    therapeutic_class: str
    chemical_class: str | None = None
    action_class: str | None = None
    is_habit_forming: bool = False
    is_prescription: bool = False
    manufacturer: str | None = None
    price: float = 0.0
    uses: list[str] = []
    side_effects: list[str] = []
    substitutes: list[str] = []