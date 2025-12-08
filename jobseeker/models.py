from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100,default="")
    full_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=15)
    profilephoto = models.ImageField(upload_to='profilephotos/')
    professionalNo = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')
    email = models.CharField(max_length=100)
    address = models.TextField(max_length=255)
    skills = models.TextField(max_length=225)
    education = models.TextField(max_length=225)
    experience = models.TextField(max_length=225)
    certifications = models.TextField(max_length=225)
    job_preferences = models.TextField(max_length=225)
    desired_salary = models.CharField(max_length=50)
    expected_salary = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50)
    preferred_location = models.CharField(max_length=100)

    def _str_(self):
        return self.full_name