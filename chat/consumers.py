from typing import Dict

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from chat.models.lobby import Lobby


class LobbyConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        """
        Retrieves a lobby identified and checks if it exists.
        If check passes, user consumer is accepted into the group.
        If if does not, we close the connection with a custom code.
        """
        self.room_name = self.scope["url_route"]["kwargs"]["lobby_id"]
        await self.accept()

        lobby = await Lobby.get_lobby_by_pk(self.room_name)
        if lobby is not None:
            self.room_group_name = lobby.group_name

            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        else:
            await self.close(code=4000)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        if "message" in content:
            message = content.ge("message")
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
        await self.send_json(content={"message": message, "is_typing": False})

    async def chat_typing(self, event: Dict):
        """
        Sends message to group that the user has started or stopped typing
        """
        is_typing = event.get("is_typing")
        await self.send_json(content={"is_typing": is_typing})
