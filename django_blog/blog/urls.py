from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # User pages
    path('feeds/', views.feeds, name='feeds'),
    path('profile/', views.profile, name='profile'),

     # Authentication views
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/auth/logout.html'), name='logout'),
    
     # Public pages
    path('', views.home, name='home'),
]