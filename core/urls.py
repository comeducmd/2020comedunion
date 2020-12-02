from django.urls import path
from . import views as core_views
from posts import views as post_views

app_name = "core"

urlpatterns = [
    path("", core_views.IntroView, name="intro"),
    path("home/", post_views.HomeView.as_view(), name="home"),
]
