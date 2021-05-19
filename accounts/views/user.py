from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, filters
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(methods=["get"], detail=False, url_path="me", url_name="me")
    def me(self, request, pk=None) -> Response:
        """
        Retrieves data for the current authenticated user
        """
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data)

    @me.mapping.patch
    def me_partial_update(self, request, pk=None) -> Response:
        """
        Partial update endpoint for current authenticated user
        """
        serializer = self.get_serializer(
            self.request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
