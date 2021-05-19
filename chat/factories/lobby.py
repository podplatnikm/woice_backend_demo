import factory.django

from accounts.factories.user import UserFactory
from chat.models.lobby import Lobby


class LobbyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lobby

    title = factory.Sequence(lambda n: f"fan_club{n}")
    user = factory.SubFactory(UserFactory)
