from typing import Dict

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from accounts.serializers.user import UserBaseSerializer
from chat.models.lobby import Lobby
from chat.models.message import Message
from chat.serializers.message import MessageBaseSerializer


class LobbyConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        """
        Retrieves a lobby identified and checks if it exists.
        If check passes, user consumer is accepted into the group.
        If if does not, we close the connection with a custom code.
        """
        self.room_name = self.scope["url_route"]["kwargs"]["lobby_id"]
        self.user = self.scope["user"]

        if not self.user.is_authenticated:
            await self.close(code=4001)
        else:
            self.lobby = await Lobby.get_by_pk_from_async(self.room_name)
            if self.lobby is None:
                await self.close(code=4000)
            else:
                self.room_group_name = self.lobby.group_name
                await self.channel_layer.group_add(
                    self.room_group_name, self.channel_name
                )
                await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, "room_group_name"):
            await self.channel_layer.group_discard(
                self.room_group_name, self.channel_name
            )

    async def receive_json(self, content, **kwargs):
        if "message" in content:
            message = content.get("message")
            instance = await Message.create_from_async(
                content=message, user=self.user, lobby=self.lobby
            )
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "instance": instance,
                    "user": self.user,
                },
            )

        if "is_typing" in content:
            is_typing = bool(content.get("is_typing"))
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_typing",
                    "is_typing": is_typing,
                    "user": self.user,
                    "sender_channel_name": self.channel_name,
                },
            )

    async def chat_message(self, event):
        """
        Sends message to the group about user message
        """
        message = event.get("message")
        user_dict = UserBaseSerializer(event.get("user")).data
        instance_dict = MessageBaseSerializer(event.get("instance")).data
        await self.send_json(
            content={
                "message": message,
                "is_typing": False,
                "user": user_dict,
                "instance": instance_dict,
            }
        )

    async def chat_typing(self, event: Dict):
        """
        Sends message to group (except sender) that the user has started or stopped typing
        """
        if self.channel_name != event.get("sender_channel_name"):
            user_dict = UserBaseSerializer(event.get("user")).data
            is_typing = event.get("is_typing")
            await self.send_json(content={"is_typing": is_typing, "user": user_dict})
