from accounts.serializers.user import UserBaseSerializer
from chat.models.message import Message
from chat.serializers.lobby import LobbyBaseSerializer
from common.serializers.base import BaseModelSerializer


class MessageBaseSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Message
        read_only_fields = BaseModelSerializer.Meta.read_only_fields + ["user", "lobby"]
        fields = read_only_fields + ["content"]


class MessageListRetrieveSerializer(MessageBaseSerializer):
    lobby = LobbyBaseSerializer(read_only=True)
    user = UserBaseSerializer(read_only=True)
