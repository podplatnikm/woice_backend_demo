from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(get_user_model())
class UserModelAdmin(BaseUserAdmin):
    list_display = ("id",) + BaseUserAdmin.list_display
    list_display_links = ("id", "username", "email")
    fieldsets = BaseUserAdmin.fieldsets + ((_("Profile"), {"fields": ("avatar",)}),)
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
