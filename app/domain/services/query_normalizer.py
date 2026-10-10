class QueryNormalizer:
    """Нормалізація запиту: нижній регістр + слова за алфавітом (ключ кешу)."""

    def normalize(self, raw: str) -> str:
        raise NotImplementedError