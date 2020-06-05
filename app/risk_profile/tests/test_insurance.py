from django.test import TestCase
from risk_profile.insurance import InsuranceCalculate, Profile


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

    def test_calculate_disability(self):
        profile = Profile(**self.payload)
        insurance = InsuranceCalculate(profile)
        insurance.calculate_disability()
        self.assertEqual(insurance.disability, 'ineligible')

    def test_calculate_age(self):
        profile = Profile(**self.payload)
        insurance = InsuranceCalculate(profile)
        insurance.calculate_age()

        self.assertEqual(insurance.auto, 0)
        self.assertEqual(insurance.disability, 0)
        self.assertEqual(insurance.home, 0)
        self.assertEqual(insurance.life, 0)

    def test_calculate_income(self):
        profile = Profile(**self.payload)
        insurance = InsuranceCalculate(profile)
        insurance.calculate_income()

        self.assertEqual(insurance.auto, 0)
        self.assertEqual(insurance.disability, 0)
        self.assertEqual(insurance.home, 0)
        self.assertEqual(insurance.life, 0)

    def test_calculate_house_status(self):
        profile = Profile(**self.payload)
        insurance = InsuranceCalculate(profile)
        insurance.calculate_house()

        self.assertEqual(insurance.home, 0)
        self.assertEqual(insurance.disability, 0)

    def test_calculate_dependents(self):
        profile = Profile(**self.payload)
        insurance = InsuranceCalculate(profile)
        insurance.calculate_dependents()

        self.assertEqual(insurance.disability, 1)
        self.assertEqual(insurance.life, 1)

    def test_calculate_marital_status(self):
        profile = Profile(**self.payload)
        insurance = InsuranceCalculate(profile)
        insurance.calculate_marital_status()

        self.assertEqual(insurance.auto, 0)
        self.assertEqual(insurance.life, 1)
        self.assertEqual(insurance.disability, 0)

    def test_calculate_vehicle_age(self):
        profile = Profile(**self.payload)
        insurance = InsuranceCalculate(profile)
        insurance.calculate_vehicle_age()

        self.assertEqual(insurance.auto, 1)

    def test_calculate_risk_profile(self):
        profile = Profile(**self.payload)
        insurance = InsuranceCalculate(profile)
        insurance.calculate_disability()
        insurance.calculate_age()
        insurance.calculate_income()
        insurance.calculate_house()
        insurance.calculate_dependents()
        insurance.calculate_marital_status()
        insurance.calculate_vehicle_age()

        self.assertEqual(
            insurance.translated_field('auto'),
            'regular'
        )
        self.assertEqual(
            insurance.translated_field('disability'),
            'ineligible'
        )
        self.assertEqual(
            insurance.translated_field('home'),
            'economic'
        )
        self.assertEqual(
            insurance.translated_field('life'),
            'regular'
        )
