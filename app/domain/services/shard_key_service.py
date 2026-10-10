from app.domain.entities.medicine import Medicine


class ShardKeyService:
    """Гарантує непорожній therapeutic_class (значення 'unknown'),
    бо він входить у ключ шардінгу {therapeutic_class, medicine_id}."""

    def ensure_shard_key(self, medicine: Medicine) -> Medicine:
        raise NotImplementedError