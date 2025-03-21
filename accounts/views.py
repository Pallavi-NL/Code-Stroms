from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import re

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Define valid courses
        valid_courses = ["BTECH", "BCA", "MBA", "MTECH", "BBA", "BSC", "MSC", "PHD"]

        # Regex to validate email format
        email_pattern = r"^([a-zA-Z]+)([A-Z]+)(\d{2})@ced\.alliance\.edu\.in$"
        match = re.match(email_pattern, email)

        if not match:
            messages.error(request, "Invalid email format! Use your Alliance University email.")
            return render(request, 'core/register.html')

        # Extract username, course, and year from email
        extracted_username, course_code, year = match.groups()

        # Check if course is valid
        if course_code not in valid_courses:
            messages.error(request, "Invalid course in email! Use your correct Alliance University email.")
            return render(request, 'core/register.html')

        # Check if passwords match
        if password != password2:
            messages.error(request, "Passwords do not match")
            return render(request, 'core/register.html')

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully! You can log in now.")
            return redirect('login')

    return render(request, 'core/register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home.html after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "core/login.html")
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect("login")
