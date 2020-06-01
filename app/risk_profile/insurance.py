import datetime


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
    disability = ''
    disability_number = 0
    home = 0
    life = 0


class Insurance(Score):

    def __init__(self, profile):
        self.profile = profile

    def calculate_disability(self):
        if self.profile.income == 0\
            or not self.profilfe.vehicle\
                or not self.profile.house:
            self.disability = 'ineligible'

    def calculate_age(self):
        age = self.profile.age
        if age < 30:
            self.auto -= 2
            self.disability_number -= 2
            self.home -= 2
            self.life -= 2
        elif age >= 30 and age <= 40:
            self.auto -= 1
            self.disability_number -= 1
            self.home -= 1
            self.life -= 1
        elif age > 60:
            self.disability = 'ineligible'

    def calculate_income(self):
        if self.profile.income > 200000:
            self.auto -= 1
            self.disability_number -= 1
            self.home -= 1
            self.life -= 1

    def calculate_house(self):
        house = self.profile.house
        if house:
            if house['ownership_status'] == 'mortgaged':
                self.home += 1
                self.disability_number += 1

    def calculate_dependents(self):
        if self.profile.dependents:
            self.disability_number += 1
            self.life += 1

    def calculate_marital_status(self):
        if self.profile.marital_status == 'married':
            self.disability_number -= 1
            self.life += 1

    def calculate_vehicle_age(self):
        if self.profile.vehicle:
            vehicle = self.profile.vehicle
            now = datetime.datetime.now()
            result = now.year - vehicle['year']
            if result <= 5:
                self.auto += 1
