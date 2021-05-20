from typing import Dict

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from accounts.serializers.user import UserBaseSerializer
from chat.models.lobby import Lobby
from chat.models.message import Message


class LobbyConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        """
        Retrieves a lobby identified and checks if it exists.
        If check passes, user consumer is accepted into the group.
        If if does not, we close the connection with a custom code.
        """
        self.room_name = self.scope["url_route"]["kwargs"]["lobby_id"]
        self.user = self.scope["user"]
        await self.accept()

        if not self.user.is_authenticated:
            await self.close(code=4001)

        self.lobby = await Lobby.get_by_pk_from_async(self.room_name)
        if self.lobby is None:
            await self.close(code=4000)

        self.room_group_name = self.lobby.group_name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        if "message" in content:
            message = content.get("message")
            instance = await Message.create_from_async(
                content=message, user=self.user, lobby=self.lobby
            )
            print("instance: ", instance)
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "message": message}
            )

        if "is_typing" in content:
            is_typing = bool(content.get("is_typing"))
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_typing", "is_typing": is_typing}
            )

    async def chat_message(self, event):
        """
        Sends message to the group about user message
        """
        message = event.get("message")
        user_dict = UserBaseSerializer(self.user).data
        await self.send_json(
            content={"message": message, "is_typing": False, "user": user_dict}
        )

    async def chat_typing(self, event: Dict):
        """
        Sends message to group that the user has started or stopped typing
        """
        user_dict = UserBaseSerializer(self.user).data
        is_typing = event.get("is_typing")
        await self.send_json(content={"is_typing": is_typing, "user": user_dict})
