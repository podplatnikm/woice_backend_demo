from django.urls import path, include
from rest_framework import routers

from accounts.views.user import UserViewSet
from woice import constants

router = routers.SimpleRouter()

# Users
router.register(r"users", UserViewSet, basename="user")


urlpatterns = [
    path(constants.API_V1 + "accounts/", include(router.urls)),
]
