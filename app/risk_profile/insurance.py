from datetime import date


def deduct_value(field, value):
    return field - value if field > value else 0


def append_value(field, value):
    return field + value


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
        if age > 60:
            self.disability = 'ineligible'
        else:
            point = 2 if age < 30 else 1
            self.auto = deduct_value(self.auto, point)
            self.disability_number = deduct_value(
                self.disability_number, point)
            self.home = deduct_value(self.home, point)
            self.life = deduct_value(self.life, point)

    def calculate_income(self):
        if self.profile.income > 200000:
            point = 1
            self.auto = deduct_value(self.auto, point)
            self.disability_number = deduct_value(
                self.disability_number, point)
            self.home = deduct_value(self.home, point)
            self.life = deduct_value(self.life, point)

    def calculate_house(self):
        house = self.profile.house
        if house:
            if house['ownership_status'] == 'mortgaged':
                self.home = append_value(self.home, 1)
                self.disability_number = append_value(
                    self.disability_number, 1)

    def calculate_dependents(self):
        if self.profile.dependents:
            self.disability_number = append_value(
                self.disability_number, 1)
            self.life = append_value(self.life, 1)

    def calculate_marital_status(self):
        if self.profile.marital_status == 'married':
            self.disability_number = deduct_value(
                self.disability_number, 1)
            self.life = append_value(self.life, 1)

    def calculate_vehicle_age(self):
        if self.profile.vehicle:
            vehicle = self.profile.vehicle
            result = date.today().year - vehicle['year']
            if result <= 5:
                self.auto = append_value(self.auto, 1)
