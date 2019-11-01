"""Test the user viewset."""


import pytest
from base.models import User


@pytest.mark.django_db
def test_get_returns_users(admin_client):
    """Test that a get request returns the users."""
    User.objects.create_user(
        username="maddie", first_name="maddie", last_name="maddie", password="hunter2"
    )
    response = admin_client.get("/api/users/")

    assert response.status_code == 200
    assert len(response.data) == 2

    assert "username" in response.data[0].keys()
    assert "first_name" in response.data[0].keys()
    assert "last_name" in response.data[0].keys()
