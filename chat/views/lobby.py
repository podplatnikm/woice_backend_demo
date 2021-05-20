from django.db.models import Q
from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated

from chat.models.lobby import Lobby
from chat.serializers.lobby import LobbyBaseSerializer, LobbyListRetrieveSerializer
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

    def get_queryset(self):
        queryset = super(LobbyViewSet, self).get_queryset()
        return queryset.filter(
            Q(users=None) | Q(user=self.request.user) | Q(users__in=[self.request.user])
        ).distinct()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LobbyListRetrieveSerializer
        return super(LobbyViewSet, self).get_serializer_class()
