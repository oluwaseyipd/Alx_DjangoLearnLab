from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, CommentListView, CommentDetailView
from . import views




urlpatterns = [

    # User pages
    #Comment related URLs
    path('post/<int:post_id>/comments/new', CommentCreateView.as_view(), name='add-comment'),
    path('post/<int:post_id>/comments/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('post/<int:post_id>/comments/<int:comment_id>/update/', CommentUpdateView.as_view(), name='update-comment'),

    # Post-related URLs
    path('posts/', PostListView.as_view(), name='feeds'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('profile/', views.profile, name='profile'),

     # Authentication views
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/auth/logout.html'), name='logout'),
    
     # Public pages
    path('', views.home, name='home'),
]