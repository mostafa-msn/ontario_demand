from django.urls import path
from .views import DemandReportCreateAPI


urlpatterns = [
      path('create', DemandReportCreateAPI.as_view()),

]