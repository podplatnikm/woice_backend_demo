from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from chat.models.lobby import Lobby
from common.models.timestamp import TimestampModel


class MessageManager(models.Manager):
    def by_room(self, lobby):
        """
        Returns latest messages first for a certain lobby
        :param lobby: primary key of the Lobby model instance
        """
        return self.get_queryset().filter(lobby=lobby).order_by("-created_at")


class Message(TimestampModel):
    """
    Chat message created by a user inside a lobby
    """

    content = models.TextField(
        verbose_name=_("content"), help_text=_("Lobby message text")
    )

    lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = MessageManager()

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"[{self.pk}] {self.content}"
