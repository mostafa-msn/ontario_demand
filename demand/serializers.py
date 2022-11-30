from rest_framework import serializers
from .models import DemandReport


class DemandReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = DemandReport
        fields = ('date', 'hour', 'market_demand', 'ontario_demand')


class CreateDemandReportSerializer(serializers.Serializer):
    demand = DemandReportSerializer(many=True)

    class Meta:
        fields = ['demand']

    def create(self, validated_data):
        all_demand = validated_data.pop('demand')
        for demand in all_demand:
            # save DemandReport
            try:
                demand_report = DemandReport.objects.get(
                    date=demand['date'],
                    hour=demand['hour'])
                demand_report.market_demand = demand['market_demand']
                demand_report.ontario_demand = demand['ontario_demand']
                demand_report.save()
            except DemandReport.DoesNotExist:
                DemandReport.objects.create(**demand)

        return all_demand
