from abc import ABC, abstractmethod
from app.domain.entities.disease import Disease

class GraphRepository(ABC):
    """Обхід зв'язків: аналоги, хвороби, побічні ефекти (реалізація: Neo4j)."""

    @abstractmethod
    async def find_analogues(self, medicine_id: str, depth: int = 1) -> list[str]: ...

    @abstractmethod
    async def find_by_disease(self, disease_name: str) -> list[str]: ...

    @abstractmethod
    async def exclude_by_symptom(self, medicine_ids: list[str], symptom_name: str) -> list[str]: ...

    @abstractmethod
    async def upsert_medicine_graph(self, medicine_id: str, name: str,
                                    diseases: list[str], symptoms: list[str],
                                    substitutes: list[str]) -> None: ...

    @abstractmethod
    async def delete_medicine(self, medicine_id: str) -> None: ...