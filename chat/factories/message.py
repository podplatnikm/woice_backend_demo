import factory.django

from accounts.factories.user import UserFactory
from chat.factories.lobby import LobbyFactory
from chat.models.message import Message


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    content = factory.Sequence(lambda n: f"to the moon #{n}")

    user = factory.SubFactory(UserFactory)
    lobby = factory.SubFactory(LobbyFactory)
