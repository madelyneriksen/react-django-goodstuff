"""Serializers for base models."""


from rest_framework.serializers import ModelSerializer

from base.models import User


class UserSerializer(ModelSerializer):
    """Serializer for custom users."""

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
