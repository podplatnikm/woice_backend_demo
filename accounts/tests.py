from django.conf import settings
from django.urls import reverse
from rest_framework import status

from accounts.factories.user import UserFactory
from common.tests import BasicAPITestCase


class UserTestCase(BasicAPITestCase):
    def setUp(self) -> None:
        self.USER_LIST = "user-list"
        self.USER_DETAIL = "user-detail"
        self.USER_ME = "user-me"
        self.USER_CLASS_LABEL = settings.AUTH_USER_MODEL
        super(UserTestCase, self).setUp()

    def test_user_list(self):
        """
        User should be able to list all users
        """
        quantity = 2
        [UserFactory() for i in range(quantity)]

        response = self.user_client.get(reverse(self.USER_LIST))
        self.assert_response_length(
            response, quantity + 1
        )  # we add one since we create a user in setUp

    def test_user_retrieve(self):
        """
        User should be able to retrieve a more detail version of a single user
        """
        response = self.user_client.get(reverse(self.USER_DETAIL, args=[self.user.pk]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data.get("email") == self.user.email

    def test_user_me_retrieve(self):
        """
        User should be able to retrieve personal information
        """
        response = self.user_client.get(reverse(self.USER_ME))
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get("email") == self.user.email
        assert response.json().get("id") == self.user.pk

    def test_user_me_update(self):
        """
        User should be able to update personal information
        """
        new_username = "zaho_viola"
        assert self.user.username != new_username

        data = {"username": new_username}
        response = self.user_client.patch(
            reverse(self.USER_ME), data=data, format="json"
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get("id") == self.user.pk
        assert response.json().get("username") == new_username
