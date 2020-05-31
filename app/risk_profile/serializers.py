from rest_framework import serializers

MARITAL_STATUS = ('single', 'married')


class Profile(object):
    def __init__(self, **kwargs):
        fields = ('age', 'dependents',
                  'house', 'income',
                  'marital_status',
                  'risk_questions', 'vehicle')
        for field in fields:
            setattr(self, field, kwargs.get(field, None))


class RiskProfileSerializers(serializers.Serializer):
    age = serializers.IntegerField()
    dependents = serializers.IntegerField()
    house = serializers.JSONField()
    income = serializers.IntegerField()
    marital_status = serializers.ChoiceField(
        choices=MARITAL_STATUS, default='single')
    risk_questions = serializers.JSONField()
    vehicle = serializers.JSONField()

    def create(self, validated_data):
        return Profile(**validated_data)
