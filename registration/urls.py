from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('schedule/', views.about, name='schedule'),
    path('speakers/', views.about, name='speakers'),
    path('blog/', views.about, name='blog'),
    path('contact/', views.about, name='contact'),
    path('registration_success/', views.registration_success, name='registration_success'),  # Success page
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('logout/', views.logout_view, name='logout'),





]
