import factory.django
from django.db import models

from accounts.factories.user import UserFactory
from chat.models.lobby import Lobby


class LobbyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lobby

    title = factory.Sequence(lambda n: f"fan_club{n}")
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        # An iterable of groups were passed in, use it
        if isinstance(extracted, (list, set, tuple, models.QuerySet)):
            self.users.add(*extracted)  # bulk addition
