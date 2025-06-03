from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="customers/login.html",
            authentication_form=LoginForm,
            next_page="main_page",
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="main_page"), name="logout"),
]
