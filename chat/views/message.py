from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from chat.models.message import Message
from chat.serializers.message import (
    MessageBaseSerializer,
    MessageListRetrieveSerializer,
)
from common.permissions import IsUserOrReadOnly


class MessageViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Message.objects.all()
    serializer_class = MessageBaseSerializer
    permission_classes = [IsAuthenticated, IsUserOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["content"]
    filterset_fields = ["lobby", "user"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return MessageListRetrieveSerializer
        return super(MessageViewSet, self).get_serializer_class()
