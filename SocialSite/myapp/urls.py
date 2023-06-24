from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from myapp import views

app_name = "myapp"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="myapp/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
