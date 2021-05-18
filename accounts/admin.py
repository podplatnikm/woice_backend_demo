from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(get_user_model())
class UserModelAdmin(BaseUserAdmin):
    list_display = ("id", ) + BaseUserAdmin.list_display
    list_display_links = ("id", "username", "email")
