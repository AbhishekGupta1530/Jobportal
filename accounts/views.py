from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Home Page
def home(request):
    return render(request, 'index.html')

# Register User
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
      
    
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('/register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('/register')

        # Create new user
        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('/login')

    return render(request, 'register.html')


# Login User
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
      
        user = authenticate(username=username,password=password)
        
       

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {username} it's you!")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/login')

    return render(request, 'login.html')


# Logout User
def logoutView(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('/login')

