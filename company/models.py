from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    company_name = models.CharField(max_length=200)
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=20, blank=True, null=True)
    company_location = models.CharField(max_length=200, blank=True, null=True)

    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    founded_year = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    company_size = models.CharField(max_length=50, blank=True, null=True)

    company_description = models.TextField(blank=True, null=True)

    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name
