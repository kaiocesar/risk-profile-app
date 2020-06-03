from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import RiskProfileSerializers
from risk_profile.insurance import Profile, Insurance


class RiskProfileViewSet(viewsets.ViewSet):

    serializer_class = RiskProfileSerializers

    def create(self, request):
        serializer = RiskProfileSerializers(
            data=request.data)

        if serializer.is_valid():
            profile = Profile(**serializer.data)
            insurance = Insurance(profile)
            insurance.calculate_risk_profile()
            result = {
                'auto': insurance.auto,
                'disability': insurance.disability,
                'home': insurance.home,
                'life': insurance.life
            }
            return Response(
                result,
                status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
