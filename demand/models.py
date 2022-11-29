from django.utils.translation import gettext_lazy as _
from django.db import models


class DemandReport(models.Model):
    date = models.DateTimeField(_("date"), null=True)
    hour = models.IntegerField(_("hour"), null=True)
    market_demand = models.IntegerField(_("market_demand"), null=True)
    ontario_demand = models.IntegerField(_("ontario_demand"), null=True)
    market_peak_day = models.BooleanField(_("market_peak_day"), default=False)
    ontario_peak_day = models.BooleanField(_("ontario_peak_day"), default=False)
    market_peak_month = models.BooleanField(_("market_peak_month"), default=False)
    ontario_peak_month = models.BooleanField(_("ontario_peak_month"), default=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Demand Report")
        verbose_name_plural = _("Demand Report")

    def __str__(self):
        return self.date
