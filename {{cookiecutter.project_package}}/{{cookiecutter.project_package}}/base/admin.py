"""Admin for {{ cookiecutter.project_title }} base models."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Admin for custom users."""
