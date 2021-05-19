from django.urls import reverse
from rest_framework import status

from accounts.factories.user import UserFactory
from chat.factories.lobby import LobbyFactory
from chat.models.lobby import Lobby
from common.tests import BasicAPITestCase


class LobbyTestCase(BasicAPITestCase):
    def setUp(self) -> None:
        super(LobbyTestCase, self).setUp()
        self.LOBBY_LIST = "lobby-list"
        self.LOBBY_DETAIL = "lobby-detail"

    def test_lobby_list(self):
        """
        User should be able to list all lobbies created
        """
        quantity = 3
        [LobbyFactory() for i in range(quantity)]

        response = self.user_client.get(reverse(self.LOBBY_LIST))
        self.assert_response_length(response, quantity)

    def test_lobby_retrieve(self):
        """
        User should be able to retrieve a single instance of a lobby model
        """
        lobby_1: Lobby = LobbyFactory(user=self.user)

        response = self.user_client.get(reverse(self.LOBBY_DETAIL, args=[lobby_1.pk]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data.get("title") == lobby_1.title
        assert response.data.get("user") == self.user.pk

    def test_lobby_create(self):
        """
        User should be able to create a lobby
        """
        title = "Zaho fun club"
        data = {"title": title}
        response = self.user_client.post(
            reverse(self.LOBBY_LIST), data=data, format="json"
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get("title") == title
        assert response.data.get("user") == self.user.pk

    def test_lobby_delete(self):
        """
        User should be able to delete a lobby he created
        """
        lobby_1: Lobby = LobbyFactory(user=self.user)

        response = self.user_client.delete(
            reverse(self.LOBBY_DETAIL, args=[lobby_1.pk])
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Lobby.objects.count() == 0

    def test_lobby_delete_not_owner(self):
        """
        User should not be able to delete a lobby someone else created
        """
        user_2 = UserFactory()
        lobby_1: Lobby = LobbyFactory(user=user_2)

        response = self.user_client.delete(
            reverse(self.LOBBY_DETAIL, args=[lobby_1.pk])
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN
