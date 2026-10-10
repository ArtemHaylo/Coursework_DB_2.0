from abc import ABC, abstractmethod

class CacheStore(ABC):
    """Кеш результатів та конфігурація (реалізація: Redis).
    Ключ кешу має включати нормалізований запит І фільтри."""

    @abstractmethod
    async def get(self, key: str) -> str | None: ...

    @abstractmethod
    async def set(self, key: str, value: str, ttl: int) -> None: ...

    @abstractmethod
    async def get_rate(self) -> int: ...

    @abstractmethod
    async def set_rate(self, rate: int) -> None: ...