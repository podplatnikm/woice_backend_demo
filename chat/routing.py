from django.urls import re_path

from chat.consumers import LobbyConsumer

websocket_urlpatterns = [
    re_path(r"ws/lobby/(?P<lobby_id>[0-9]+)/$", LobbyConsumer.as_asgi()),
]
