from django.urls import path
from  Job.views import job,viewJob

urlpatterns = [
    path('', job),
    path("viewjob",viewJob),
]





