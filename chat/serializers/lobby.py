from accounts.serializers.user import UserBaseSerializer
from chat.models.lobby import Lobby
from common.serializers.base import BaseModelSerializer


class LobbyBaseSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Lobby
        read_only_fields = BaseModelSerializer.Meta.read_only_fields + [
            "user",
            "is_private",
        ]
        fields = read_only_fields + ["title", "users"]

    def _get_m2m_fields(self):
        return ["users"]


class LobbyListRetrieveSerializer(LobbyBaseSerializer):
    users = UserBaseSerializer(read_only=True, many=True)
