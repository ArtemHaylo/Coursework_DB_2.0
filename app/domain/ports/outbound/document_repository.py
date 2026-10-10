from abc import ABC, abstractmethod
from app.domain.entities.medicine import Medicine

class DocumentRepository(ABC):
    """CRUD-репозиторій карток препаратів (реалізація: MongoDB)."""

    @abstractmethod
    async def create(self, medicine: Medicine) -> Medicine: ...

    @abstractmethod
    async def get_by_id(self, medicine_id: str) -> Medicine | None: ...

    @abstractmethod
    async def by_ids(self, ids: list[str]) -> list[Medicine]: ...

    @abstractmethod
    async def update(self, medicine_id: str, medicine: Medicine) -> Medicine: ...

    @abstractmethod
    async def delete(self, medicine_id: str) -> None: ...

    @abstractmethod
    async def find(self, filters: dict, limit: int = 20, offset: int = 0) -> list[Medicine]: ...

    @abstractmethod
    async def bulk_insert(self, medicines: list[Medicine]) -> int: ...