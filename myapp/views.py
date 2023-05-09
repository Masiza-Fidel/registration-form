from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserRegistration

def register_user(request):
    if request.method == 'POST':
        # Get all the data from the form and save it to the database
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        fan_activity = request.POST.get('fan_activity', '')
        free_time_activity = request.POST.get('free_time_activity', '')
        crazy_idea = request.POST.get('crazy_idea', '')
        location = request.POST.get('location', '')
        skills = request.POST.get('skills', '')
        goals = request.POST.get('goals', '')
        phone_number = request.POST.get('phone_number', '')
        email = request.POST.get('email', '')
   

        # Check if email is already registered
        if UserRegistration.objects.filter(email=email).exists():
            messages.error(request, 'This email address has already been registered. Please use a different email address.')
            return redirect('register')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('register')

        # Save data to the database
        user = UserRegistration(first_name=first_name, last_name=last_name, password=password, confirm_password=confirm_password,
                                fan_activity=fan_activity, free_time_activity=free_time_activity, crazy_idea=crazy_idea,
                                location=location, skills=skills, goals=goals, phone_number=phone_number, email=email)
        user.save()
        
        # Show success message and redirect to home page
        messages.success(request, f'Thank you {first_name}, your registration was successful!')
        return redirect('home')

    else:
        # If request method is GET, render the registration form template
        return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')



