from django.shortcuts import render, redirect
from .models import Company
from django.contrib import messages

def company_register(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        company_email = request.POST.get("company_email")
        company_phone = request.POST.get("company_phone")
        company_location = request.POST.get("company_location")
        company_logo = request.FILES.get("company_logo")

        founded_year = request.POST.get("founded_year")
        industry = request.POST.get("industry")
        company_size = request.POST.get("company_size")
        company_description = request.POST.get("company_description")

        website = request.POST.get("website")
        linkedin = request.POST.get("linkedin")

        company = Company(
            user=request.user,
            company_name=company_name,
            company_email=company_email,
            company_phone=company_phone,
            company_location=company_location,
            company_logo=company_logo,
            founded_year=founded_year if founded_year else None,
            industry=industry,
            company_size=company_size,
            company_description=company_description,
            website=website,
            linkedin=linkedin,
        )

        company.save()
        messages.success(request, "Company profile created successfully!")
        return redirect("/company/")

    return render(request, "company.html")
