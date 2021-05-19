from chat.models.lobby import Lobby
from common.serializers.base import BaseModelSerializer


class LobbyBaseSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Lobby
        read_only_fields = BaseModelSerializer.Meta.read_only_fields + ["user"]
        fields = read_only_fields + ["title"]
