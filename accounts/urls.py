from django.urls import path
from accounts.views import home,loginView,register,logoutView

urlpatterns = [
    path('', home),
    path('login',loginView),
    path('register',register),
    path('logout',logoutView),
]

