from django.urls import path
from .views import DemandReportCreateAPI, DemandReportListAPI, DemandReportDeleteAPI


urlpatterns = [
      path('create', DemandReportCreateAPI.as_view()),
      path('', DemandReportListAPI.as_view()),
      path('delete', DemandReportDeleteAPI.as_view()),

]