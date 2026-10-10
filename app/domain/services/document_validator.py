from app.domain.entities.medicine import Medicine

class DocumentValidator:
    """Валідація документа перед записом (непорожні name, therapeutic_class тощо)."""

    def validate(self, medicine: Medicine) -> bool:
        raise NotImplementedError