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
    disability = 0
    home = 0
    life = 0


class Insurance(Score):

    def __init__(self, profile):
        self.profile = profile

    def calculate_disability(self):
        if self.profile.income == 0\
            or not self.profilfe.vehicle\
                or not self.profile.house:
            self.disability = -1

    def calculate_age(self):
        age = self.profile.age
        if age > 60:
            self.disability = -1
        else:
            point = 2 if age < 30 else 1
            self.auto = deduct_value(self.auto, point)
            self.disability = deduct_value(
                self.disability, point)
            self.home = deduct_value(self.home, point)
            self.life = deduct_value(self.life, point)

    def calculate_income(self):
        if self.profile.income > 200000:
            point = 1
            self.auto = deduct_value(self.auto, point)
            self.disability = deduct_value(
                self.disability, point)
            self.home = deduct_value(self.home, point)
            self.life = deduct_value(self.life, point)

    def calculate_house(self):
        house = self.profile.house
        if house:
            if house['ownership_status'] == 'mortgaged':
                self.home = append_value(self.home, 1)
                self.disability = append_value(
                    self.disability, 1)

    def calculate_dependents(self):
        if self.profile.dependents:
            self.disability = append_value(
                self.disability, 1)
            self.life = append_value(self.life, 1)

    def calculate_marital_status(self):
        if self.profile.marital_status == 'married':
            self.disability = deduct_value(
                self.disability, 1)
            self.life = append_value(self.life, 1)

    def calculate_vehicle_age(self):
        if self.profile.vehicle:
            vehicle = self.profile.vehicle
            result = date.today().year - vehicle['year']
            if result <= 5:
                self.auto = append_value(self.auto, 1)

    def calculate_risk_profile(self):
        self.calculate_disability()
        self.calculate_age()
        self.calculate_income()
        self.calculate_house()
        self.calculate_dependents()
        self.calculate_marital_status()
        self.calculate_vehicle_age()

    def get_translated_field(self, field):
        insurance_value = getattr(self, field)
        if insurance_value <= 0:
            return 'economic'
        elif insurance_value >= 3:
            return 'responsible'
        else:
            return 'regular'
