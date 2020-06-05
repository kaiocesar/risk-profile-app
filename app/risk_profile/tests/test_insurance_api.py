from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

RISK_ENDPOINT = reverse('create')


class InsuranceApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_empty_payload(self):
        payload = {}
        res = self.client.post(RISK_ENDPOINT, data=payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_full_payload(self):
        payload = {
            "age": 35,
            "dependents": 2,
            "house": {"ownership_status": "owned"},
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2018}
        }
        res = self.client.post(RISK_ENDPOINT, data=payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_invalid_payload(self):
        payload = {
            "age": 'thirty-five',
            "dependents": -1,
            "house": {"ownership_status": "borrowed"},
            "income": -100,
            "marital_status": "complicated",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2198}
        }
        res = self.client.post(RISK_ENDPOINT, data=payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_output_valid_payload(self):
        payload = {
            "age": 35,
            "dependents": 2,
            "house": {"ownership_status": "owned"},
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2018}
        }

        res = self.client.post(RISK_ENDPOINT, data=payload, format='json')

        self.assertEqual(res.data['auto'], 'regular')
        self.assertEqual(res.data['disability'], 'ineligible')
        self.assertEqual(res.data['home'], 'economic')
        self.assertEqual(res.data['life'], 'regular')
