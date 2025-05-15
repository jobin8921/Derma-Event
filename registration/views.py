from django.shortcuts import render, redirect, get_object_or_404
from .models import Registration, News
from django.contrib.auth import logout
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import datetime
# from social_django.utils import load_strategy
# from social_core.exceptions import AuthException


ADMIN_PASSWORD = "derma2025"  # Change this to something secure


def home(request):
    news_items = News.objects.all().order_by('-news_date')
    return render(request, 'index.html', {'news_items': news_items})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def schedule(request):
    return render(request, 'schedule.html')


def blog(request):
    news_items = News.objects.all().order_by('-news_date')
    return render(request, 'blog.html', {'news_items': news_items})


def speakers(request):
    return render(request, 'speakers.html')

def register(request):
    return render(request, 'register.html')

def sponser_register(request):
    return render(request, 'sponser.html')
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
        # Handle login
        if 'password' in request.POST:
            password = request.POST.get("password")
            if password == ADMIN_PASSWORD:
                attendees = Registration.objects.all().order_by('-registered_at')
                news_items = News.objects.all().order_by('-news_date')
                return render(request, 'adminpanel.html', {
                    'attendees': attendees,
                    'news_items': news_items
                })
            else:
                return render(request, 'adminlogin.html', {'error': 'Incorrect password'})

        # Handle news creation (assume already logged in)
        elif 'title' in request.POST:
            title = request.POST.get('title')
            description = request.POST.get('description')
            news_date = request.POST.get('news_date')
            image = request.FILES.get('image')

            news = News(title=title, description=description, news_date=news_date)
            if image:
                news.image = image
            news.save()

            attendees = Registration.objects.all().order_by('-registered_at')
            news_items = News.objects.all().order_by('-news_date')
            return render(request, 'adminpanel.html', {
                'attendees': attendees,
                'news_items': news_items,
                'message': 'News added successfully'
            })

    # GET request, show login page
    return render(request, 'adminlogin.html')


def logout_view(request):
    logout(request)
    return redirect('home')  # You can replace 'home' with your desired redirect URL



def delete_news(request, pk):
    if request.method == 'POST':
        news_item = get_object_or_404(News, pk=pk)
        news_item.delete()
    return redirect('admin_panel')



    