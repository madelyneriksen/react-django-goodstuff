"""Get a redis instance."""


import os

from functools import lru_cache

from django_redis import get_redis_connection
from redis import Redis


@lru_cache(maxsize=1)
def connection():
    """Redis connection singleton factory."""
    return get_redis_connection("default")


class RedisMixin:
    """Mixin to add Redis support to a class.

    Usage:
    >>> class MyClass(RedisMixin):
    >>>     pass
    >>>
    >>> my_instance = MyClass()
    >>> my_instance.redis.get("some_key")
    """

    @property
    def redis(self) -> Redis:
        """Get the redis instance."""
        return connection()
