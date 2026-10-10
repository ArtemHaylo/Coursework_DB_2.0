from dataclasses import dataclass

@dataclass
class Symptom:
    """Симптом / побічний ефект (вузол графа)."""
    symptom_id: str
    name: str
    drug_count: int = 0