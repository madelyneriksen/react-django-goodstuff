"""Test the redis connection is a singleton."""


from base.utils.redis import connection as rconn


def test_connection_is_singleton():
    conn_one = rconn()
    conn_two = rconn()

    assert conn_one is conn_two
