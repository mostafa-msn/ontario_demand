from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import Max
from django.utils import timezone


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

    def save(self, **kwargs):
        super(DemandReport, self).save(**kwargs)

        # market_peak_day
        market_demand_peak_day = DemandReport.objects.filter(date=self.date) \
            .aggregate(Max('market_demand')).get('market_demand__max')
        if self.market_demand == market_demand_peak_day:
            self.market_peak_day = True
            # set false to others
            DemandReport.objects \
                .filter(date=self.date) \
                .exclude(pk=self.pk) \
                .update(market_peak_day=False)

        # market_peak_month
        market_demand_peak_month = DemandReport.objects.filter(
            date__month=self.date.month, date__year=self.date.year) \
            .aggregate(Max('market_demand')).get('market_demand__max')
        if self.market_demand == market_demand_peak_month:
            self.market_peak_month = True
            # set false to others
            DemandReport.objects \
                .filter(date__month=self.date.month, date__year=self.date.year) \
                .exclude(pk=self.pk) \
                .update(market_peak_month=False)

    def __str__(self):
        return str(self.date)
