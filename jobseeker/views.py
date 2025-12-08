from django.shortcuts import render,redirect
from jobseeker.models import Profile

# Create your views here.


def jobseekerProfile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phone')
        location = request.POST.get('location')
        profilephoto = request.FILES.get('profile_photo')
        resume = request.FILES.get('resume')
        skills = request.POST.get('skills')
        education = request.POST.get('education')
        experience = request.POST.get('experience')
        certifications = request.POST.get('certifications')
        job_preferences = request.POST.get('desired_job_title')
        expected_salary = request.POST.get('expected_salary')
        preferred_location = request.POST.get('preferred_location')

        # Save data into model
        Profile.objects.create(
            name = name,
            full_name=full_name,
            email=email,
            phoneno=phoneno,
            location=location,
            profilephoto=profilephoto,
            resume=resume,
            skills=skills,
            education=education,
            experience=experience,
            certifications=certifications,
            job_preferences=job_preferences,
            expected_salary=expected_salary,
            preferred_location=preferred_location
        )

        return redirect('/')   # Or wherever you want after saving

    return render(request, 'profile.html')


def viewProfile(request, name):
    profile = Profile.objects.get(name=name)
    return render(request, "viewprofile.html", {"profile": profile})




        