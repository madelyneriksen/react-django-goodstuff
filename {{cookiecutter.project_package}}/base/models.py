"""Base models for {{ cookiecutter.project_title }}"""


import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    """Base model all models inherit from."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        """Metadata."""
        abstract = True


class User(BaseModel, AbstractUser):
    """Base user class."""

    class Meta:
        """Metadata."""
        db_table = "users"
