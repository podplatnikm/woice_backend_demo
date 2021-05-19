from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, filters

from accounts.serializers.user import UserBaseSerializer


class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = get_user_model().objects.filter(is_active=True)
    serializer_class = UserBaseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["username", "email"]
