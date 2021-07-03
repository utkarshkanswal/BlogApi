from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json


class TestPerformance(APITestCase):
    def setUp(self):
        self.customer = {
            "name": "Ritik Kumar",
            "age": 21,
            "phone": "971957118987",
            "city": "Najibabad",
            "country": "India",
            "linkedin_profile": "http://www.ksksks.com"
        }

    def test_get(self):
        for i in range(0, 1000):
            response = self.client.post(
                '/api/user', self.customer, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
