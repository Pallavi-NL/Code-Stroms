from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import re  # Import regex for email validation



def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Email validation for Alliance University students
        email_pattern = r"^[a-zA-Z0-9]+[A-Za-z]+[0-9]{2}@ced\.alliance\.edu\.in$"
        
        if not re.match(email_pattern, email):
            messages.error(request, "Invalid email! Use your Alliance University email.")
            return render(request, 'core/register.html')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already in use.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully! You can now log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'core/register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'core/login.html')

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "core/home.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
