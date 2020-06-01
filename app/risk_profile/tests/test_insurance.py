from django.test import TestCase
from risk_profile.insurance import Insurance, Profile


class InsuranceTest(TestCase):

    def setUp(self):

        self.payload = {
            "age": 35,
            "dependents": 2,
            "house": {"ownership_status": "owned"},
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2018}
        }

        self.profile = Profile(**self.payload)
        self.insurance = Insurance(self.profile)

    def test_calculate_disability(self):
        self.insurance.calculate_disability()
        self.assertEqual(self.insurance.disability, 'ineligible')

    def test_calculate_age(self):
        self.insurance.calculate_age()

        self.assertEqual(self.insurance.auto, -1)
        self.assertEqual(self.insurance.disability_number, -1)
        self.assertEqual(self.insurance.home, -1)
        self.assertEqual(self.insurance.life, -1)

    def test_calculate_income(self):
        self.insurance.calculate_income()

        self.assertEqual(self.insurance.auto, 0)
        self.assertEqual(self.insurance.disability_number, 0)
        self.assertEqual(self.insurance.home, 0)
        self.assertEqual(self.insurance.life, 0)

    def test_calculate_house_status(self):
        self.insurance.calculate_house()

        self.assertEqual(self.insurance.home, 0)
        self.assertEqual(self.insurance.disability_number, 0)

    def test_calculate_dependents(self):
        self.insurance.calculate_dependents()

        self.assertEqual(self.insurance.disability_number, 1)
        self.assertEqual(self.insurance.life, 1)

    def test_calculate_marital_status(self):
        self.insurance.calculate_marital_status()

        self.assertEqual(self.insurance.life, 1)
        self.assertEqual(self.insurance.disability_number, -1)

    def test_calculate_vehicle_age(self):
        self.insurance.calculate_vehicle_age()

        self.assertEqual(self.insurance.auto, 1)
