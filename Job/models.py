from django.db import models
from company.models import Company

class JobModel(models.Model):
    # Job Type Choices (Matches the <select> options)
    JOB_TYPE_CHOICES = [
        ('FULL_TIME', 'Full-time'),
        ('PART_TIME', 'Part-time'),
        ('REMOTE', 'Remote'),
        ('INTERNSHIP', 'Internship'),
        ('CONTRACT', 'Contract'),
    ]

    # Required Fields    
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    
    
    job_type = models.CharField(
        max_length=10,
        choices=JOB_TYPE_CHOICES,
        default='FULL_TIME',
    )
    
    # Optional Fields
    required_skills = models.TextField(
        blank=True, 
        null=True,
        help_text="List key skills, separated by commas (e.g., Python, SQL, AWS, Django)."
    )
    salary_min = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True
    )
    salary_max = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True
    )
    deadline = models.DateField(blank=True, null=True)
    
    # Status and Metadata
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

