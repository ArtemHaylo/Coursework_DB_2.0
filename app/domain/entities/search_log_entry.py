from dataclasses import dataclass
from datetime import datetime

@dataclass
class SearchLogEntry:
    """Службовий запис журналу пошуку для панелі моніторингу."""
    query_id: str
    raw_query: str
    normalized_query: str
    results_count: int
    cache_hit: bool
    latency_ms: int
    created_at: datetime