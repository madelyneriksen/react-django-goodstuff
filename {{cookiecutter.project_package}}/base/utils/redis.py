"""Get a redis instance."""


import os

from functools import lru_cache
from redis import Redis


@lru_cache(maxsize=1)
def connection():
    """Redis connection singleton factory."""
    return Redis(os.getenv("REDIS_URL", "redis://redis:6379/0"))
