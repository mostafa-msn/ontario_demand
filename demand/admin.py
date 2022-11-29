from django.contrib import admin
from .models import DemandReport


class DemandReportAdmin(admin.ModelAdmin):
    list_display = [
        "date", "hour", "market_demand",
        "ontario_demand", "market_peak_day", "market_peak_month",
    ]
    list_filter = ("market_peak_month", )
    search_fields = ["market_demand", "ontario_demand", ]
    ordering = ('id',)


admin.site.register(DemandReport, DemandReportAdmin)