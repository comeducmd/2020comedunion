from django.urls import path, include
from . import views as core_views
from posts import views as post_views

app_name = "core"

urlpatterns = [
    path("", core_views.IntroView, name="intro"),
    path("home/", post_views.HomeView.as_view(), name="home"),
    path("1/", core_views.video_1, name="v1"),
    path("2/", core_views.video_2, name="v2"),
    path("3/", core_views.video_3, name="v3"),
    path("4/", core_views.video_4, name="v4"),
    path("5/", core_views.video_5, name="v5"),
]