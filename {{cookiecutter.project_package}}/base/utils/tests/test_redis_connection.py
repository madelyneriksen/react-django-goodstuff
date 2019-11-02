"""Test the redis connection is a singleton."""


from base.utils.redis import connection as rconn
from base.utils.redis import RedisMixin


def test_connection_is_singleton():
    conn_one = rconn()
    conn_two = rconn()

    assert conn_one is conn_two


def test_redis_mixin():
    """Test that the connection is a singleton in a class."""

    class MyClass(RedisMixin):
        pass

    instance_one = MyClass()
    instance_two = MyClass()

    assert instance_one.redis is instance_two.redis
