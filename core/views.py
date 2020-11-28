from django.shortcuts import render, reverse

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
