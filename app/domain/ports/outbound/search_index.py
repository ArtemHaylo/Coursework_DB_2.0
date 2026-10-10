from abc import ABC, abstractmethod
from app.domain.entities.hit import Hit

class SearchIndex(ABC):
    """Повнотекстовий пошук (реалізація: Elasticsearch)."""

    @abstractmethod
    async def search(self, query: str, filters: dict, limit: int = 20, offset: int = 0) -> list[Hit]: ...

    @abstractmethod
    async def index(self, medicine_id: str, name: str, full_description: str,
                    attributes: dict) -> None: ...

    @abstractmethod
    async def bulk_index(self, documents: list[dict]) -> int: ...

    @abstractmethod
    async def delete(self, medicine_id: str) -> None: ...