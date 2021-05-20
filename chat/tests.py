from django.urls import reverse
from rest_framework import status

from accounts.factories.user import UserFactory
from chat.factories.lobby import LobbyFactory
from chat.factories.message import MessageFactory
from chat.models.lobby import Lobby
from chat.models.message import Message
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

    def test_lobby_retrieve_private(self):
        """
        User should be able to retrieve private lobbies he created or is a part of
        """
        user_2 = UserFactory()
        lobby_1: Lobby = LobbyFactory(user=self.user, users=[user_2])
        response = self.user_client.get(reverse(self.LOBBY_DETAIL, args=[lobby_1.pk]))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data.get("users")) == 1

    def test_lobby_retrieve_private_not_member(self):
        """
        User should not be able to retrieve private lobbies he is not a part of
        """
        user_2 = UserFactory()
        user_3 = UserFactory()
        lobby_1: Lobby = LobbyFactory(user=user_2, users=[user_3])
        response = self.user_client.get(reverse(self.LOBBY_DETAIL, args=[lobby_1.pk]))
        assert response.status_code == status.HTTP_404_NOT_FOUND

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

    def test_lobby_create_private(self):
        """
        User should be able to create a private lobby
        """
        user_2 = UserFactory()
        data = {"title": "Dana voda", "users": [user_2.pk]}

        response = self.user_client.post(
            reverse(self.LOBBY_LIST), data=data, format="json"
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert len(response.data.get("users")) == 1

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


class MessageTestCase(BasicAPITestCase):
    def setUp(self) -> None:
        super(MessageTestCase, self).setUp()
        self.MESSAGE_LIST = "message-list"
        self.MESSAGE_DETAIL = "message-detail"

    def test_message_list(self):
        """
        User should be able to list all messages
        """
        quantity = 3
        [MessageFactory() for i in range(quantity)]

        response = self.user_client.get(reverse(self.MESSAGE_LIST))
        self.assert_response_length(response, quantity)

    def test_message_list_filter_by_user(self):
        """
        User should be able to filter messages by user primary key
        """
        user_2 = UserFactory()
        message_1 = MessageFactory(user=self.user)
        message_2 = MessageFactory(user=user_2)

        response = self.user_client.get(
            f"{reverse(self.MESSAGE_LIST)}?user={self.user.pk}"
        )
        self.assert_response_length(response, 1)
        self.assert_ids_in_results(response.json().get("results"), [message_1.pk])

    def test_message_list_filter_by_lobby(self):
        """
        User should be able to filter messages by lobby primary key
        """
        lobby_1 = LobbyFactory()
        lobby_2 = LobbyFactory()
        message_1 = MessageFactory(lobby=lobby_1)
        message_2 = MessageFactory(lobby=lobby_2)

        response = self.user_client.get(
            f"{reverse(self.MESSAGE_LIST)}?lobby={lobby_2.pk}"
        )
        self.assert_response_length(response, 1)
        self.assert_ids_in_results(response.json().get("results"), [message_2.pk])

    def test_message_list_private_messages(self):
        """
        User should not be able to list messages from private lobbies he is not a part of
        """
        user_2 = UserFactory()
        user_3 = UserFactory()
        lobby_1 = LobbyFactory(user=user_2, users=[user_3])
        message_1 = MessageFactory(lobby=lobby_1)

        response = self.user_client.get(reverse(self.MESSAGE_LIST))
        self.assert_response_length(response, 0)

    def test_message_retrieve(self):
        """
        User should be able to retrieve a single instance of message
        """
        message_1: Message = MessageFactory(user=self.user)

        response = self.user_client.get(
            reverse(self.MESSAGE_DETAIL, args=[message_1.pk])
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data.get("content") == message_1.content
        assert response.data.get("user").get("id") == self.user.pk
        assert response.data.get("lobby").get("id") == message_1.lobby.id

    def test_message_update(self):
        """
        User should be able to update a message he created
        """
        message_1: Message = MessageFactory(user=self.user)

        new_content = "KAZN"
        data = {"content": new_content}

        response = self.user_client.patch(
            reverse(self.MESSAGE_DETAIL, args=[message_1.pk]), data=data, format="json"
        )
        assert response.status_code == status.HTTP_200_OK

    def test_message_update_not_owner(self):
        """
        User should not be able to update a message someone else created
        """
        user_2 = UserFactory()
        message_1 = MessageFactory(user=user_2)

        response = self.user_client.patch(
            reverse(self.MESSAGE_DETAIL, args=[message_1.pk]), data={}, format="json"
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_message_delete(self):
        """
        User should be able to delete a message he created
        """
        message_1: Message = MessageFactory(user=self.user)
        assert Message.objects.count() == 1

        response = self.user_client.delete(
            reverse(self.MESSAGE_DETAIL, args=[message_1.pk])
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Message.objects.count() == 0

    def test_message_delete_not_owner(self):
        """
        User should not be able to delete a message someone else created
        """
        user_2 = UserFactory()
        message_1 = MessageFactory(user=user_2)

        response = self.user_client.delete(
            reverse(self.MESSAGE_DETAIL, args=[message_1.pk])
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN
