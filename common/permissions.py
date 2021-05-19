from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Only allow non safe actions to users that are also the creator of the instance.
    Assumes there is a user field on the object
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or obj.user == request.user:
            return True
        return False
