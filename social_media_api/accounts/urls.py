from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnFollowUserView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("follow/<str:username>/", FollowUserView.as_view(), name="follow"),
    path("unfollow/<str:username>/", UnFollowUserView.as_view(), name="unfollow"),
]
