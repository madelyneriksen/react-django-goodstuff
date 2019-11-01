"""Viewsets for base models."""


from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from base.models import User
from .serializers import UserSerializer


class UserViewset(ReadOnlyModelViewSet):
    """Viewset for the user model."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
