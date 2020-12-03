from django.shortcuts import render, reverse
from posts import models
# Create your views here.

def IntroView(request):
    home = reverse("core:home")

    return render(
        request,
        "intro.html",
        {
            "home": home,
        },
    )

def SearchView(request):
    search = reverse("core:search")

    return render(
        request,
        "posts/post_search.html",
        {
            "search": search,
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
