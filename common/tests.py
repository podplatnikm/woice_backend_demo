from typing import Type, List

from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from accounts.factories.user import UserFactory


class BasicAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.user_client = self.client_class()
        self.user_client.force_authenticate(user=self.user)

    def assert_response_length(self, response: Type[Response], count: int) -> None:
        """
        Checks if the request body has returned the expected number of objects
        :param response: response from a DRF client request
        :param count: number of expected objects
        """
        assert status.is_success(response.status_code)
        body = response.data
        assert body.get("count") == count
        assert len(body.get("results")) == count

    def assert_ids_in_results(self, results: List, ids: List[int]) -> bool:
        """
        Checks if the provided ids are returned in a results list from api response
        """
        id_array = ids
        for result in results:
            assert result.get("id") in id_array
            id_array.remove(result.get("id"))
        return len(id_array) == 0
