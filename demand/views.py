from rest_framework import generics, status
from .serializers import CreateDemandReportSerializer
from rest_framework.response import Response


class DemandReportCreateAPI(generics.CreateAPIView):
    serializer_class = CreateDemandReportSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(instance, status=status.HTTP_201_CREATED)

