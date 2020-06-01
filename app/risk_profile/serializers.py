from rest_framework import serializers

from risk_profile.insurance import Profile

MARITAL_STATUS = ('single', 'married')


class RiskProfileSerializers(serializers.Serializer):
    age = serializers.IntegerField(min_value=0, max_value=150)
    dependents = serializers.IntegerField(min_value=0, default=0)
    house = serializers.JSONField()
    income = serializers.IntegerField(min_value=0, default=0)
    marital_status = serializers.ChoiceField(
        choices=MARITAL_STATUS, default='single')
    risk_questions = serializers.JSONField()
    vehicle = serializers.JSONField()

    class Meta:
        fields = (
            'age',
            'dependents',
            'house',
            'income',
            'marital_status',
            'risk_questions',
            'vehicle'
        )

    def create(self, validated_data):
        return Profile(**validated_data)
