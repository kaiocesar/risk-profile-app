from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import RiskProfileSerializers
from risk_profile.insurance import Profile, InsuranceCalculate


class RiskProfileViewSet(viewsets.ViewSet):

    serializer_class = RiskProfileSerializers

    def create(self, request):
        serializer = RiskProfileSerializers(
            data=request.data)

        if serializer.is_valid():
            profile = Profile(**serializer.data)
            insurance = InsuranceCalculate(profile)

            return Response(
                insurance.calculate_risk_profile(),
                status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
