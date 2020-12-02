from django.urls import path
from . import views
from core import views as core_views

app_name = "users"

urlpatterns = [
    path("login/", core_views.LoginPageView, name="login"),
    path("login/kakao/", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback/", views.kakao_callback, name="kakao-callback"),
]
