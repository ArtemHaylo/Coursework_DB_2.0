from dataclasses import dataclass

@dataclass
class Disease:
    """Хвороба (вузол графа). Зв'язки з препаратами лежать у Neo4j як ребра"""
    disease_id: str
    name: str
    drug_count: int = 0