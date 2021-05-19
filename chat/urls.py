from django.urls import path, include
from rest_framework import routers

from chat.views.lobby import LobbyViewSet
from chat.views.message import MessageViewSet
from woice import constants

router = routers.SimpleRouter()

# Lobbies
router.register(r"lobbies", LobbyViewSet, basename="lobby")

# Messages
router.register(r"messages", MessageViewSet, basename="message")

urlpatterns = [
    path(constants.API_V1 + "chat/", include(router.urls)),
]
