from abc import ABC, abstractmethod
from app.domain.entities.search_log_entry import SearchLogEntry

class MetricsSink(ABC):
    """Журнал запитів для моніторингу (реалізація: MongoDB, колекція search_log)."""

    @abstractmethod
    async def record_query(self, entry: SearchLogEntry) -> None: ...

    @abstractmethod
    async def recent_queries(self, limit: int = 50) -> list[SearchLogEntry]: ...