from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Post
    paginate_by = 6
    paginate_orphans = 5
    ordering = "pub_date"
    context_object_name = "posts"
