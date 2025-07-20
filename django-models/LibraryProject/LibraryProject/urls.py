from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from relationships_app import views as relationship_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_views.register, name="register"),
    path("login/", user_views.login, name="login"),
    path("", include("bookshelf.urls")),
     path('', include('relationship_app.urls')),
]