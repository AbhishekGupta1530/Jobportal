from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import JobModel as Job
from django.urls import reverse
from django.utils import timezone
from company.models import Company


def job(request):
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')
    company=Company.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company_name')
        location = request.POST.get('location')
        description = request.POST.get('description')
        job_type = request.POST.get('job_type')
        required_skills = request.POST.get('required_skills', "")
        salary_min = request.POST.get('salary_min')
        salary_max = request.POST.get('salary_max')
        deadline = request.POST.get('deadline')
        print(title,company,location,description,job_type,required_skills,salary_min,salary_max,deadline)

        job = Job(
            title=title,
            company=company,
            location=location,
            description=description,
            job_type=job_type,
            required_skills=required_skills,
            salary_min=salary_min if salary_min else None,
            salary_max=salary_max if salary_max else None,
            deadline=deadline if deadline else None,
        )
        job.save()

        messages.success(request, "Job created successfully!")
        return redirect("/Job/")
    return render(request, "job.html", {"jobs": jobs,"company":company})

def viewJob(req):
    q = req.GET.get("q","")
    if q:
        jobs = Job.objects.filter(title__icontains=q)
    else:

        jobs=Job.objects.all()
    return render(req,'viewjob.html',context={"jobs":jobs})

