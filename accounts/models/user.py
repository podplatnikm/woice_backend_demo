from channels.db import database_sync_to_async
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(verbose_name=_("email address"), unique=True)
    username = models.CharField(
        verbose_name=_("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[AbstractUser.username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        blank=True,
    )
    avatar = models.ImageField(
        _("avatar"), blank=True, null=True, help_text=_("Profile picture")
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @classmethod
    @database_sync_to_async
    def get_by_pk_from_async(cls, pk):
        try:
            return cls.objects.get(pk=pk)
        except cls.DoesNotExist:
            AnonymousUser()
