from datetime import date
from .utils import append_point, deduct_point


class Profile(object):

    def __init__(self, **kwargs):
        fields = ('age', 'dependents',
                  'house', 'income',
                  'marital_status',
                  'risk_questions', 'vehicle')
        for field in fields:
            setattr(self, field, kwargs.get(field, None))


class Score:
    auto = 0
    disability = 0
    home = 0
    life = 0


class InsuranceCalculate(Score):

    def __init__(self, profile):
        self.profile = profile

    def calculate_disability(self):
        if self.profile.income <= 0\
            or not self.profilfe.vehicle\
                or not self.profile.house:
            self.disability = 'ineligible'

    def calculate_age(self):
        age = self.profile.age
        if age > 60:
            self.disability = 'ineligible'
        else:
            point = 2 if age < 30 else 1
            self.auto = deduct_point(self.auto, point)
            self.disability = deduct_point(
                self.disability, point)
            self.home = deduct_point(self.home, point)
            self.life = deduct_point(self.life, point)

    def calculate_income(self):
        if self.profile.income > 200000:
            point = 1
            self.auto = deduct_point(self.auto, point)
            self.disability = deduct_point(
                self.disability, point)
            self.home = deduct_point(self.home, point)
            self.life = deduct_point(self.life, point)

    def calculate_house(self):
        house = self.profile.house
        if house:
            if house['ownership_status'] == 'mortgaged':
                self.home = append_point(self.home, 1)
                self.disability = append_point(
                    self.disability, 1)

    def calculate_dependents(self):
        if self.profile.dependents:
            self.disability = append_point(
                self.disability, 1)
            self.life = append_point(self.life, 1)

    def calculate_marital_status(self):
        if self.profile.marital_status == 'married':
            self.disability = deduct_point(
                self.disability, 1)
            self.life = append_point(self.life, 1)

    def calculate_vehicle_age(self):
        if self.profile.vehicle:
            vehicle = self.profile.vehicle
            result = date.today().year - vehicle['year']
            if result <= 5:
                self.auto = append_point(self.auto, 1)

    def calculate_risk_profile(self):
        self.calculate_disability()
        self.calculate_age()
        self.calculate_income()
        self.calculate_house()
        self.calculate_dependents()
        self.calculate_marital_status()
        self.calculate_vehicle_age()

        return {
            'auto': self.translated_field('auto'),
            'home': self.translated_field('home'),
            'life': self.translated_field('life'),
            'disability': self.translated_field('disability')}

    def translated_field(self, field):
        insurance_value = getattr(self, field)
        if isinstance(insurance_value, str):
            return insurance_value
        if insurance_value <= 0:
            return 'economic'
        elif insurance_value >= 3:
            return 'responsible'
        else:
            return 'regular'
