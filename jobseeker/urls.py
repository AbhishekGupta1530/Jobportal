from django.urls import path
from jobseeker.views import jobseekerProfile,viewProfile


urlpatterns = [
    path('profile',jobseekerProfile),
    path('viewProfile/<str:name>',viewProfile)
]
