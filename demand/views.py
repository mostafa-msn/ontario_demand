from rest_framework import generics, status
from .models import DemandReport
from .serializers import DemandReportSerializer, CreateDemandReportSerializer
from rest_framework.response import Response


class DemandReportCreateAPI(generics.CreateAPIView):
    serializer_class = CreateDemandReportSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(instance, status=status.HTTP_201_CREATED)


class DemandReportListAPI(generics.ListAPIView):
    serializer_class = DemandReportSerializer
    queryset = DemandReport.objects.all()

    def get_queryset(self):
        start_date = self.request.query_params['start']
        end_date = self.request.query_params['end']
        demand_report = self.queryset.filter(
            date__gt=start_date, date__lt=end_date)
        return demand_report
