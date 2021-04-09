
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


ENDPOINT = '/'


class HealthCheckAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_success_health_check(self):
        res = self.client.get(ENDPOINT)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
