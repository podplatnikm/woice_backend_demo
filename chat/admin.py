from django.contrib import admin

from chat.models.lobby import Lobby
from chat.models.message import Message


@admin.register(Lobby)
class LobbyAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "user", "is_private", "created_at"]
    list_display_links = ["id", "title"]
    search_fields = ["id", "title", "user__email", "user__username"]
    list_filter = ["created_at"]
    readonly_fields = ["created_at", "updated_at"]
    raw_id_fields = ["user"]
    filter_horizontal = ["users"]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "lobby", "user", "created_at", "updated_at"]
    list_display_links = ["id"]
    search_fields = ["lobby__title", "user__username", "user__email", "content"]
    list_filter = ["created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
    raw_id_fields = ["user", "lobby"]
