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

    def test_35_years_regular_profile(self):
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

    def test_60_years_economic_profile(self):
        payload = {
            "age": 60,
            "dependents": 0,
            "house": {},
            "income": 0,
            "marital_status": "single",
            "risk_questions": [0, 0, 0],
            "vehicle": {}
        }

        res = self.client.post(RISK_ENDPOINT, data=payload, format='json')

        self.assertEqual(res.data['auto'], 'economic')
        self.assertEqual(res.data['disability'], 'ineligible')
        self.assertEqual(res.data['home'], 'economic')
        self.assertEqual(res.data['life'], 'economic')

    def test_60_years_regular_profile(self):
        payload = {
            "age": 60,
            "dependents": 1,
            "house": {"ownership_status": "owned"},
            "income": 250000,
            "marital_status": "married",
            "risk_questions": [0, 0, 0],
            "vehicle": {"year": 2016}
        }

        res = self.client.post(RISK_ENDPOINT, data=payload, format='json')

        self.assertEqual(res.data['auto'], 'regular')
        self.assertEqual(res.data['disability'], 'economic')
        self.assertEqual(res.data['home'], 'economic')
        self.assertEqual(res.data['life'], 'regular')

    def test_61_years_ineligible_profile(self):
        payload = {
            "age": 61,
            "dependents": 0,
            "house": {"ownership_status": "mortgaged"},
            "income": 150000,
            "marital_status": "single",
            "risk_questions": [1, 0, 0],
            "vehicle": {"year": 1975}
        }

        res = self.client.post(RISK_ENDPOINT, data=payload, format='json')

        self.assertEqual(res.data['auto'], 'economic')
        self.assertEqual(res.data['disability'], 'ineligible')
        self.assertEqual(res.data['home'], 'regular')
        self.assertEqual(res.data['life'], 'ineligible')

    def test_61_years_ineligible_regular_profile(self):
        payload = {
            "age": 61,
            "dependents": 1,
            "house": {"ownership_status": "owned"},
            "income": 15000000,
            "marital_status": "married",
            "risk_questions": [1, 0, 0],
            "vehicle": {"year": 2019}
        }

        res = self.client.post(RISK_ENDPOINT, data=payload, format='json')

        self.assertEqual(res.data['auto'], 'regular')
        self.assertEqual(res.data['disability'], 'ineligible')
        self.assertEqual(res.data['home'], 'economic')
        self.assertEqual(res.data['life'], 'ineligible')

    def test_18_years_economic_profile(self):
        payload = {
            "age": 18,
            "dependents": 0,
            "house": {},
            "income": 0,
            "marital_status": "single",
            "risk_questions": [1, 0, 0],
            "vehicle": {}
        }

        res = self.client.post(RISK_ENDPOINT, data=payload, format='json')

        self.assertEqual(res.data['auto'], 'economic')
        self.assertEqual(res.data['disability'], 'ineligible')
        self.assertEqual(res.data['home'], 'economic')
        self.assertEqual(res.data['life'], 'economic')

    def test_18_years_regular_profile(self):
        payload = {
            "age": 18,
            "dependents": 1,
            "house": {"ownership_status": "mortgaged"},
            "income": 0,
            "marital_status": "single",
            "risk_questions": [1, 0, 0],
            "vehicle": {"year": 2000}
        }

        res = self.client.post(RISK_ENDPOINT, data=payload, format='json')

        self.assertEqual(res.data['auto'], 'economic')
        self.assertEqual(res.data['disability'], 'ineligible')
        self.assertEqual(res.data['home'], 'regular')
        self.assertEqual(res.data['life'], 'regular')

    def test_30_years_regular(self):
        payload = {
            "age": 30,
            "dependents": 0,
            "house": {"ownership_status": "owned"},
            "income": 1000000,
            "marital_status": "married",
            "risk_questions": [1, 0, 1],
            "vehicle": {"year": 2018}
        }

        res = self.client.post(RISK_ENDPOINT, data=payload, format='json')

        self.assertEqual(res.data['auto'], 'regular')
        self.assertEqual(res.data['disability'], 'economic')
        self.assertEqual(res.data['home'], 'economic')
        self.assertEqual(res.data['life'], 'regular')
