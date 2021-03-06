from channels.db import database_sync_to_async
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.timestamp import TimestampModel


class Lobby(TimestampModel):
    title = models.CharField(
        verbose_name=_("title"),
        max_length=100,
        unique=True,
        help_text=_("Name of the chat lobby."),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text=_("Creator of the lobby"),
        related_name="created_lobbies",
    )
    users = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        blank=True,
        help_text=_("Invitees to private lobby"),
    )

    class Meta:
        verbose_name = "Lobby"
        verbose_name_plural = "Lobbies"

    def __str__(self):
        return f"[{self.pk}] {self.title}"

    @property
    def group_name(self):
        """
        Returns the channels group name that sockets should subscribe to and get sent messages
        """
        return f"lobby_{self.pk}"

    @property
    def is_private(self):
        return self.users.count() > 0

    @database_sync_to_async
    def allow_access_for_user_from_async(self, user):
        if self.is_private and user not in self.users.all():
            return False
        return True

    @classmethod
    @database_sync_to_async
    def get_by_pk_from_async(cls, pk):
        try:
            return cls.objects.get(pk=pk)
        except cls.DoesNotExist:
            return None
