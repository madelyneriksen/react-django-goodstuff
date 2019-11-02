"""Django Rest Framework enabled router."""


from rest_framework.routers import DefaultRouter

from .base.api.viewsets import UserViewset


router = DefaultRouter()
router.register("users", UserViewset)
