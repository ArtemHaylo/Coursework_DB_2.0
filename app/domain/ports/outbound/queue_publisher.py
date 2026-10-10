from abc import ABC, abstractmethod

class QueuePublisher(ABC):
    """Публікація пакетів документів у чергу (реалізація: RabbitMQ)."""

    @abstractmethod
    async def publish_batch(self, documents: list[dict]) -> None: ...