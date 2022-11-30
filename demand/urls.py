from django.urls import path
from .views import DemandReportCreateAPI, DemandReportListAPI


urlpatterns = [
      path('create', DemandReportCreateAPI.as_view()),
      path('', DemandReportListAPI.as_view()),

]