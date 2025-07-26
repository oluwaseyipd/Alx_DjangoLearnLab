from django.contrib import admin
from django.urls import path, include
from relationship_app import views as relationship_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", relationship_views.register, name="register"),
    path("login/", relationship_views.login_view, name="login"),
    path("", include("relationship_app.urls")),
]
