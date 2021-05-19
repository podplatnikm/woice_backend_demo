from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated

from chat.models.lobby import Lobby
from chat.serializers.lobby import LobbyBaseSerializer
from common.permissions import IsUserOrReadOnly


class LobbyViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Lobby.objects.all()
    serializer_class = LobbyBaseSerializer
    permission_classes = [IsAuthenticated, IsUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
