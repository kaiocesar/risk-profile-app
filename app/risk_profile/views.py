from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import RiskProfileSerializers


class RiskProfileViewSet(viewsets.ViewSet):

    serializer_class = RiskProfileSerializers

    def create(self, request):
        serializer = RiskProfileSerializers(
            data=request.data)

        if serializer.is_valid():

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
