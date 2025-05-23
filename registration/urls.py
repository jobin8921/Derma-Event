from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('schedule/', views.schedule, name='schedule'),
    path('register/', views.register, name='register'),
    path('sponser_register/', views.sponser_register, name='sponser_register'),
    path('speakers/', views.speakers, name='speakers'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('registration_success/', views.registration_success, name='registration_success'),  # Success page
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('logout/', views.logout_view, name='logout'),



    path('delete-news/<int:pk>/', views.delete_news, name='delete_news'),







]
