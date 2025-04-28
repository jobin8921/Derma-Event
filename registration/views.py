from django.shortcuts import render, redirect
from .models import Registration
from django.contrib.auth import logout
# from social_django.utils import load_strategy
# from social_core.exceptions import AuthException


ADMIN_PASSWORD = "derma2025"  # Change this to something secure


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



def registration_success(request):
    user = request.user
    if user.is_authenticated:
        # Check if already registered
        reg_data, created = Registration.objects.get_or_create(
            email=user.email,
            defaults={'full_name': user.get_full_name()}
        )
        return render(request, 'registration_success.html', {'reg_data': reg_data})
    else:
        return redirect('login')
    

def admin_panel(request):
    if request.method == "POST":
        password = request.POST.get("password")
        if password == ADMIN_PASSWORD:
            attendees = Registration.objects.all().order_by('-registered_at')
            return render(request, 'adminpanel.html', {'attendees': attendees})
        else:
            return render(request, 'adminlogin.html', {'error': 'Incorrect password'})
    return render(request, 'adminlogin.html')



def logout_view(request):
    logout(request)
    return redirect('home')  # You can replace 'home' with your desired redirect URL

