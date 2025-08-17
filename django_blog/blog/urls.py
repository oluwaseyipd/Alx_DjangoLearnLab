from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views




urlpatterns = [

    # User pages
    path('posts/', PostListView.as_view(), name='feeds'), 
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('profile/', views.profile, name='profile'),

     # Authentication views
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/auth/logout.html'), name='logout'),
    
     # Public pages
    path('', views.home, name='home'),
]