from django.urls import path
from company.views import company_register

urlpatterns = [
    path("",company_register),
]
