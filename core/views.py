from django.shortcuts import render, reverse
from posts import models

# Create your views here.


def IntroView(request):
    home = reverse("core:home")
    video1 = reverse("core:v1")
    video2 = reverse("core:v2")
    video3 = reverse("core:v3")
    video4 = reverse("core:v4")
    video5 = reverse("core:v5")

    return render(
        request,
        "intro.html",
        {
            "home": home,
            "video1": video1,
            "video2": video2,
            "video3": video3,
            "video4": video4,
            "video5": video5,
        },
    )


def LoginPageView(request):
    kakao_login = reverse("users:kakao-login")

    return render(
        request,
        "users/login_page.html",
        {
            "kakao_login": kakao_login,
        },
    )


def video_1(request):
    video1 = reverse("core:v1")

    return render(
        request,
        "1.html",
        {
            "video1": video1,
        },
    )


def video_2(request):
    video2 = reverse("core:v2")

    return render(
        request,
        "2.html",
        {
            "video2": video2,
        },
    )


def video_3(request):
    video3 = reverse("core:v2")

    return render(
        request,
        "3.html",
        {
            "video3": video3,
        },
    )


def video_4(request):
    video4 = reverse("core:v2")

    return render(
        request,
        "4.html",
        {
            "video4": video4,
        },
    )


def video_5(request):
    video5 = reverse("core:v2")

    return render(
        request,
        "5.html",
        {
            "video5": video5,
        },
    )