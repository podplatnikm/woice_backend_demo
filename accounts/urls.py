from django.urls import path, include
from rest_framework import routers

from woice import constants

router = routers.SimpleRouter()

urlpatterns = [
    path(constants.API_V1 + "accounts/", include(router.urls)),
]
